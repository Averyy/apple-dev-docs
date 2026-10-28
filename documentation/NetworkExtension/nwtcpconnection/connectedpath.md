# connectedPath

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The network path over which the connection was established.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_connection_copy_current_path(_:)`](../../Network/nw_connection_copy_current_path%28_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
var connectedPath: NWPath? { get }
```

```objc
@property (nonatomic, readonly, nullable) NWPath * connectedPath;
```

## Discussion

The caller can query additional properties from the [`NWPath`](../nwpath.md) object for more information. Note that this contains a snapshot of information at the time of connection establishment for this connection only. As a result, some underlying properties might change in time and might not reflect the path for other connections that might be established at different times.

## See Also

### Getting connection properties
- [var endpoint: NWEndpoint](./endpoint.md)
  The destination endpoint with which this connection was created.
- [var localAddress: NWEndpoint?](./localaddress.md)
  The IP address endpoint from which the connection was established.
- [var remoteAddress: NWEndpoint?](./remoteaddress.md)
  The IP address endpoint to which the connection was established.
- [var txtRecord: Data?](./txtrecord.md)
  The TXT record associated with a connected Bonjour service endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnection/connectedpath)*