# txtRecord

**Framework**: Network Extension  
**Kind**: property

The TXT record associated with a connected Bonjour service endpoint.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var txtRecord: Data? { get }
```

#### Discussion

When the connection is connected to a Bonjour service endpoint, the TXT record associated with the Bonjour service is available via this property.

> ❗ **Important**:  Note that the value comes from an untrusted network source. Care must be taken when parsing this potentially malicious value.

 Note that the value comes from an untrusted network source. Care must be taken when parsing this potentially malicious value.

## See Also

- [var endpoint: NWEndpoint](nwtcpconnection/endpoint.md)
  The destination endpoint with which this connection was created.
- [var localAddress: NWEndpoint?](nwtcpconnection/localaddress.md)
  The IP address endpoint from which the connection was established.
- [var remoteAddress: NWEndpoint?](nwtcpconnection/remoteaddress.md)
  The IP address endpoint to which the connection was established.
- [var connectedPath: NWPath?](nwtcpconnection/connectedpath.md)
  The network path over which the connection was established.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwtcpconnection/txtrecord)*