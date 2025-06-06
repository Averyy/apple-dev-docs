# defaultAttachmentScaling

**Framework**: AppKit  
**Kind**: property

The default amount of scaling to apply when an attachment image is too large to fit in a text container.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var defaultAttachmentScaling: NSImageScaling { get set }
```

#### Discussion

Attachment cells control their own size and drawing, so this setting is only advisory to them, but Application Kit–supplied attachment cells respect it.

## See Also

- [func showAttachmentCell(NSCell, in: NSRect, characterIndex: Int)](nslayoutmanager/showattachmentcell(_:in:characterindex:).md)
  Draws an attachment cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/defaultattachmentscaling)*