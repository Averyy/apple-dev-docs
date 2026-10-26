# NSAvailableWindowDepths

**Framework**: AppKit  
**Kind**: func  
**Role**: Function

Returns the available window depth values.

**Availability**:
- macOS

## Declaration

```c
extern const NSWindowDepth *NSAvailableWindowDepths();
```

#### Discussion

Returns a null-terminated array of [`NSWindow.Depth`](./nswindow/depth.md) values that specify which window depths are currently available. Window depth values are converted to specific display properties using the functions [`bitsPerPixel`](./nswindow/depth/bitsperpixel.md), [`bitsPerSample`](./nswindow/depth/bitspersample.md), [`colorSpaceName`](./nswindow/depth/colorspacename.md), and [`isPlanar`](./nswindow/depth/isplanar.md).

## See Also

### Working with Window Depths
- [NSBestDepth](./nsbestdepth.md)
  Attempts to return a window depth adequate for the specified parameters.
- [var bitsPerPixel: Int](./nswindow/depth/bitsperpixel.md)
  Returns the bits per pixel for the specified window depth.
- [var bitsPerSample: Int](./nswindow/depth/bitspersample.md)
  Returns the bits per sample for the specified window depth.
- [var colorSpaceName: NSColorSpaceName?](./nswindow/depth/colorspacename.md)
  Returns the name of the color space corresponding to the passed window depth.
- [var numberOfColorComponents: Int](./nscolorspacename/numberofcolorcomponents.md)
  Returns the number of color components in the specified color space.
- [var isPlanar: Bool](./nswindow/depth/isplanar.md)
  Returns whether the specified window depth is planar.
- [func canRepresent(NSDisplayGamut) -> Bool](./nswindow/canrepresent%28_%29.md)
  A Boolean value that indicates if the window and its screen use a color space that can represent the specified display gamut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsavailablewindowdepths)*