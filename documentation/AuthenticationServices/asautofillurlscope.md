# ASAutoFillURLScope

**Framework**: Authentication Services  
**Kind**: struct

This structure represents the subset of URL components supported for the AutoFill of credentials.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- macOS 26.2+
- visionOS 26.2+

## Declaration

```swift
struct ASAutoFillURLScope
```

## Topics

### Initializers
- [init(scheme: ASAutoFillURLScope.Scheme, host: String, port: Int?, path: String)](asautofillurlscope/init(scheme:host:port:path:).md)
  Creates a URL components instance
- [init?(url: URL)](asautofillurlscope/init(url:).md)
  Initialize with the components of a URL.
### Instance Properties
- [var host: String](asautofillurlscope/host.md)
  The host subcomponent.
- [var path: String](asautofillurlscope/path.md)
  The path subcomponent.
- [var port: Int?](asautofillurlscope/port.md)
  The port subcomponent.
- [var scheme: ASAutoFillURLScope.Scheme](asautofillurlscope/scheme-swift.property.md)
  The scheme subcomponent of the URL.
- [var url: URL?](asautofillurlscope/url.md)
  A URL created from the components.
### Enumerations
- [ASAutoFillURLScope.Scheme](asautofillurlscope/scheme-swift.enum.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asautofillurlscope)*