# remoteEndpoint

**Framework**: Network Extension  
**Kind**: property

An [`NWEndpoint`](nwendpoint.md) object containing information about the intended remote endpoint of the flow.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var remoteEndpoint: NWEndpoint { get }
```

#### Discussion

If the flow’s corresponding socket was created using one of the high-level networking APIs such as [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) or [`NSURLConnection`](https://developer.apple.com/documentation/Foundation/NSURLConnection), then the hostname property of the `remoteEndpoint` object contains the DNS name of the remote host. If the flow’s corresponding socket was created using the sockets API directly, then the hostname property of the `remoteEndpoint` object contains the IP address of the remote host.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxytcpflow/remoteendpoint)*