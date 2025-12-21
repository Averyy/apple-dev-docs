# isEditable

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the user can drag a new image into the image view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isEditable: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the user can set the displayed image by dragging an image onto the image view. The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), which causes the image view to display only the programmatically set image.

## See Also

- [var allowsCutCopyPaste: Bool](nsimageview/allowscutcopypaste.md)
  A Boolean value indicating whether the image view lets the user cut, copy, and paste the image contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimageview/iseditable)*