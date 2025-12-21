# TN3151: Choosing the right networking API

**Framework**: Technotes

Learn which networking API is best for you.

#### Overview

Apple platforms have a wide range of networking APIs, spanning many different frameworks:

- [`Foundation`](https://developer.apple.com/documentation/Foundation)
- [`Network`](https://developer.apple.com/documentation/Network)
- BSD Sockets in the System framework
- And more

With all that choice, it’s hard to know where to start.  This technote aims to clarify that.  It makes specific recommendations as to which API to use for a given network protocol.  It then discusses [`Alternative APIs`](tn3151-choosing-the-right-networking-api#Alternative-APIs.md) and some [`Best practices`](tn3151-choosing-the-right-networking-api#Best-practices.md).

> ❗ **Important**: If you’re working on watchOS, read [`TN3135: Low-level networking on watchOS`](tn3135-low-level-networking-on-watchos.md) to understand its unique constraints.

The focus here is on APIs that allow you to  the networking stack.  If you want to  the networking stack—for example, to add support for a custom VPN protocol—implement a Network Extension provider.  For the details, see [`Network Extension`](https://developer.apple.com/documentation/NetworkExtension).

#### Recommendations By Protocol

This section lists API recommendations for common network protocols.  Follow the advice for the protocol you’re using:

-  [`HTTP`](tn3151-choosing-the-right-networking-api#HTTP.md), [`WebSocket`](tn3151-choosing-the-right-networking-api#WebSocket.md), [`FTP`](tn3151-choosing-the-right-networking-api#FTP.md)
-  [`QUIC`](tn3151-choosing-the-right-networking-api#QUIC.md), [`TCP`](tn3151-choosing-the-right-networking-api#TCP.md), [`UDP`](tn3151-choosing-the-right-networking-api#UDP.md)
-  [`Bonjour service discovery`](tn3151-choosing-the-right-networking-api#Bonjour-service-discovery.md), [`DNS`](tn3151-choosing-the-right-networking-api#DNS.md), [`Peer-to-peer networking`](tn3151-choosing-the-right-networking-api#Peer-to-peer-networking.md), [`Wi-Fi`](tn3151-choosing-the-right-networking-api#Wi-Fi.md)

##### Http

For HTTP, including HTTPS, there is one really good choice: Foundation’s [`URL Loading System`](https://developer.apple.com/documentation/Foundation/url-loading-system), commonly known as `URLSession`.  It supports all the latest features, including Swift concurrency and the HTTP/2 and HTTP/3 protocols.

For more options, see [`HTTP alternatives`](tn3151-choosing-the-right-networking-api#HTTP-alternatives.md).

`URLSession` background sessions allow your app to run an HTTP transfer that continues even if the app stops running.  This is most important on iOS, tvOS, and watchOS, where the system suspends your app shortly after the user moves it to the background.  To learn more about this feature, see [`Downloading files in the background`](https://developer.apple.com/documentation/Foundation/downloading-files-in-the-background).  Alternative HTTP APIs don’t support this feature.

##### Websocket

For WebSocket you have two choices:

- `URLSession` using [`URLSessionWebSocketTask`](https://developer.apple.com/documentation/Foundation/URLSessionWebSocketTask)
- [`Network`](https://developer.apple.com/documentation/Network) framework using a [`Network framework API choices`](tn3151-choosing-the-right-networking-api#Network-framework-API-choices.md)

Unless you have a specific reason to use `URLSession`, use Network framework for new WebSocket code.

For more options, see [`WebSocket alternatives`](tn3151-choosing-the-right-networking-api#WebSocket-alternatives.md).

##### Ftp

FTP is a very old and dilapidated protocol.  FTP is inappropriate to use on the modern internet because it provides  security.  Because of this, Apple has no supported FTP APIs.

Your best option here is to switch to a newer protocol, like HTTP.  It may require some coordination with your server folks, but that will pay off in the long term.

For other options, see [`FTP alternatives`](tn3151-choosing-the-right-networking-api#FTP-alternatives.md).

##### Quic

[`Network`](https://developer.apple.com/documentation/Network) framework introduced QUIC support in [`Versions`](tn3151-choosing-the-right-networking-api#Versions.md).  It supports both QUIC client and QUIC server development.

The QUIC protocol has significant advantages over TCP.  If you’re building a custom network protocol, consider using QUIC instead of TCP.

> ❗ **Important**: QUIC is a key component of HTTP/3.  If your ultimate goal is to support HTTP/3, use `URLSession`.  It has direct support for HTTP/3.  Network framework’s QUIC support allows you to create custom network protocols running over QUIC.

##### Tcp

For TCP you have two reasonable options:

- [`Network`](https://developer.apple.com/documentation/Network) framework using a [`Network framework API choices`](tn3151-choosing-the-right-networking-api#Network-framework-API-choices.md)
- BSD Sockets

Network framework is by far the best choice.  BSD Sockets is an acceptable choice if you have compatibility constraints, for example:

- When writing cross-platform code
- When using an existing library that’s based on BSD Sockets

For more options, see [`TCP alternatives`](tn3151-choosing-the-right-networking-api#TCP-alternatives.md).  If you decide to use BSD Sockets, read [`BSD Sockets best practices`](tn3151-choosing-the-right-networking-api#BSD-Sockets-best-practices.md).

##### Udp

For UDP you have two reasonable options:

- [`Network`](https://developer.apple.com/documentation/Network) framework using a [`Network framework API choices`](tn3151-choosing-the-right-networking-api#Network-framework-API-choices.md)
- BSD Sockets

For UDP flows—where you have a stream of unicast datagrams flowing between two peers—Network framework is the best choice.  If you use BSD Sockets for this case, you’ll have to do a bunch of extra work.

However, not all UDP communication is that straightforward.  UDP also supports multicast, broadcast, and other asymmetric designs.  Network framework supports UDP multicast using the [`NWConnectionGroup`](https://developer.apple.com/documentation/Network/NWConnectionGroup) class, but that support has limits and, specifically, it does not support UDP broadcast.  If you need something that’s not supported by Network framework, use BSD Sockets.

> **Note**: If you’re using UDP to implement a service discovery protocol, consider adopting Bonjour instead.  For more details, see [`Bonjour service discovery`](tn3151-choosing-the-right-networking-api#Bonjour-service-discovery.md).

Regardless of the API you use, if you work with multicast or broadcast UDP on iOS, iPadOS, or visionOS, you must have the multicast networking entitlement.  For the details, see [`com.apple.developer.networking.multicast`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.networking.multicast).

If your target platform supports local network privacy, multicast and broadcast require local network access.  For more on local network privacy, see [`TN3179: Understanding local network privacy`](tn3179-understanding-local-network-privacy.md).

For more options, see [`UDP alternatives`](tn3151-choosing-the-right-networking-api#UDP-alternatives.md).  If you decide to use BSD Sockets, read [`BSD Sockets best practices`](tn3151-choosing-the-right-networking-api#BSD-Sockets-best-practices.md).

##### Bonjour Service Discovery

Bonjour is an Apple term for three industry standard technologies: link-local addresses ([`RFC 3927`](https://developer.apple.comhttp://www.ietf.org/rfc/rfc3927.txt)), multicast DNS ([`RFC 6762`](https://developer.apple.comhttp://www.ietf.org/rfc/rfc6762.txt)), and DNS-based service discovery ([`RFC 6763`](https://developer.apple.comhttp://www.ietf.org/rfc/rfc6763.txt)).  Use Bonjour to create network features that work well even if there’s no network infrastructure.  For example, when you browse for network servers using Finder > Go > Connect to Server, you’re using Bonjour.

Bonjour enables three fundamental operations:

- Advertise, to publish a service on the network so that clients can find it by browsing
- Browse, to browse for services on a network so that the user can choose a service
- Connect, to connect to a service chosen by the user

[`Network`](https://developer.apple.com/documentation/Network) framework is your best option for all three of these operations.

If you have specialist needs that aren’t covered by Network framework—for example, you want to resolve a service without connecting to it—use the low-level [`dnssd`](https://developer.apple.com/documentation/dnssd) API.

If your target platform supports local network privacy, declare your Bonjour service types in the [`NSBonjourServices`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSBonjourServices) property.  For more on local network privacy, see [`TN3179: Understanding local network privacy`](tn3179-understanding-local-network-privacy.md).

For more options, see [`Bonjour alternatives`](tn3151-choosing-the-right-networking-api#Bonjour-alternatives.md).

##### Peer to Peer Networking

Peer-to-peer Wi-Fi allows you to communicate with nearby devices and accessories without configuring a Wi-Fi network.  Apple platforms support two peer-to-peer Wi-Fi technologies:

- Wi-Fi Aware™ (also known as Neighbor Awareness Networking or NAN)
- Apple peer-to-peer Wi-Fi

To get started with Wi-Fi Aware, see the [`Wi-Fi Aware`](https://developer.apple.com/documentation/WiFiAware) framework documentation.  Use this API to set up a peer-to-peer data path and then use a [`Network framework API choices`](tn3151-choosing-the-right-networking-api#Network-framework-API-choices.md) for the actual data transfer.

Apple peer-to-peer Wi-Fi is directly supported by [`Network`](https://developer.apple.com/documentation/Network) framework.  Opt in to peer-to-peer Wi-Fi by setting the [`includePeerToPeer`](https://developer.apple.com/documentation/Network/NWParameters/includePeerToPeer) property of the parameters object you use to create your [`Network framework API choices`](tn3151-choosing-the-right-networking-api#Network-framework-API-choices.md).

> **Note**: The on-the-wire protocol used by Apple peer-to-peer Wi-Fi is not documented for third-party use, so this only works between Apple devices.

To communicate between a watchOS app and its companion iOS app, use [`Watch Connectivity`](https://developer.apple.com/documentation/WatchConnectivity).  In many cases, however, it might be better to have your watchOS app operate independently, using `URLSession` to communicate directly with your server.

To connect a tvOS app to a mobile device on the local network, use [`DeviceDiscoveryUI`](https://developer.apple.com/documentation/DeviceDiscoveryUI).

If you’re developing a network-based accessory, consider using Thread.  For more background on this, see [`ThreadNetwork`](https://developer.apple.com/documentation/ThreadNetwork).

Some platforms limit access to the local network; for the details, see [`TN3179: Understanding local network privacy`](tn3179-understanding-local-network-privacy.md).

For more options, see [`Peer-to-peer alternatives`](tn3151-choosing-the-right-networking-api#Peer-to-peer-alternatives.md).

##### Dns

In most cases you don’t need to resolve a DNS address manually.  Rather, use an API with connect-by-name semantics.  For more details, see [`Connect by name`](tn3151-choosing-the-right-networking-api#Connect-by-name.md).

To perform advanced DNS operations using the system resolver, use the low-level [`dnssd`](https://developer.apple.com/documentation/dnssd) API.

To perform DNS queries without using the system resolver—for example, if you’re building a DNS debugging tool—use the `<dns.h>` and `<dns_util.h>` APIs.

> **Note**: The `<dns_util.h>` API was deprecated in [`Versions`](tn3151-choosing-the-right-networking-api#Versions.md).  There is no direct replacement.  If you need to parse DNS packets, look for a third-party DNS library.

For more options, see [`DNS alternatives`](tn3151-choosing-the-right-networking-api#DNS-alternatives.md).

##### Wi Fi

iOS supports a number of special-purpose Wi-Fi APIs.  For a summary, see [`TN3111: iOS Wi-Fi API overview`](tn3111-ios-wifi-api-overview.md).

To scan for and configure Wi-Fi networks on macOS, use [`Core WLAN`](https://developer.apple.com/documentation/CoreWLAN).

#### Alternative Apis

Many protocols have alternative APIs, ones that are either deprecated or limited to some specific task.

##### Http Alternatives

Apple has two alternative HTTP APIs:

- [`NSURLConnection`](https://developer.apple.com/documentation/Foundation/NSURLConnection) is the predecessor to `URLSession`.  It’s been redundant since the introduction of `URLSession` in [`Versions`](tn3151-choosing-the-right-networking-api#Versions.md).  It was formally deprecated in [`Versions`](tn3151-choosing-the-right-networking-api#Versions.md).  Don’t use it for new code.  If you have existing `NSURLConnection` code, make a plan to migrate to `URLSession`.
- `CFHTTPStream`, part of the CFNetwork framework, has been deprecated since [`Versions`](tn3151-choosing-the-right-networking-api#Versions.md).  Avoid using it in new code.  If you have existing `CFHTTPStream` code, make a plan to migrate to something more modern.  Typically, that’s `URLSession`.

In some very specific cases, you might find that `URLSession` doesn’t meet your needs.  In such cases, you might be able to work around that limitation using `CFHTTPStream`, or perhaps by building a simplistic HTTP client using `CFHTTPMessage` on top of a TCP API.  However, building a general-purpose HTTP client is hard.  If you need a general-purpose HTTP client and `URLSession` doesn’t work for you, look for a third-party HTTP library.  One good option is the [`AsyncHTTPClient`](https://developer.apple.comhttps://github.com/swift-server/async-http-client) Swift library.

> ❗ **Important**: If you need to do some HTTP task that’s not supported by `URLSession`, let us know by [`filing a suggestion`](https://developer.apple.comhttps://developer.apple.com/bug-reporting/) describing your requirements and why `URLSession` doesn’t work for you.

##### Websocket Alternatives

Both of the recommended WebSocket APIs were introduced in [`Versions`](tn3151-choosing-the-right-networking-api#Versions.md).  If you need to support older OS releases, there are a variety of good quality third-party WebSocket libraries available for Apple platforms.

If you’re currently using a third-party WebSocket library, and your deployment target allows for it, consider moving to [`Network`](https://developer.apple.com/documentation/Network) framework.

##### Ftp Alternatives

Apple has two FTP APIs:

- `URLSession` for FTP downloads, deprecated since [`Versions`](tn3151-choosing-the-right-networking-api#Versions.md)
- `CFFTPStream`, deprecated since [`Versions`](tn3151-choosing-the-right-networking-api#Versions.md)

Don’t write new code using them.  If you have existing code, you have two options.  The first, and by far the best, is to switch to a newer protocol, like HTTP.

In some circumstances that may not be possible.  Perhaps you’re working with an accessory that only supports FTP, and you’re unable to convince the vendor to update its firmware.  In that case, you have two options:

- Write your own FTP protocol implementation.
- Adopt a third-party FTP library.

> ❗ **Important**: When you evaluate a third-party FTP library, check that it implements FTP directly.  If the library uses `CFFTPStream` internally, there’s no point adopting it.

In `URLSession`, FTP downloads are only supported by the classic loading mode, as controlled by [`usesClassicLoadingMode`](https://developer.apple.com/documentation/Foundation/URLSessionConfiguration/usesClassicLoadingMode).

##### Tcp Alternatives

Apple platforms support a variety of alternative TCP APIs:

- `CFSocketStream` was marked as to-be-deprecated in [`Versions`](tn3151-choosing-the-right-networking-api#Versions.md).  Apple will not enhance it to support new features.  For example, Apple added TLS 1.3 support to Network framework in [`Versions`](tn3151-choosing-the-right-networking-api#Versions.md), but has not added it to `CFSocketStream`.
- The TCP networking support in `NSStream`, most notably [`getStreamsToHost(withName:port:inputStream:outputStream:)`](https://developer.apple.com/documentation/Foundation/Stream/getStreamsToHost(withName:port:inputStream:outputStream:)), is layered on top of `CFSocketStream` and is on the same deprecation path.
- It’s possible to use [`FileHandle`](https://developer.apple.com/documentation/Foundation/FileHandle) for networking in conjunction with BSD Sockets.  While this is still supported, it’s not recommended for all the same reasons that BSD Sockets is not recommended.  See [`BSD Sockets best practices`](tn3151-choosing-the-right-networking-api#BSD-Sockets-best-practices.md).
- [`CFSocket`](https://developer.apple.com/documentation/CoreFoundation/CFSocket) is much like `FileHandle`: It’s possible to use it to run a TCP connection, but it has all the same limitations as BSD Sockets.
- [`URLSessionStreamTask`](https://developer.apple.com/documentation/Foundation/URLSessionStreamTask) is much like `URLSessionWebSocketTask`: Unless you have a specific reason to use `URLSession`, use Network framework instead.
- Network Extension in-provider networking includes `NWTCPConnection`.  While there are some very limited circumstances where this is still useful, in most cases it’s better to use Network framework.  For more details, see [`In-Provider Networking`](https://developer.apple.com/documentation/NetworkExtension/in-provider-networking).
- Foundation has a number of classes, like `NSConnection` and `NSSocketPort`, that  like they might be useful for TCP networking.  They are not.  These are part of Foundation’s legacy Distributed Objects (DO) system.  DO was never a good choice for networking; moreover, it was formally deprecated in [`Versions`](tn3151-choosing-the-right-networking-api#Versions.md).

##### Udp Alternatives

Network Extension in-provider networking includes `NWUDPSession`.  While there are some very limited circumstances where this is still useful, in most cases it’s better to use Network framework.  For more details, see [`In-Provider Networking`](https://developer.apple.com/documentation/NetworkExtension/in-provider-networking).

##### Bonjour Alternatives

There are two older Bonjour APIs:

- [`NetService`](https://developer.apple.com/documentation/Foundation/NetService)
- [`CFNetService`](https://developer.apple.com/documentation/CFNetwork/CFNetService)

In [`Versions`](tn3151-choosing-the-right-networking-api#Versions.md) both of these were marked as to-be-deprecated in favor of Network framework.

##### Peer to Peer Alternatives

[`Multipeer Connectivity`](https://developer.apple.com/documentation/MultipeerConnectivity) is a high-level API that supports Apple peer-to-peer Wi-Fi.  It includes:

- A very opinionated networking model, where every participant in a session is a symmetric peer
- User interface components for advertising and joining a session

Use it when your requirements are aligned with those features.  Don’t use it if your program uses a client/server architecture; Network framework works better in that case.  For an example, see [`Building a custom peer-to-peer protocol`](https://developer.apple.com/documentation/Network/building-a-custom-peer-to-peer-protocol).

> ❗ **Important**: A common misconception is that Multipeer Connectivity is the only way to use Apple peer-to-peer Wi-Fi.  That’s not the case.  Network framework has opt-in peer-to-peer Wi-Fi support.  For the details, see [`Peer-to-peer networking`](tn3151-choosing-the-right-networking-api#Peer-to-peer-networking.md).

Foundation also supports Apple peer-to-peer Wi-Fi:

- When advertising a service using `NSNetService`, set the [`includesPeerToPeer`](https://developer.apple.com/documentation/Foundation/NetService/includesPeerToPeer) property.
- To accept connections, set the [`listenForConnections`](https://developer.apple.com/documentation/Foundation/NetService/Options/listenForConnections) flag and implement the [`netService(_:didAcceptConnectionWith:outputStream:)`](https://developer.apple.com/documentation/Foundation/NetServiceDelegate/netService(_:didAcceptConnectionWith:outputStream:)) delegate callback.
- When browsing for services using `NSNetServiceBrowser`, set the [`includesPeerToPeer`](https://developer.apple.com/documentation/Foundation/NetServiceBrowser/includesPeerToPeer) property.
- After discovering a service with a peer-to-peer enabled browser, connect to that service using [`getInputStream(_:outputStream:)`](https://developer.apple.com/documentation/Foundation/NetService/getInputStream(_:outputStream:)).

These APIs were marked as to-be-deprecated in [`Versions`](tn3151-choosing-the-right-networking-api#Versions.md).  If you have existing code that uses them, make a plan to migrate to [`Network`](https://developer.apple.com/documentation/Network) framework.

The [`dnssd`](https://developer.apple.com/documentation/dnssd) API supports Apple peer-to-peer Wi-Fi but with an important caveat: If you advertise a service on peer-to-peer Wi-Fi using dnssd, the service’s listener must be run by a peer-to-peer aware API, like `NWListener` or `NSNetService`.  Given that those APIs already have a facility to opt in to Apple peer-to-peer Wi-Fi, there’s very little point using dnssd for this.

##### Dns Alternatives

`NSHost` supports synchronous DNS name-to-address and address-to-name translation.  It was only ever supported on macOS.

`CFHost` supports DNS name-to-address and address-to-name translation, both synchronously and asynchronously.

Both of these APIs were marked as to-be-deprecated in [`Versions`](tn3151-choosing-the-right-networking-api#Versions.md).  If you have existing code that uses them, make a plan to migrate to a preferred API.  In many cases that means switching to a connect-by-name API.  See [`Connect by name`](tn3151-choosing-the-right-networking-api#Connect-by-name.md).  For other cases, see [`DNS`](tn3151-choosing-the-right-networking-api#DNS.md).

#### Best Practices

Apple’s preferred networking APIs, including [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) and [`Network`](https://developer.apple.com/documentation/Network) framework, implement various best practices by default.  If you choose to use an alternative API, you take on the responsibility of implementing these best practices yourself.  This section addresses some of the more common issues.

##### Connect By Name

Traditionally, you connect to a TCP service using two steps:

1. Resolve the DNS name to a set of IPv4 and IPv6 addresses.
2. Connect to one of those addresses.

This two-step approach is an anti-pattern on Apple platforms for two reasons:

- It doesn’t support on-demand connections, such as VPN On Demand.
- It’s hard to implement the second step correctly.  The industry standard for this is called the  algorithm ([`RFC 8305`](https://developer.apple.comhttps://tools.ietf.org/html/rfc8305)).  It’s a non-trivial amount of work.

Apple’s preferred networking APIs support connect-by-name semantics, where you pass the API a DNS name and it takes care of all the details.  If you can use a connect-by-name API, do that.  If you can’t—and the prime offender here is BSD Sockets—you’ll have to implement Happy Eyeballs yourself.

Sadly, even with all of that extra code, your program will still be incompatible with VPN On Demand.

##### Bsd Sockets Best Practices

BSD Sockets has a number of limitations.  Your life will be easier if you use [`Network`](https://developer.apple.com/documentation/Network) framework rather than BSD Sockets.  If that’s not possible—say you’re working on a cross-platform codebase that mandates the use of sockets—apply the following best practices:

- If you’re using BSD Sockets to implement a URL loading library, think about whether it should be subject to URL filtering.  If so, call [`NEURLFilter`](https://developer.apple.com/documentation/NetworkExtension/NEURLFilter) to determine whether to load the URL or not.
- Implement your own connect-by-name semantics.  If you don’t do this, your program might fail to connect, or connect very slowly, in adverse network conditions.  For more details, see [`Connect by name`](tn3151-choosing-the-right-networking-api#Connect-by-name.md).
- For each socket that makes on outgoing connection, call `ne_socket_set_domains`, declared in `<networkext/ne_socket.h>`, to associated the socket with its original DNS name.  This gives network infrastructure, like content filters, more information about the context of the connection.
- Write code that supports both IPv4 and IPv6.  Test that code on an IPv6-only network.  See [`Test for IPv6 DNS64/NAT64 Compatibility Regularly`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/NetworkingOverview/UnderstandingandPreparingfortheIPv6Transition/UnderstandingandPreparingfortheIPv6Transition.html#//apple_ref/doc/uid/TP40010220-CH213-SW16).
- Use the system DNS resolver.  For more on this, see [`DNS best practices`](tn3151-choosing-the-right-networking-api#DNS-best-practices.md).
- BSD Sockets does not support TLS directly.  If you want secure connections, and really you should, add your own TLS implementation.  For more on this, see [`TLS best practices`](tn3151-choosing-the-right-networking-api#TLS-best-practices.md).
- Once you’ve established a connection, use [`SCNetworkReachabilityCreateWithAddressPair(_:_:_:)`](https://developer.apple.com/documentation/SystemConfiguration/SCNetworkReachabilityCreateWithAddressPair(_:_:_:)) to monitor its viability.  Without this, your program won’t notice that a connection is stuck due to a TCP/IP stack reconfiguration.

> ❗ **Important**: If you don’t follow these best practices your networking code will fail in some specific network environments.  Such environments are hard to replicate at your workplace, so you might only notice the problem when your program fails after it’s been deployed.

> **Note**: While [`SCNetworkReachabilityCreateWithAddressPair(_:_:_:)`](https://developer.apple.com/documentation/SystemConfiguration/SCNetworkReachabilityCreateWithAddressPair(_:_:_:)) is deprecated for most use cases, it’s still the best option for monitoring a socket’s viability (r. 158759893).

If your primary reason for using BSD Sockets is cross-platform support, consider using a network abstraction layer that adapts to the target platform.  One such option is [`SwiftNIO Transport Services`](https://developer.apple.comhttps://github.com/apple/swift-nio-transport-services), which makes it straightforward to use Network framework on Apple platforms and BSD Sockets elsewhere.

Apple’s BSD Sockets implementation is documented in the man pages.  If you’re unfamiliar with that term, see [`Reading UNIX Manual Pages`](https://developer.apple.com/documentation/os/reading-unix-manual-pages).  Man pages are notoriously succinct.  If you’re getting started with BSD Sockets, take advantage of the wide range of non-Apple resources out there.  A classic work in the field is the book  by Stevens et al.

One traditional challenge with BSD Sockets is how best to handle nonblocking sockets.  For cross-platform code you have all the usual options (`select`, `poll`, `kqueue`).  For Apple-specific code you have one more: a Dispatch read source.  Use this to integrate a nonblocking socket into existing code that uses Dispatch queues.  For more details, see [`Dispatch Source`](https://developer.apple.com/documentation/Dispatch/dispatch-source).

> **Note**: If you’re using [`CFSocket`](https://developer.apple.com/documentation/CoreFoundation/CFSocket) to handle a nonblocking socket, consider switching to a Dispatch read source.

##### Dns Best Practices

Use the system DNS resolver.  Implementing your own DNS resolver is extra work, wastes resources, and causes problems in specific network environments.

If you’re using BSD Sockets, use the `getaddrinfo` and `getnameinfo` APIs.  BSD Sockets has a range of legacy DNS APIs, like `gethostbyname`, that embody known anti-patterns.  For example, `gethostbyname` doesn’t support IPv6 and relies on thread-local storage.

Also use `getaddrinfo` and `getnameinfo` to convert between strings and IP addresses.  Again, the legacy APIs for this have various problems.  For example, `inet_addr` doesn’t support IPv6 and relies on thread-local storage.  When converting an IP address to a string, pass `AI_NUMERICHOST` and `AI_NUMERICSERV` to `getaddrinfo` to ensure that it doesn’t generate any network traffic.  Likewise, when going the other way, pass `NI_NUMERICHOST` and `NI_NUMERICSERV` to `getnameinfo`.

If you’re using BSD Sockets and want to resolve a DNS address asynchronously, use [`DNSServiceGetAddrInfo(_:_:_:_:_:_:_:)`](https://developer.apple.com/documentation/dnssd/DNSServiceGetAddrInfo(_:_:_:_:_:_:_:)).

##### Tls Best Practices

Apple’s preferred networking APIs, including [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) and [`Network`](https://developer.apple.com/documentation/Network) framework, use a built-in, modern TLS stack.  That’s not available if you use BSD Sockets.  To use TLS in that case, add your own TLS implementation.

Make sure your TLS implementation uses Apple’s trust evaluation infrastructure.  If you implement your own trust evaluation, it won’t match that of the built-in apps, like Safari and Mail.  For more about Apple’s trust evaluation APIs, see [`Trust`](https://developer.apple.com/documentation/Security/trust).

Don’t use [`Secure Transport`](https://developer.apple.com/documentation/Security/secure-transport) for your TLS implementation.  It’s been deprecated since [`Versions`](tn3151-choosing-the-right-networking-api#Versions.md) and doesn’t support TLS 1.3.  If you have existing code that uses Secure Transport, make a plan to migrate off it.

##### Network Framework Api Choices

Network framework supports three APIs:

| Language | Connection type | Listener type | Introduced |
| --- | --- | --- | --- |
| C | [`nw_connection_t`](https://developer.apple.com/documentation/Network/nw_connection_t) | [`nw_listener_t`](https://developer.apple.com/documentation/Network/nw_listener_t) | [`Versions`](tn3151-choosing-the-right-networking-api#Versions.md) |
| Swift (old) | [`NWConnection`](https://developer.apple.com/documentation/Network/NWConnection) | [`NWListener`](https://developer.apple.com/documentation/Network/NWListener) | [`Versions`](tn3151-choosing-the-right-networking-api#Versions.md) |
| Swift (new) | [`NetworkConnection`](https://developer.apple.com/documentation/Network/NetworkConnection) | [`NetworkListener`](https://developer.apple.com/documentation/Network/NetworkListener) | [`Versions`](tn3151-choosing-the-right-networking-api#Versions.md) |

Use the C API for all C-based languages, including C, Objective-C, and C++.

The new Swift API is tightly integrated with the Swift type system and fully supports structured concurrency.

#### Versions

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

#### Revision History

-  Added links to [`TN3179: Understanding local network privacy`](tn3179-understanding-local-network-privacy.md).  Added links to the Network framework Swift API introduced in 2025.  Added information about Wi-Fi Aware.  Updated “BSD Sockets best practices” to discuss `NEURLFilter` and `ne_socket_set_domains`.  Updated the version list.  Made other editorial changes.
-  Added information about `CFSocket`.
-  First published.

## See Also

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
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3191: IMAP extensions supported by Mail for iOS, iPadOS, and visionOS](tn3191-imap-extensions-supported-by-mail.md)
  Learn which extensions to the RFC 3501 IMAP protocol are supported by Mail for iOS, iPadOS, and visionOS.
- [TN3134: Network Extension provider deployment](tn3134-network-extension-provider-deployment.md)
  Explore the platforms, packaging, OS versions, and device configurations for Network Extension provider deployment.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3151-choosing-the-right-networking-api)*