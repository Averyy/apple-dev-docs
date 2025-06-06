# init(attachment:)

**Framework**: Foundation  
**Kind**: init

Creates an attributed string with an attachment.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(attachment: NSTextAttachment)
```

#### Return Value

An attributed string containing the attachment.

#### Discussion

This is a convenience method for creating an attributed string containing an attachment using [`character`](https://developer.apple.com/documentation/AppKit/NSTextAttachment/character) as the base character.

## Parameters

- `attachment`: The attrachment to place in the string.

## See Also

- [convenience init(attachment: NSTextAttachment, attributes: [NSAttributedString.Key : Any])](nsattributedstring/init(attachment:attributes:).md)
  Creates an attributed string with an attachment and applies the specified attributes to it.
- [convenience init(adaptiveImageGlyph: NSAdaptiveImageGlyph, attributes: [NSAttributedString.Key : Any])](nsattributedstring/init(adaptiveimageglyph:attributes:).md)
  Creates an attributed string with an adaptive image glyph and applies the specified attributes to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/init(attachment:))*