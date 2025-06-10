# vImageNewResamplingFilterForFunctionUsingBuffer(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Creates a resampling filter object that encapsulates a resampling kernel function that you provide.

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
func vImageNewResamplingFilterForFunctionUsingBuffer(_ filter: ResamplingFilter, _ scale: Float, _ kernelFunc: ((UnsafePointer<Float>?, UnsafeMutablePointer<Float>?, UInt, UnsafeMutableRawPointer?) -> Void)!, _ kernelWidth: Float, _ userData: UnsafeMutableRawPointer!, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes described in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

This function creates a reusable resampling filter object  that you can pass to a shear function. Before calling this function, you must allocate a buffer to contain the resampling filter object returned by this function. You can get the necessary size by calling the function [`vImageGetResamplingFilterSize(_:_:_:_:)`](vimagegetresamplingfiltersize(_:_:_:_:).md). When you no longer need this object, you’re responsible for deallocating its memory. Don’t use the function [`vImageDestroyResamplingFilter(_:)`](vimagedestroyresamplingfilter(_:).md) to deallocate custom resampling filter objects; it’s not designed to deallocate them.

If you need precise control over the memory used for a resampling filter object  but want to use the default, pass `NULL` as the `kernelFunc` parameter. This causes vImage to create a resampling filter object that corresponds to its default kernel. You can then determine where in memory the resampling filter object is located. You can reuse the buffer to reduce memory allocation, and so on. Note that a resampling filter object created in this way isn’t necessarily the same as one created by the function [`vImageNewResamplingFilter(_:_:)`](vimagenewresamplingfilter(_:_:).md). You must still  deallocate the object yourself; you can’t pass it to the function [`vImageDestroyResamplingFilter(_:)`](vimagedestroyresamplingfilter(_:).md).

## Parameters

- `filter`: A pointer to a buffer. On return, the buffer contains a resampling filter object. You must allocate the memory for this buffer yourself. Call the function    to obtain the size of this buffer.
- `scale`: A scale factor to associated with the resampling filter object. Shear functions to which you pass the resampling filter object use this factor when performing a shear operation. The shear function applies the scale factor  to the entire image, in a direction appropriate to the shear function, either horizontal or vertical.
- `kernelFunc`: If you need precise control over the memory used for a resampling filter object  but want to use the default, pass   as the   parameter. This causes vImage to create a resampling filter object that corresponds to its default kernel. You can then determine where in memory the resampling filter object is located. You can reuse the buffer to reduce memory allocation, and so on. Note that a resampling filter object created in this way isn’t necessarily the same as one created by the function  . You must still  deallocate the object yourself; you can’t pass it to the function  .
- `kernelWidth`: A bounding value for the domain of your resampling kernel function. The shearing operation passes x-values to your function that are in the range –  and + , inclusive.
- `userData`: If your resampling kernel function does nor require user data, pass  .
- `flags`: This function ignores the   flag.

## See Also

- [func vImageNewResamplingFilter(Float, vImage_Flags) -> ResamplingFilter!](vimagenewresamplingfilter(_:_:).md)
  Creates a resampling filter object that corresponds to the default kernel supplied by the vImage framework.
- [func vImageGetResamplingFilterExtent(ResamplingFilter, vImage_Flags) -> vImagePixelCount](vimagegetresamplingfilterextent(_:_:).md)
  Returns the maximum sampling radius for a resampling filter.
- [func vImageGetResamplingFilterSize(Float, ((UnsafePointer<Float>?, UnsafeMutablePointer<Float>?, UInt, UnsafeMutableRawPointer?) -> Void)!, Float, vImage_Flags) -> Int](vimagegetresamplingfiltersize(_:_:_:_:).md)
  Returns the minimum size, in bytes, for the buffer needed by the new resampling filter function.
- [func vImageDestroyResamplingFilter(ResamplingFilter!)](vimagedestroyresamplingfilter(_:).md)
  Disposes of a resampling filter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagenewresamplingfilterforfunctionusingbuffer(_:_:_:_:_:_:))*