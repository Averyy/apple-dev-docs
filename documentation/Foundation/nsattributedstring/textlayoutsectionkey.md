# NSAttributedString.TextLayoutSectionKey

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

## Overview

Use these constants as values for the [`textLayoutSections`](./documentattributekey/textlayoutsections.md) key in the document attributes dictionary.

## Topics

### Getting keys for text layouts
- [static let orientation: NSAttributedString.TextLayoutSectionKey](./textlayoutsectionkey/orientation.md)
  The orientation of the text.
- [static let range: NSAttributedString.TextLayoutSectionKey](./textlayoutsectionkey/range.md)
  The character range.
### Initializers
- [init(rawValue: String)](./textlayoutsectionkey/init%28rawvalue%29.md)
  Creates a text layout section key with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting document-wide attributes
- [NSAttributedString.DocumentAttributeKey](./documentattributekey.md)
  The attributes you apply to an entire document.
- [NSAttributedString.DocumentReadingOptionKey](./documentreadingoptionkey.md)
  Options for constructing an attributed string from data you read from disk.
- [HTML attributes](../html-attributes.md)
  Documentwide attributes that provide control over the form of generated HTML.
- [NSAttributedString.DocumentType](./documenttype.md)
  Constants for the document type document attribute key.
- [enum NSTextScalingType](../../UIKit/nstextscalingtype.md)
  Constants that specify the text scaling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/textlayoutsectionkey)*