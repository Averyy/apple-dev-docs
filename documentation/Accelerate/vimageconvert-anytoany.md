# vImageConvert_AnyToAny(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Converts the pixels in a vImage buffer to another format, using the specified converter.

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
func vImageConvert_AnyToAny(_ converter: vImageConverter, _ srcs: UnsafePointer<vImage_Buffer>, _ dests: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ flags: vImage_Flags) -> vImage_Error
```

## Mentions

- [Building a basic image conversion workflow](building-a-basic-image-conversion-workflow.md)

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, a negative value indicates one of the error codes that [`Data Types and Constants`](data-types-and-constants.md) describes, and a positive value indicates the required size for the temporary buffer.

#### Discussion

With an appropriately configured vImage converter, convert the image channels found in `srcs` to the image channels found in `dests`. Whenever possible, conversion passes are vectorized and multithreaded to reduce the time and energy cost of the function.

Use [`vImageConverter_MustOperateOutOfPlace(_:_:_:_:)`](vimageconverter_mustoperateoutofplace(_:_:_:_:).md) to determine whether a particular conversion can operate in place. For an in-place conversion to work, you must ensure that `srcs[i].data = dests[i].data` and `srcs[i].rowBytes = dests[i].rowBytes`.

All scanlines must start at a byte-aligned address. Some formats have 1, 2, 4, or 12 bits per channel/pixel and might not start at a byte-aligned address. A single byte can’t span multiple rows of data.

Some formats, particularly YUV422 and YUV420, and those with a pixel size that’s not evenly divisible by 8 bits, operate in chunks containing multiple pixels. For example, a YCbCr422 chunk may have `{Y0, Cb, Y1, Cr}` in the chunk. The chunk contains two pixels, each with an independent Y (luminance) component, but shared chrominance.  Even though the chunk width is two, it’s still possible for an image to have a width that’s not divisible by two. This means that some part of the chunk on the rightmost edge of the scanline must refer to a nonexistent pixel.

When reading incomplete chunks, vImage touches only the unused parts of the chunk when it knows it to be safe to do so. When writing incomplete chunks, vImage copies the rightmost valid pixel color into the unused part of the chunk. Thus, on reading, the entire chunk doesn’t have to be there, but on writing, it does. Conventions vary among chunk-using imaging pipelines, and this conservative approach should interoperate with most. However, be careful when writing to chunk-based formats (not to be confused with chunky formats, which merely have several channels interleaved) to make sure that the buffer is large enough to tolerate the write policy.  If you’re tiling chunk-based data, be careful not to run tile boundaries through the middle of a chunk.  Chunks are assumed to be indivisible.

##### Optimize Performance with Temporary Buffers

This function uses a multiple-pass algorithm that saves intermediate pixel values between passes. In some cases, the destination buffer may not be large enough to store that intermediate data, so the operation requires additional storage.

Pass `nil` to the `tempBuffer` parameter to have vImage create and manage this temporary storage for you.

In cases where your code calls the function frequently (for example, when processing video), create and manage this temporary buffer yourself and reuse it across function calls. Reusing a buffer avoids vImage allocating the temporary storage with each call.

To use your own temporary buffer, first call the function with the same values for all other parameters that you intend to use for subsequent calls. In addition, pass the `kvImageGetTempBufferSize` flag. The `kvImageGetTempBufferSize` instructs the function not to perform any processing, and to return a positive value that represents the minimum size, in bytes, of the temporary buffer. A negative return value represents an error.

After you allocate the memory for the temporary buffer, pass that to the `tempBuffer` parameter for subsequent calls to the function, and don’t pass the `kvImageGetTempBufferSize` flag.

## Parameters

- `converter`: A valid   instance indicating the conversion to perform. You can use the same converter concurrently in multiple threads. To create a converter, you can use  ,  ,  , or  .
- `srcs`: A pointer to an array of vImage buffer structures that describe the color planes that make up the input image. For the order and number of input buffers, see the description of the function that creates the   instance. You can also determine the order manually using  .
- `dests`: A pointer to an array of vImage buffer structures that describe the color planes that make up the result image. For the order and number of input buffers, see the description of the function that creates the   instance. You can also determine the order manually using  . The destination buffer may only alias the   buffers if   returns 0 and the respective scanlines of the aliasing buffers start at the same address.
- `tempBuffer`: A pointer to workspace memory the function uses as it operates on an image. Pass   to instruct the function to allocate, use, and then free its own temporary buffer.
- `flags`: The options to use when performing this operation. The following flags are supported:

## See Also

- [vImage Buffer Type Codes](1399056-vimage-buffer-type-codes.md)
  Constants that specify the contents of vImage buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_anytoany(_:_:_:_:_:))*