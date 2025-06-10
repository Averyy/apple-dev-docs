# vImageDestroyResamplingFilter(_:)

**Framework**: Accelerate  
**Kind**: func

Disposes of a resampling filter object.

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
func vImageDestroyResamplingFilter(_ filter: ResamplingFilter!)
```

#### Discussion

This function deallocates the memory associated with a resampling filter object that was created by calling the function [`vImageNewResamplingFilter(_:_:)`](vimagenewresamplingfilter(_:_:).md). Don’t directly deallocate this memory yourself.

Don’t pass this function a resampling filter object created by the function [`vImageNewResamplingFilterForFunctionUsingBuffer(_:_:_:_:_:_:)`](vimagenewresamplingfilterforfunctionusingbuffer(_:_:_:_:_:_:).md). You’re responsible for deallocating the memory associated with resampling filter objects created by that call.

## Parameters

- `filter`: The resampling filter object to dispose of.

## See Also

- [func vImageNewResamplingFilter(Float, vImage_Flags) -> ResamplingFilter!](vimagenewresamplingfilter(_:_:).md)
  Creates a resampling filter object that corresponds to the default kernel supplied by the vImage framework.
- [func vImageNewResamplingFilterForFunctionUsingBuffer(ResamplingFilter, Float, ((UnsafePointer<Float>?, UnsafeMutablePointer<Float>?, UInt, UnsafeMutableRawPointer?) -> Void)!, Float, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](vimagenewresamplingfilterforfunctionusingbuffer(_:_:_:_:_:_:).md)
  Creates a resampling filter object that encapsulates a resampling kernel function that you provide.
- [func vImageGetResamplingFilterExtent(ResamplingFilter, vImage_Flags) -> vImagePixelCount](vimagegetresamplingfilterextent(_:_:).md)
  Returns the maximum sampling radius for a resampling filter.
- [func vImageGetResamplingFilterSize(Float, ((UnsafePointer<Float>?, UnsafeMutablePointer<Float>?, UInt, UnsafeMutableRawPointer?) -> Void)!, Float, vImage_Flags) -> Int](vimagegetresamplingfiltersize(_:_:_:_:).md)
  Returns the minimum size, in bytes, for the buffer needed by the new resampling filter function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagedestroyresamplingfilter(_:))*