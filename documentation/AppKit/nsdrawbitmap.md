# NSDrawBitmap(_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: AppKit  
**Kind**: func

Draws a bitmap image.

**Availability**:
- macOS ?+

## Declaration

```swift
func NSDrawBitmap(_ rect: NSRect, _ width: Int, _ height: Int, _ bps: Int, _ spp: Int, _ bpp: Int, _ bpr: Int, _ isPlanar: Bool, _ hasAlpha: Bool, _ colorSpaceName: NSColorSpaceName, _ data: UnsafePointer<UnsafePointer<UInt8>?>)
```

#### Discussion

This function is marginally obsolete. Most applications are better served using the [`NSBitmapImageRep`](nsbitmapimagerep.md) class to read and display bitmap images.

This function renders an image from a bitmap, binary data that describes the pixel values for the image.

This function renders a bitmap image using an appropriate display operator. It puts the image in the rectangular area specified by its first argument, `rect`; the rectangle is specified in the current coordinate system and is located in the current window. The next two arguments, `pixelsWide` and `pixelsHigh`, give the width and height of the image in pixels. If either of these dimensions is larger or smaller than the corresponding dimension of the destination rectangle, the image will be scaled to fit.

The remaining arguments describe the bitmap data, as explained in the following paragraphs.

The `bitsPerSample` argument is the number of bits per sample for each pixel and `samplesPerPixel` is the number of samples per pixel. `bitsPerPixel` is based on `samplesPerPixel` and the configuration of the bitmap: if the configuration is planar, then the value of `bitsPerPixel` should equal the value of `bitsPerSample`; if the configuration isn’t planar (is meshed instead), `bitsPerPixel` should equal `bitsPerSample * samplesPerPixel`.

The `bytesPerRow` argument is calculated in one of two ways, depending on the configuration of the image data (data configuration is described below). If the data is planar, `bytesPerRow is (7 + (pixelsWide * bitsPerSample)) / 8`. If the data is meshed, `bytesPerRow is (7 + (pixelsWide * bitsPerSample * samplesPerPixel)) / 8`.

A sample is data that describes one component of a pixel. In an RGB color system, the red, green, and blue components of a color are specified as separate samples, as are the cyan, magenta, yellow, and black components in a CMYK system. Color values in a grayscale are a single sample. Alpha values that determine transparency and opaqueness are specified as a coverage sample separate from color. In bitmap images with alpha, the color (or gray) components have to be premultiplied with the alpha. This is the way images with alpha are displayed, this is the way they are read back, and this is the way they are stored in TIFFs.

The `isPlanar` argument refers to the way data is configured in the bitmap. This flag should be set to [`true`](https://developer.apple.com/documentation/swift/true) if a separate data channel is used for each sample. The function provides for up to five channels, `data1`, `data2`, `data3`, `data4`, and `data5`. It should be set [`false`](https://developer.apple.com/documentation/swift/false) if sample values are interwoven in a single channel (meshed); all values for one pixel are specified before values for the next pixel.

Grayscale windows store pixel data in planar configuration; color windows store it in meshed configuration. `NSDrawBitmap` can render meshed data in a planar window, or planar data in a meshed window. However, it’s more efficient if the image has a depth (`bitsPerSample`) and configuration (`isPlanar`) that match the window.

The `hasAlpha` argument indicates whether the image contains alpha. If it does, the number of samples should be 1 greater than the number of color components in the model (for example, 4 for RGB).

The `colorSpace` argument can be [`custom`](nscolorspacename/custom.md), indicating that the image data is to be interpreted according to the current color space in the graphics state. This allows for imaging using custom color spaces. The image parameters supplied as the other arguments should match what the color space is expecting.

If the image data is planar, `data`[0] through `data`[`samplesPerPixel`–1] point to the planes; if the `data` is meshed, only `data`[0] needs to be set.

## See Also

- [class func tiffRepresentationOfImageReps(in: [NSImageRep]) -> Data?](nsbitmapimagerep/tiffrepresentationofimagereps(in:).md)
  Returns a TIFF representation of the specified images.
- [class func tiffRepresentationOfImageReps(in: [NSImageRep], using: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?](nsbitmapimagerep/tiffrepresentationofimagereps(in:using:factor:).md)
  Returns a TIFF representation of the specified images using the specified compression scheme and factor.
- [var tiffRepresentation: Data?](nsbitmapimagerep/tiffrepresentation.md)
  A TIFF representation of the bitmap image data.
- [func tiffRepresentation(using: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?](nsbitmapimagerep/tiffrepresentation(using:factor:).md)
  Returns a TIFF representation of the image using the specified compression.
- [class func representationOfImageReps(in: [NSImageRep], using: NSBitmapImageRep.FileType, properties: [NSBitmapImageRep.PropertyKey : Any]) -> Data?](nsbitmapimagerep/representationofimagereps(in:using:properties:).md)
  Formats the specified bitmap images using the specified storage type and properties and returns them in a data object.
- [func representation(using: NSBitmapImageRep.FileType, properties: [NSBitmapImageRep.PropertyKey : Any]) -> Data?](nsbitmapimagerep/representation(using:properties:).md)
  Formats the bitmap representation’s image data using the specified storage type and properties and returns it in a data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawbitmap(_:_:_:_:_:_:_:_:_:_:_:))*