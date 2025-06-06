# showsBorderOnlyWhileMouseInside

**Framework**: AppKit  
**Kind**: property

A Boolean value that determines whether the button displays its border only when the pointer is over it.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var showsBorderOnlyWhileMouseInside: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the button’s border is displayed only when the pointer is over the button and the button is active. The value is [`false`](https://developer.apple.com/documentation/swift/false) if the border is displayed all the time, regardless of the position of the pointer. By default, this method returns [`false`](https://developer.apple.com/documentation/swift/false).

If [`isBordered`](nsbutton/isbordered.md) is [`false`](https://developer.apple.com/documentation/swift/false), the border is never displayed, regardless of the value of [`showsBorderOnlyWhileMouseInside`](nsbutton/showsborderonlywhilemouseinside.md).

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
- [var imageHugsTitle: Bool](nsbutton/imagehugstitle.md)
  A Boolean value that determines how the button’s image and title are positioned together within the button bezel.
- [var imageScaling: NSImageScaling](nsbutton/imagescaling.md)
  The scaling mode applied to make the cell’s image fit the frame of the image view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbutton/showsborderonlywhilemouseinside)*