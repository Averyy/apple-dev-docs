# init(data:width:height:byteCountPerRow:pixelFormat:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new buffer that references existing data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
init(data: UnsafeMutableRawPointer, width: Int, height: Int, byteCountPerRow: Int, pixelFormat: Format.Type)
```

Available when `Format` conforms to `SinglePlanePixelFormat`.

## Discussion

You can use this function to simplify interoperation with other libraries and frameworks. For example, the following code shows a function that permutes the channels of a [`CGImage`](../../../CoreGraphics/cgimage.md) instance. The function creates a pixel buffer that uses the storage a [`CGDataProvider`](../../../CoreGraphics/cgdataprovider.md) instance’s [`data`](../../../CoreGraphics/cgdataprovider/data.md) property provides. The [`data`](../../../CoreGraphics/cgdataprovider/data.md) property is a copy of the image data, therefore, the code returns a new [`CGImage`](../../../CoreGraphics/cgimage.md) instance that it generates from the permuted pixel buffer.

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

### Creating a pixel buffer from raw pixel data
- [init<U>(pixelValues: U, size: vImage.Size, pixelFormat: Format.Type)](./init%28pixelvalues,size,pixelformat%29.md)
  Creates a new pixel buffer by copying the supplied collection of pixel values.
- [init(data: UnsafeMutableRawPointer, width: Int, height: Int, byteCountPerRow: Int?, pixelFormat: Format.Type)](./init%28data,width,height,bytecountperrow,pixelformat%29-27czc.md)
  Calculates the correct bytes per row and returns a new buffer that references existing data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/init(data:width:height:bytecountperrow:pixelformat:)-zwzz)*