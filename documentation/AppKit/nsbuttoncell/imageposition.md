# imagePosition

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The position of the button’s image relative to its title.

**Availability**:
- macOS

## Declaration

```swift
var imagePosition: NSControl.ImagePosition { get set }
```

```objc
@property NSCellImagePosition imagePosition;
```

#### Discussion

The value of this property is one of the image positions described in the “Constants” section of [`NSCell`](../nscell.md). If the title is above, below, or overlapping the image, or if there is no image, the text is horizontally centered within the button.

## See Also

### Related Documentation
- [var image: NSImage?](../nscell/image.md)
  The image displayed by the cell, if any.
- [class NSButtonCell](../nsbuttoncell.md)
  An object that defines the user interface of a button or other clickable region of a view.
- [func setButtonType(NSButton.ButtonType)](./setbuttontype%28_%29.md)
  Sets how the button highlights while pressed and how it shows its state.
### Managing Images
- [var alternateImage: NSImage?](./alternateimage.md)
  The image the button displays in its alternate state.
- [var imageScaling: NSImageScaling](./imagescaling.md)
  The scale factor for the button’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbuttoncell/imageposition)*