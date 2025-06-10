# vImageCreateCGImageFromBuffer(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Creates a Core Graphics image from a vImage buffer.

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
func vImageCreateCGImageFromBuffer(_ buf: UnsafePointer<vImage_Buffer>, _ format: UnsafePointer<vImage_CGImageFormat>, _ callback: ((UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Void)!, _ userData: UnsafeMutableRawPointer!, _ flags: vImage_Flags, _ error: UnsafeMutablePointer<vImage_Error>!) -> Unmanaged<CGImage>!
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The following code shows a passthrough function that generates an output Core Graphics image using no-copy mode. The vImage buffer, `buffer`, and the Core Graphics image, `destinationCGImage`, share the same memory. In this example, the deallocation callback deallocates the memory that the `data` variable points to:

```swift
static func passThrough(sourceImage: CGImage) throws -> CGImage? {
    
    let alignmentAndRowBytes = try vImage_Buffer.preferredAlignmentAndRowBytes(
        width: sourceImage.width,
        height: sourceImage.height,
        bitsPerPixel: UInt32(sourceImage.bitsPerPixel))
    
    let data = UnsafeMutableRawPointer.allocate(
        byteCount: alignmentAndRowBytes.rowBytes * alignmentAndRowBytes.rowBytes,
        alignment: alignmentAndRowBytes.alignment)
    
    var buffer = vImage_Buffer(
        data: data,
        height: vImagePixelCount(sourceImage.height),
        width: vImagePixelCount(sourceImage.width),
        rowBytes: alignmentAndRowBytes.rowBytes)
    
    var format = vImage_CGImageFormat()
    
    vImageBuffer_InitWithCGImage(
        &buffer,
        &format,
        nil,
        sourceImage,
        vImage_Flags(kvImageNoAllocate))

    func callback(_: UnsafeMutableRawPointer?,
                  bufferData: UnsafeMutableRawPointer?) {
        bufferData?.deallocate()
    }
    
    let destinationCGImage = vImageCreateCGImageFromBuffer(
        &buffer,
        &format,
        callback,
        nil,
        vImage_Flags(kvImageNoAllocate),
        nil)
    
    return destinationCGImage?.takeRetainedValue()
}
```

## Parameters

- `buf`: The source vImage buffer.
- `format`: The image format of the source vImage buffer. If the format’s color space is  , the function uses sRGB. The new Core Graphics image retains the color space.
- `callback`: A callback function that deallocates the source buffer’s data when the returned image no longer needs it. Pass this callback when you call this function in no-copy mode; that is, when you pass   to  . The system may call this function at any time — including before   returns — and from any thread.
- `userData`: The value that passes to the   function’s   parameter.
- `flags`: Pass   to specify high-quality resampling if the function resamples the output image to a smaller size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecreatecgimagefrombuffer(_:_:_:_:_:_:))*