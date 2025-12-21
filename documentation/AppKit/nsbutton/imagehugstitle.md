# imageHugsTitle

**Framework**: AppKit  
**Kind**: property

A Boolean value that determines how the button’s image and title are positioned together within the button bezel.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
var imageHugsTitle: Bool { get set }
```

#### Discussion

When the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false) (the default value), the button’s image is positioned according to the [`imagePosition`](nsbutton/imageposition.md) property at the edge of the button bezel, and the title is positioned within the remaining space.

When this property is [`true`](https://developer.apple.com/documentation/Swift/true), the button’s image is positioned directly adjacent to the title based on the [`imagePosition`](nsbutton/imageposition.md) property, and the image and title are positioned within the button bezel as a single unit.

## See Also

- [var image: NSImage?](nsbutton/image.md)
  The image that appears on the button when it’s in an off state, or `nil` if there is no such image.
- [var alternateImage: NSImage?](nsbutton/alternateimage.md)
  An alternate image that appears on the button when the button is in an on state.
- [var imagePosition: NSControl.ImagePosition](nsbutton/imageposition.md)
  The position of the button’s image relative to its title.
- [NSControl.ImagePosition](nscontrol/imageposition.md)
  A constant for specifying the position of a button’s image relative to its title.
- [var isBordered: Bool](nsbutton/isbordered.md)
  A Boolean value that determines whether the button has a border.
- [var isTransparent: Bool](nsbutton/istransparent.md)
  A Boolean value that indicates whether the button is transparent.
- [var bezelStyle: NSButton.BezelStyle](nsbutton/bezelstyle-swift.property.md)
  The appearance of the button’s border.
- [var bezelColor: NSColor?](nsbutton/bezelcolor.md)
  The color of the button’s bezel, in appearances that support it.
- [var showsBorderOnlyWhileMouseInside: Bool](nsbutton/showsborderonlywhilemouseinside.md)
  A Boolean value that determines whether the button displays its border only when the pointer is over it.
- [var imageScaling: NSImageScaling](nsbutton/imagescaling.md)
  The scaling mode applied to make the cell’s image fit the frame of the image view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/imagehugstitle)*