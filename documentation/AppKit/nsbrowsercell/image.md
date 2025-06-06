# image

**Framework**: AppKit  
**Kind**: property

The browser cell’s image.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var image: NSImage? { get set }
```

#### Discussion

The image is drawn vertically centered on the left edge of the browser cell.

Note that the image is drawn at the given size of the image. `NSBrowserCell` does not set the size of the image, nor does it clip the drawing of the image. Make sure this image is the correct size for drawing in the browser cell.

When the value of this property is `nil`, it removes the image for the browser cell.

## See Also

- [var alternateImage: NSImage?](nsbrowsercell/alternateimage.md)
  The browser cell’s image for the highlighted state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowsercell/image)*