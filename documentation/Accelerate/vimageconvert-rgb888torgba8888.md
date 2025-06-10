# vImageConvert_RGB888toRGBA8888(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Combines an 8-bit-per-channel, 3-channel RGB buffer and either an 8-bit alpha buffer or constant alpha value to produce an RGBA result.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 6.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageConvert_RGB888toRGBA8888(_: UnsafePointer<vImage_Buffer>, _: UnsafePointer<vImage_Buffer>!, _: Pixel_8, _: UnsafePointer<vImage_Buffer>, _: Bool, _: vImage_Flags) -> vImage_Error
```

#### Discussion

##### Parameters

If you specify `premultiply` as `true`, the function uses the following calculation to perform the conversion:

```objc
 r = (a * r + 127) / 255
 g = (a * g + 127) / 255
 b = (a * b + 127) / 255
```

## See Also

- [func vImageConvert_RGB888toARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>!, Pixel_8, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error](vimageconvert_rgb888toargb8888(_:_:_:_:_:_:).md)
  Combines an 8-bit-per-channel, 3-channel RGB buffer and either an 8-bit alpha buffer or constant alpha value to produce an ARGB result.
- [func vImageConvert_RGB888toBGRA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>!, Pixel_8, UnsafePointer<vImage_Buffer>, Bool, vImage_Flags) -> vImage_Error](vimageconvert_rgb888tobgra8888(_:_:_:_:_:_:).md)
  Combines an 8-bit-per-channel, 3-channel RGB buffer and either an 8-bit alpha buffer or constant alpha value to produce a BGRA result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_rgb888torgba8888(_:_:_:_:_:_:))*