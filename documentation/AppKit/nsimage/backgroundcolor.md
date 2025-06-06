# backgroundColor

**Framework**: AppKit  
**Kind**: property

The background color for the image.

**Availability**:
- macOS ?+

## Declaration

```swift
@NSCopying
var backgroundColor: NSColor { get set }
```

#### Discussion

The background color is visible only if the drawn image representation does not completely cover all of the pixels available for the image’s current size.  The background color is ignored for cached image representations; such caches are always created with a white background. Assigning a new background color does not cause the receiver to recache itself.

The default color is transparent, as returned by the [`clear`](nscolor/clear.md) method of `NSColor`.

## See Also

- [func recache()](nsimage/recache.md)
  Invalidates and frees offscreen caches of all image representations.
- [var isValid: Bool](nsimage/isvalid.md)
  A Boolean value that indicates whether it is possible to draw an image representation.
- [var capInsets: NSEdgeInsets](nsimage/capinsets.md)
  The cap insets for the image.
- [var resizingMode: NSImage.ResizingMode](nsimage/resizingmode-swift.property.md)
  The resizing mode for the image.
- [NSImage.ResizingMode](nsimage/resizingmode-swift.enum.md)
  Constants that describe the resizing mode for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/backgroundcolor)*