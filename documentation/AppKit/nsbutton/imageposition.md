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

If the title is above, below, or overlapping the image, or if there is no image, the text is horizontally centered within the button. See [`NSControl.ImagePosition`](../nscontrol/imageposition.md) in [`NSCell`](../nscell.md) for the list of possible image positions.

## See Also

### Related Documentation
- [var title: String](./title.md)
  The title displayed on the button when it’s in an off state.
- [func setButtonType(NSButton.ButtonType)](./setbuttontype%28_%29.md)
  Sets the button’s type, which affects its user interface and behavior when clicked.
### Configuring button images
- [var image: NSImage?](./image.md)
  The image that appears on the button when it’s in an off state, or `nil` if there is no such image.
- [var alternateImage: NSImage?](./alternateimage.md)
  An alternate image that appears on the button when the button is in an on state.
- [NSControl.ImagePosition](../nscontrol/imageposition.md)
  A constant for specifying the position of a button’s image relative to its title.
- [var isBordered: Bool](./isbordered.md)
  A Boolean value that determines whether the button has a border.
- [var isTransparent: Bool](./istransparent.md)
  A Boolean value that indicates whether the button is transparent.
- [var bezelStyle: NSButton.BezelStyle](./bezelstyle-swift.property.md)
  The appearance of the button’s border.
- [var bezelColor: NSColor?](./bezelcolor.md)
  The color of the button’s bezel, in appearances that support it.
- [var showsBorderOnlyWhileMouseInside: Bool](./showsborderonlywhilemouseinside.md)
  A Boolean value that determines whether the button displays its border only when the pointer is over it.
- [var imageHugsTitle: Bool](./imagehugstitle.md)
  A Boolean value that determines how the button’s image and title are positioned together within the button bezel.
- [var imageScaling: NSImageScaling](./imagescaling.md)
  The scaling mode applied to make the cell’s image fit the frame of the image view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/imageposition)*