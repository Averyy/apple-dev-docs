# vImageGamma_PlanarF(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Applies a gamma function to a PlanarF image.

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
func vImageGamma_PlanarF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ gamma: GammaFunction!, _ flags: vImage_Flags) -> vImage_Error
```

```c
vImage_Error vImageGamma_PlanarF(const vImage_Buffer *src, const vImage_Buffer *dest, GammaFunction const gamma, vImage_Flags flags);
```

#### Return Value

[`kvImageNoError`](./kvimagenoerror.md); otherwise, one of the error codes in [Data Types and Constants](./data-types-and-constants.md).

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the `height`, `width`, and `rowBytes` fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `gamma`: The gamma function object.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](./kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](./kvimagenoflags.md).

## See Also

### Applying a gamma function
- [func vImageCreateGammaFunction(Float, Int32, vImage_Flags) -> GammaFunction!](./vimagecreategammafunction%28_,_,_%29.md)
  Returns a gamma function object.
- [Gamma function types](./api-1584480-gamma-function-types.md)
  Types of full- or half-precision gamma functions.
- [func vImageGamma_Planar8toPlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, GammaFunction!, vImage_Flags) -> vImage_Error](./vimagegamma_planar8toplanarf%28_,_,_,_%29.md)
  Applies a gamma function to an 8-bit planar image to produce a 32-bit planar image.
- [func vImageGamma_PlanarFtoPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, GammaFunction!, vImage_Flags) -> vImage_Error](./vimagegamma_planarftoplanar8%28_,_,_,_%29.md)
  Applies a gamma function to a 32-bit planar image to produce an 8-bit planar image.
- [func vImageDestroyGammaFunction(GammaFunction!)](./vimagedestroygammafunction%28_%29.md)
  Destroys a gamma function object.
- [Adjusting saturation and applying tone mapping](./adjusting-saturation-and-applying-tone-mapping.md)
  Convert an RGB image to discrete luminance and chrominance channels, and apply color and contrast treatments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagegamma_planarf(_:_:_:_:))*