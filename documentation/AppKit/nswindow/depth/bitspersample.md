# bitsPerSample

**Framework**: AppKit  
**Kind**: property

Returns the bits per sample for the specified window depth.

**Availability**:
- macOS ?+

## Declaration

```swift
var bitsPerSample: Int { get }
```

#### Discussion

Returns the number of bits per sample (bits per pixel in each color component) for the window depth specified by `depth`.

## See Also

- [var bitsPerPixel: Int](nswindow/depth/bitsperpixel.md)
  Returns the bits per pixel for the specified window depth.
- [var colorSpaceName: NSColorSpaceName?](nswindow/depth/colorspacename.md)
  Returns the name of the color space corresponding to the passed window depth.
- [var numberOfColorComponents: Int](nscolorspacename/numberofcolorcomponents.md)
  Returns the number of color components in the specified color space.
- [var isPlanar: Bool](nswindow/depth/isplanar.md)
  Returns whether the specified window depth is planar.
- [func canRepresent(NSDisplayGamut) -> Bool](nswindow/canrepresent(_:).md)
  A Boolean value that indicates if the window and its screen use a color space that can represent the specified display gamut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/depth/bitspersample)*