# init(attachment:attributes:)

**Framework**: Foundation  
**Kind**: init

Creates an attributed string with an attachment and applies the specified attributes to it.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
convenience init(attachment: NSTextAttachment, attributes: [NSAttributedString.Key : Any] = [:])
```

#### Return Value

An attributed string containing the attachment.

## Parameters

- `attachment`: The attrachment to place in the string.
- `attributes`: The attributes to apply to the attachment. Specify an empty dictionary to create the string without any extra attributes.

## See Also

- [init(attachment: NSTextAttachment)](nsattributedstring/init(attachment:).md)
  Creates an attributed string with an attachment.
- [convenience init(adaptiveImageGlyph: NSAdaptiveImageGlyph, attributes: [NSAttributedString.Key : Any])](nsattributedstring/init(adaptiveimageglyph:attributes:).md)
  Creates an attributed string with an adaptive image glyph and applies the specified attributes to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/init(attachment:attributes:))*