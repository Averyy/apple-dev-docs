# alternateImage

**Framework**: AppKit  
**Kind**: property

The image the button displays in its alternate state.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var alternateImage: NSImage? { get set }
```

#### Discussion

The value of this property is the image displayed by the button when it’s in its alternate state, or `nil` if there is no alternate image. Note that some button types don’t display an alternate image. Buttons don’t display images by default. Setting this property may redraw the contents of the button.

## See Also

- [var image: NSImage?](nscell/image.md)
  The image displayed by the cell, if any.
- [var keyEquivalent: String](nsbuttoncell/keyequivalent.md)
  The button’s key-equivalent character.
- [func setButtonType(NSButton.ButtonType)](nsbuttoncell/setbuttontype(_:).md)
  Sets how the button highlights while pressed and how it shows its state.
- [var imagePosition: NSControl.ImagePosition](nsbuttoncell/imageposition.md)
  The position of the button’s image relative to its title.
- [var imageScaling: NSImageScaling](nsbuttoncell/imagescaling.md)
  The scale factor for the button’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/alternateimage)*