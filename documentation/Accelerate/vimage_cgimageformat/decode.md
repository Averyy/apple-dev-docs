# decode

**Framework**: Accelerate  
**Kind**: property

The decode array for the image.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var decode: UnsafePointer<CGFloat>!
```

#### Discussion

The decode array contains the upper and lower bounds for each color channel. When you define a decode array, the conversion functions that accept a [`vImage_CGImageFormat`](vimage_cgimageformat.md) parameter apply a linear transform to map colors to the specified bounds.

A decode array for an RGB color space contains six entries: one pair for each red, green, and blue channel.

The following code shows how the vImage library remaps a buffer that contains five planar pixels in the range `0 ... 0.5` to the range `0 ... 1`. The code passes a decode array with the values `[0, 0.5]` to the [`makeCGImage(cgImageFormat:)`](vimage/pixelbuffer/makecgimage(cgimageformat:).md) function that remaps the source pixel values from `[0.0, 0.125, 0.25, 0.375, 0.5]` to `[0.0, 0.25, 0.5, 0.75, 1.0]`.

```swift
// Create a grayscale vImage pixel buffer.
let pixels: [Pixel_F] = [0.0, 0.125, 0.25, 0.375, 0.5]
let pixelBuffer = vImage.PixelBuffer(
    pixelValues: pixels,
    size: .init(width: 5, height: 1),
    pixelFormat: vImage.PlanarF.self)

// Define the decode array to `0 ... 0.5`.
let decodeArray: [CGFloat] = [0, 0.5]

decodeArray.withUnsafeBufferPointer { decodeArrayPtr in

    let cgImageFormat = vImage_CGImageFormat(
        bitsPerComponent: 32,
        bitsPerPixel: 32,
        colorSpace: Unmanaged.passRetained(CGColorSpaceCreateDeviceGray()),
        bitmapInfo: CGBitmapInfo(
            rawValue: CGBitmapInfo.byteOrder32Little.rawValue |
                CGBitmapInfo.floatComponents.rawValue |
                CGImageAlphaInfo.none.rawValue),
        version: 0,
        decode: decodeArrayPtr.baseAddress,
        renderingIntent: .defaultIntent)
    
    let cgImage = pixelBuffer.makeCGImage(cgImageFormat: cgImageFormat)
    
    // Display the raw pixel values of the `CGImage`.
    if let pixelData = cgImage?.dataProvider?.data {
        let pixelPointer = (pixelData as NSData)
            .bytes
            .assumingMemoryBound(to: Pixel_F.self)
        
        let recreatedPixels = UnsafeBufferPointer<Pixel_F>(
            start: pixelPointer,
            count: 5)
        
        // Prints "[0.0, 0.25, 0.5, 0.75, 1.0]".
        print(Array(recreatedPixels))
    }
}
```

Set the `decodeArray` to `nil` to prevent the vImage-Core Graphics conversion functions from remapping values.

## See Also

- [var bitsPerComponent: UInt32](vimage_cgimageformat/bitspercomponent.md)
  The number of bits that represents one channel of data in one pixel.
- [var bitsPerPixel: UInt32](vimage_cgimageformat/bitsperpixel.md)
  The number of bits that represents one pixel.
- [var colorSpace: Unmanaged<CGColorSpace>!](vimage_cgimageformat/colorspace.md)
  A description of the position of the pixel data in the image, relative to a reference XYZ color space.
- [var bitmapInfo: CGBitmapInfo](vimage_cgimageformat/bitmapinfo.md)
  The component information that describes the color channels.
- [var version: UInt32](vimage_cgimageformat/version.md)
  The version number.
- [var renderingIntent: CGColorRenderingIntent](vimage_cgimageformat/renderingintent.md)
  A rendering intent constant that specifies how Core Graphics handles colors that aren’t within the destination color space gamut.
- [var componentCount: Int](vimage_cgimageformat/componentcount.md)
  The number of color and alpha channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_cgimageformat/decode)*