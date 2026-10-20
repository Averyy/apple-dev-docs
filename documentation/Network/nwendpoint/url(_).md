# NWEndpoint.url(_:)

**Framework**: Network  
**Kind**: case  
**Role**: Case

An endpoint represented as a URL, with host and port values inferred from the URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case url(URL)
```

## See Also

### Endpoint Types
- [case hostPort(host: NWEndpoint.Host, port: NWEndpoint.Port)](./hostport%28host,port%29.md)
  An endpoint represented as a host and port, with the host including both names and addresses.
- [case service(name: String, type: String, domain: String, interface: NWInterface?)](./service%28name,type,domain,interface%29.md)
  An endpoint represented as a Bonjour service.
- [case unix(path: String)](./unix%28path%29.md)
  An endpoint represented as a UNIX domain path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwendpoint/url(_:))*