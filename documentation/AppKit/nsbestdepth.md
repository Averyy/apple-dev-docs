# NSBestDepth

**Framework**: AppKit  
**Kind**: func  
**Role**: Function

Attempts to return a window depth adequate for the specified parameters.

**Availability**:
- macOS

## Declaration

```c
extern NSWindowDepth NSBestDepth(NSColorSpaceName colorSpace, NSInteger bps, NSInteger bpp, BOOL planar, BOOL *exactMatch);
```

#### Discussion

Returns a window depth deep enough for the given number of colors in `colorSpace`, bits per sample specified by `bps`, bits per pixel specified by `bpp`, and whether planar as specified by `planar`. Upon return, the variable pointed to by `exactMatch` is [`true`](../Swift/true.md) if the window depth can accommodate all of the values specified by the parameters, [`false`](../Swift/false.md) if it can’t.

Use this function to compute window depths. This function tries to accommodate all the parameters (match or better); if there are multiple matches, it gives the closest, with matching `colorSpace` first, then `bps`, then `planar`, then `bpp`. `bpp` is “bits per pixel”; 0 indicates default (same as the number of bits per plane, either `bps` or `bps` * [`numberOfColorComponents`](./nscolorspacename/numberofcolorcomponents.md)); other values may be used as hints to provide backing stores of different configuration; for instance, 8-bit color. The `exactMatch` parameter is optional and indicates whether all the parameters matched exactly.

## See Also

### Working with Window Depths
- [NSAvailableWindowDepths](./nsavailablewindowdepths.md)
  Returns the available window depth values.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbestdepth)*