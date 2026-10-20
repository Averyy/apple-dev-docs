# defaultAttachmentScaling

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The default amount of scaling to apply when an attachment image is too large to fit in a text container.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var defaultAttachmentScaling: NSImageScaling { get set }
```

```objc
@property NSImageScaling defaultAttachmentScaling;
```

#### Discussion

Attachment cells control their own size and drawing, so this setting is only advisory to them, but Application Kit–supplied attachment cells respect it.

## See Also

### Managing attachments
- [func showAttachmentCell(NSCell, in: NSRect, characterIndex: Int)](./showattachmentcell%28_,in,characterindex%29.md)
  Draws an attachment cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/defaultattachmentscaling)*