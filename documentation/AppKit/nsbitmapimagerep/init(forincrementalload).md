# init(forIncrementalLoad:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes a newly allocated bitmap image representation for incremental loading.

**Availability**:
- macOS

## Declaration

```swift
init(forIncrementalLoad: ())
```

```objc
- (instancetype) initForIncrementalLoad;
```

## Discussion

The receiver returns itself after setting its size and data buffer to zero. You can then call [`incrementalLoad(from:complete:)`](./incrementalload%28from,complete%29.md) to incrementally add image data.

## See Also

### Related Documentation
- [func incrementalLoad(from: Data, complete: Bool) -> Int](./incrementalload%28from,complete%29.md)
  Loads the current image data into an incrementally-loaded image representation and returns the current status of the image.
### Creating Bitmap Representations of Images
- [class func imageReps(with: Data) -> [NSImageRep]](./imagereps%28with%29.md)
  Creates and returns an array of bitmap image representation objects that correspond to the images in the specified data.
- [func colorize(byMappingGray: CGFloat, to: NSColor?, blackMapping: NSColor?, whiteMapping: NSColor?)](./colorize%28bymappinggray,to,blackmapping,whitemapping%29.md)
  Colorizes a grayscale image.
- [init?(bitmapDataPlanes: UnsafeMutablePointer<UnsafeMutablePointer<UInt8>?>?, pixelsWide: Int, pixelsHigh: Int, bitsPerSample: Int, samplesPerPixel: Int, hasAlpha: Bool, isPlanar: Bool, colorSpaceName: NSColorSpaceName, bitmapFormat: NSBitmapImageRep.Format, bytesPerRow: Int, bitsPerPixel: Int)](./init%28bitmapdataplanes,pixelswide,pixelshigh,bitspersample,samplesperpixel,hasalpha,isplanar,colorspacename,bitmapformat,bytesperrow,bitsperpixel%29.md)
  Initializes a newly allocated bitmap image representation so it can render the specified image.
- [init?(bitmapDataPlanes: UnsafeMutablePointer<UnsafeMutablePointer<UInt8>?>?, pixelsWide: Int, pixelsHigh: Int, bitsPerSample: Int, samplesPerPixel: Int, hasAlpha: Bool, isPlanar: Bool, colorSpaceName: NSColorSpaceName, bytesPerRow: Int, bitsPerPixel: Int)](./init%28bitmapdataplanes,pixelswide,pixelshigh,bitspersample,samplesperpixel,hasalpha,isplanar,colorspacename,bytesperrow,bitsperpixel%29.md)
  Initializes a newly allocated bitmap image representation so it can render the specified image.
- [init(cgImage: CGImage)](./init%28cgimage%29-7o5tz.md)
  Returns a bitmap image representation from a Core Graphics image object.
- [init(ciImage: CIImage)](./init%28ciimage%29-7bi19.md)
  Returns a bitmap image representation from a Core Image object.
- [init?(data: Data)](./init%28data%29.md)
  Initializes a newly allocated bitmap image representation from the specified data.
- [init?(focusedViewRect: NSRect)](./init%28focusedviewrect%29.md)
  Initializes a newly allocated bitmap image representation with bitmap data from a rendered image.
- [+ imageRepWithData:](./imagerepwithdata_.md)
  Creates and returns a bitmap image representation with the first image in the specified data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/init(forincrementalload:))*