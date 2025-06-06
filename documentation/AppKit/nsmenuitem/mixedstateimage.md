# mixedStateImage

**Framework**: AppKit  
**Kind**: property

The image of the menu item that indicates a “mixed” state, that is, a state neither “on” nor “off.”

**Availability**:
- macOS ?+

## Declaration

```swift
var mixedStateImage: NSImage! { get set }
```

#### Discussion

A mixed state is useful for indicating a mix of “off” and “on” attribute values in a group of selected objects, such as a selection of text containing boldface and plain (non-boldface) words. By default this is a horizontal line.

## See Also

- [var state: NSControl.StateValue](nsmenuitem/state.md)
  The state of the menu item.
- [var image: NSImage?](nsmenuitem/image.md)
  The menu item’s image.
- [var onStateImage: NSImage!](nsmenuitem/onstateimage.md)
  The image of the menu item that indicates an “on” state.
- [var offStateImage: NSImage?](nsmenuitem/offstateimage.md)
  The image of the menu item that indicates an “off” state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitem/mixedstateimage)*