# remoteEndpoint

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

An [`NWEndpoint`](../nwendpoint.md) object containing information about the intended remote endpoint of the flow.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
var remoteEndpoint: NWEndpoint { get }
```

```objc
@property (readonly) NWEndpoint * remoteEndpoint;
```

## Discussion

If the flow’s corresponding socket was created using one of the high-level networking APIs such as [`URLSession`](../../Foundation/urlsession.md) or [`NSURLConnection`](../../Foundation/nsurlconnection.md), then the hostname property of the `remoteEndpoint` object contains the DNS name of the remote host. If the flow’s corresponding socket was created using the sockets API directly, then the hostname property of the `remoteEndpoint` object contains the IP address of the remote host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxytcpflow/remoteendpoint)*