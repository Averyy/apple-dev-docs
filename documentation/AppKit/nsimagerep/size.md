# size

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The size of the image representation, measured in points in the user coordinate space.

**Availability**:
- macOS

## Declaration

```swift
var size: NSSize { get set }
```

```objc
@property NSSize size;
```

## Discussion

This size is the size of the image representation when it’s rendered. It is not necessarily the same as the width and height of the image in pixels as specified by the image data, nor must it be equal to the size set for the `NSImage` object that wraps this image representation.

The size of an image representation combined with the physical dimensions of the image data determine the resolution of the image.

## See Also

### Related Documentation
- [var pixelsHigh: Int](./pixelshigh.md)
  The height of the image, measured in pixels.
- [var pixelsWide: Int](./pixelswide.md)
  The width of the image, measured in pixels.
- [func draw() -> Bool](./draw%28%29.md)
  Implemented by subclasses to draw the image in the current coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/size)*