# bitsPerPixel

**Framework**: AppKit  
**Kind**: property

Returns the bits per pixel for the specified window depth.

**Availability**:
- macOS ?+

## Declaration

```swift
var bitsPerPixel: Int { get }
```

#### Discussion

Returns the number of bits per pixel for the window depth specified by `depth`.

## See Also

- [var bitsPerSample: Int](nswindow/depth/bitspersample.md)
  Returns the bits per sample for the specified window depth.
- [var colorSpaceName: NSColorSpaceName?](nswindow/depth/colorspacename.md)
  Returns the name of the color space corresponding to the passed window depth.
- [var numberOfColorComponents: Int](nscolorspacename/numberofcolorcomponents.md)
  Returns the number of color components in the specified color space.
- [var isPlanar: Bool](nswindow/depth/isplanar.md)
  Returns whether the specified window depth is planar.
- [func canRepresent(NSDisplayGamut) -> Bool](nswindow/canrepresent(_:).md)
  A Boolean value that indicates if the window and its screen use a color space that can represent the specified display gamut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/depth/bitsperpixel)*