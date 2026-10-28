# backgroundColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The background color for the image.

**Availability**:
- macOS

## Declaration

```swift
@NSCopying
var backgroundColor: NSColor { get set }
```

```objc
@property (copy) NSColor * backgroundColor;
```

## Discussion

The background color is visible only if the drawn image representation does not completely cover all of the pixels available for the image’s current size.  The background color is ignored for cached image representations; such caches are always created with a white background. Assigning a new background color does not cause the receiver to recache itself.

The default color is transparent, as returned by the [`clear`](../nscolor/clear.md) method of `NSColor`.

## See Also

### Related Documentation
- [func recache()](./recache%28%29.md)
  Invalidates and frees offscreen caches of all image representations.
### Managing Drawing Options
- [var isValid: Bool](./isvalid.md)
  A Boolean value that indicates whether it is possible to draw an image representation.
- [var capInsets: NSEdgeInsets](./capinsets.md)
  The cap insets for the image.
- [var resizingMode: NSImage.ResizingMode](./resizingmode-swift.property.md)
  The resizing mode for the image.
- [NSImage.ResizingMode](./resizingmode-swift.enum.md)
  Constants that describe the resizing mode for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/backgroundcolor)*