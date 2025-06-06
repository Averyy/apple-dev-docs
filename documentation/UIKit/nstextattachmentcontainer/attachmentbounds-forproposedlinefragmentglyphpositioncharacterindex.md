# attachmentBounds(for:proposedLineFragment:glyphPosition:characterIndex:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns the layout bounds of the text attachment to the layout manager.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func attachmentBounds(for textContainer: NSTextContainer?, proposedLineFragment lineFrag: CGRect, glyphPosition position: CGPoint, characterIndex charIndex: Int) -> CGRect
```

#### Return Value

The [`bounds`](nstextattachment/bounds.md) rectangle of the text attachment if not [`CGRectZero`](https://developer.apple.com/documentation/CoreGraphics/CGRectZero); otherwise, the rectangle of the [`size`](uiimage/size.md) property of the attachment’s [`image`](nstextattachment/image.md) property.

#### Discussion

Conforming objects can implement more sophisticated logic for negotiating the attachment bounds based on the available container space and proposed line fragment rectangle.

## Parameters

- `textContainer`: The text container for the text being laid out.
- `lineFrag`: The line fragment containing the text attachment.
- `position`: The glyph location inside   which is the origin of the returned bounds rectangle.
- `charIndex`: The character location inside the text storage for the attachment character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextattachmentcontainer/attachmentbounds(for:proposedlinefragment:glyphposition:characterindex:))*