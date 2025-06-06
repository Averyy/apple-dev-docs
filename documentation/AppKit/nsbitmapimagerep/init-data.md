# init(data:)

**Framework**: AppKit  
**Kind**: init

Initializes a newly allocated bitmap image representation from the specified data.

**Availability**:
- macOS ?+

## Declaration

```swift
init?(data: Data)
```

#### Return Value

Returns an initialized [`NSBitmapImageRep`](nsbitmapimagerep.md) if the initialization was successful or `nil` if it was unable to interpret the contents of `bitmapData`.

## Parameters

- `data`: A data object containing image data. The contents of   can be any supported bitmap format. For TIFF data, the   is initialized from the first header and image data found in  .

## See Also

- [class func imageReps(with: Data) -> [NSImageRep]](nsbitmapimagerep/imagereps(with:).md)
  Creates and returns an array of bitmap image representation objects that correspond to the images in the specified data.
- [func colorize(byMappingGray: CGFloat, to: NSColor?, blackMapping: NSColor?, whiteMapping: NSColor?)](nsbitmapimagerep/colorize(bymappinggray:to:blackmapping:whitemapping:).md)
  Colorizes a grayscale image.
- [init?(bitmapDataPlanes: UnsafeMutablePointer<UnsafeMutablePointer<UInt8>?>?, pixelsWide: Int, pixelsHigh: Int, bitsPerSample: Int, samplesPerPixel: Int, hasAlpha: Bool, isPlanar: Bool, colorSpaceName: NSColorSpaceName, bitmapFormat: NSBitmapImageRep.Format, bytesPerRow: Int, bitsPerPixel: Int)](nsbitmapimagerep/init(bitmapdataplanes:pixelswide:pixelshigh:bitspersample:samplesperpixel:hasalpha:isplanar:colorspacename:bitmapformat:bytesperrow:bitsperpixel:).md)
  Initializes a newly allocated bitmap image representation so it can render the specified image.
- [init?(bitmapDataPlanes: UnsafeMutablePointer<UnsafeMutablePointer<UInt8>?>?, pixelsWide: Int, pixelsHigh: Int, bitsPerSample: Int, samplesPerPixel: Int, hasAlpha: Bool, isPlanar: Bool, colorSpaceName: NSColorSpaceName, bytesPerRow: Int, bitsPerPixel: Int)](nsbitmapimagerep/init(bitmapdataplanes:pixelswide:pixelshigh:bitspersample:samplesperpixel:hasalpha:isplanar:colorspacename:bytesperrow:bitsperpixel:).md)
  Initializes a newly allocated bitmap image representation so it can render the specified image.
- [init(cgImage: CGImage)](nsbitmapimagerep/init(cgimage:).md)
  Returns a bitmap image representation from a Core Graphics image object.
- [init(ciImage: CIImage)](nsbitmapimagerep/init(ciimage:).md)
  Returns a bitmap image representation from a Core Image object.
- [init(forIncrementalLoad: ())](nsbitmapimagerep/init(forincrementalload:).md)
  Initializes a newly allocated bitmap image representation for incremental loading.
- [init?(focusedViewRect: NSRect)](nsbitmapimagerep/init(focusedviewrect:).md)
  Initializes a newly allocated bitmap image representation with bitmap data from a rendered image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/init(data:))*