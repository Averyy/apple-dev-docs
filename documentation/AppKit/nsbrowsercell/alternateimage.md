# alternateImage

**Framework**: AppKit  
**Kind**: property

The browser cell’s image for the highlighted state.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var alternateImage: NSImage? { get set }
```

#### Discussion

The image is drawn vertically centered on the left edge of the browser cell.

Note that the image is drawn at the given size of the image. `NSBrowserCell` does not set the size of the image, nor does it clip the drawing of the image. Make sure this image is the correct size for drawing in the browser cell.

When the value of this property is `nil`, it removes the alternate image for the browser cell.

## See Also

- [var image: NSImage?](nsbrowsercell/image.md)
  The browser cell’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowsercell/alternateimage)*