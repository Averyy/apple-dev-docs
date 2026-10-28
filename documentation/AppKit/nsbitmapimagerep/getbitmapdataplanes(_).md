# getBitmapDataPlanes(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns by indirection bitmap data of the bitmap image representation separated into planes.

**Availability**:
- macOS

## Declaration

```swift
func getBitmapDataPlanes(_ data: UnsafeMutablePointer<UnsafeMutablePointer<UInt8>?>)
```

```objc
- (void) getBitmapDataPlanes:(unsigned char **) data;
```

## Discussion

Color components in planar configuration are arranged in the expected order—for example, red before green before blue for RGB color. All color planes precede the coverage plane. For bitmaps whose [`bitmapFormat`](./bitmapformat.md) mask does not include [`alphaNonpremultiplied`](./format/alphanonpremultiplied.md), if a coverage plane exists, the bitmap’s color components are premultiplied with it. In this case, if you modify the contents of the bitmap, you are responsible for premultiplying the data.

## Parameters

- `data`: On return, a C array of five character pointers. If the bitmap data is in planar configuration, each pointer will be initialized to point to one of the data planes. If there are less than five planes, the remaining pointers will be set to `NULL`. If the bitmap data is in meshed configuration, only the first pointer will be initialized; the others will be `NULL`.

## See Also

### Related Documentation
- [init?(bitmapDataPlanes: UnsafeMutablePointer<UnsafeMutablePointer<UInt8>?>?, pixelsWide: Int, pixelsHigh: Int, bitsPerSample: Int, samplesPerPixel: Int, hasAlpha: Bool, isPlanar: Bool, colorSpaceName: NSColorSpaceName, bitmapFormat: NSBitmapImageRep.Format, bytesPerRow: Int, bitsPerPixel: Int)](./init%28bitmapdataplanes,pixelswide,pixelshigh,bitspersample,samplesperpixel,hasalpha,isplanar,colorspacename,bitmapformat,bytesperrow,bitsperpixel%29.md)
  Initializes a newly allocated bitmap image representation so it can render the specified image.
- [var isPlanar: Bool](./isplanar.md)
  A Boolean value that indicates whether the image data is in a planar configuration.
- [init?(bitmapDataPlanes: UnsafeMutablePointer<UnsafeMutablePointer<UInt8>?>?, pixelsWide: Int, pixelsHigh: Int, bitsPerSample: Int, samplesPerPixel: Int, hasAlpha: Bool, isPlanar: Bool, colorSpaceName: NSColorSpaceName, bytesPerRow: Int, bitsPerPixel: Int)](./init%28bitmapdataplanes,pixelswide,pixelshigh,bitspersample,samplesperpixel,hasalpha,isplanar,colorspacename,bytesperrow,bitsperpixel%29.md)
  Initializes a newly allocated bitmap image representation so it can render the specified image.
### Getting the Bitmap Data
- [var bitmapData: UnsafeMutablePointer<UInt8>?](./bitmapdata.md)
  A pointer to the bitmap data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/getbitmapdataplanes(_:))*