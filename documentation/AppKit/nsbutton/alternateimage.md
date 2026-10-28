# alternateImage

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An alternate image that appears on the button when the button is in an on state.

**Availability**:
- macOS

## Declaration

```swift
var alternateImage: NSImage? { get set }
```

```objc
@property (strong, nullable) NSImage * alternateImage;
```

## Discussion

The value of this property is `nil` if there is no alternate image for the button. Note that some button types don’t display an alternate image, and buttons don’t display images by default. If you use this property to set an image, the button redraws its contents if necessary.

## See Also

### Related Documentation
- [var keyEquivalent: String](./keyequivalent.md)
  The key-equivalent character of the button.
- [func setButtonType(NSButton.ButtonType)](./setbuttontype%28_%29.md)
  Sets the button’s type, which affects its user interface and behavior when clicked.
### Configuring button images
- [var image: NSImage?](./image.md)
  The image that appears on the button when it’s in an off state, or `nil` if there is no such image.
- [var imagePosition: NSControl.ImagePosition](./imageposition.md)
  The position of the button’s image relative to its title.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/alternateimage)*