# showAttachmentCell(_:in:characterIndex:)

**Framework**: AppKit  
**Kind**: method

Draws an attachment cell.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func showAttachmentCell(_ cell: NSCell, in rect: NSRect, characterIndex attachmentIndex: Int)
```

#### Discussion

The `attachmentIndex` parameter is provided for cells that alter their appearance based on their location.

## Parameters

- `cell`: The attachment cell to draw.
- `rect`: The rectangle within which to draw  .
- `attachmentIndex`: The location of the attachment cell.

## See Also

- [var defaultAttachmentScaling: NSImageScaling](nslayoutmanager/defaultattachmentscaling.md)
  The default amount of scaling to apply when an attachment image is too large to fit in a text container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/showattachmentcell(_:in:characterindex:))*