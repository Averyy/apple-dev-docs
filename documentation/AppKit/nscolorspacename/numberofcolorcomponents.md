# numberOfColorComponents

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the number of color components in the specified color space.

**Availability**:
- macOS

## Declaration

```swift
var numberOfColorComponents: Int { get }
```

```c
extern NSInteger NSNumberOfColorComponents(NSColorSpaceName colorSpaceName);
```

## Discussion

Returns the number of color components in the color space whose name is provided by `colorSpaceName`.

## See Also

### Working with Window Depths
- [var bitsPerPixel: Int](../nswindow/depth/bitsperpixel.md)
  Returns the bits per pixel for the specified window depth.
- [var bitsPerSample: Int](../nswindow/depth/bitspersample.md)
  Returns the bits per sample for the specified window depth.
- [var colorSpaceName: NSColorSpaceName?](../nswindow/depth/colorspacename.md)
  Returns the name of the color space corresponding to the passed window depth.
- [var isPlanar: Bool](../nswindow/depth/isplanar.md)
  Returns whether the specified window depth is planar.
- [func canRepresent(NSDisplayGamut) -> Bool](../nswindow/canrepresent%28_%29.md)
  A Boolean value that indicates if the window and its screen use a color space that can represent the specified display gamut.
- [NSAvailableWindowDepths](../nsavailablewindowdepths.md)
  Returns the available window depth values.
- [NSBestDepth](../nsbestdepth.md)
  Attempts to return a window depth adequate for the specified parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorspacename/numberofcolorcomponents)*