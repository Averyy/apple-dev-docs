# bezelStyle

**Framework**: AppKit  
**Kind**: property

The appearance of the button’s border.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var bezelStyle: NSButton.BezelStyle { get set }
```

#### Return Value

The bezel style of the button. See [`NSButton.BezelStyle`](nsbutton/bezelstyle-swift.enum.md) in [`NSButtonCell`](nsbuttoncell.md) for the list of possible values.

#### Discussion

Note that if the button is not bordered, the bezel style is ignored.

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
- [var bezelColor: NSColor?](nsbutton/bezelcolor.md)
  The color of the button’s bezel, in appearances that support it.
- [var showsBorderOnlyWhileMouseInside: Bool](nsbutton/showsborderonlywhilemouseinside.md)
  A Boolean value that determines whether the button displays its border only when the pointer is over it.
- [var imageHugsTitle: Bool](nsbutton/imagehugstitle.md)
  A Boolean value that determines how the button’s image and title are positioned together within the button bezel.
- [var imageScaling: NSImageScaling](nsbutton/imagescaling.md)
  The scaling mode applied to make the cell’s image fit the frame of the image view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.property)*