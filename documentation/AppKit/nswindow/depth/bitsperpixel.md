# bitsPerPixel

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the bits per pixel for the specified window depth.

**Availability**:
- macOS

## Declaration

```swift
var bitsPerPixel: Int { get }
```

```c
extern NSInteger NSBitsPerPixelFromDepth(NSWindowDepth depth);
```

## Discussion

Returns the number of bits per pixel for the window depth specified by `depth`.

## See Also

### Working with Window Depths
- [var bitsPerSample: Int](./bitspersample.md)
  Returns the bits per sample for the specified window depth.
- [var colorSpaceName: NSColorSpaceName?](./colorspacename.md)
  Returns the name of the color space corresponding to the passed window depth.
- [var numberOfColorComponents: Int](../../nscolorspacename/numberofcolorcomponents.md)
  Returns the number of color components in the specified color space.
- [var isPlanar: Bool](./isplanar.md)
  Returns whether the specified window depth is planar.
- [func canRepresent(NSDisplayGamut) -> Bool](../canrepresent%28_%29.md)
  A Boolean value that indicates if the window and its screen use a color space that can represent the specified display gamut.
- [NSAvailableWindowDepths](../../nsavailablewindowdepths.md)
  Returns the available window depth values.
- [NSBestDepth](../../nsbestdepth.md)
  Attempts to return a window depth adequate for the specified parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/depth/bitsperpixel)*