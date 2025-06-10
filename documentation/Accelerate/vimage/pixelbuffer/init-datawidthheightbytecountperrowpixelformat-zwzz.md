# init(data:width:height:byteCountPerRow:pixelFormat:)

**Framework**: Accelerate  
**Kind**: init

Returns a new buffer that references existing data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
init(data: UnsafeMutableRawPointer, width: Int, height: Int, byteCountPerRow: Int, pixelFormat: Format.Type)
```

#### Discussion

You can use this function to simplify interoperation with other libraries and frameworks. For example, the following code shows a function that permutes the channels of a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) instance. The function creates a pixel buffer that uses the storage a [`CGDataProvider`](https://developer.apple.com/documentation/CoreGraphics/CGDataProvider) instance’s [`data`](https://developer.apple.com/documentation/CoreGraphics/CGDataProvider/data) property provides. The [`data`](https://developer.apple.com/documentation/CoreGraphics/CGDataProvider/data) property is a copy of the image data, therefore, the code returns a new [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) instance that it generates from the permuted pixel buffer.

```swift
static func permute(image: CGImage,
                    to permuteMap: (UInt8, UInt8, UInt8, UInt8)) -> CGImage? {
    
    let bitsPerPixel = image.bitsPerPixel
    let bitsPerComponent = image.bitsPerComponent

    guard bitsPerPixel == 32 && bitsPerComponent == 8,
          let format = vImage_CGImageFormat(cgImage: image),
          let pixelData = image.dataProvider?.data else {
        return nil
    }
    
    return withExtendedLifetime(pixelData) {
        let pixelBuffer = vImage.PixelBuffer(
            data: UnsafeMutableRawPointer(mutating: CFDataGetBytePtr($0)),
            width: image.width,
            height: image.height,
            byteCountPerRow: image.bytesPerRow,
            pixelFormat: vImage.Interleaved8x4.self)
        
        pixelBuffer.permuteChannels(to: permuteMap,
                                    destination: pixelBuffer)
        
        return pixelBuffer.makeCGImage(cgImageFormat: format)
    }
}
```

> ❗ **Important**:  The pixel buffer is valid only for the lifetime of `data`.

## Parameters

- `data`: A pointer to the top-left pixel of the buffer.
- `width`: The width, in pixels, of the pixel buffer.
- `height`: The height, in pixels, of the pixel buffer.
- `byteCountPerRow`: The number of bytes in a pixel row.
- `pixelFormat`: The pixel format of the initialized buffer.

## See Also

- [init<U>(pixelValues: U, size: vImage.Size, pixelFormat: Format.Type)](vimage/pixelbuffer/init(pixelvalues:size:pixelformat:).md)
  Creates a new pixel buffer by copying the supplied collection of pixel values.
- [init(data: UnsafeMutableRawPointer, width: Int, height: Int, byteCountPerRow: Int?, pixelFormat: Format.Type)](vimage/pixelbuffer/init(data:width:height:bytecountperrow:pixelformat:)-27czc.md)
  Calculates the correct bytes per row and returns a new buffer that references existing data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/init(data:width:height:bytecountperrow:pixelformat:)-zwzz)*