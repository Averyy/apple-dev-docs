# availableDepths

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

An array that contains all available windows depths.

**Availability**:
- macOS 10.9+
- Swift 4.0+

## Declaration

```swift
static var availableDepths: [NSWindow.Depth] { get }
```

## See Also

### Accessing Depth Details
- [static func bestDepth(colorSpaceName: NSColorSpaceName, bitsPerSample: Int, bitsPerPixel: Int, isPlanar: Bool) -> (NSWindow.Depth, isExactMatch: Bool)](./bestdepth%28colorspacename,bitspersample,bitsperpixel,isplanar%29.md)
  Determines the best window depth that most closely matches the given properties.
- [var bitsPerPixel: Int](./bitsperpixel.md)
  Returns the bits per pixel for the specified window depth.
- [var bitsPerSample: Int](./bitspersample.md)
  Returns the bits per sample for the specified window depth.
- [var colorSpaceName: NSColorSpaceName?](./colorspacename.md)
  Returns the name of the color space corresponding to the passed window depth.
- [var isPlanar: Bool](./isplanar.md)
  Returns whether the specified window depth is planar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/depth/availabledepths)*