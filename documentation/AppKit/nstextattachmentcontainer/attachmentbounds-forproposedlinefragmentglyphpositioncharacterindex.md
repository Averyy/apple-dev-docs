# attachmentBounds(for:proposedLineFragment:glyphPosition:characterIndex:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the layout bounds of the text attachment to the layout manager.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func attachmentBounds(for textContainer: NSTextContainer?, proposedLineFragment lineFrag: CGRect, glyphPosition position: CGPoint, characterIndex charIndex: Int) -> CGRect
```

#### Return Value

The [`bounds`](nstextattachment/bounds.md) rectangle of the text attachment if not [`CGRectZero`](https://developer.apple.com/documentation/CoreGraphics/CGRectZero); otherwise, the rectangle of the [`size`](https://developer.apple.com/documentation/UIKit/UIImage/size) property of the attachment’s [`image`](nstextattachment/image.md) property.

#### Discussion

Conforming objects can implement more sophisticated logic for negotiating the attachment bounds based on the available container space and proposed line fragment rectangle.

## Parameters

- `textContainer`: The text container for the text being laid out.
- `lineFrag`: The line fragment containing the text attachment.
- `position`: The glyph location inside   which is the origin of the returned bounds rectangle.
- `charIndex`: The character location inside the text storage for the attachment character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextattachmentcontainer/attachmentbounds(for:proposedlinefragment:glyphposition:characterindex:))*