# imageReps(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates and returns an array of bitmap image representation objects that correspond to the images in the specified data.

**Availability**:
- macOS

## Declaration

```swift
class func imageReps(with data: Data) -> [NSImageRep]
```

```objc
+ (NSArray<NSImageRep *> *) imageRepsWithData:(NSData *) data;
```

#### Return Value

An array of [`NSBitmapImageRep`](../nsbitmapimagerep.md) instances or an empty array if the class is unable to create any image representations.

## Parameters

- `data`: A data object containing one or more bitmapped images or `nil` if the class is unable to create an image representation. The `bitmapData` parameter can contain data in any supported bitmap format.

## See Also

### Creating Bitmap Representations of Images
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
- [init(forIncrementalLoad: ())](./init%28forincrementalload%29.md)
  Initializes a newly allocated bitmap image representation for incremental loading.
- [init?(focusedViewRect: NSRect)](./init%28focusedviewrect%29.md)
  Initializes a newly allocated bitmap image representation with bitmap data from a rendered image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/imagereps(with:))*