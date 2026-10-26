# init(cgImage:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns a bitmap image representation from a Core Graphics image object.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init(cgImage: CGImage)
```

```objc
- (instancetype) initWithCGImage:(CGImageRef) cgImage;
```

#### Return Value

An [`NSBitmapImageRep`](../nsbitmapimagerep.md) object initialized from the contents of the Core Graphics image.

#### Discussion

If you use this method, you should treat the resulting bitmap [`NSBitmapImageRep`](../nsbitmapimagerep.md) object as read only. Because it only retains the value in the `cgImage` parameter, rather than unpacking the data, accessing the pixel data requires the creation of a copy of that data in memory. Changes to that data are not saved back to the Core Graphics image.

## Parameters

- `cgImage`: A Core Graphics image object (an opaque type) from which to create the receiver. This opaque type is retained.

## See Also

### Related Documentation
- [var cgImage: CGImage?](./cgimage.md)
  A Core Graphics image object based on the bitmap image representation’s data.
### Creating Bitmap Representations of Images
- [class func imageReps(with: Data) -> [NSImageRep]](./imagereps%28with%29.md)
  Creates and returns an array of bitmap image representation objects that correspond to the images in the specified data.
- [func colorize(byMappingGray: CGFloat, to: NSColor?, blackMapping: NSColor?, whiteMapping: NSColor?)](./colorize%28bymappinggray,to,blackmapping,whitemapping%29.md)
  Colorizes a grayscale image.
- [init?(bitmapDataPlanes: UnsafeMutablePointer<UnsafeMutablePointer<UInt8>?>?, pixelsWide: Int, pixelsHigh: Int, bitsPerSample: Int, samplesPerPixel: Int, hasAlpha: Bool, isPlanar: Bool, colorSpaceName: NSColorSpaceName, bitmapFormat: NSBitmapImageRep.Format, bytesPerRow: Int, bitsPerPixel: Int)](./init%28bitmapdataplanes,pixelswide,pixelshigh,bitspersample,samplesperpixel,hasalpha,isplanar,colorspacename,bitmapformat,bytesperrow,bitsperpixel%29.md)
  Initializes a newly allocated bitmap image representation so it can render the specified image.
- [init?(bitmapDataPlanes: UnsafeMutablePointer<UnsafeMutablePointer<UInt8>?>?, pixelsWide: Int, pixelsHigh: Int, bitsPerSample: Int, samplesPerPixel: Int, hasAlpha: Bool, isPlanar: Bool, colorSpaceName: NSColorSpaceName, bytesPerRow: Int, bitsPerPixel: Int)](./init%28bitmapdataplanes,pixelswide,pixelshigh,bitspersample,samplesperpixel,hasalpha,isplanar,colorspacename,bytesperrow,bitsperpixel%29.md)
  Initializes a newly allocated bitmap image representation so it can render the specified image.
- [init(ciImage: CIImage)](./init%28ciimage%29-7bi19.md)
  Returns a bitmap image representation from a Core Image object.
- [init?(data: Data)](./init%28data%29.md)
  Initializes a newly allocated bitmap image representation from the specified data.
- [init(forIncrementalLoad: ())](./init%28forincrementalload%29.md)
  Initializes a newly allocated bitmap image representation for incremental loading.
- [init?(focusedViewRect: NSRect)](./init%28focusedviewrect%29.md)
  Initializes a newly allocated bitmap image representation with bitmap data from a rendered image.
- [+ imageRepWithData:](./imagerepwithdata_.md)
  Creates and returns a bitmap image representation with the first image in the specified data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/init(cgimage:)-7o5tz)*