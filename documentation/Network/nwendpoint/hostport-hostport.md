# NWEndpoint.hostPort(host:port:)

**Framework**: Network  
**Kind**: case

An endpoint represented as a host and port, with the host including both names and addresses.

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
case hostPort(host: NWEndpoint.Host, port: NWEndpoint.Port)
```

## See Also

- [case service(name: String, type: String, domain: String, interface: NWInterface?)](nwendpoint/service(name:type:domain:interface:).md)
  An endpoint represented as a Bonjour service.
- [NWEndpoint.url(_:)](nwendpoint/url(_:).md)
  An endpoint represented as a URL, with host and port values inferred from the URL.
- [case unix(path: String)](nwendpoint/unix(path:).md)
  An endpoint represented as a UNIX domain path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwendpoint/hostport(host:port:))*