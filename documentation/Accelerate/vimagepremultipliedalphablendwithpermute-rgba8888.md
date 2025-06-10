# vImagePremultipliedAlphaBlendWithPermute_RGBA8888(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Permutes the top 8-bit, 4-channel premultiplied buffer, and composites with the bottom buffer.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 7.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImagePremultipliedAlphaBlendWithPermute_RGBA8888(_ srcTop: UnsafePointer<vImage_Buffer>, _ srcBottom: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ permuteMap: UnsafePointer<UInt8>, _ makeDestAlphaOpaque: Bool, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The `permuteMap` parameter changes the order of the `srcTop` channels:

- `permuteMap[0]` specifies which channel in the source top image the function treats as the alpha channel.
- `permuteMap[1]` specifies which channel in the source top image the function treats as the red channel.
- `permuteMap[2]` specifies which channel in the source top image the function treats as the green channel.
- `permuteMap[3]` specifies which channel in the source top image the function treats as the blue channel.

## Parameters

- `srcTop`: The vImage buffer that provides the source top image.
- `srcBottom`: The vImage buffer that provides the source bottom image.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `permuteMap`: An array of four 8-bit integers with the values  ,  ,  , and 3, in some order. Each value specifies the channel from the source image that the function uses as the destination channel at the corresponding index.
- `makeDestAlphaOpaque`: A Boolean value that specifies whether the function generates a destination image with opaque an alpha channel.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [Compositing images with alpha blending](compositing-images-with-alpha-blending.md)
  Combine two images by using alpha blending to create a single output.
- [func vImagePremultipliedAlphaBlendWithPermute_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, Bool, vImage_Flags) -> vImage_Error](vimagepremultipliedalphablendwithpermute_argb8888(_:_:_:_:_:_:).md)
  Permutes the top 8-bit, 4-channel premultiplied buffer, and composites with the bottom buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagepremultipliedalphablendwithpermute_rgba8888(_:_:_:_:_:_:))*