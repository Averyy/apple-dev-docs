# bestDepth(colorSpaceName:bitsPerSample:bitsPerPixel:isPlanar:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Determines the best window depth that most closely matches the given properties.

**Availability**:
- macOS 10.9+
- Swift 4.0+

## Declaration

```swift
static func bestDepth(colorSpaceName: NSColorSpaceName, bitsPerSample: Int, bitsPerPixel: Int, isPlanar: Bool) -> (NSWindow.Depth, isExactMatch: Bool)
```

#### Return Value

The window depth that most closely matches the properties this function requests.

## Parameters

- `colorSpaceName`: The name of a color space to match.
- `bitsPerSample`: The bits per sample to match.
- `bitsPerPixel`: The bits per pixel to match.
- `isPlanar`: A Boolean that indicates whether the window depth is planar.

## See Also

### Accessing Depth Details
- [static var availableDepths: [NSWindow.Depth]](./availabledepths.md)
  An array that contains all available windows depths.
- [var bitsPerPixel: Int](./bitsperpixel.md)
  Returns the bits per pixel for the specified window depth.
- [var bitsPerSample: Int](./bitspersample.md)
  Returns the bits per sample for the specified window depth.
- [var colorSpaceName: NSColorSpaceName?](./colorspacename.md)
  Returns the name of the color space corresponding to the passed window depth.
- [var isPlanar: Bool](./isplanar.md)
  Returns whether the specified window depth is planar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/depth/bestdepth(colorspacename:bitspersample:bitsperpixel:isplanar:))*