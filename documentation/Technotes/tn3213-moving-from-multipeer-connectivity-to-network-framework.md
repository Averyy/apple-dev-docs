# TN3213: Moving from Multipeer Connectivity to Network framework

**Framework**: Technotes

Learn how to migrate your Multipeer Connectivity app to Network framework.

#### Overview

Xcode 27 deprecates the entire Multipeer Connectivity framework.  If you have an app that uses Multipeer Connectivity, plan to migrate your code to [`Network`](https://developer.apple.com/documentation/Network) framework.  Follow this step-by-step guide:

1. [`Plan for security`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Plan-for-security.md)
2. [`Select a network architecture`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Select-a-network-architecture.md)
3. [`Create a peer identifier`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Create-a-peer-identifier.md)
4. [`Choose a protocol to match your send mode`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Choose-a-protocol-to-match-your-send-mode.md)
5. [`Discover peers`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Discover-peers.md)
6. [`Design for privacy`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Design-for-privacy.md)
7. [`Configure your connections`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Configure-your-connections.md)
8. [`Manage a listener`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Manage-a-listener.md)
9. [`Manage a network connection`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Manage-a-network-connection.md)
10. [`Send and receive reliable messages`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Send-and-receive-reliable-messages.md)
11. [`Send and receive best-effort messages`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Send-and-receive-best-effort-messages.md)
12. [`Start a stream`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Start-a-stream.md)
13. [`Send a resource`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Send-a-resource.md)

Additionally:

- Read [`Final notes`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Final-notes.md) for some general hints and tips.
- If you’re not sure where to start when migrating a specific Multipeer Connectivity feature, consult [`Symbol cross reference`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Symbol-cross-reference.md).  This maps symbols in the Multipeer Connectivity framework to sections in this technote.

> **Note**: A common misconception is that Multipeer Connectivity is the only way to use Apple peer-to-peer Wi-Fi.  That’s not the case.  Network framework has opt-in support for Apple peer-to-peer Wi-Fi.  It also supports industry standard peer-to-peer Wi-Fi via the [`Wi-Fi Aware`](https://developer.apple.com/documentation/WiFiAware) framework.  For the details, see [`Enable peer-to-peer Wi-Fi`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Enable-peer-to-peer-Wi-Fi.md).

This technote uses the Network framework API introduced in iOS 26 and aligned releases: [`NetworkConnection`](https://developer.apple.com/documentation/Network/NetworkConnection), [`NetworkListener`](https://developer.apple.com/documentation/Network/NetworkListener), and [`NetworkBrowser`](https://developer.apple.com/documentation/Network/NetworkBrowser).  Everything discussed here is possible with the older Network framework API ([`NWConnection`](https://developer.apple.com/documentation/Network/NWConnection), [`NWListener`](https://developer.apple.com/documentation/Network/NWListener), and [`NWBrowser`](https://developer.apple.com/documentation/Network/NWBrowser)) and with the Network framework C API ([`nw_connection_t`](https://developer.apple.com/documentation/Network/nw_connection_t), [`nw_listener_t`](https://developer.apple.com/documentation/Network/nw_listener_t), and [`nw_browser_t`](https://developer.apple.com/documentation/Network/nw_browser_t)).  However, the mechanics are quite different.  For information about these older APIs, see the [`Network`](https://developer.apple.com/documentation/Network) framework documentation.

Many of the techniques described by this technote are covered by sample code, including [`Building peer-to-peer apps`](https://developer.apple.com/documentation/WiFiAware/Building-peer-to-peer-apps), [`Connecting iPadOS and visionOS apps over the local network`](https://developer.apple.com/documentation/visionOS/connecting-ipados-and-visionos-apps-over-the-local-network), [`Building a custom peer-to-peer protocol`](https://developer.apple.com/documentation/Network/building-a-custom-peer-to-peer-protocol), and [`Configuring a Wi-Fi accessory to join a network`](https://developer.apple.com/documentation/NetworkExtension/configuring-a-wi-fi-accessory-to-join-a-network).

#### Plan for Security

To start, think about security.  Multipeer Connectivity offers three security models, expressed as [`MCEncryptionPreference`](https://developer.apple.com/documentation/MultipeerConnectivity/MCEncryptionPreference) choices:

- [`MCEncryptionPreference.none`](https://developer.apple.com/documentation/MultipeerConnectivity/MCEncryptionPreference/none)
- [`MCEncryptionPreference.optional`](https://developer.apple.com/documentation/MultipeerConnectivity/MCEncryptionPreference/optional)
- [`MCEncryptionPreference.required`](https://developer.apple.com/documentation/MultipeerConnectivity/MCEncryptionPreference/required)

Optional security has limited utility.  It’s more complex than no security but doesn’t yield any actual security benefits.  If your app is currently using optional security, decide whether it needs security or not and proceed accordingly.

This technote focuses on TLS-PKI (public key infrastructure) because that matches the approach used by Multipeer Connectivity.  Specifically, when you use the [`MCEncryptionPreference.required`](https://developer.apple.com/documentation/MultipeerConnectivity/MCEncryptionPreference/required) security model in Multipeer Connectivity, you must supply a [`SecIdentity`](https://developer.apple.com/documentation/Security/SecIdentity), and Network framework has a similar constraint.

> **Note**: Network framework has some support for TLS-PSK (pre-shared key), but that has significant limitations: it doesn’t work with QUIC, it doesn’t support TLS 1.3, and it only works with the older Network framework API ([`NWConnection`](https://developer.apple.com/documentation/Network/NWConnection) and friends).

In Network framework you configure your networking objects using a builder closure.  For example, you create a TCP connection like so:

```swift
let endpoint: NWEndpoint = … the address to connect to …
try await withNetworkConnection(to: endpoint, using: {
    TCP()
}) { … work with the connection … }
```

The focus of this section is the builder closure used to configure the connection.  In this example that closure is very small, containing just the `TCP()` call, but the following examples expand on that.  If you’re curious about the mechanics of configuring and managing a connection, see [`Configure your connections`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Configure-your-connections.md) and [`Manage a network connection`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Manage-a-network-connection.md).

In Network framework you connect to a network address that’s represented by a [`NWEndpoint`](https://developer.apple.com/documentation/Network/NWEndpoint) value.  This might hold, for example, a DNS name and a port number.  However, in a peer-to-peer app this typically holds a Bonjour service name.  To learn more about that, see [`Discover peers`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Discover-peers.md).

To create a TLS-over-TCP connection, add [`TLS`](https://developer.apple.com/documentation/Network/TLS) to the builder:

```swift
try await withNetworkConnection(to: endpoint, using: {
    TLS {
        TCP()
    }
}) { … work with the connection … }
```

TLS defaults to TCP, so you can omit that for brevity:

```swift
try await withNetworkConnection(to: endpoint, using: {
    TLS()
}) { … work with the connection … }
```

The `TLS` type supports modifiers to configure TLS.  For example, to apply a [`SecIdentity`](https://developer.apple.com/documentation/Security/SecIdentity) to TLS, use the [`localIdentity(_:)`](https://developer.apple.com/documentation/Network/TLS/localIdentity(_:)) modifier:

```swift
let identity: SecIdentity = …
let secIdentity = sec_identity_create(identity)!
try await withNetworkConnection(to: endpoint, using: {
    TLS()
        .localIdentity(secIdentity)
        … and more …
}) { … work with the connection … }
```

There are numerous TLS modifiers.  In a peer-to-peer environment, you typically want to configure TLS to:

- Require authentication on both peers, that is, mutual TLS
- Use a local identity
- Customize the trust evaluation of the remote peer’s certificate

In code this looks like:

```swift
TLS()
    .peerAuthentication(.required)
    .localIdentity(secIdentity)
    .certificateValidator { metadata, secTrust in
        let trust = sec_trust_copy_ref(secTrust).takeRetainedValue()
        let isTrusted: Bool =  … evaluate `trust` here …
        return isTrusted
    }
```

TLS is a fundamental part of QUIC.  Configure it using the [`tls`](https://developer.apple.com/documentation/Network/QUIC/tls-swift.property) property.  Its value supports the same TLS modifiers:

```swift
try await withNetworkConnection(to: endpoint, using: {
    QUIC(alpn: ["MyALPN"])
        .tls.localIdentity(secIdentity)
        … and more …
}) { connection in
    … work with the connection …
}
```

> **Note**: This example uses an Application-Layer Protocol Negotiation (ALPN) value of `MyALPN`.  In a peer-to-peer app it’s fine to hard code an arbitrary ALPN value like this.  Just make sure to use the same value for your listener.  If your app connects to a server where the ALPN value is significant, read [`RFC 7301`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7301) for detailed advice on how to use ALPNs.

Given that TLS is a fundamental part of QUIC, it doesn’t support the equivalent of Multipeer Connectivity’s [`MCEncryptionPreference.none`](https://developer.apple.com/documentation/MultipeerConnectivity/MCEncryptionPreference/none) security model.  Fortunately, there’s a way around this.  Embed a single digital identity in your app, apply it to all listeners and connections, and disable trust evaluation of the remote peer’s certificate.  This allows you to use QUIC without any meaningful security.

> ❗ **Important**: Think carefully before using this technique to disable QUIC’s built-in security.  Your move from Multipeer Connectivity to Network framework is an excellent opportunity to add security to your peer-to-peer app.

Adding meaningful security to your app means coming up with a plan for managing digital identities.  The details of that are up to you, but many approaches require you to locally create a new digital identity.  Apple platforms have no API to do that; you’ll need to write or acquire your own library for it.  One such library is the [`swift-certificates`](https://developer.apple.comhttps://github.com/apple/swift-certificates) package.

#### Select a Network Architecture

Multipeer Connectivity uses a fully connected network architecture.  All peers are equal, and every peer is effectively connected to every other peer.  Many apps work better with the client-server architecture, where one peer acts on the server and all the others are clients.  Network framework supports both architectures.

To implement a client-server architecture with Network framework:

1. Designate one peer as the server and all the others as clients.
2. On the server, use [`NetworkListener`](https://developer.apple.com/documentation/Network/NetworkListener) to listen for incoming connections.
3. On each client, use [`NetworkConnection`](https://developer.apple.com/documentation/Network/NetworkConnection) to make an outgoing connection to the server.

To implement a fully connected network architecture with Network framework:

1. On each peer, start a listener.
2. And also start a connection to each of the other peers.

This is likely to generate a lot of redundant connections, as peer A connects to peer B and vice versa.  To maintain efficiency and avoid confusion, add a mechanism to deduplicate those connections, as explained in the next section.

> ❗ **Important**: While the fully connected network architecture is more likely to create redundant connections, the client-server network architecture can generate redundant connections as well.  The advice in the next section applies to both architectures.

The client-server architecture is more familiar and easier to implement.  If you previously struggled with the fully connected network architecture, use this opportunity to switch to client-server.

#### Create a Peer Identifier

Multipeer Connectivity uses [`MCPeerID`](https://developer.apple.com/documentation/MultipeerConnectivity/MCPeerID) to uniquely identify each peer.  There’s nothing particularly special about `MCPeerID`; it’s effectively a wrapper around a large random number.

To identify each peer in Network framework, generate your own large random number.  One good choice for a peer identifier is a locally generated UUID, created using Foundation’s [`UUID`](https://developer.apple.com/documentation/Foundation/UUID) type.

Some Multipeer Connectivity apps persist their local `MCPeerID` value, taking advantage of its support for [`NSSecureCoding`](https://developer.apple.com/documentation/Foundation/NSSecureCoding).  You can do the same with a `UUID`, using either its string representation or its `Codable` support.

> ❗ **Important**: Before you decide to persist a peer identifier, think about the privacy implications.  For more on that, see [`Design for privacy`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Design-for-privacy.md).

Avoid having multiple connections between any two peers; that’s both wasteful and potentially confusing.  Use your peer identifier to deduplicate connections.

Deduplicating connections in a client-server network architecture is easy.  Have each client check in with the server with its peer identifier.  If the server already has a connection for that identifier, it can either close the old connection and keep the new connection, or vice versa.

Deduplicating connections in a fully connected network architecture is a bit trickier.  One option is to have each peer send its peer identifier to the other peer and then the peer with the ‘best’ identifier wins.  For example, imagine that peer A makes an outgoing connection to peer B while peer B is simultaneously making an outgoing connection to peer A.  When a peer receives a peer identifier from a connection, it checks for a duplicate.  If it finds one, it compares the peer identifiers and then chooses a connection to drop based on that comparison:

```None
if local peer identifier > remote peer identifier then
    drop outgoing connection
else
    drop incoming connection
end if
```

So, peer A drops its incoming connection and peer B drops its outgoing connection.

The mechanism you use to determine the winning peer identifier is up to you.  For example, if you use a `UUID` as your peer identifier, you might compare their string representations:

```swift
func isBetter(local: UUID, remote: UUID) -> Bool {
    local.uuidString > remote.uuidString
}
```

#### Choose a Protocol to Match Your Send Mode

Multipeer Connectivity offers two send modes, expressed as [`MCSessionSendDataMode`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSessionSendDataMode) choices:

- [`MCSessionSendDataMode.reliable`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSessionSendDataMode/reliable) for reliable messages
- [`MCSessionSendDataMode.unreliable`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSessionSendDataMode/unreliable) for best-effort messages

Best-effort is useful when sending latency-sensitive data, that is, data where retransmission is pointless because, by the time the retransmission arrives, the data will no longer be relevant.  A good example of this is a VoIP app.

In Network framework the send mode is set by the connection’s protocol:

- A QUIC connection supports zero or more reliable streams and at most one best-effort datagram channel.
- A WebSocket and TCP connection supports a single reliable stream.
- A UDP connection supports a single best-effort datagram channel.

Start with a reliable stream.  In many cases you can stop there, because most apps don’t need best-effort datagrams.

If you’re not sure which reliable protocol to use, choose QUIC.

If you need best-effort datagrams, get started with a reliable stream and use that to bootstrap your parallel best-effort datagram channel.  With QUIC this is easy: Get the [`datagrams`](https://developer.apple.com/documentation/Network/NetworkConnection/datagrams) property from the QUIC connection.  With other protocols this is a little trickier.  For example, with WebSocket you might have an exchange like this:

1. Peer A uses its reliable WebSocket connection to peer B to send a request for a parallel best-effort UDP connection.
2. Peer B receives that, opens a UDP listener, and sends the UDP listener’s port number back to peer A.
3. Peer A opens a parallel UDP connection to that port on peer B.

> ❗ **Important**: For step 3, get peer B’s IP address from the [`currentPath`](https://developer.apple.com/documentation/Network/NetworkConnection/currentPath) property of the reliable WebSocket connection.

#### Discover Peers

Multipeer Connectivity has a type for advertising a peer’s session ([`MCAdvertiserAssistant`](https://developer.apple.com/documentation/MultipeerConnectivity/MCAdvertiserAssistant)) and a type for browsing for peers ([`MCNearbyServiceBrowser`](https://developer.apple.com/documentation/MultipeerConnectivity/MCNearbyServiceBrowser)).

In Network framework, when creating a [`NetworkListener`](https://developer.apple.com/documentation/Network/NetworkListener), configure it to advertise a Bonjour service by passing in a [`bonjour(name:type:domain:txtRecord:)`](https://developer.apple.com/documentation/Network/ListenerProvider/bonjour(name:type:domain:txtRecord:)) listener provider:

```swift
try await NetworkListener(for: .bonjour(type: "_example._udp")) {
    QUIC(alpn: ["MyALPN"])
        … configure TLS …
}
.onServiceRegistrationUpdate { listener, change in
    switch change {
    case .add(let endpoint):
        … update UI for the added listener endpoint …
    case .remove(let endpoint):
        … update UI for the removed listener endpoint …
    @unknown default:
        break
    }
}
… modifiers to run the listener …
```

Also use the [`onServiceRegistrationUpdate(_:)`](https://developer.apple.com/documentation/Network/NetworkListener/onServiceRegistrationUpdate(_:)) modifier to install a closure that updates your UI to reflect the registration state.  Be prepared for this to be called at any time.  For example, Network framework will call your closure if it has to rename your service due to a name conflict.

This example uses a Bonjour service type of `_example._udp`.  See [`About service types`](tn3213-moving-from-multipeer-connectivity-to-network-framework#About-service-types.md) for more details on that.

The focus of this section is Bonjour, and so this example only shows that aspect of the listener.  For information on how to actually listen for connections, see [`Manage a listener`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Manage-a-listener.md).

There are two ways to browse for Bonjour services.  If you want to present the user with a list of services to choose from, run a browser like this:

```swift
try await NetworkBrowser(
    for: .bonjour("_example._udp")
)
.onStateUpdate { browser, newState in
    … handle a browser state change …
}
.run { endpoints in
    … update UI to show the latest results …
    … cancel this task to finish browsing …
}
```

Alternatively, if you know the service you’re looking for—perhaps you’re interested in a service with a particular value in its TXT record—you can run the browser like this:

```swift
let result = try await NetworkBrowser(
    for: .bonjour("_example._udp", includeTxtRecord: true)
)
.onStateUpdate { browser, newState in
    … handle a browser state change …
}
.run { endpoints in
    if let endpoint = endpoints.first(where: {
        isThisTheDroidWereLookingFor($0)
    }) {
        return .finish(endpoint)
    } else {
        return .continue
    }
}
… `result` is the endpoint to connect to …
```

In this example `isThisTheDroidWereLookingFor(_:)` is a filter function you write that checks whether the endpoint is the one you’re looking for.  For more about this concept, see [`Discover TXT records`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Discover-TXT-records.md).

The end result of both of these processes is an endpoint that the client connects to with `NetworkConnection`.

##### About Service Types

The examples in this technote use `_example._udp` for the service type.  The first part, `_example`, is directly analogous to the `serviceType` value you supply when creating `MCAdvertiserAssistant` and `MCNearbyServiceBrowser` objects.  The second part is either `_tcp` or `_udp` depending on the underlying transport protocol.  For TCP and WebSocket, use `_tcp`.  For UDP and QUIC, use `_udp` (QUIC is implemented on top of UDP).

Service types are described in [`RFC 6335`](https://developer.apple.comhttps://tools.ietf.org/html/rfc6335).  If you deploy an app that uses a new service type, register that service type with the [`Internet Assigned Numbers Authority`](https://developer.apple.comhttps://www.iana.org) (IANA).

##### Discovery Ui

Multipeer Connectivity also has UI components for advertising ([`MCNearbyServiceAdvertiser`](https://developer.apple.com/documentation/MultipeerConnectivity/MCNearbyServiceAdvertiser)) and browsing ([`MCBrowserViewController`](https://developer.apple.com/documentation/MultipeerConnectivity/MCBrowserViewController)).  There’s no direct equivalent to these in Network framework, but there are other options:

- If you’re using [`Wi-Fi Aware`](https://developer.apple.com/documentation/WiFiAware), use [`DeviceDiscoveryUI`](https://developer.apple.com/documentation/DeviceDiscoveryUI) to pair with another device and then use Network framework to communicate with it.
- Similarly, if you’re creating an Apple TV app, use [`DeviceDiscoveryUI`](https://developer.apple.com/documentation/DeviceDiscoveryUI) to connect to your iOS, iPadOS, or watchOS app and then use Network framework to communicate with it
- Otherwise, use your preferred UI framework to create a UI that best suits your app.

##### Discover Txt Records

The Bonjour service discovery protocol used by Network framework supports TXT records.  Using these, a listener can associate metadata with its service and a browser can get that metadata for each discovered service.

To advertise a TXT record with your listener, create a [`NWTXTRecord`](https://developer.apple.com/documentation/Network/NWTXTRecord) value and pass it to [`bonjour(name:type:domain:txtRecord:)`](https://developer.apple.com/documentation/Network/ListenerProvider/bonjour(name:type:domain:txtRecord:)) when creating the listener:

```swift
let peerID: UUID = …
var txtRecord = NWTXTRecord()
txtRecord["peerID"] = peerID.uuidString
try await NetworkListener(
    for: .bonjour(type: "_example._udp", txtRecord: txtRecord)
) {
    QUIC(alpn: ["MyALPN"])
        … configure TLS …
}
… modifiers to run the listener …
```

In this example the listener publishes its peer identifier in the TXT record under the `peerID` key.

To browse for services and their associated TXT records, configure your browser to return TXT records, as shown by the example in [`Discover peers`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Discover-peers.md).  You might then implement a filter function like this:

```swift
func isThisTheDroidWereLookingFor(_ endpoint: Bonjour.Endpoint) -> Bool
{
    guard
        let peerIDString = endpoint.txtRecord["peerID"],
        let peerID = UUID(uuidString: peerIDString)
    else { return false }
    return peerID == … some specific value …
}
```

This example returns true if the TXT record contains a specific peer identifier, but that’s just one potential use for TXT records.

#### Design for Privacy

This section covers some privacy issues to consider as you implement your app.  This isn’t an exhaustive list.  For general advice on this topic, see [`Protecting user privacy`](https://developer.apple.com/documentation/HealthKit/protecting-user-privacy).

There can be no privacy without security.  If you didn’t enable security with Multipeer Connectivity, now is the time to correct that misstep.  For more on this topic, see [`Plan for security`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Plan-for-security.md).

When you advertise a service with a listener, it defaults to using the [`name`](https://developer.apple.com/documentation/UIKit/UIDevice/name) as the service name.  To override that, pass a custom name to [`bonjour(name:type:domain:txtRecord:)`](https://developer.apple.com/documentation/Network/ListenerProvider/bonjour(name:type:domain:txtRecord:)) when creating the listener:

```swift
let customName: String = …
try await NetworkListener(
    for: .bonjour(name: customName, type: "_example._udp")
) {
    QUIC(alpn: ["MyALPN"])
        … configure TLS …
}
… modifiers to run the listener …
```

Whether this makes sense depends on the nature of your app:

- If your app presents a list of remote peers and the user chooses from that list, it’s best to stick with the user-assigned device name because that’s what the user will recognize.
- If your app automatically connects to services as it discovers them, it’s reasonable to override the service name because the user won’t see it.  A common choice is to use the peer identifier as the service name.

If you stick with the user-assigned device name, consider whether to include the peer identifier in your TXT record.  See [`Discover TXT records`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Discover-TXT-records.md).

> ❗ **Important**: Using a peer identifier in your service name or TXT record is a heuristic to reduce the number of duplicate connections.  Don’t rely on it for correctness.  Rather, deduplicate connections using the process described in [`Create a peer identifier`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Create-a-peer-identifier.md).

You have the option of persisting your peer identifier.  Doing that has obvious advantages—it allows for a more stable view of the network—but it also has significant privacy implications.  A persistent peer identifier can be tracked over time and between networks.  Consider whether you need a persistent peer identifier at all.  If you do, consider whether it makes sense to rotate that identifier over time.

A persistent peer identifier is of particular concern if you use it as your service name, or put it in your TXT record, because Bonjour allows any peer on the network to discover those items.

If you use a custom name for your service, make sure to handle the case where Network framework renames your service due to a name conflict.

#### Configure Your Connections

Multipeer Connectivity’s symmetric architecture means that it uses a single type, [`MCSession`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSession), to manage the connections to all peers.  In Network framework, that role is fulfilled by two types:

- [`NetworkListener`](https://developer.apple.com/documentation/Network/NetworkListener) listens for incoming connections.
- [`NetworkConnection`](https://developer.apple.com/documentation/Network/NetworkConnection) makes an outgoing connection.

Both types support a builder closure to specify the network protocol and options to use.  For example, here’s how to configure and run the simplest possible listener for TCP:

```swift
try await NetworkListener {
    TCP()
}
.run { connection in
    … handle a connection of type `NetworkConnection<TCP>` …
}
```

When creating an outgoing connection, call [`withNetworkConnection(to:using:_:)`](https://developer.apple.com/documentation/Network/withNetworkConnection(to:using:_:)-1sik8), passing it an `NWEndpoint` with the address to connect to, a builder closure, and a closure to run the connection.  For example, here’s how you configure and run the simplest possible TCP connection:

```swift
let endpoint: NWEndpoint = … the address to connect to …
try await withNetworkConnection(to: endpoint, using: {
    TCP()
}) { connection in
    … work with the connection …
}
```

In both cases the builder closure supports more complex protocol stacks.  For example, to enable TLS over TCP with the security configuration outlined in [`Plan for security`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Plan-for-security.md), replace `TCP()` in the above code snippets with this:

```swift
TLS {
    TCP()
}
.peerAuthentication(.required)
.localIdentity(secIdentity)
.certificateValidator { metadata, secTrust in
    let trust = sec_trust_copy_ref(secTrust).takeRetainedValue()
    let isTrusted: Bool = … evaluate `trust` here …
    return isTrusted
}
```

You can also use the builder closure to layer protocols on top of TCP.  For example, to use type-length-value (TLV) framing on top of TLS, use a builder like this:

```swift
TLV(type: MessageType.RawValue.self, length: UInt16.self) {
    TLS {
        TCP()
    }
}

… elsewhere …

enum MessageType: UInt16 {
    case hello = 0
    case goodbye = 1
}
```

This uses a `UInt16` for the message length and a `MessageType` enum, which has raw value that’s also a `UInt16`, for the message type.

For more about message framing in Network framework, see [`Send and receive reliable messages`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Send-and-receive-reliable-messages.md).

The following snippet summarizes the builder syntax for the most common connection types:

**TCP**:

```swift
TCP()
```

**TLS over TCP**:

```swift
TLS {
    TCP()
}
.peerAuthentication(.required)
… other TLS modifiers …
```

**UDP**:

```swift
UDP()
```

**WebSocket over TCP**:

```swift
WebSocket {
    TCP()
}
```

**WebSocket over TLS over TCP**:

```swift
WebSocket {
    TLS {
        TCP()
    }
    .peerAuthentication(.required)
    … other TLS modifiers …
}
```

**QUIC, with implicit TLS**:

```swift
QUIC(alpn: ["MyALPN"])
    .tls.peerAuthentication(.required)
    … other TLS modifiers …
```

##### Enable Peer to Peer Wi Fi

By default, Network framework doesn’t enable peer-to-peer Wi-Fi.  If you want that, explicitly enable it using the [`peerToPeerIncluded(_:)`](https://developer.apple.com/documentation/Network/NWParametersProvider/peerToPeerIncluded(_:)-60331) modifier.  This involves a slight tweak to the overall builder closure, as shown in this connection example:

```swift
try await withNetworkConnection(to: endpoint, using: .parameters {
        TCP()
    }
    .peerToPeerIncluded(true)
) { connection in
    … work with the connection …
}
```

This uses the [`parameters(_:)`](https://developer.apple.com/documentation/Network/NWParametersBuilder/parameters(_:)) function to create an [`NWParametersBuilder`](https://developer.apple.com/documentation/Network/NWParametersBuilder) value which supports lots of modifiers via its [`NWParametersProvider`](https://developer.apple.com/documentation/Network/NWParametersProvider) conformance.

A similar approach works for `NetworkListener` and `NetworkBrowser`.

> ❗ **Important**: Enabling peer-to-peer Wi-Fi can reduce network performance both for your app and for other apps on the device.  Only enable it if it’s a significant benefit to your app.  Consider using [`Wi-Fi Aware`](https://developer.apple.com/documentation/WiFiAware) instead.  Although note that the combination of Wi-Fi Aware and QUIC is not supported prior to iOS 27 and aligned releases (r. 175046087).

If you enable peer-to-peer Wi-Fi, it’s critical to stop network operations as soon as you’re done with them.  For example, if you’re browsing for services with peer-to-peer Wi-Fi enabled and the user picks a service, stop the browse operation immediately, before you kick off the connection to that service.  Otherwise, the ongoing browse operation might affect the performance of your connection.

#### Manage a Listener

In Network framework, use [`NetworkListener`](https://developer.apple.com/documentation/Network/NetworkListener) to listen for incoming connections:

```swift
let service: BonjourListenerProvider = …
try await NetworkListener(for: service) {
    QUIC(alpn: ["MyALPN"])
        … configure TLS …
}
.onStateUpdate { listener, state in
    … handle a listener state change …
}
.onServiceRegistrationUpdate { listener, change in
    … handle a service registration change …
}
.run { connection in
    … handle a connection of type `NetworkConnection<QUIC>` …
}
```

> ❗ **Important**: The remainder of this technote focuses on the QUIC protocol.  If you decide to use a different protocol, some things get easier and some things get harder.  For example, if you use TCP then managing a listener is easier because each incoming connection is a TCP stream.  On the other hand, setting up a parallel best-effort datagram channel is harder because you need to use a completely different protocol, UDP.

For details on how to use the builder closure to configure the listener, see [`Configure your connections`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Configure-your-connections.md).  For details on how to set up `service` and deal with service registration changes, see [`Discover peers`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Discover-peers.md).

Network framework calls your state update handler when the listener changes state:

```swift
.onStateUpdate { listener, state in
    switch newState {
    case .setup:
        … the listener has not yet started …
    case .waiting(let error):
        … the listener tried to start and failed; it might recover in the future …
    case .ready:
        … the listener is running …
    case .failed(let error):
        … the listener tried to start and failed irrecoverably …
    case .cancelled:
        … the listener was cancelled by you …
    @unknown default:
        break
    }
}
```

Every time a client connects to the listener, the listener’s [`run(_:)`](https://developer.apple.com/documentation/Network/NetworkListener/run(_:)-42k25) method spawns a child task to call your new connection handler.  Each connection represents a QUIC tunnel.  You don’t send data over the tunnel directly.  Rather, you listen for incoming streams running over that tunnel:

```swift
… create and configure listener as shown above …
.run { connection in
    try await connection.inboundStreams { stream in
        … handle a stream of type `QUIC.Stream<QUICStream>` …
    }
}
```

In this example, `stream` is of type `QUIC.Stream<QUICStream>`, which has methods to send and receive data.  This is a subclass of [`NetworkChannel`](https://developer.apple.com/documentation/Network/NetworkChannel), which is Network framework’s base class for types that can transfer data.  To learn more about how to send and receive data on a network channel, see [`Manage a network connection`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Manage-a-network-connection.md).

> ❗ **Important**: Network framework uses the word *channel* to represent its core data transfer abstraction.  A TCP connection (`NetworkConnection<TCP>`) is a channel, as is a UDP flow (`NetworkConnection<UDP>`).  A QUIC connection is not a channel, but you can create QUIC streams that run over that connection, and each QUIC stream (`QUIC.Stream<QUICStream>`) is a channel.

In Multipeer Connectivity, the session ([`MCSession`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSession)) keeps track of all the peers you’re communicating with.  With Network framework, that responsibility falls on you.  The best approach depends on your network architecture:

- In the client-server network architecture, the client only needs to manage the connection to a single peer, the server.
- In contrast, the server must manage connections to all client peers.
- In the fully connected network architecture, every peer must maintain a listener *and* connections to each of the other peers.

##### Understand Udp Flows

Network framework handles UDP using the same [`NetworkListener`](https://developer.apple.com/documentation/Network/NetworkListener) and [`NetworkConnection`](https://developer.apple.com/documentation/Network/NetworkConnection) types as it uses for TCP.  However, the underlying UDP protocol is stateless; it has no notion of listeners and connections.  To square this circle Network framework works in terms of UDP flows.  A UDP flow is defined as a bidirectional sequence of UDP datagrams with the same 4 tuple (local IP address, local port, remote IP address, and remote port).  In Network framework:

- Each `NetworkConnection` object manages a single UDP flow.
- If a `NetworkListener` receives a UDP datagram whose 4 tuple doesn’t match any known `NetworkConnection`, it creates a new `NetworkConnection`.

This introduces some complexity.  For example, because UDP is stateless your listener isn’t notified when a client goes away.  If you want to detect that, you must send a *still there?* message to any client you haven’t heard from in a while.

To avoid this complexity, use QUIC datagrams rather than using UDP directly.  In QUIC, you start by creating a QUIC connection (`NetworkConnection<QUIC>`).  While that connection is actually implemented on top of UDP, QUIC adds its own connection semantics.  When you get the connection’s QUIC datagram channel ([`datagrams`](https://developer.apple.com/documentation/Network/NetworkConnection/datagrams)), it remains associated with the connection.  So, to learn about the client going away, monitor the state of the connection as a whole.

#### Manage a Network Connection

In Network framework, call [`withNetworkConnection(to:using:_:)`](https://developer.apple.com/documentation/Network/withNetworkConnection(to:using:_:)-1sik8) to start an outgoing connection:

```swift
let endpoint: NWEndpoint = …
try await withNetworkConnection(to: endpoint, using: {
    QUIC(alpn: ["MyALPN"])
        … configure TLS …
}) { connection in
    connection.onStateUpdate { connection, state in
        … handle a connection state change …
    }
    connection.onViabilityUpdate { connection, isViable in
        … handle a viability change …
    }
    … work with the connection …
}
```

You pass in an [`NWEndpoint`](https://developer.apple.com/documentation/Network/NWEndpoint) value that represents the address to connect to.  In a traditional networking application this might hold a DNS name and a port number.  In a peer-to-peer app this typically holds a Bonjour service name.  You discover these endpoints using Bonjour browser, as explained in [`Discover peers`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Discover-peers.md).

The `connection` value passed to the trailing closure is of type [`NetworkConnection`](https://developer.apple.com/documentation/Network/NetworkConnection).  That’s a generic type, and in this specific example the `ApplicationProtocol` type parameter is [`QUIC`](https://developer.apple.com/documentation/Network/QUIC), making for a concrete type of `NetworkConnection<QUIC>`.  You can’t transfer data directly over this QUIC connection.  Instead, call [`openStream(directionality:)`](https://developer.apple.com/documentation/Network/NetworkConnection/openStream(directionality:)) to start a stream:

```swift
let stream = try await connection.openStream()
… send and receive on the stream …
```

Once you have a stream you can start transferring data; see [`Send and receive reliable messages`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Send-and-receive-reliable-messages.md) for the details.

As in the listener case, you’re responsible for keeping track of these connections and streams, and the best approach depends on your network architecture.

To monitor the state of the connection, install a state update handler:

```swift
connection.onStateUpdate { connection, state in
    switch state {
    case .setup:
        … connection has not yet started …
    case .preparing:
        … connection is starting …
    case .waiting(let error):
        … connection tried to start and failed; it might recover in the future …
    case .ready:
        … connection is running …
    case .failed(let error):
        … connection tried to start and failed irrecoverably …
    case .cancelled:
        // … connection was cancelled by you …
    @unknown default:
        break
    }
}
```

To close a connection, simply drop the last reference to the `NetworkConnection` object.  If you’re using Swift concurrency, as shown by the examples here, you can achieve this in one of two ways:

- Have the task running the connection end normally.
- Cancel the task that’s running the connection.

In Swift concurrency:

- A task can’t terminate until all of its child tasks have terminated.
- Cancelling a task automatically cancels any child tasks.

These rules have important consequences for QUIC.  First, if your code calls [`inboundStreams(_:)`](https://developer.apple.com/documentation/Network/NetworkConnection/inboundStreams(_:)) on a connection, the connection spawns a child task for each new inbound stream.  The `inboundStreams(_:)` call won’t return until the connection can no longer create inbound streams (for example, because the remote peer closed it) and every child task running one of the connection’s stream has terminated.

Second, if you cancel a task that’s handling new streams by running inside `inboundStreams(_:)`, that automatically cancels all of the child tasks running one the connection’s streams.

#### Send and Receive Reliable Messages

In Multipeer Connectivity, a single session supports both reliable and best-effort send modes.  In Network framework, the supported send modes vary based on the connection type.  Again, this example focuses on QUIC, but the techniques discussed here also apply to other stream-oriented protocols, most notably TCP.

You can think of a QUIC connection as a tunnel, which supports multiple independent streams of data.  A simple app might open a single stream over the tunnel and transfer all of its messages over that stream.  A more complex app might create many independent streams.  See [`Start a stream`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Start-a-stream.md) for an example of that.

In the simple case, the app sets up a QUIC connection and then opens a bidirectional stream over that connection.  See [`Manage a listener`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Manage-a-listener.md) and [`Manage a network connection`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Manage-a-network-connection.md) for examples of that.

A QUIC stream is represented by the `QUIC.Stream<QUICStream>` type.  That type supports sending and receiving chunks of bytes:

```swift
let stream: QUIC.Stream<QUICStream> = …

let bytesToSend = Data("Hello Cruel World!".utf8)
try await stream.send(bytesToSend)

let (bytesReceived, _) = try await stream.receive(atLeast: 1, atMost: 1024)
… process the incoming bytes …
```

> **Note**: In Network framework, each receive method returns a tuple of data and metadata.  This snippet ignores the metadata returned by `receive(atLeast:atMost:)`.

A QUIC stream doesn’t preserve message boundaries.  If you send a sequence of bytes on the stream the remote peer will receive that exact sequence—or the stream will fail with an error—but the grouping might be different.  The above example sends 18 bytes in one chunk.  The remote peer might receive one 18 byte chunk, or 18 one byte chunks, or any other combination.  To manage this complexity, add a framing protocol to your stream.

Network framework supports a number of framing protocols.  [`Configure your connections`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Configure-your-connections.md) demonstrates a simple but effective framing protocol, [`TLV`](https://developer.apple.com/documentation/Network/TLV).  The following example uses the `Coder` framing protocol, which is more complex to set up but much nicer to use.

The first step is to define a message format as a Swift type that conforms to the `Codable` protocol.  This example declares an enum that has one case for a *hello* message, intended to be the first message on the stream, and another case for a *goodbye* message, intended to be the last message.

```swift
enum Message: Codable {
    case hello(peerID: String)
    // … other cases …
    case goodbye(error: Int, message: String)
}
```

Next add the [`Coder`](https://developer.apple.com/documentation/Network/Coder) framing protocol to the stream.  Both the client and the server have to do this.  In the case of the client, it passes a builder closure to the connection’s [`openStream(directionality:_:)`](https://developer.apple.com/documentation/Network/NetworkConnection/openStream(directionality:_:)) method:

```swift
let connection: NetworkConnection<QUIC> = …
let messageChannel = try await connection.openStream { stream in
    Coder(Message.self, using: .json) {
        stream
    }
}
```

In the case of the server, it passes a builder closure to the connection’s [`inboundStreams(prepending:_:)`](https://developer.apple.com/documentation/Network/NetworkConnection/inboundStreams(prepending:_:)) method:

```swift
let connection: NetworkConnection<QUIC> = connection // …
try await connection.inboundStreams(prepending: { stream in
    Coder(Message.self, using: .json) {
        stream
    }
}) { messageChannel in
    … handle messages on the channel …
}
```

Now the client and the server both have a `messageChannel` value which can send and receive messages.

> **Note**: The type of that value is complex, being `QUIC.Stream<Coder<Message, Message, NetworkJSONCoder>>`.

You might use this channel like so:

```swift
let messageChannel = … as above …

let peerID = UUID().uuidString
try await messageChannel.send(.hello(peerID: peerID))

let (message, _) = try await messageChannel.receive()
switch message {
case .hello(peerID: let remotePeerID):
    … handle 'hello' message from remote peer …
case .goodbye(error: let error, message: let message):
    … handle 'goodbye' message from remote peer …
}
```

Note how this works in terms of `Message` values, rather than chunks of bytes.  Network framework handles the process of serializing and framing sent messages and unframing and deserializing received ones.

Many network apps use a request-response protocol: The client sends a request and the server replies with a response.  If your app uses a request-response protocol and each message is small, you don’t have to worry about flow control (also known as back pressure).  In contrast, if your app might stream unbounded amounts of data, or it uses a request-response protocol with large messages, flow control is a concern.  For more about flow control, see [`Start a stream`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Start-a-stream.md).

Multipeer Connectivity supports sending the same message to multiple peers in a single send call.  In Network framework each send call targets a specific connection.  To send a message to multiple peers, make a send call on the connection associated with each peer.

#### Send and Receive Best Effort Messages

In Multipeer Connectivity, a single session supports both reliable and best-effort send modes.  In Network framework, the exact set of data transfer operations depends on the connection type.  A QUIC connection supports zero or more reliable streams and at most one best-effort datagram channel.

To get the best-effort datagram channel for a connection, fetch the [`datagrams`](https://developer.apple.com/documentation/Network/NetworkConnection/datagrams) property:

```swift
let datagramChannel = try await connection.datagrams
```

Every datagram channel has a limit to the maximum size of its datagrams:

- For a UDP connection, get the [`maximumDatagramSize`](https://developer.apple.com/documentation/Network/NetworkChannel/maximumDatagramSize) property.
- For a QUIC datagram channel, get the [`usableDatagramFrameSize`](https://developer.apple.com/documentation/Network/NetworkConnection/usableDatagramFrameSize) property from the parent QUIC connection.

Limit your sends on that channel to this size.

> ❗ **Important**: If you need to send a message that’s larger than this size, you must fragment the message on send and reassemble the message on receive.

To send a datagram on the channel, call the [`send(_:metadata:)`](https://developer.apple.com/documentation/Network/NetworkChannel/send(_:metadata:)-42nkz) method:

```swift
let datagramToSend = Data("Hello Cruel World!".utf8)
try await datagramChannel.send(datagramToSend)
```

To receive a datagram on that channel, call the [`receive()`](https://developer.apple.com/documentation/Network/NetworkChannel/receive()-3a115) method:

```swift
let (datagramReceived, _) = try await datagramChannel.receive()
```

> **Note**: This example, like the earlier receive examples, ignores the returned metadata.

#### Start a Stream

In Multipeer Connectivity you can ask the session to start a stream to a specific peer.  The way you do this in Network framework depends on the connection type.  For a QUIC connection it’s very straightforward:

- The peer that wants to initiate a stream calls [`openStream(directionality:)`](https://developer.apple.com/documentation/Network/NetworkConnection/openStream(directionality:)), or [`openStream(directionality:_:)`](https://developer.apple.com/documentation/Network/NetworkConnection/openStream(directionality:_:)), as shown in [`Manage a network connection`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Manage-a-network-connection.md).
- The peer that wants to accept new streams calls [`inboundStreams(_:)`](https://developer.apple.com/documentation/Network/NetworkConnection/inboundStreams(_:)), or [`inboundStreams(prepending:_:)`](https://developer.apple.com/documentation/Network/NetworkConnection/inboundStreams(prepending:_:)), as explained in [`Manage a listener`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Manage-a-listener.md).

> ❗ **Important**: Either peer can initiate a stream.  There’s no requirement that the stream be initiated by the peer that opened the connection over which the stream is running.  It’s just fine for the server to initiate a stream to the client.

It’s common for a client to initiate a QUIC connection to the server, immediately open a command-and-control stream over that connection, and use messages on that command-and-control stream to set up other streams.  However, that’s certainly not required.  QUIC and Network framework offer a lot of flexibility, and you decide how to use that.

One common reason to start a new stream is that you want to send a lot of data to the remote peer.  In that case you need to worry about flow control  (also known as back pressure).  Flow control applies to both the send and receive side.

> ❗ **Important**: Failing to implement flow control can result in unbounded memory growth in your app.  This is particularly bad on iOS, where excessive memory use will cause the system to terminate your app (a [`Diagnosing issues using crash reports and device logs`](https://developer.apple.com/documentation/Xcode/diagnosing-issues-using-crash-reports-and-device-logs#Uncover-memory-inefficiencies-using-jetsam-event-reports)).

Fortunately, Network framework’s support for Swift concurrency makes flow control very simple.  When you send data to a stream, the system buffers that data in a send buffer until it has a chance to transfer it over the network.  That send buffer has a limited size.  If you consistently send data faster than the network can transfer it, the send buffer fills up.  At that point any subsequent send calls will wait until space is available.

Given that, you implement send-side flow control using a very simple loop:

```swift
func produceNextChunkToSend() async throws -> Data? { … your code here … }

let stream: QUIC.Stream<QUICStream> = …

repeat {
    guard let chunk = try await produceNextChunkToSend() else {
        break
    }
    try await stream.send(chunk)
} while true
```

The loop calls `produceNextChunkToSend()` to get the next chunk of data to send.  If there is no more data, it leaves the loop.  If there’s a chunk of data to send, it sends that and then loops.

For best performance, use a chunk size of at least 64 KiB.  If you’re expecting to run on a fast device with a fast network, a chunk size of 1 MiB is reasonable.

Receive-side flow control is a natural extension of the standard receive pattern:

```swift
func consumeChunkReceived(_ chunk: Data) async throws { … your code here … }
let stream: QUIC.Stream<QUICStream> = …

repeat {
    let (chunk, meta) = try await stream.receive(atLeast: 1, atMost: 64 * 1024)
    try await consumeChunkReceived(chunk)
    if meta.endOfStream {
        break
    }
} while true
```

This example takes advantage of the fact that the [`receive(atLeast:atMost:)`](https://developer.apple.com/documentation/Network/NetworkChannel/receive(atLeast:atMost:)) method returns both data and metadata.  The `endOfStream` property of the `QUICStream.Metadata` type tells you whether this is the last chunk that the stream will deliver.

> ❗ **Important**: The above assumes that `consumeChunkReceived(_:)` is an async function that itself supports flow control.  If your implementation of that routine stores the data in an unbounded memory buffer, as in the example shown below, you’ve not implemented receive-side flow control properly.

```swift
// -- DON’T DO THIS --

var buffer = Data()

func consumeChunkReceived(_ chunk: Data) async throws {
    buffer.append(chunk)
}

// -- DON’T DO THIS --
```

#### Send a Resource

In Multipeer Connectivity you can ask the session to send a complete resource, identified by either a file or HTTP URL, to a specific peer.  Network framework has no direct support for this.  If you need this, implement it on top of a stream.  For example, to transfer a file:

- On the send side, open a stream and then read chunks of data from the file and send them over that stream.
- On the receive side, open a stream and then receive chunks of data from that stream and write them to the file.

As the file might be larger than the available memory it’s critical to implement flow control, as described in the previous section.

#### Final Notes

The following sections collect together some general hints and tips.

##### Concurrency

In Multipeer Connectivity, each session ([`MCSession`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSession)) has its own internal Dispatch queue and calls delegate callbacks on that queue.  Network framework is based on Swift concurrency rather than Dispatch queues.  Enable the Swift 6 language mode so that the compiler finds and reports any data races in your code.

In a simple app it’s reasonable to use the main actor for networking.  If you do this, be careful not to do CPU intensive work in your networking code.  For example, if you receive a message that holds JPEG data, don’t decode that data on the main actor, but instead call out to a concurrent async function.  Also, if your app uses the network intensively—for example, a server that manages dozens of simultaneous connections—that might overload the main actor and you should consider alternatives.

##### Overriding Protocol Defaults

TCP and QUIC are intended to be deployed at vast scale across the wider Internet.  For that reason they use default options that aren’t optimized for local networking.  Consider changing these defaults in your app.

TCP has the concept of a *send timeout*.  If you send data on a TCP connection and TCP is unable to successfully transfer it to the remote peer within the send timeout, TCP will fail the connection.  The default send timeout is infinite.  TCP just keeps trying.  To change this, apply the [`retransmitConnectionDropTime(_:)`](https://developer.apple.com/documentation/Network/TCP/retransmitConnectionDropTime(_:)) modifier.

TCP also has the concept of *keepalives*.  If a connection is idle, TCP will send keepalives over the connection.  This has two benefits:

- If the connection is running through a NAT, the keepalives prevent the NAT mapping from timing out.
- If the remote peer is inaccessible, the keepalives cause the connection to fail.  This prevents idle but dead connections from lingering indefinitely.

TCP keepalives default to disabled.  To enable them, apply the [`keepalive(idleTimeInSeconds:count:intervalInSeconds:)`](https://developer.apple.com/documentation/Network/TCP/keepalive(idleTimeInSeconds:count:intervalInSeconds:)) modifier.

QUIC has the concept of an *idle timeout*.  A QUIC connection that’s been idle for longer than this timeout will close.  The default value on Apple platforms is 30 seconds.  To change that, apply the [`idleTimeout(_:)`](https://developer.apple.com/documentation/Network/QUIC/idleTimeout(_:)) modifier.

QUIC also has the concept of *keepalives*.  QUIC keepalives default to disabled.  To enable them, change the [`keepAlive`](https://developer.apple.com/documentation/Network/NWProtocolQUIC/Metadata/keepAlive) property on the protocol metadata.

#### Symbol Cross Reference

If you’re not sure where to start with a specific Multipeer Connectivity construct, find it in the tables below and follow the link to the relevant section.

| For symbol | See |
| --- | --- |
| [`MCAdvertiserAssistant`](https://developer.apple.com/documentation/MultipeerConnectivity/MCAdvertiserAssistant) | [`Discover peers`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Discover-peers.md) |
| [`MCAdvertiserAssistantDelegate`](https://developer.apple.com/documentation/MultipeerConnectivity/MCAdvertiserAssistantDelegate) | [`Discover peers`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Discover-peers.md) |
| [`MCBrowserViewController`](https://developer.apple.com/documentation/MultipeerConnectivity/MCBrowserViewController) | [`Discover peers`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Discover-peers.md) |
| [`MCBrowserViewControllerDelegate`](https://developer.apple.com/documentation/MultipeerConnectivity/MCBrowserViewControllerDelegate) | [`Discover peers`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Discover-peers.md) |
| [`MCNearbyServiceAdvertiser`](https://developer.apple.com/documentation/MultipeerConnectivity/MCNearbyServiceAdvertiser) | [`Discover peers`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Discover-peers.md) |
| [`MCNearbyServiceAdvertiserDelegate`](https://developer.apple.com/documentation/MultipeerConnectivity/MCNearbyServiceAdvertiserDelegate) | [`Discover peers`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Discover-peers.md) |
| [`MCNearbyServiceBrowser`](https://developer.apple.com/documentation/MultipeerConnectivity/MCNearbyServiceBrowser) | [`Discover peers`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Discover-peers.md) |
| [`MCNearbyServiceBrowserDelegate`](https://developer.apple.com/documentation/MultipeerConnectivity/MCNearbyServiceBrowserDelegate) | [`Discover peers`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Discover-peers.md) |
| [`MCPeerID`](https://developer.apple.com/documentation/MultipeerConnectivity/MCPeerID) | [`Create a peer identifier`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Create-a-peer-identifier.md) |
| [`MCSession`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSession) | See below. |
| [`MCSessionDelegate`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSessionDelegate) | See below. |

Within [`MCSession`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSession):

| For symbol | See |
| --- | --- |
| [`cancelConnectPeer(_:)`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSession/cancelConnectPeer(_:)) | [`Manage a network connection`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Manage-a-network-connection.md) |
| [`connectedPeers`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSession/connectedPeers) | [`Manage a listener`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Manage-a-listener.md) |
| [`connectPeer(_:withNearbyConnectionData:)`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSession/connectPeer(_:withNearbyConnectionData:)) | [`Manage a network connection`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Manage-a-network-connection.md) |
| [`disconnect()`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSession/disconnect()) | [`Manage a network connection`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Manage-a-network-connection.md) |
| [`encryptionPreference`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSession/encryptionPreference) | [`Plan for security`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Plan-for-security.md) |
| [`myPeerID`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSession/myPeerID) | [`Create a peer identifier`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Create-a-peer-identifier.md) |
| [`nearbyConnectionData(forPeer:withCompletionHandler:)`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSession/nearbyConnectionData(forPeer:withCompletionHandler:)) | [`Discover peers`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Discover-peers.md) |
| [`securityIdentity`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSession/securityIdentity) | [`Plan for security`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Plan-for-security.md) |
| [`send(_:toPeers:with:)`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSession/send(_:toPeers:with:)) | [`Send and receive reliable messages`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Send-and-receive-reliable-messages.md) |
| [`sendResource(at:withName:toPeer:withCompletionHandler:)`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSession/sendResource(at:withName:toPeer:withCompletionHandler:)) | [`Send a resource`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Send-a-resource.md) |
| [`startStream(withName:toPeer:)`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSession/startStream(withName:toPeer:)) | [`Start a stream`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Start-a-stream.md) |

Within [`MCSessionDelegate`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSessionDelegate):

| For symbol | See |
| --- | --- |
| [`session(_:didFinishReceivingResourceWithName:fromPeer:at:withError:)`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSessionDelegate/session(_:didFinishReceivingResourceWithName:fromPeer:at:withError:)) | [`Send a resource`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Send-a-resource.md) |
| [`session(_:didReceive:fromPeer:)`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSessionDelegate/session(_:didReceive:fromPeer:)) | [`Send and receive reliable messages`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Send-and-receive-reliable-messages.md) |
| [`session(_:didReceive:withName:fromPeer:)`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSessionDelegate/session(_:didReceive:withName:fromPeer:)) | [`Start a stream`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Start-a-stream.md) |
| [`session(_:didReceiveCertificate:fromPeer:certificateHandler:)`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSessionDelegate/session(_:didReceiveCertificate:fromPeer:certificateHandler:)) | [`Plan for security`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Plan-for-security.md) |
| [`session(_:didStartReceivingResourceWithName:fromPeer:with:)`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSessionDelegate/session(_:didStartReceivingResourceWithName:fromPeer:with:)) | [`Send a resource`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Send-a-resource.md) |
| [`session(_:peer:didChange:)`](https://developer.apple.com/documentation/MultipeerConnectivity/MCSessionDelegate/session(_:peer:didChange:)) | [`Manage a network connection`](tn3213-moving-from-multipeer-connectivity-to-network-framework#Manage-a-network-connection.md) |

#### Revision History

- **2026-07-14** Republished as TN3213.  Updated to use the latest Network framework API and to focus on QUIC.
- **2025-03-07** First published as ”Moving from Multipeer Connectivity to Network Framework” on the Apple Developer Forums

## See Also

- [TN3210: Optimizing your app for iPhone Mirroring](tn3210-optimizing-your-app-for-iphone-mirroring.md)
  Test your app and improve compatibility with iPhone Mirroring.
- [TN3211: Resolving SwiftUI source incompatibilities for State and ContentBuilder](tn3211-resolving-swiftui-source-incompatibilities-for-state-and-contentbuilder.md)
  Update existing code for two foundational changes in SwiftUI built with Xcode 27.
- [TN3212: Adopting gesture recognizers for Sidecar touch support](tn3212-adopting-gesture-recognizers-for-sidecar-touch-support.md)
  Use gesture recognizers to handle Sidecar touch input and update your event-handling code for macOS 27.
- [TN3208: Preparing your app’s launch screen to meet App Store requirements](tn3208-preparing-your-apps-launch-screen-to-meet-app-store-requirements.md)
  Understand the launch screen requirement for App Store submission starting in iOS 27 and iPadOS 27.
- [TN3205: Low-latency communication with RDMA over Thunderbolt](tn3205-low-latency-communication-with-rdma-over-thunderbolt.md)
  Learn how to use RDMA over Thunderbolt to enable low-latency communication between clusters of Mac computers.
- [TN3206: Updating Apple Pay certificates](tn3206-updating-apple-pay-certificates.md)
  Learn how to create, manage, and rotate Apple Pay certificates to maintain uninterrupted payment processing.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3190: USB audio device design considerations](tn3190-usb-audio-device-design-considerations.md)
  Learn the best techniques for designing devices that conform to the USB Audio Device Class specifications.
- [TN3194: Handling account deletions and revoking tokens for Sign in with Apple](tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple.md)
  Learn the best techniques for managing Sign in with Apple user sessions and responding to account deletion requests.
- [TN3193: Managing the on-device foundation model’s context window](tn3193-managing-the-on-device-foundation-model-s-context-window.md)
  Learn how to budget for the context window limit of Apple’s on-device foundation model and handle the error when reaching the limit.
- [TN3115: Bluetooth State Restoration app relaunch rules](tn3115-bluetooth-state-restoration-app-relaunch-rules.md)
  Learn about the conditions under which an iOS app will be relaunched by Bluetooth State Restoration.
- [TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key](tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md)
  Support iPad multitasking and dynamic resizing while updating your app to remove the deprecated full-screen compatibility mode.
- [TN3151: Choosing the right networking API](tn3151-choosing-the-right-networking-api.md)
  Learn which networking API is best for you.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3191: IMAP extensions supported by Mail for iOS, iPadOS, and visionOS](tn3191-imap-extensions-supported-by-mail.md)
  Learn which extensions to the RFC 3501 IMAP protocol are supported by Mail for iOS, iPadOS, and visionOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3213-moving-from-multipeer-connectivity-to-network-framework)*