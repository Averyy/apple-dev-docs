# txtRecord

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The TXT record associated with a connected Bonjour service endpoint.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_endpoint_copy_txt_record(_:)`](../../Network/nw_endpoint_copy_txt_record%28_%29.md) function from the [Network](../../Network/Network.md) framework instead.

## Declaration

```swift
var txtRecord: Data? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSData * txtRecord;
```

#### Discussion

When the connection is connected to a Bonjour service endpoint, the TXT record associated with the Bonjour service is available via this property.

> ❗ **Important**:  Note that the value comes from an untrusted network source. Care must be taken when parsing this potentially malicious value.

## See Also

### Getting connection properties
- [var endpoint: NWEndpoint](./endpoint.md)
  The destination endpoint with which this connection was created.
- [var localAddress: NWEndpoint?](./localaddress.md)
  The IP address endpoint from which the connection was established.
- [var remoteAddress: NWEndpoint?](./remoteaddress.md)
  The IP address endpoint to which the connection was established.
- [var connectedPath: NWPath?](./connectedpath.md)
  The network path over which the connection was established.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnection/txtrecord)*