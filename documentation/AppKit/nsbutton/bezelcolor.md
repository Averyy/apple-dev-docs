# bezelColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The color of the button’s bezel, in appearances that support it.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@NSCopying
var bezelColor: NSColor? { get set }
```

```objc
@property (copy, nullable) NSColor * bezelColor;
```

## See Also

### Configuring button images
- [var image: NSImage?](./image.md)
  The image that appears on the button when it’s in an off state, or `nil` if there is no such image.
- [var alternateImage: NSImage?](./alternateimage.md)
  An alternate image that appears on the button when the button is in an on state.
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
- [var showsBorderOnlyWhileMouseInside: Bool](./showsborderonlywhilemouseinside.md)
  A Boolean value that determines whether the button displays its border only when the pointer is over it.
- [var imageHugsTitle: Bool](./imagehugstitle.md)
  A Boolean value that determines how the button’s image and title are positioned together within the button bezel.
- [var imageScaling: NSImageScaling](./imagescaling.md)
  The scaling mode applied to make the cell’s image fit the frame of the image view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/bezelcolor)*