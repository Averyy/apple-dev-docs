# AttributeScopes.SwiftUIAttributes.StrikethroughStyleAttribute

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

A key for the line drawn through a run of attributed text.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@frozen
enum StrikethroughStyleAttribute
```

#### Overview

Set this key to mark text as no longer current, such as a completed item or a superseded price. The value carries both the pattern and the color of the line:

```
var price = AttributedString("$24.00")
price.strikethroughStyle = .single

Text(price)
```

## Relationships

### Conforms To
- [AttributedStringKey](../../attributedstringkey.md)
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Copyable](../../../Swift/copyable.md)
- [DecodableAttributedStringKey](../../decodableattributedstringkey.md)
- [EncodableAttributedStringKey](../../encodableattributedstringkey.md)
- [Escapable](../../../Swift/escapable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributescopes/swiftuiattributes/strikethroughstyleattribute)*