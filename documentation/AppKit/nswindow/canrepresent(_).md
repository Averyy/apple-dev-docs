# canRepresent(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

A Boolean value that indicates if the window and its screen use a color space that can represent the specified display gamut.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func canRepresent(_ displayGamut: NSDisplayGamut) -> Bool
```

```objc
- (BOOL) canRepresentDisplayGamut:(NSDisplayGamut) displayGamut;
```

## See Also

### Working with Window Depths
- [var bitsPerPixel: Int](./depth/bitsperpixel.md)
  Returns the bits per pixel for the specified window depth.
- [var bitsPerSample: Int](./depth/bitspersample.md)
  Returns the bits per sample for the specified window depth.
- [var colorSpaceName: NSColorSpaceName?](./depth/colorspacename.md)
  Returns the name of the color space corresponding to the passed window depth.
- [var numberOfColorComponents: Int](../nscolorspacename/numberofcolorcomponents.md)
  Returns the number of color components in the specified color space.
- [var isPlanar: Bool](./depth/isplanar.md)
  Returns whether the specified window depth is planar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/canrepresent(_:))*