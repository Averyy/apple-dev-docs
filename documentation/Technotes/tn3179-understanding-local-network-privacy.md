# TN3179: Understanding local network privacy

**Framework**: Technotes

Learn how local network privacy affects your software.

#### Overview

Local network privacy puts people in control of which programs can interact with devices on their network.  The first time a program accesses the local network, the system displays an alert asking the user to approve that access.  The system records their decision, so future accesses don’t prompt.

To learn more, see:

- WWDC 2020 Session 10110: [`Support local network privacy in your app`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2020/10110/), which introduced the feature on iOS
- WWDC 2024 Session 10123: [`What’s new in privacy`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2024/10123/), which introduced the feature on macOS
- [`If an app would like to connect to devices on your local network`](https://developer.apple.comhttps://support.apple.com/en-us/102229), which explains local network privacy to people who use iOS

Users configure local network privacy in Settings > Privacy & Security > Local Network (System Settings on macOS).  The OS adds an app to this list after it attempts to access a local network.

Device managers aren’t able to configure local network privacy using MDM.

The following platforms support local network privacy:

| Platform | Supported | Introduced |
| --- | --- | --- |
| iOS | yes | iOS 14 |
| iPadOS | yes | iPadOS 14 |
| macOS | yes | macOS 15 |
| tvOS | no | - |
| visionOS | yes | visionOS 1 |
| watchOS | no | - |

Local network privacy works the same on iOS, iPadOS, and visionOS.  Unless otherwise noted, assume that any info about iOS applies to all three platforms.  See [`iOS considerations`](tn3179-understanding-local-network-privacy#iOS-considerations.md) for information specific to these three platforms.

Local network privacy on macOS shares all of the same core concepts, but there are platform-specific differences.  See [`macOS considerations`](tn3179-understanding-local-network-privacy#macOS-considerations.md) for more on this.

#### Essentials

Local network privacy regulates your program’s ability to perform local network operations.  If your program has local network access, the system allows the operation.  If not, the system blocks it.

> **Note**: See [`Local network operations`](tn3179-understanding-local-network-privacy#Local-network-operations.md) for more precise definitions of  and .

See [`Local network operations`](tn3179-understanding-local-network-privacy#Local-network-operations.md) for more precise definitions of  and .

In most cases, the user controls local network access by way of the Local Network privilege.  This has three states:

- Undetermined
- Allowed
- Denied

Your program starts in the undetermined state.  The first time it performs a local network operation, the system presents the local network alert.  The user chooses to either allow or deny the access.  The system records the user’s choice and applies it to subsequent operations.  The user can change this state at any time in Settings.

> **Note**: Some programs have local network access based on factors other than the Local Network privilege.  For the details, see [`App extension considerations`](tn3179-understanding-local-network-privacy#App-extension-considerations.md) and [`macOS considerations`](tn3179-understanding-local-network-privacy#macOS-considerations.md).

Some programs have local network access based on factors other than the Local Network privilege.  For the details, see [`App extension considerations`](tn3179-understanding-local-network-privacy#App-extension-considerations.md) and [`macOS considerations`](tn3179-understanding-local-network-privacy#macOS-considerations.md).

If your app accesses the local network, add the [`NSLocalNetworkUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocalNetworkUsageDescription) property to its `Info.plist` to explain its behavior to the user.

If your app allows people to enter an arbitrary network address, consider what happens if they enter a local network address.  For example, if you’re building an email client, check that it behaves correctly when the email server is on a local network.

If your app’s local network usage involves registering or browsing for specific Bonjour services, add a list of service types to the [`NSBonjourServices`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSBonjourServices) property in your app’s `Info.plist`.  For more information about the Bonjour operations that require this, see [`Bonjour operations`](tn3179-understanding-local-network-privacy#Bonjour-operations.md) below.

Additionally, if your iOS app performs multicast operations, sign it with the [`com.apple.developer.networking.multicast`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.networking.multicast) entitlement.  For information about what constitutes a multicast operation, see [`Multicast operations`](tn3179-understanding-local-network-privacy#Multicast-operations.md) below.  If you use Xcode’s automatic code signing, use the [`Capabilities`](https://developer.apple.com/documentation/Xcode/capabilities) editor to enable this capability.  If not, see [`Developer Account > Reference > Provisioning with capabilities`](https://developer.apple.comhttps://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities).

> ❗ **Important**: The multicast entitlement isn’t required on macOS.

The multicast entitlement isn’t required on macOS.

If you’re building an app extension, see [`App extension considerations`](tn3179-understanding-local-network-privacy#App-extension-considerations.md).

If you’re building some other sort of program for macOS—a `launchd` daemon or agent, a system extension, and so on—see [`macOS considerations`](tn3179-understanding-local-network-privacy#macOS-considerations.md).

If the system presents a local network alert in response to one of your local network operations, it may deny the operation immediately, before the user has responded to the alert.  To handle this smoothly, use an API that supports waiting for connectivity, like Network framework or `URLSession` with [`waitsForConnectivity`](https://developer.apple.com/documentation/foundation/urlsessionconfiguration/2908812-waitsforconnectivity) enabled.  If you can’t use one of these preferred APIs, add appropriate retry logic.

For an overview of the networking APIs on Apple platforms, see [`TN3151: Choosing the right networking API`](tn3151-choosing-the-right-networking-api.md).

#### Local Network Operations

A local network is an IP network associated with a broadcast-capable network interface.  Such interfaces include Wi-Fi and Ethernet, but not cellular (WWAN) or VPN.  A local network address is any address on a local network.  Traffic to a local network address goes directly; it’s not forwarded by a router.

In addition, all multicast addresses (224.0.0.0/4, ff00::/8) and the IPv4 broadcast address (255.255.255.255) are local network addresses.

Outgoing traffic to a local network address requires local network access.  The following table lists some common cases:

| Operation | Required |
| --- | --- |
| Making an outgoing TCP connection | yes |
| Listening for and accepting incoming TCP connections | no |
| Sending a UDP unicast | yes |
| Sending a UDP multicast | yes |
| Sending a UDP broadcast | yes |
| Connecting a UDP socket | yes |
| Receiving an incoming UDP unicast | no |
| Receiving an incoming UDP multicast | yes |
| Receiving an incoming UDP broadcast | yes |

The system implements these TCP and UDP checks deep in the networking stack, and thus they apply to all networking APIs.  This includes [`Network`](https://developer.apple.com/documentation/Network) framework, BSD Sockets, [`URL Loading System`](https://developer.apple.com/documentation/Foundation/url-loading-system), and any APIs implemented on top of those.

Note these exceptions to the rules above:

- If your device’s DNS server is on a local network, traffic to it doesn’t require local network access.
- If your device uses a network proxy and that proxy is on a local network, traffic to it doesn’t require local network access.
- Traffic originating from [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView), [`SFSafariViewController`](https://developer.apple.com/documentation/SafariServices/SFSafariViewController), and Safari doesn’t require local network access.

#### Dns Operations

Certain DNS operations also require local network access.  The following table lists some common cases:

| Operation | Required |
| --- | --- |
| Resolving a local DNS name | yes |
| Resolving a non-local DNS name with the system resolver | no |

This check applies to a wide variety of APIs including [`dnssd`](https://developer.apple.com/documentation/dnssd), `<net_db.h>`, and any APIs that use them.

In this context, a local DNS name is one ending with `.local` (or `.local.`), per [`RFC 6762`](https://developer.apple.comhttps://tools.ietf.org/html/rfc6762).

Additionally, Bonjour operations require local network access, as described in the next section.

#### Bonjour Operations

All Bonjour operations require local network access.

| Operation | Required |
| --- | --- |
| Registering a service with Bonjour | yes |
| Browsing for Bonjour services | yes |
| Resolving a Bonjour service | yes |

These checks apply to all APIs that use Bonjour, including [`dnssd`](https://developer.apple.com/documentation/dnssd), [`Network`](https://developer.apple.com/documentation/Network) framework, and Multipeer Connectivity.

> **Note**: If you’re using Multipeer Connectivity, see [`Multipeer Connectivity considerations`](tn3179-understanding-local-network-privacy#Multipeer-Connectivity-considerations.md).

If you’re using Multipeer Connectivity, see [`Multipeer Connectivity considerations`](tn3179-understanding-local-network-privacy#Multipeer-Connectivity-considerations.md).

High-level services that use Bonjour internally don’t require local network access.  That’s because these services isolate your app from any details about the local network.  Such services include:

| Operation | Required |
| --- | --- |
| AirPlay | no |
| Printing via UIKit | no |
| DeviceDiscoveryUI | no |
| AccessorySetupKit | no |

Some specific Bonjour operations require the multicast entitlement as well.   See the next section for the details.

#### Multicast Operations

Sending or receiving multicast or broadcast traffic is a local network operation on all platforms, as described in [`Local network operations`](tn3179-understanding-local-network-privacy#Local-network-operations.md).  However, iOS puts additional restrictions on these operations.  To send or receive multicast or broadcast traffic, sign your app with the [`com.apple.developer.networking.multicast`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.networking.multicast) entitlement.

The following table lists some common cases.

| Operation | Required |
| --- | --- |
| Sending a UDP unicast | no |
| Sending a UDP multicast | yes |
| Sending a UDP broadcast | yes |
| Receiving an incoming UDP unicast | no |
| Receiving an incoming UDP multicast | yes |
| Receiving an incoming UDP broadcast | yes |

Some uncommon Bonjour operations also require the multicast entitlement.

| Operation | Required |
| --- | --- |
| Working with arbitrary Bonjour service types | yes |
| Browsing for all advertised service types | yes |

For information on how to browse for all advertised service types using a `_services._dns-sd._udp.local.` query, see QA1337 [`Discovering all advertised Bonjour service types`](https://developer.apple.comhttps://developer.apple.com/library/archive/qa/qa1337/_index.html).

#### Multipeer Connectivity Considerations

[`Multipeer Connectivity`](https://developer.apple.com/documentation/MultipeerConnectivity) uses Bonjour internally.  If your app uses Multipeer Connectivity, follow all the Bonjour guidance in this technote.

Specifically, list your Multipeer Connectivity service type in the [`NSBonjourServices`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSBonjourServices) property.  To format that entry, take your Multipeer Connectivity service type and add a leading underscore (`_`) and a trailing `._tcp`.  For example, if you pass `waffle-varnish` to the `serviceType` parameter of [`init(serviceType:discoveryInfo:session:)`](https://developer.apple.com/documentation/MultipeerConnectivity/MCAdvertiserAssistant/init(serviceType:discoveryInfo:session:)), add `_waffle-varnish._tcp` to the [`NSBonjourServices`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSBonjourServices) property.

#### App Extension Considerations

In general, app extensions share the Local Network privilege state of their container app.

Some app extension types are assumed to be running in the background.  If such an extension performs a local network operation while its Local Network privilege is undetermined, the system denies that operation as it would for an iOS app running in the background.  For more on that, see [`iOS considerations`](tn3179-understanding-local-network-privacy#iOS-considerations.md).

Network Extension packet tunnel provider, app proxy provider, and DNS proxy provider app extensions have local network access regardless of the Local Network privilege state of their container app.

If your app has app extensions, add the [`NSLocalNetworkUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocalNetworkUsageDescription) and [`NSBonjourServices`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSBonjourServices) properties to the app’s `Info.plist`, not to the app extension’s.

#### Ios Considerations

If an iOS app is in the background and performs a local network operation while its Local Network privilege is undetermined, the system denies that operation without presenting the local network alert.  The system doesn’t record that decision.  If, later on, the app performs a local network operation while in the foreground, the system presents the alert to the user as if this were the first local network operation.

App Clips can’t perform local network operations.  See [`Choosing the right functionality for your App Clip`](https://developer.apple.com/documentation/AppClip/choosing-the-right-functionality-for-your-app-clip).

The simulator doesn’t support local network privacy.  Test your local network privacy behavior on a real device.

On Shared iPad, all users share the same local network privacy state.

It  possible for your app to trigger the local network alert when the device is “off Wi-Fi”, that is, when there’s no Wi-Fi symbol in the status bar.  An easy way to demonstrate this is to perform a Bonjour operation with peer-to-peer Wi-Fi enabled, but there lots of other ways this can happen.

The above is true regardless of whether the device has cellular networking or not.

For more information about peer-to-peer Wi-Fi, see [`TN3151: Choosing the right networking API`](tn3151-choosing-the-right-networking-api.md).

#### Macos Considerations

macOS maintains separate local network privacy state for each user account.

macOS automatically allows local network access by:

- Any daemon started by `launchd`
- Any program running as root
- Command-line tools run from Terminal or over SSH, including any child processes they spawn

> ❗ **Important**: The exception for `launchd` daemons doesn’t apply to `launchd` agents.  If you’re building a `launchd` agent, see the discussion below.

The exception for `launchd` daemons doesn’t apply to `launchd` agents.  If you’re building a `launchd` agent, see the discussion below.

If you’re creating some other type of program, expect the system to block its local network operations until the user grants it the Local Network privilege.

When a process performs a local network operation, macOS tries to track down the responsible code.  For example, if your app spawns a helper tool and the helper tool performs a local network operation, macOS considers the app to be the responsible code.

macOS uses the responsible code to:

- Show a meaningful app name and usage description in the local network alert
- Record the user’s choice for the whole app, not just that specific helper tool
- Present that choice in System Settings

If you ship a `launchd` agent that’s not installed using `SMAppService`, make macOS aware of the responsible code by setting the `AssociatedBundleIdentifiers` property in your `launchd` property list.  See the `launchd.plist` man page for details.  For information on how to access that documentation, see [`Reading UNIX Manual Pages`](https://developer.apple.com/documentation/os/reading-unix-manual-pages).

Most standalone executables—that is, executables that aren’t the main executable for a bundle—don’t need the [`NSLocalNetworkUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocalNetworkUsageDescription) property because they’re either:

- Automatically allowed local network access, for example, daemons and command-line tools
- Have an app that acts as their responsible code, for example, a helper tool

If you manage to create a standalone executable that does need the [`NSLocalNetworkUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocalNetworkUsageDescription) property, add it to an `Info.plist` that’s embedded in your executable.  In Xcode, set this up using the  [`Build settings reference`](https://developer.apple.com/documentation/Xcode/build-settings-reference) build setting.

macOS 15.1 fixed a number of local network privacy bugs.  If you encounter local network privacy problems on macOS 15.0, retest on macOS 15.1 or later.

People might see unexpected behavior in System Settings > Privacy & Security if they have multiple versions of the same app installed (FB15568200).

For the latest news about local network privacy, see the [`macOS Release Notes`](https://developer.apple.com/documentation/macos-release-notes).

#### Build Time Considerations

Local network privacy uses your main executable UUID as part of its implementation.  If your main executable has no UUID, or shares a UUID with other programs, local network privacy may behave weirdly.  To fix that, make sure your main executable has a UUID and that it’s unique.  For more about this, see [`TN3178: Checking for and resolving build UUID problems`](tn3178-checking-for-and-resolving-build-uuid-problems.md).

#### Reset Local Network State

During testing, you might want to reset your program’s Local Network privilege to the undetermined state.  Your options for this vary by platform.

On iOS, the easiest option is to delete your app.

Alternatively, if you don’t want to delete your app for some reason, reset the entire privacy subsystem using Settings > General > Transfer or Reset > Reset > Reset Location & Privacy.

On macOS there’s no way to reset your program’s Local Network privilege to the undetermined state (FB14944392).  One alternative is to run your program in a virtual machine (VM).  To retest, restore the VM from a snapshot taken before you installed your program.

Alternatively, create a new user account and run your test there.  Remember that macOS maintains separate local network privacy state for each user account.

#### Trigger the Local Network Alert

You don’t need to do anything special to bring up the local network alert.  The system displays it automatically when your program performs a local network operation.  In most cases that’s the correct behavior.  The user is more likely to grant your program the Local Network privilege if they understand the context of the request.

However, in specific circumstances it may be necessary to manually bring up the local network privacy alert.  For example, the user might have configured your program to perform a local network operation at some point in the future, when they’re not able to respond to the alert.

There’s no API to explicitly bring up the local network alert (FB8711182), but you can do this implicitly by performing a local network operation.  One approach that works well is to connect a UDP socket to a local network address.  This triggers the local network alert without generating any network traffic.

The following code shows how to do this in a general fashion:

```swift
/// Attempts to trigger the local network privacy alert.
/// 
/// This builds a list of link-local IPv6 addresses and then creates a connected
/// UDP socket to each in turn.  Connecting a UDP socket triggers the local
/// network alert without actually sending any traffic.
/// 
/// This is a ‘best effort’ approach, and it handles errors by ignoring them.
/// There’s no guarantee that it’ll actually trigger the alert (FB8711182).

func triggerLocalNetworkPrivacyAlert() {
    let addresses = selectedLinkLocalIPv6Addresses()
    for address in addresses {
        let sock6 = socket(AF_INET6, SOCK_DGRAM, 0)
        guard sock6 >= 0 else { return }
        defer { close(sock6) }

        withUnsafePointer(to: address) { sa6 in
            sa6.withMemoryRebound(to: sockaddr.self, capacity: 1) { sa in
                _ = connect(sock6, sa, socklen_t(sa.pointee.sa_len)) >= 0
            }
        }
    }
}

/// Returns a selection of IPv6 addresses to connect to.
///
/// To build this list it:
///
/// 1. Finds the IPv6 address of every broadcast-capable interface.
///
/// 2. Filters out all the ones that aren’t link-local.
///
/// 3. Sets the port number to port 9, that is, the discard service.  Even
///    though the caller won’t actually send any traffic, this ensures that it
///    would be discarded if it were sent.
///
/// 4. Creates two copies of each address, and replaces the host part with a
///    random number.

private func selectedLinkLocalIPv6Addresses() -> [sockaddr_in6]
{
    let r1 = (0..<8).map { _ in UInt8.random(in: 0...255) }
    let r2 = (0..<8).map { _ in UInt8.random(in: 0...255) }
    return Array(ipv6AddressesOfBroadcastCapableInterfaces()
        .filter { isIPv6AddressLinkLocal($0) }
        .map { var addr = $0 ; addr.sin6_port = UInt16(9).bigEndian ; return addr }
        .map { [setIPv6LinkLocalAddressHostPart(of: $0, to: r1), setIPv6LinkLocalAddressHostPart(of: $0, to: r2)] }
        .joined())
}

/// Replaces the host part of an IPv6 link-local address with the supplied
/// value.
///
/// In this context, _host part_ refers to the bottom 64-bits of the address,
/// that is, the `interface ID` as defined in Section 2.5.6 of [RFC
/// 4291](https://tools.ietf.org/html/rfc4291)).  Thus, the host part parameter
/// must be exactly 8 bytes.

private func setIPv6LinkLocalAddressHostPart(of address: sockaddr_in6, to hostPart: [UInt8]) -> sockaddr_in6 {
    precondition(hostPart.count == 8)
    var result = address
    withUnsafeMutableBytes(of: &result.sin6_addr) { buf in
        buf[8...].copyBytes(from: hostPart)
    }
    return result
}

/// Returns whether the supplied IPv6 address is link-local.
///
/// Link-local address have the fe:c0/10 prefix.

private func isIPv6AddressLinkLocal(_ address: sockaddr_in6) -> Bool {
    address.sin6_addr.__u6_addr.__u6_addr8.0 == 0xfe
        && (address.sin6_addr.__u6_addr.__u6_addr8.1 & 0xc0) == 0x80
}

/// Returns the IPv6 address of every broadcast-capable interface.

private func ipv6AddressesOfBroadcastCapableInterfaces() -> [sockaddr_in6] {
    var addrList: UnsafeMutablePointer<ifaddrs>? = nil
    let err = getifaddrs(&addrList)
    guard err == 0, let start = addrList else { return [] }
    defer { freeifaddrs(start) }
    return sequence(first: start, next: { $0.pointee.ifa_next })
        .compactMap { i -> sockaddr_in6? in
            guard
                (i.pointee.ifa_flags & UInt32(bitPattern: IFF_BROADCAST)) != 0,
                let sa = i.pointee.ifa_addr,
                sa.pointee.sa_family == AF_INET6,
                sa.pointee.sa_len >= MemoryLayout<sockaddr_in6>.size
            else { return nil }
            return UnsafeRawPointer(sa).load(as: sockaddr_in6.self)
        }
}
```

#### Check for Local Network Access

There’s no general API that returns whether the current process has local network access (FB8711182).  There are, however, a couple of techniques you can use in specific circumstances.

If you’re using Bonjour, check whether your operation is waiting with the `kDNSServiceErr_PolicyDenied` (-65570) error.  For example, for an `NWBrowser` object, your state update handler might look like this:

```swift
 browser.stateUpdateHandler = { state in
    switch state {
    case .waiting(let error):
        switch error {
        case .dns(let code):
            switch Int(code) {
            case kDNSServiceErr_PolicyDenied:
                … no local network access …
            …
            }
        …
        }
    …
    }
}
```

If your goal is to make a TCP connection to a local network address, manage that connection with [`NWConnection`](https://developer.apple.com/documentation/Network/NWConnection).  If your program doesn’t have local network access, the connection enters the [`NWConnection.State.waiting(_:)`](https://developer.apple.com/documentation/Network/NWConnection/State-swift.enum/waiting(_:)) state and the current path lists an unsatisfied reason of [`NWPath.UnsatisfiedReason.localNetworkDenied`](https://developer.apple.com/documentation/Network/NWPath/UnsatisfiedReason-swift.enum/localNetworkDenied).  To check for that:

```swift
let connection: NWConnection = … your existing logic …
connection.stateUpdateHandler = { state in
    switch state {
    case .waiting(_):
        if case .localNetworkDenied? = connection.currentPath?.unsatisfiedReason {
            … no local network access …
        }
    … other states …
    }
}
```

If the user subsequently changes the Local Network privilege to grant your program local network access, the system automatically retries the connection.

If your program successfully made a TCP connection to a local network address and then the user changed the Local Network privilege to deny it local network access, the connection closes.  When you open a new connection, it enters the [`NWConnection.State.waiting(_:)`](https://developer.apple.com/documentation/Network/NWConnection/State-swift.enum/waiting(_:)) state as described above.

If these techniques don’t meet all of your requirements, file an [`enhancement request`](https://developer.apple.comhttps://developer.apple.com/bug-reporting/) with the details.

#### Unexpected Local Network Alert

In most cases it’s easy to understand why you’re seeing the local network alert.  You do something in your program that performs a local network operation, and the system presents the alert.

However, in some cases the local network alert shows up unexpectedly.  A common cause of this is third-party libraries, where a library performs a local network operation for no obvious reason.  For example, a library might access the local network as soon as you initialize it.

There’s no direct way to track down unexpected local network operations.  Your best option is to remove code from your program until it stops presenting the local network alert.  Once that happens, add smaller chunks of code back into your program to home in on the cause.

That process might lead to a third-party library for which you don’t have the source code.  If that happens, raise this issue with the library’s vendor.

#### Identify the Wi Fi Interface Correctly

Some iOS apps assume that the Wi-Fi interface name is always `en0`.  This isn’t a valid assumption.  BSD interface names, like `en0`, aren’t considered API on any Apple platform.  If you write code based on this false assumption and deploy your app to a wide range of users, your app will fail for a small fraction of those users.

The reports from these users might suggest that local network privacy is misbehaving.  For example, a user might report that they did a local network operation and no local network alert showed up.  However, local network privacy is working correctly.  The real problem is that you’re assuming that `en0` is the Wi-Fi interface, and it isn’t.

> ❗ **Important**: To avoid problems like this, don’t hard code BSD interface names like `en0`.

To avoid problems like this, don’t hard code BSD interface names like `en0`.

In many cases you can avoid this problem by reworking your code.  For example, if you’re building a custom service discovery protocol on top of UDP broadcasts, life will be easier if you use Bonjour instead.  For more information about Bonjour, see [`TN3151: Choosing the right networking API`](tn3151-choosing-the-right-networking-api.md).

If you can’t use Bonjour—perhaps you’re working with an accessory with legacy firmware—run your service discovery code on  broadcast-capable interfaces.  Not only does that avoid this problem, but folks who have their devices plugged into Ethernet will love you forever!

If you must work with a specific type of interface, call `getifaddrs` to get the full interface list and then filter that list by the interface type.  Get the functional type of the interface using the `SIOCGIFFUNCTIONALTYPE` ioctl.

#### Revision History

-  Rewritten and republished as TN3179.
-  First posted as the  on the Apple Developer Forums.

## See Also

- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.
- [TN3181: Debugging an invalid privacy manifest](tn3181-debugging-invalid-privacy-manifest.md)
  Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
- [TN3180: Reverting to App Store Server Notifications V1](tn3180-reverting-app-store-server-notifications-v1.md)
  Migrate from version 2 to version 1 of App Store Server Notifications using the Modify an App endpoint.
- [TN3178: Checking for and resolving build UUID problems](tn3178-checking-for-and-resolving-build-uuid-problems.md)
  Ensure that every Mach-O image has a UUID, and that every distinct Mach-O image has its own unique UUID.
- [TN3177: Understanding alternate audio track groups in movie files](tn3177-understanding-alternate-audio-track-groups-in-movie-files.md)
  Learn how alternate groups collect audio tracks, and how to choose which audio track to use in your app.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.
- [TN3175: Diagnosing issues with displaying the Apple Pay button on your website](tn3175-diagnosing-issues-with-displaying-the-apple-pay-button-on-your-website.md)
  Diagnose common errors received while displaying the Apple Pay button on your website by identifying the underlying causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3179-understanding-local-network-privacy)*