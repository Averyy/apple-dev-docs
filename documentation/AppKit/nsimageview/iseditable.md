# isEditable

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the user can drag a new image into the image view.

**Availability**:
- macOS

## Declaration

```swift
var isEditable: Bool { get set }
```

```objc
@property (getter=isEditable) BOOL editable;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the user can set the displayed image by dragging an image onto the image view. The default value of this property is [`false`](../../Swift/false.md), which causes the image view to display only the programmatically set image.

## See Also

### Responding to user events
- [var allowsCutCopyPaste: Bool](./allowscutcopypaste.md)
  A Boolean value indicating whether the image view lets the user cut, copy, and paste the image contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimageview/iseditable)*