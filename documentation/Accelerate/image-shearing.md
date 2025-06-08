# Image shearing

**Framework**: Accelerate

Shear images horizontally and vertically.

## Topics

### Shearing an image horizontally
- [Single-precision horizontal shearing](single-precision-horizontal-shearing.md)
  Apply single-precision horizontal shearing to images.
- [Double-precision horizontal shearing](double-precision-horizontal-shearing.md)
  Apply double-precision horizontal shearing to images.
### Shearing an image vertically
- [Single-precision vertical shearing](single-precision-vertical-shearing.md)
  Apply single-precision vertical shearing to images.
- [Double-precision vertical shearing](double-precision-vertical-shearing.md)
  Apply double-precision vertical shearing to images.
### Resampling filters
- [func vImageNewResamplingFilter(Float, vImage_Flags) -> ResamplingFilter!](vimagenewresamplingfilter(_:_:).md)
  Creates a resampling filter object that corresponds to the default kernel supplied by the vImage framework.
- [func vImageNewResamplingFilterForFunctionUsingBuffer(ResamplingFilter, Float, ((UnsafePointer<Float>?, UnsafeMutablePointer<Float>?, UInt, UnsafeMutableRawPointer?) -> Void)!, Float, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](vimagenewresamplingfilterforfunctionusingbuffer(_:_:_:_:_:_:).md)
  Creates a resampling filter object that encapsulates a resampling kernel function that you provide.
- [func vImageGetResamplingFilterExtent(ResamplingFilter, vImage_Flags) -> vImagePixelCount](vimagegetresamplingfilterextent(_:_:).md)
  Returns the maximum sampling radius for a resampling filter.
- [func vImageGetResamplingFilterSize(Float, ((UnsafePointer<Float>?, UnsafeMutablePointer<Float>?, UInt, UnsafeMutableRawPointer?) -> Void)!, Float, vImage_Flags) -> Int](vimagegetresamplingfiltersize(_:_:_:_:).md)
  Returns the minimum size, in bytes, for the buffer needed by the new resampling filter function.
- [func vImageDestroyResamplingFilter(ResamplingFilter!)](vimagedestroyresamplingfilter(_:).md)
  Disposes of a resampling filter object.

## See Also

- [Resampling in vImage](resampling-in-vimage.md)
  Learn how vImage resamples image data during geometric operations.
- [Reducing artifacts with custom resampling filters](reducing-artifacts-with-custom-resampling-filters.md)
  Implement custom linear interpolation to prevent the ringing effects associated with scaling an image with the default Lanczos algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/image-shearing)*