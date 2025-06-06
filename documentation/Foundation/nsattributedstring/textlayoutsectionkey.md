# NSAttributedString.TextLayoutSectionKey

**Framework**: Foundation  
**Kind**: struct

Constants for the text layout sections document attribute key.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct TextLayoutSectionKey
```

#### Overview

Use these constants as values for the [`textLayoutSections`](nsattributedstring/documentattributekey/textlayoutsections.md) key in the document attributes dictionary.

## Topics

### Getting keys for text layouts
- [static let orientation: NSAttributedString.TextLayoutSectionKey](nsattributedstring/textlayoutsectionkey/orientation.md)
  The orientation of the text.
- [static let range: NSAttributedString.TextLayoutSectionKey](nsattributedstring/textlayoutsectionkey/range.md)
  The character range.
### Initializers
- [init(rawValue: String)](nsattributedstring/textlayoutsectionkey/init(rawvalue:).md)
  Creates a text layout section key with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NSAttributedString.DocumentAttributeKey](nsattributedstring/documentattributekey.md)
  The attributes you apply to an entire document.
- [NSAttributedString.DocumentReadingOptionKey](nsattributedstring/documentreadingoptionkey.md)
  Options for constructing an attributed string from data you read from disk.
- [HTML attributes](html-attributes.md)
  Documentwide attributes that provide control over the form of generated HTML.
- [NSAttributedString.DocumentType](nsattributedstring/documenttype.md)
  Constants for the document type document attribute key.
- [enum NSTextScalingType](../UIKit/NSTextScalingType.md)
  Constants that specify the text scaling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/textlayoutsectionkey)*