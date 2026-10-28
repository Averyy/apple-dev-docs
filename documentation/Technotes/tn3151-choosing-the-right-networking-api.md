# TN3151: Choosing the right networking API

**Framework**: Technotes  
**Role**: Technote

Learn which networking API is best for you.

## Overview

Apple platforms have a wide range of networking APIs, spanning many different frameworks:

- [Foundation](../Foundation/Foundation.md)
- [Network](../Network/Network.md)
- BSD Sockets in the System framework
- And more

With all that choice, it’s hard to know where to start.  This technote aims to clarify that.  It makes specific recommendations as to which API to use for a given network protocol.  It then discusses [Alternative APIs](./tn3151-choosing-the-right-networking-api.md#Alternative-APIs) and some [Best practices](./tn3151-choosing-the-right-networking-api.md#Best-practices).

> ❗ **Important**: If you’re working on watchOS, read [TN3135: Low-level networking on watchOS](./tn3135-low-level-networking-on-watchos.md) to understand its unique constraints.

The focus here is on APIs that allow you to *use* the networking stack.  If you want to *extend* the networking stack—for example, to add support for a custom VPN protocol—implement a Network Extension provider.  For the details, see [Network Extension](../NetworkExtension/NetworkExtension.md).

## Recommendations by protocol

The following sections offer API recommendations for common network protocols.  Follow the advice for the protocol you’re using:

- **Application Layer:** [HTTP](./tn3151-choosing-the-right-networking-api.md#HTTP), [WebSocket](./tn3151-choosing-the-right-networking-api.md#WebSocket), [FTP](./tn3151-choosing-the-right-networking-api.md#FTP)
- **Transport Layer:** [QUIC](./tn3151-choosing-the-right-networking-api.md#QUIC), [TCP](./tn3151-choosing-the-right-networking-api.md#TCP), [UDP](./tn3151-choosing-the-right-networking-api.md#UDP)
- **Other:** [Bonjour service discovery](./tn3151-choosing-the-right-networking-api.md#Bonjour-service-discovery), [DNS](./tn3151-choosing-the-right-networking-api.md#DNS), [Peer-to-peer networking](./tn3151-choosing-the-right-networking-api.md#Peer-to-peer-networking), [Wi-Fi](./tn3151-choosing-the-right-networking-api.md#Wi-Fi)

### HTTP

For HTTP, including HTTPS, there’s one really good choice: Foundation’s [URL Loading System](../Foundation/url-loading-system.md), commonly known as `URLSession`.  It supports all the latest features, including Swift concurrency and the HTTP/2 and HTTP/3 protocols.

For more options, see [HTTP alternatives](./tn3151-choosing-the-right-networking-api.md#HTTP-alternatives).

`URLSession` background sessions allow your app to run an HTTP transfer that continues even if the app stops running.  This is most important on iOS, iPadOS, tvOS, watchOS, and visionOS, where the system suspends your app shortly after the user moves it to the background.  To learn more about this feature, see [Downloading files in the background](../Foundation/downloading-files-in-the-background.md).  Alternative HTTP APIs don’t support this feature.

### WebSocket

For WebSocket you have two choices:

- `URLSession` using [`URLSessionWebSocketTask`](../Foundation/urlsessionwebsockettask.md)
- [Network](../Network/Network.md) framework using a [connection API](./tn3151-choosing-the-right-networking-api.md#Network-framework-API-choices)

Unless you have a specific reason to use `URLSession`, use Network framework for new WebSocket code.

For more options, see [WebSocket alternatives](./tn3151-choosing-the-right-networking-api.md#WebSocket-alternatives).

### FTP

FTP is a very old and dilapidated protocol.  FTP is inappropriate to use on the modern internet because it provides *no* security.  Because of this, Apple has no supported FTP APIs.

Your best option here is to switch to a newer protocol, like HTTP.  It may require some coordination with your server folks, but that will pay off in the long term.

For other options, see [FTP alternatives](./tn3151-choosing-the-right-networking-api.md#FTP-alternatives).

### QUIC

[Network](../Network/Network.md) framework introduced QUIC support in [2021](./tn3151-choosing-the-right-networking-api.md#Versions).  It supports both QUIC client and QUIC server development.

The QUIC protocol has significant advantages over TCP.  If you’re building a custom network protocol, consider using QUIC instead of TCP.

> ❗ **Important**: QUIC is a key component of HTTP/3.  If your ultimate goal is to support HTTP/3, use `URLSession`.  It has direct support for HTTP/3.  Network framework’s QUIC support allows you to create custom network protocols running over QUIC.

### TCP

For TCP you have two reasonable options:

- [Network](../Network/Network.md) framework using a [connection API](./tn3151-choosing-the-right-networking-api.md#Network-framework-API-choices)
- BSD Sockets

Network framework is by far the best choice.  BSD Sockets is an acceptable choice if you have compatibility constraints, for example:

- When writing cross-platform code
- When using an existing library that’s based on BSD Sockets

For more options, see [TCP alternatives](./tn3151-choosing-the-right-networking-api.md#TCP-alternatives).  If you decide to use BSD Sockets, read [BSD Sockets best practices](./tn3151-choosing-the-right-networking-api.md#BSD-Sockets-best-practices).

### UDP

For UDP you have two reasonable options:

- [Network](../Network/Network.md) framework using a [connection API](./tn3151-choosing-the-right-networking-api.md#Network-framework-API-choices)
- BSD Sockets

For UDP flows—where you have a sequence of unicast datagrams flowing between two peers—Network framework is the best choice.  If you use BSD Sockets for this case, you’ll have to do a bunch of extra work.

However, not all UDP communication is that straightforward.  UDP also supports multicast, broadcast, and other asymmetric designs.  Network framework supports UDP multicast using the [`NWConnectionGroup`](../Network/nwconnectiongroup.md) class, but that support has limits and, specifically, it does not support UDP broadcast.  If you need something that’s not supported by Network framework, use BSD Sockets.

> **Note**: If you’re using UDP to implement a service discovery protocol, consider adopting Bonjour instead.  For more details, see [Bonjour service discovery](./tn3151-choosing-the-right-networking-api.md#Bonjour-service-discovery).

Regardless of the API you use, if you work with multicast or broadcast UDP on iOS, iPadOS, or visionOS, you must have the multicast networking entitlement.  For the details, see [`com.apple.developer.networking.multicast`](../BundleResources/entitlements/com.apple.developer.networking.multicast.md).

If your target platform supports local network privacy, multicast and broadcast require local network access.  For more on local network privacy, see [TN3179: Understanding local network privacy](./tn3179-understanding-local-network-privacy.md).

For more options, see [UDP alternatives](./tn3151-choosing-the-right-networking-api.md#UDP-alternatives).  If you decide to use BSD Sockets, read [BSD Sockets best practices](./tn3151-choosing-the-right-networking-api.md#BSD-Sockets-best-practices).

### Bonjour service discovery

Bonjour is an Apple term for three industry standard technologies: link-local addresses ([RFC 3927](http://www.ietf.org/rfc/rfc3927.txt)), multicast DNS ([RFC 6762](http://www.ietf.org/rfc/rfc6762.txt)), and DNS-based service discovery ([RFC 6763](http://www.ietf.org/rfc/rfc6763.txt)).  Use Bonjour to create network features that work well even if there’s no network infrastructure.  For example, when you browse for network servers using Finder > Go > Connect to Server, you’re using Bonjour.

Bonjour enables three fundamental operations:

- Advertise, to publish a service on the network so that clients can find it by browsing
- Browse, to browse for services on a network so that the user can choose a service
- Connect, to connect to a service chosen by the user

[Network](../Network/Network.md) framework is your best option for all three of these operations.

If you have specialist needs that aren’t covered by Network framework—for example, you want to resolve a service without connecting to it—use the low-level [dnssd](../dnssd/dnssd.md) API.

If your target platform supports local network privacy, declare your Bonjour service types in the [`NSBonjourServices`](../BundleResources/information-property-list/nsbonjourservices.md) property.  For more on local network privacy, see [TN3179: Understanding local network privacy](./tn3179-understanding-local-network-privacy.md).

For more options, see [Bonjour alternatives](./tn3151-choosing-the-right-networking-api.md#Bonjour-alternatives).

### Peer-to-peer networking

Peer-to-peer Wi-Fi allows you to communicate with nearby devices and accessories without configuring a Wi-Fi network.  Apple platforms support two peer-to-peer Wi-Fi technologies:

- Wi-Fi Aware™ (also known as Neighbor Awareness Networking or NAN)
- Apple peer-to-peer Wi-Fi

To get started with Wi-Fi Aware, see the [Wi-Fi Aware](../WiFiAware/WiFiAware.md) framework documentation.  Use this API to set up a peer-to-peer data path and then use a [Network framework connection API](./tn3151-choosing-the-right-networking-api.md#Network-framework-API-choices) for the actual data transfer.

Apple peer-to-peer Wi-Fi is directly supported by [Network](../Network/Network.md) framework.  Opt in to peer-to-peer Wi-Fi by setting the [`includePeerToPeer`](../Network/nwparameters/includepeertopeer.md) property of the parameters object you use to create your [connections and listeners](./tn3151-choosing-the-right-networking-api.md#Network-framework-API-choices).

> **Note**: The on-the-wire protocol used by Apple peer-to-peer Wi-Fi is not documented for third-party use, so this only works between Apple devices.

To communicate between a watchOS app and its companion iOS app, use [Watch Connectivity](../WatchConnectivity/WatchConnectivity.md).  In many cases, however, it might be better to have your watchOS app operate independently, using `URLSession` to communicate directly with your server.  For more about this concept, see [Creating independent watchOS apps](../watchOS-Apps/creating-independent-watchos-apps.md).

To connect a tvOS app to a mobile device on the local network, use [DeviceDiscoveryUI](../DeviceDiscoveryUI/DeviceDiscoveryUI.md).

If you’re developing a network-based accessory, consider using Thread.  For more background on this, see [ThreadNetwork](../ThreadNetwork/ThreadNetwork.md).

Some platforms limit access to the local network; for the details, see [TN3179: Understanding local network privacy](./tn3179-understanding-local-network-privacy.md).

For more options, see [Peer-to-peer alternatives](./tn3151-choosing-the-right-networking-api.md#Peer-to-peer-alternatives).

### DNS

In most cases you don’t need to resolve a DNS address manually.  Rather, use an API with connect-by-name semantics.  For more details, see [Connect by name](./tn3151-choosing-the-right-networking-api.md#Connect-by-name).

To perform advanced DNS operations using the system resolver, use the low-level [dnssd](../dnssd/dnssd.md) API.

To perform DNS queries without using the system resolver—for example, if you’re building a DNS debugging tool—use the `<dns.h>` and `<dns_util.h>` APIs.

> **Note**: The `<dns_util.h>` API was deprecated in [2022](./tn3151-choosing-the-right-networking-api.md#Versions).  There is no direct replacement.  If you need to parse DNS packets, look for a third-party DNS library.

For more options, see [DNS alternatives](./tn3151-choosing-the-right-networking-api.md#DNS-alternatives).

### Wi-Fi

iOS and iPadOS support a number of special-purpose Wi-Fi APIs.  For a summary, see [TN3111: iOS Wi-Fi API overview](./tn3111-ios-wifi-api-overview.md).

To scan for and configure Wi-Fi networks on macOS, use [Core WLAN](../CoreWLAN/CoreWLAN.md).

## Alternative APIs

Many protocols have alternative APIs, ones that are either deprecated or limited to some specific task.

### HTTP alternatives

Apple has two alternative HTTP APIs:

- [`NSURLConnection`](../Foundation/nsurlconnection.md) is the predecessor to `URLSession`.  It’s been redundant since the introduction of `URLSession` in [2013](./tn3151-choosing-the-right-networking-api.md#Versions).  It was formally deprecated in [2015](./tn3151-choosing-the-right-networking-api.md#Versions).  Don’t use it for new code.  If you have existing `NSURLConnection` code, make a plan to migrate to `URLSession`.
- `CFHTTPStream`, part of the CFNetwork framework, has been deprecated since [2015](./tn3151-choosing-the-right-networking-api.md#Versions).  Avoid using it in new code.  If you have existing `CFHTTPStream` code, make a plan to migrate to something more modern.  Typically, that’s `URLSession`.

In some very specific cases, you might find that `URLSession` doesn’t meet your needs.  In such cases, you might be able to work around that limitation using `CFHTTPStream`, or perhaps by building a simplistic HTTP client using `CFHTTPMessage` on top of a TCP API.  However, building a general-purpose HTTP client is hard.  If you need a general-purpose HTTP client and `URLSession` doesn’t work for you, look for a third-party HTTP library.  One good option is the [AsyncHTTPClient](https://github.com/swift-server/async-http-client) Swift library.

> ❗ **Important**: If you need to do some HTTP task that’s not supported by `URLSession`, let us know by [filing a suggestion](https://developer.apple.com/bug-reporting/) describing your requirements and why `URLSession` doesn’t work for you.

### WebSocket alternatives

Both of the recommended WebSocket APIs were introduced in [2015](./tn3151-choosing-the-right-networking-api.md#Versions).  If you need to support older OS releases, there are a variety of good quality third-party WebSocket libraries available for Apple platforms.

If you’re currently using a third-party WebSocket library, and your deployment target allows for it, consider moving to [Network](../Network/Network.md) framework.

### FTP alternatives

Apple has two FTP APIs:

- `URLSession` for FTP downloads, deprecated since [2022](./tn3151-choosing-the-right-networking-api.md#Versions)
- `CFFTPStream`, deprecated since [2016](./tn3151-choosing-the-right-networking-api.md#Versions)

Don’t write new code using them.  If you have existing code, you have two options.  The first, and by far the best, is to switch to a newer protocol, like HTTP.

In some circumstances that may not be possible.  Perhaps you’re working with an accessory that only supports FTP, and you’re unable to convince the vendor to update its firmware.  In that case, you have two options:

- Write your own FTP protocol implementation.
- Adopt a third-party FTP library.

> ❗ **Important**: When you evaluate a third-party FTP library, check that it implements FTP directly.  If the library uses `CFFTPStream` internally, there’s no point adopting it.

In `URLSession`, FTP downloads are only supported by the classic loading mode, as controlled by [`usesClassicLoadingMode`](../Foundation/urlsessionconfiguration/usesclassicloadingmode.md).

### TCP alternatives

Apple platforms support a variety of alternative TCP APIs:

- `CFSocketStream` was marked as to-be-deprecated in [2021](./tn3151-choosing-the-right-networking-api.md#Versions).  Apple will not enhance it to support new features.  For example, Apple added TLS 1.3 support to Network framework in [2019](./tn3151-choosing-the-right-networking-api.md#Versions), but has not added it to `CFSocketStream`.
- The TCP networking support in `NSStream`, most notably [`getStreamsToHost(withName:port:inputStream:outputStream:)`](../Foundation/stream/getstreamstohost%28withname,port,inputstream,outputstream%29.md), is layered on top of `CFSocketStream` and is on the same deprecation path.
- It’s possible to use [`FileHandle`](../Foundation/filehandle.md) for networking in conjunction with BSD Sockets.  While this is still supported, it’s not recommended for all the same reasons that BSD Sockets is not recommended.  See [BSD Sockets best practices](./tn3151-choosing-the-right-networking-api.md#BSD-Sockets-best-practices).
- [`CFSocket`](../CoreFoundation/cfsocket.md) is much like `FileHandle`: It’s possible to use it to run a TCP connection, but it has all the same limitations as BSD Sockets.
- [`URLSessionStreamTask`](../Foundation/urlsessionstreamtask.md) is much like `URLSessionWebSocketTask`: Unless you have a specific reason to use `URLSession`, use Network framework instead.
- Network Extension in-provider networking includes `NWTCPConnection`.  While there are some very limited circumstances where this is still useful, in most cases it’s better to use Network framework.  For more details, see [In-Provider Networking](../NetworkExtension/in-provider-networking.md).
- Foundation has a number of classes, like `NSConnection` and `NSSocketPort`, that *seem* like they might be useful for TCP networking.  They are not.  These are part of Foundation’s legacy Distributed Objects (DO) system.  DO was never a good choice for networking; moreover, it was formally deprecated in [2017](./tn3151-choosing-the-right-networking-api.md#Versions).

### UDP alternatives

Network Extension in-provider networking includes `NWUDPSession`.  While there are some very limited circumstances where this is still useful, in most cases it’s better to use Network framework.  For more details, see [In-Provider Networking](../NetworkExtension/in-provider-networking.md).

### Bonjour alternatives

There are two older Bonjour APIs:

- [`NetService`](../Foundation/netservice.md)
- [`CFNetService`](../CFNetwork/cfnetservice.md)

In [2021](./tn3151-choosing-the-right-networking-api.md#Versions) both of these were marked as to-be-deprecated in favor of Network framework.

### Peer-to-peer alternatives

[Multipeer Connectivity](../MultipeerConnectivity/MultipeerConnectivity.md) is a high-level API that supports Apple peer-to-peer Wi-Fi.  It was deprecated in [2026](./tn3151-choosing-the-right-networking-api.md#Versions).  Avoid using it in new code.  If you have existing Multipeer Connectivity code, think about whether it makes sense to migrate that code to Network framework.  For advice on how to do that, see [TN3213: Moving from Multipeer Connectivity to Network framework](./tn3213-moving-from-multipeer-connectivity-to-network-framework.md).

> ❗ **Important**: A common misconception is that Multipeer Connectivity is the only way to use Apple peer-to-peer Wi-Fi.  That’s not the case.  Network framework has opt-in peer-to-peer Wi-Fi support.  For the details, see [Peer-to-peer networking](./tn3151-choosing-the-right-networking-api.md#Peer-to-peer-networking).

Foundation also supports Apple peer-to-peer Wi-Fi:

- When advertising a service using `NSNetService`, set the [`includesPeerToPeer`](../Foundation/netservice/includespeertopeer.md) property.
- To accept connections, set the [`listenForConnections`](../Foundation/netservice/options/listenforconnections.md) flag and implement the [`netService(_:didAcceptConnectionWith:outputStream:)`](../Foundation/netservicedelegate/netservice%28_,didacceptconnectionwith,outputstream%29.md) delegate callback.
- When browsing for services using `NSNetServiceBrowser`, set the [`includesPeerToPeer`](../Foundation/netservicebrowser/includespeertopeer.md) property.
- After discovering a service with a peer-to-peer enabled browser, connect to that service using [`getInputStream(_:outputStream:)`](../Foundation/netservice/getinputstream%28_,outputstream%29.md).

These APIs were marked as to-be-deprecated in [2021](./tn3151-choosing-the-right-networking-api.md#Versions).  If you have existing code that uses them, make a plan to migrate to [Network](../Network/Network.md) framework.

The [dnssd](../dnssd/dnssd.md) API supports Apple peer-to-peer Wi-Fi but with an important caveat: If you advertise a service on peer-to-peer Wi-Fi using dnssd, the service’s listener must be run by a peer-to-peer aware API, like `NWListener` or `NSNetService`.  Given that those APIs already have a facility to opt in to Apple peer-to-peer Wi-Fi, there’s very little point using dnssd for this.

### DNS alternatives

`NSHost` supports synchronous DNS name-to-address and address-to-name translation.  It was only ever supported on macOS.

`CFHost` supports DNS name-to-address and address-to-name translation, both synchronously and asynchronously.

Both of these APIs were marked as to-be-deprecated in [2021](./tn3151-choosing-the-right-networking-api.md#Versions).  If you have existing code that uses them, make a plan to migrate to a preferred API.  In many cases that means switching to a connect-by-name API.  See [Connect by name](./tn3151-choosing-the-right-networking-api.md#Connect-by-name).  For other cases, see [DNS](./tn3151-choosing-the-right-networking-api.md#DNS).

## Best practices

Apple’s preferred networking APIs, including [`URLSession`](../Foundation/urlsession.md) and [Network](../Network/Network.md) framework, implement various best practices by default.  If you choose to use an alternative API, you take on the responsibility of implementing these best practices yourself.  This section addresses some of the more common issues.

### Connect by name

Traditionally, you connect to a TCP service using two steps:

1. Resolve the DNS name to a set of IPv4 and IPv6 addresses.
2. Connect to one of those addresses.

This two-step approach is an anti-pattern on Apple platforms for two reasons:

- It doesn’t support on-demand connections, such as VPN On Demand.
- It’s hard to implement the second step correctly.  The industry standard for this is called the *Happy Eyeballs* algorithm ([RFC 8305](https://tools.ietf.org/html/rfc8305)).  It’s a non-trivial amount of work.

Apple’s preferred networking APIs support connect-by-name semantics, where you pass the API a DNS name and it takes care of all the details.  If you can use a connect-by-name API, do that.  If you can’t—and the prime offender here is BSD Sockets—you’ll have to implement Happy Eyeballs yourself.

Sadly, even with all of that extra code, your program will still be incompatible with VPN On Demand.

### BSD Sockets best practices

BSD Sockets has a number of limitations.  Your life will be easier if you use [Network](../Network/Network.md) framework rather than BSD Sockets.  If that’s not possible—say you’re working on a cross-platform codebase that mandates the use of sockets—apply the following best practices:

- If you’re using BSD Sockets to implement a URL loading library, think about whether it should be subject to URL filtering.  If so, call [`NEURLFilter`](../NetworkExtension/neurlfilter.md) to determine whether to load the URL or not.
- Implement your own connect-by-name semantics.  If you don’t do this, your program might fail to connect, or connect very slowly, in adverse network conditions.  For more details, see [Connect by name](./tn3151-choosing-the-right-networking-api.md#Connect-by-name).
- For each socket that makes on outgoing connection, call `ne_socket_set_domains`, declared in `<networkext/ne_socket.h>`, to associated the socket with its original DNS name.  This gives network infrastructure, like content filters, more information about the context of the connection.
- Write code that supports both IPv4 and IPv6.  Test that code on an IPv6-only network.  See [Test for IPv6 DNS64/NAT64 Compatibility Regularly](https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/NetworkingOverview/UnderstandingandPreparingfortheIPv6Transition/UnderstandingandPreparingfortheIPv6Transition.html#//apple_ref/doc/uid/TP40010220-CH213-SW16).
- Use the system DNS resolver.  For more on this, see [DNS best practices](./tn3151-choosing-the-right-networking-api.md#DNS-best-practices).
- BSD Sockets does not support TLS directly.  If you want secure connections, and really you should, add your own TLS implementation.  For more on this, see [TLS best practices](./tn3151-choosing-the-right-networking-api.md#TLS-best-practices).
- Once you’ve established a connection, use [`SCNetworkReachabilityCreateWithAddressPair(_:_:_:)`](../SystemConfiguration/scnetworkreachabilitycreatewithaddresspair%28_,_,_%29.md) to monitor its viability.  Without this, your program won’t notice that a connection is stuck due to a TCP/IP stack reconfiguration.

> ❗ **Important**: If you don’t follow these best practices your networking code will fail in some specific network environments.  Such environments are hard to replicate at your workplace, so you might only notice the problem when your program fails after it’s been deployed.

> **Note**: While [`SCNetworkReachabilityCreateWithAddressPair(_:_:_:)`](../SystemConfiguration/scnetworkreachabilitycreatewithaddresspair%28_,_,_%29.md) is deprecated for most use cases, it’s still the best option for monitoring a socket’s viability (r. 158759893).

If your primary reason for using BSD Sockets is cross-platform support, consider using a network abstraction layer that adapts to the target platform.  One such option is [SwiftNIO Transport Services](https://github.com/apple/swift-nio-transport-services), which makes it straightforward to use Network framework on Apple platforms and BSD Sockets elsewhere.

Apple’s BSD Sockets implementation is documented in the man pages.  If you’re unfamiliar with that term, see https://developer.apple.com/documentation/os/reading-unix-manual-pages.  Man pages are notoriously succinct.  If you’re getting started with BSD Sockets, take advantage of the wide range of non-Apple resources out there.  A classic work in the field is the book *UNIX Network Programming* by Stevens et al.

One traditional challenge with BSD Sockets is how best to handle nonblocking sockets.  For cross-platform code you have all the usual options (`select`, `poll`, `kqueue`).  For Apple-specific code you have one more: a Dispatch read source.  Use this to integrate a nonblocking socket into existing code that uses Dispatch queues.  For more details, see [Dispatch Source](../Dispatch/dispatch-source.md).

> **Note**: If you’re using [`CFSocket`](../CoreFoundation/cfsocket.md) to handle a nonblocking socket, consider switching to a Dispatch read source.

### DNS best practices

Use the system DNS resolver.  Implementing your own DNS resolver is extra work, wastes resources, and causes problems in specific network environments.

If you’re using BSD Sockets, use the `getaddrinfo` and `getnameinfo` APIs.  BSD Sockets has a range of legacy DNS APIs, like `gethostbyname`, that embody known anti-patterns.  For example, `gethostbyname` doesn’t support IPv6 and relies on thread-local storage.

Also use `getaddrinfo` and `getnameinfo` to convert between strings and IP addresses.  Again, the legacy APIs for this have various problems.  For example, `inet_addr` doesn’t support IPv6 and relies on thread-local storage.  When converting an IP address to a string, pass `AI_NUMERICHOST` and `AI_NUMERICSERV` to `getaddrinfo` to ensure that it doesn’t generate any network traffic.  Likewise, when going the other way, pass `NI_NUMERICHOST` and `NI_NUMERICSERV` to `getnameinfo`.

If you’re using BSD Sockets and want to resolve a DNS address asynchronously, use [`DNSServiceGetAddrInfo(_:_:_:_:_:_:_:)`](../dnssd/dnsservicegetaddrinfo%28_,_,_,_,_,_,_%29.md).

### TLS best practices

Apple’s preferred networking APIs, including [`URLSession`](../Foundation/urlsession.md) and [Network](../Network/Network.md) framework, use a built-in, modern TLS stack.  That’s not available if you use BSD Sockets.  To use TLS in that case, add your own TLS implementation.

Make sure your TLS implementation uses Apple’s trust evaluation infrastructure.  If you implement your own trust evaluation, it won’t match that of the built-in apps, like Safari and Mail.  For more about Apple’s trust evaluation APIs, see [Trust](../Security/trust.md).

Don’t use [Secure Transport](../Security/secure-transport.md) for your TLS implementation.  It’s been deprecated since [2019](./tn3151-choosing-the-right-networking-api.md#Versions) and doesn’t support TLS 1.3.  If you have existing code that uses Secure Transport, make a plan to migrate off it.

### Network framework API choices

Network framework supports three APIs:

| Language | Connection type | Listener type | Introduced |
| --- | --- | --- | --- |
| C | [`nw_connection_t`](../Network/nw_connection_t.md) | [`nw_listener_t`](../Network/nw_listener_t.md) | [2019](./tn3151-choosing-the-right-networking-api.md#Versions) |
| Swift (old) | [`NWConnection`](../Network/nwconnection.md) | [`NWListener`](../Network/nwlistener.md) | [2019](./tn3151-choosing-the-right-networking-api.md#Versions) |
| Swift (new) | [`NetworkConnection`](../Network/networkconnection.md) | [`NetworkListener`](../Network/networklistener.md) | [2025](./tn3151-choosing-the-right-networking-api.md#Versions) |

Use the C API for all C-based languages, including C, Objective-C, and C++.

The new Swift API is tightly integrated with the Swift type system and fully supports structured concurrency.

## Versions

Networking is fundamental to all Apple platforms.  When Apple introduces a new networking API, or adds new support to an existing API, it typically does so on all platforms.  Likewise when Apple deprecates an API.  When this technote covers such topics, it references the year of the OS release.  The following table maps years to OS version numbers:

| Year | macOS | iOS, iPadOS, tvOS | watchOS | visionOS |
| --- | --- | --- | --- | --- |
| 2013 | 10.9 | 7 | - | - |
| 2014 | 10.10 | 8 | 1 | - |
| 2015 | 10.11 | 9 | 2 | - |
| 2016 | 10.12 | 10 | 3 | - |
| 2017 | 10.13 | 11 | 4 | - |
| 2018 | 10.14 | 12 | 5 | - |
| 2019 | 10.15 | 13 | 6 | - |
| 2020 | 11 | 14 | 7 | - |
| 2021 | 12 | 15 | 8 | - |
| 2022 | 13 | 16 | 9 | - |
| 2023 | 14 | 17 | 10 | 1 |
| 2024 | 15 | 18 | 11 | 2 |
| 2025 | 26 | 26 | 26 | 26 |
| 2026 | 27 | 27 | 27 | 27 |

## Revision History

- **2026-07-23** Updated the discussion of Multipeer Connectivity to account for its recent deprecation.  Made other minor editorial changes.
- **2025-09-05** Added links to [TN3179: Understanding local network privacy](./tn3179-understanding-local-network-privacy.md).  Added links to the Network framework Swift API introduced in 2025.  Added information about Wi-Fi Aware.  Updated “BSD Sockets best practices” to discuss `NEURLFilter` and `ne_socket_set_domains`.  Updated the version list.  Made other editorial changes.
- **2023-09-19** Added information about `CFSocket`.
- **2023-06-06** First published.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3151-choosing-the-right-networking-api)*