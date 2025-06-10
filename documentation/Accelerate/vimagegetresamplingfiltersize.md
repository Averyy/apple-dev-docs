# vImageGetResamplingFilterSize(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns the minimum size, in bytes, for the buffer needed by the new resampling filter function.

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
func vImageGetResamplingFilterSize(_ scale: Float, _ kernelFunc: ((UnsafePointer<Float>?, UnsafeMutablePointer<Float>?, UInt, UnsafeMutableRawPointer?) -> Void)!, _ kernelWidth: Float, _ flags: vImage_Flags) -> Int
```

#### Return Value

The minimum size, in bytes, of the buffer.

## Parameters

- `scale`: The scale factor that you plan to pass to the function  .
- `kernelFunc`: The function pointer that you plan to pass to the function  .
- `kernelWidth`: The kernel width that you plan to pass to the function  .
- `flags`: The flags that you plan to pass to the function  .

## See Also

- [func vImageNewResamplingFilter(Float, vImage_Flags) -> ResamplingFilter!](vimagenewresamplingfilter(_:_:).md)
  Creates a resampling filter object that corresponds to the default kernel supplied by the vImage framework.
- [func vImageNewResamplingFilterForFunctionUsingBuffer(ResamplingFilter, Float, ((UnsafePointer<Float>?, UnsafeMutablePointer<Float>?, UInt, UnsafeMutableRawPointer?) -> Void)!, Float, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](vimagenewresamplingfilterforfunctionusingbuffer(_:_:_:_:_:_:).md)
  Creates a resampling filter object that encapsulates a resampling kernel function that you provide.
- [func vImageGetResamplingFilterExtent(ResamplingFilter, vImage_Flags) -> vImagePixelCount](vimagegetresamplingfilterextent(_:_:).md)
  Returns the maximum sampling radius for a resampling filter.
- [func vImageDestroyResamplingFilter(ResamplingFilter!)](vimagedestroyresamplingfilter(_:).md)
  Disposes of a resampling filter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagegetresamplingfiltersize(_:_:_:_:))*