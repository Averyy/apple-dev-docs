# RCSService.Business.OpenURLAction.Target

**Framework**: TelephonyMessagingKit  
**Kind**: enum

Enumeration representing the target to open the URL in.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
enum Target
```

## Topics

### Accessing targets
- [RCSService.Business.OpenURLAction.Target.defaultBrowser](rcsservice/business/openurlaction/target-swift.enum/defaultbrowser.md)
  Open using default browser.
- [case inApp(detent: RCSService.Business.OpenURLAction.Detent)](rcsservice/business/openurlaction/target-swift.enum/inapp(detent:).md)
  Open in-app.
- [RCSService.Business.OpenURLAction.Detent](rcsservice/business/openurlaction/detent.md)
  Enumeration that represents a height to apply when opening a URL.
### Encoding and decoding
- [init(from: any Decoder) throws](rcsservice/business/openurlaction/target-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (RCSService.Business.OpenURLAction.Target, RCSService.Business.OpenURLAction.Target) -> Bool](rcsservice/business/openurlaction/target-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Methods
- [func encode(to: any Encoder) throws](rcsservice/business/openurlaction/target-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
### Default Implementations
- [Equatable Implementations](rcsservice/business/openurlaction/target-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let url: URL](rcsservice/business/openurlaction/url.md)
  URL to open.
- [let target: RCSService.Business.OpenURLAction.Target](rcsservice/business/openurlaction/target-swift.property.md)
  Target to use when opening URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/openurlaction/target-swift.enum)*