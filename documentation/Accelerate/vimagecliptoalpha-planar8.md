# vImageClipToAlpha_Planar8(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Clamps the values of an 8-bit planar buffer to the corresponding alpha values.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 5.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageClipToAlpha_Planar8(_ src: UnsafePointer<vImage_Buffer>, _ alpha: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

On return of this function, the value of each pixel in the destination buffer is:

```objc
color_result = MIN( color, alpha )
```

## Parameters

- `src`: The source vImage buffer.
- `alpha`: The vImage buffer that provides the source alpha.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageClipToAlpha_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagecliptoalpha_planarf(_:_:_:_:).md)
  Clamps the values of a 32-bit planar buffer to the corresponding alpha values.
- [func vImageClipToAlpha_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagecliptoalpha_argb8888(_:_:_:).md)
  Clamps the values of an 8-bit-per-channel, 4-channel ARGB buffer to the corresponding alpha values.
- [func vImageClipToAlpha_RGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagecliptoalpha_rgba8888(_:_:_:).md)
  Clamps the values of an 8-bit-per-channel, 4-channel RGBA buffer to the corresponding alpha values.
- [func vImageClipToAlpha_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagecliptoalpha_argbffff(_:_:_:).md)
  Clamps the values of a 32-bit-per-channel, 4-channel ARGB buffer to the corresponding alpha values.
- [func vImageClipToAlpha_RGBAFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimagecliptoalpha_rgbaffff(_:_:_:).md)
  Clamps the values of a 32-bit-per-channel, 4-channel RGBA buffer to the corresponding alpha values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecliptoalpha_planar8(_:_:_:_:))*