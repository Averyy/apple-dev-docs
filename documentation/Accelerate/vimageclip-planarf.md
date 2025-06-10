# vImageClip_PlanarF(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Clips the values in a floating-point 32-bit planar buffer to the specified minimum and maximum values.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 5.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageClip_PlanarF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ maxFloat: Pixel_F, _ minFloat: Pixel_F, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

This function performs the following calculation for each pixel:

```objc
 if (pixel > maxFloat)
   pixel = maxFloat;
if (pixel < minFloat)
   pixel = minFloat;
```

The following code clamps the pixel values `[-0.5, -0.25, 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5]` to the range `0...1`:

```swift
let pixelBuffer = vImage.PixelBuffer<vImage.PlanarF>(
    pixelValues: [-0.5, -0.25, 0, 0.25, 0.5, 0.75, 1, 1.25, 1.5],
    size: .init(width: 9, height: 1))

pixelBuffer.withUnsafePointerToVImageBuffer { buf in
    _ = vImageClip_PlanarF(buf,
                           buf,
                           1.0,
                           0.0,
                           vImage_Flags(kvImageNoFlags))
}

// Prints "[0.0, 0.0, 0.0, 0.25, 0.5, 0.75, 1.0, 1.0, 1.0]".
print(pixelBuffer.array)
```

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `maxFloat`: The maximum pixel value. The function sets source values that are greater than this value to this value.
- `minFloat`: The minimum pixel value. The function sets source values that are less than this value to this value.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageclip_planarf(_:_:_:_:_:))*