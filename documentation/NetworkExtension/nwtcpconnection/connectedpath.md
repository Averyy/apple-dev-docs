# connectedPath

**Framework**: Network Extension  
**Kind**: property

The network path over which the connection was established.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var connectedPath: NWPath? { get }
```

#### Discussion

The caller can query additional properties from the [`NWPath`](nwpath.md) object for more information. Note that this contains a snapshot of information at the time of connection establishment for this connection only. As a result, some underlying properties might change in time and might not reflect the path for other connections that might be established at different times.

## See Also

- [var endpoint: NWEndpoint](nwtcpconnection/endpoint.md)
  The destination endpoint with which this connection was created.
- [var localAddress: NWEndpoint?](nwtcpconnection/localaddress.md)
  The IP address endpoint from which the connection was established.
- [var remoteAddress: NWEndpoint?](nwtcpconnection/remoteaddress.md)
  The IP address endpoint to which the connection was established.
- [var txtRecord: Data?](nwtcpconnection/txtrecord.md)
  The TXT record associated with a connected Bonjour service endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnection/connectedpath)*