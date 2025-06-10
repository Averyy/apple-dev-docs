# vImageNewResamplingFilter(_:_:)

**Framework**: Accelerate  
**Kind**: func

Creates a resampling filter object that corresponds to the default kernel supplied by the vImage framework.

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
func vImageNewResamplingFilter(_ scale: Float, _ flags: vImage_Flags) -> ResamplingFilter!
```

#### Return Value

A pointer to a newly created resampling filter object; otherwise `NULL`.

#### Discussion

This function creates a reusable resampling filter object  that you can pass to a shear function. The resampling filter encapsulated by the object is the default kernel for vImage This function allocates the memory needed for the resampling filter object. To deallocate this memory, call the function [`vImageDestroyResamplingFilter(_:)`](vimagedestroyresamplingfilter(_:).md). Don’t attempt to deallocate the memory yourself.

## Parameters

- `scale`: A scale factor to associated with the resampling filter object. Shear functions to which you pass the resampling filter object use this factor when performing a shear operation. The shear function applies the scale factor  to the entire image, in a direction appropriate to the shear function, either horizontal or vertical.
- `flags`: This function ignores the   flag.

## See Also

- [func vImageNewResamplingFilterForFunctionUsingBuffer(ResamplingFilter, Float, ((UnsafePointer<Float>?, UnsafeMutablePointer<Float>?, UInt, UnsafeMutableRawPointer?) -> Void)!, Float, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](vimagenewresamplingfilterforfunctionusingbuffer(_:_:_:_:_:_:).md)
  Creates a resampling filter object that encapsulates a resampling kernel function that you provide.
- [func vImageGetResamplingFilterExtent(ResamplingFilter, vImage_Flags) -> vImagePixelCount](vimagegetresamplingfilterextent(_:_:).md)
  Returns the maximum sampling radius for a resampling filter.
- [func vImageGetResamplingFilterSize(Float, ((UnsafePointer<Float>?, UnsafeMutablePointer<Float>?, UInt, UnsafeMutableRawPointer?) -> Void)!, Float, vImage_Flags) -> Int](vimagegetresamplingfiltersize(_:_:_:_:).md)
  Returns the minimum size, in bytes, for the buffer needed by the new resampling filter function.
- [func vImageDestroyResamplingFilter(ResamplingFilter!)](vimagedestroyresamplingfilter(_:).md)
  Disposes of a resampling filter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagenewresamplingfilter(_:_:))*