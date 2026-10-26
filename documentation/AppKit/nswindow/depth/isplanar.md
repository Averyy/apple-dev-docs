# isPlanar

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns whether the specified window depth is planar.

**Availability**:
- macOS

## Declaration

```swift
var isPlanar: Bool { get }
```

```c
extern BOOL NSPlanarFromDepth(NSWindowDepth depth);
```

#### Discussion

Returns [`true`](../../../Swift/true.md) if the specified window `depth` is planar and [`false`](../../../Swift/false.md) if it is not.

## See Also

### Working with Window Depths
- [var bitsPerPixel: Int](./bitsperpixel.md)
  Returns the bits per pixel for the specified window depth.
- [var bitsPerSample: Int](./bitspersample.md)
  Returns the bits per sample for the specified window depth.
- [var colorSpaceName: NSColorSpaceName?](./colorspacename.md)
  Returns the name of the color space corresponding to the passed window depth.
- [var numberOfColorComponents: Int](../../nscolorspacename/numberofcolorcomponents.md)
  Returns the number of color components in the specified color space.
- [func canRepresent(NSDisplayGamut) -> Bool](../canrepresent%28_%29.md)
  A Boolean value that indicates if the window and its screen use a color space that can represent the specified display gamut.
- [NSAvailableWindowDepths](../../nsavailablewindowdepths.md)
  Returns the available window depth values.
- [NSBestDepth](../../nsbestdepth.md)
  Attempts to return a window depth adequate for the specified parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/depth/isplanar)*