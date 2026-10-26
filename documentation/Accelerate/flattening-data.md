# Flattening data

**Framework**: Accelerate  
**Role**: API Collection

Perform an alpha composite of a four-channel image over a solid background color.

## Topics

### Flattening 4-channel, 8-bit images
- [func vImageFlatten_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, Bool, vImage_Flags) -> vImage_Error](./vimageflatten_argb8888%28_,_,_,_,_%29.md)
  Performs an alpha composite of an 8-bit-per-channel, 4-channel ARGB buffer over a solid background color.
- [func vImageFlatten_RGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, Bool, vImage_Flags) -> vImage_Error](./vimageflatten_rgba8888%28_,_,_,_,_%29.md)
  Performs an alpha composite of an 8-bit-per-channel, 4-channel RGBA buffer over a solid background color.
### Flattening 4-channel, 8-bit images to three channels
- [func vImageFlatten_ARGB8888ToRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, Bool, vImage_Flags) -> vImage_Error](./vimageflatten_argb8888torgb888%28_,_,_,_,_%29.md)
  Flattens an 8-bit-per-channel ARGB buffer against a solid background to produce an 8-bit-per-channel RGB result.
- [func vImageFlatten_BGRA8888ToRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, Bool, vImage_Flags) -> vImage_Error](./vimageflatten_bgra8888torgb888%28_,_,_,_,_%29.md)
  Flattens an 8-bit-per-channel BGRA buffer against a solid background to produce an 8-bit-per-channel RGB result.
- [func vImageFlatten_RGBA8888ToRGB888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, Bool, vImage_Flags) -> vImage_Error](./vimageflatten_rgba8888torgb888%28_,_,_,_,_%29.md)
  Flattens an 8-bit-per-channel RGBA buffer against a solid background to produce an 8-bit-per-channel RGB result.
- [vImageFlatten_BGRA8888ToBGR888](./vimageflatten_bgra8888tobgr888.md)
  Flattens an 8-bit-per-channel BGRA buffer against a solid background to produce an 8-bit-per-channel BGR result.
- [vImageFlatten_RGBA8888ToBGR888](./vimageflatten_rgba8888tobgr888.md)
  Flattens an 8-bit-per-channel RGBA buffer against a solid background to produce an 8-bit-per-channel BGR result.
### Flattening 4-channel,16-bit images
- [func vImageFlatten_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt16>, Bool, vImage_Flags) -> vImage_Error](./vimageflatten_argb16u%28_,_,_,_,_%29.md)
  Performs an alpha composite of an unsigned 16-bit-per-channel, 4-channel ARGB buffer over a solid background color.
- [func vImageFlatten_RGBA16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt16>, Bool, vImage_Flags) -> vImage_Error](./vimageflatten_rgba16u%28_,_,_,_,_%29.md)
  Performs an alpha composite of an unsigned 16-bit-per-channel, 4-channel RGBA buffer over a solid background color.
- [func vImageFlatten_RGBA16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Int16>, Bool, vImage_Flags) -> vImage_Error](./vimageflatten_rgba16q12%28_,_,_,_,_%29.md)
  Performs an alpha composite of a fixed-point 16-bit-per-channel, 4-channel RGBA buffer over a solid background color.
- [func vImageFlatten_ARGB16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Int16>, Bool, vImage_Flags) -> vImage_Error](./vimageflatten_argb16q12%28_,_,_,_,_%29.md)
  Performs an alpha composite of a fixed-point 16-bit-per-channel, 4-channel ARGB buffer over a solid background color.
### Flattening 4-channel, 32-bit images
- [func vImageFlatten_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Bool, vImage_Flags) -> vImage_Error](./vimageflatten_argbffff%28_,_,_,_,_%29.md)
  Performs an alpha composite of a 32-bit-per-channel, 4-channel ARGB buffer over a solid background color.
- [func vImageFlatten_RGBAFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Bool, vImage_Flags) -> vImage_Error](./vimageflatten_rgbaffff%28_,_,_,_,_%29.md)
  Performs an alpha composite of a 32-bit-per-channel, 4-channel RGBA buffer over a solid background color.
### Flattening 4-channel, 32-bit images to three channels
- [func vImageFlatten_ARGBFFFFToRGBFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Bool, vImage_Flags) -> vImage_Error](./vimageflatten_argbfffftorgbfff%28_,_,_,_,_%29.md)
  Flattens a 32-bit-per-channel ARGB buffer against a solid background to produce a 32-bit-per-channel RGB result.
- [func vImageFlatten_BGRAFFFFToRGBFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Bool, vImage_Flags) -> vImage_Error](./vimageflatten_bgrafffftorgbfff%28_,_,_,_,_%29.md)
  Flattens a 32-bit-per-channel BGRA buffer against a solid background to produce a 32-bit-per-channel RGB result.
- [func vImageFlatten_RGBAFFFFToRGBFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<Float>, Bool, vImage_Flags) -> vImage_Error](./vimageflatten_rgbafffftorgbfff%28_,_,_,_,_%29.md)
  Flattens a 32-bit-per-channel RGBA buffer against a solid background to produce a 32-bit-per-channel RGB result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/flattening-data)*