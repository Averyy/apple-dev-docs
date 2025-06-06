# imagePosition

**Framework**: AppKit  
**Kind**: property

The position of the button’s image relative to its title.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var imagePosition: NSControl.ImagePosition { get set }
```

#### Discussion

The value of this property is one of the image positions described in the “Constants” section of [`NSCell`](nscell.md). If the title is above, below, or overlapping the image, or if there is no image, the text is horizontally centered within the button.

## See Also

- [var image: NSImage?](nscell/image.md)
  The image displayed by the cell, if any.
- [class NSButtonCell](nsbuttoncell.md)
  An object that defines the user interface of a button or other clickable region of a view.
- [func setButtonType(NSButton.ButtonType)](nsbuttoncell/setbuttontype(_:).md)
  Sets how the button highlights while pressed and how it shows its state.
- [var alternateImage: NSImage?](nsbuttoncell/alternateimage.md)
  The image the button displays in its alternate state.
- [var imageScaling: NSImageScaling](nsbuttoncell/imagescaling.md)
  The scale factor for the button’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/imageposition)*