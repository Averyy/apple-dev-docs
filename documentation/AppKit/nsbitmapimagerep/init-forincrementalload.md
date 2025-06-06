# init(forIncrementalLoad:)

**Framework**: AppKit  
**Kind**: init

Initializes a newly allocated bitmap image representation for incremental loading.

**Availability**:
- macOS ?+

## Declaration

```swift
init(forIncrementalLoad: ())
```

#### Discussion

The receiver returns itself after setting its size and data buffer to zero. You can then call [`incrementalLoad(from:complete:)`](nsbitmapimagerep/incrementalload(from:complete:).md) to incrementally add image data.

## See Also

- [func incrementalLoad(from: Data, complete: Bool) -> Int](nsbitmapimagerep/incrementalload(from:complete:).md)
  Loads the current image data into an incrementally-loaded image representation and returns the current status of the image.
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
- [init?(data: Data)](nsbitmapimagerep/init(data:).md)
  Initializes a newly allocated bitmap image representation from the specified data.
- [init?(focusedViewRect: NSRect)](nsbitmapimagerep/init(focusedviewrect:).md)
  Initializes a newly allocated bitmap image representation with bitmap data from a rendered image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/init(forincrementalload:))*