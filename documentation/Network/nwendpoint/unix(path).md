# NWEndpoint.unix(path:)

**Framework**: Network  
**Kind**: case  
**Role**: Case

An endpoint represented as a UNIX domain path.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
case unix(path: String)
```

## See Also

### Endpoint Types
- [case hostPort(host: NWEndpoint.Host, port: NWEndpoint.Port)](./hostport%28host,port%29.md)
  An endpoint represented as a host and port, with the host including both names and addresses.
- [case service(name: String, type: String, domain: String, interface: NWInterface?)](./service%28name,type,domain,interface%29.md)
  An endpoint represented as a Bonjour service.
- [NWEndpoint.url(_:)](./url%28_%29.md)
  An endpoint represented as a URL, with host and port values inferred from the URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwendpoint/unix(path:))*