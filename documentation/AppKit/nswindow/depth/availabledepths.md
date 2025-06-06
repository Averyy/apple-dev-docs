# availableDepths

**Framework**: AppKit  
**Kind**: property

An array that contains all available windows depths.

**Availability**:
- macOS 10.9+
- Swift 4.0+

## Declaration

```swift
static var availableDepths: [NSWindow.Depth] { get }
```

## See Also

- [static func bestDepth(colorSpaceName: NSColorSpaceName, bitsPerSample: Int, bitsPerPixel: Int, isPlanar: Bool) -> (NSWindow.Depth, isExactMatch: Bool)](nswindow/depth/bestdepth(colorspacename:bitspersample:bitsperpixel:isplanar:).md)
  Determines the best window depth that most closely matches the given properties.
- [var bitsPerPixel: Int](nswindow/depth/bitsperpixel.md)
  Returns the bits per pixel for the specified window depth.
- [var bitsPerSample: Int](nswindow/depth/bitspersample.md)
  Returns the bits per sample for the specified window depth.
- [var colorSpaceName: NSColorSpaceName?](nswindow/depth/colorspacename.md)
  Returns the name of the color space corresponding to the passed window depth.
- [var isPlanar: Bool](nswindow/depth/isplanar.md)
  Returns whether the specified window depth is planar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/depth/availabledepths)*