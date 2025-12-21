# isPlanar

**Framework**: AppKit  
**Kind**: property

Returns whether the specified window depth is planar.

**Availability**:
- macOS ?+

## Declaration

```swift
var isPlanar: Bool { get }
```

#### Discussion

Returns [`true`](https://developer.apple.com/documentation/Swift/true) if the specified window `depth` is planar and [`false`](https://developer.apple.com/documentation/Swift/false) if it is not.

## See Also

- [var bitsPerPixel: Int](nswindow/depth/bitsperpixel.md)
  Returns the bits per pixel for the specified window depth.
- [var bitsPerSample: Int](nswindow/depth/bitspersample.md)
  Returns the bits per sample for the specified window depth.
- [var colorSpaceName: NSColorSpaceName?](nswindow/depth/colorspacename.md)
  Returns the name of the color space corresponding to the passed window depth.
- [var numberOfColorComponents: Int](nscolorspacename/numberofcolorcomponents.md)
  Returns the number of color components in the specified color space.
- [func canRepresent(NSDisplayGamut) -> Bool](nswindow/canrepresent(_:).md)
  A Boolean value that indicates if the window and its screen use a color space that can represent the specified display gamut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/depth/isplanar)*