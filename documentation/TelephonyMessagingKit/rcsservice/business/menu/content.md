# RCSService.Business.Menu.Content

**Framework**: TelephonyMessagingKit  
**Kind**: enum

Enumeration defining the contents of menu.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
enum Content
```

## Topics

### Determining content type
- [RCSService.Business.Menu.Content.submenu(_:)](rcsservice/business/menu/content/submenu(_:).md)
  A sub menu.
- [RCSService.Business.Menu.Content.suggestion(_:)](rcsservice/business/menu/content/suggestion(_:).md)
  Suggestion (action or reply).
- [RCSService.Business.Suggestion](rcsservice/business/suggestion.md)
  Enumeration representing a suggestion from a business.
### Encoding and decoding
- [init(from: any Decoder) throws](rcsservice/business/menu/content/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (RCSService.Business.Menu.Content, RCSService.Business.Menu.Content) -> Bool](rcsservice/business/menu/content/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Methods
- [func encode(to: any Encoder) throws](rcsservice/business/menu/content/encode(to:).md)
  Encodes this value into the given encoder.
### Default Implementations
- [Equatable Implementations](rcsservice/business/menu/content/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let title: String?](rcsservice/business/menu/title.md)
  Title for menu.
- [let contents: [RCSService.Business.Menu.Content]](rcsservice/business/menu/contents.md)
  Array of menu contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/menu/content)*