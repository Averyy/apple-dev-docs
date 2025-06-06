# init(bitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bitmapFormat:bytesPerRow:bitsPerPixel:)

**Framework**: AppKit  
**Kind**: init

Initializes a newly allocated bitmap image representation so it can render the specified image.

**Availability**:
- macOS ?+

## Declaration

```swift
init?(bitmapDataPlanes planes: UnsafeMutablePointer<UnsafeMutablePointer<UInt8>?>?, pixelsWide width: Int, pixelsHigh height: Int, bitsPerSample bps: Int, samplesPerPixel spp: Int, hasAlpha alpha: Bool, isPlanar: Bool, colorSpaceName: NSColorSpaceName, bitmapFormat: NSBitmapImageRep.Format, bytesPerRow rBytes: Int, bitsPerPixel pBits: Int)
```

#### Return Value

An initialized [`NSBitmapImageRep`](nsbitmapimagerep.md) object or `nil` if the object cannot be initialized.

## Parameters

- `planes`: If   is not   and the array contains at least one data pointer, the returned object will only reference the image data; it will not copy it. The object treats the image data in the buffers as immutable and will not attempt to alter it. When the object itself is freed, it will not attempt to free the buffers.
- `width`: The width of the image in pixels. This value must be greater than 0.
- `height`: The height of the image in pixels. This value must be greater than 0.
- `bps`: The number of bits used to specify one pixel in a single component of the data. All components are assumed to have the same bits per sample.   should be one of these values: 1, 2, 4, 8, 12, or 16.
- `spp`: The number of data components, or samples per pixel. This value includes both color components and the coverage component (alpha), if present. Meaningful values range from 1 through 5. An image with cyan, magenta, yellow, and black (CMYK) color components plus a coverage component would have an   of 5; a grayscale image that lacks a coverage component would have an   of 1.
- `alpha`:   if one of the components counted in the number of samples per pixel ( ) is a coverage (alpha) component, and   if there is no coverage component. If  , the color components in the bitmap data must be premultiplied with their coverage component.
- `isPlanar`: For example, in meshed configuration, the red, green, blue, and coverage values for the first pixel of an image would precede the red, green, blue, and coverage values for the second pixel, and so on. In planar configuration, red values for all the pixels in the image would precede all green values, which would precede all blue values, which would precede all coverage values.
- `colorSpaceName`: If   is 12, you cannot specify the monochrome color space.
- `bitmapFormat`: An integer that specifies the ordering of the bitmap components. It is a mask created by combining the   constants  ,   and   using the C bitwise OR operator.
- `rBytes`: If you pass in a   value of 0, the bitmap data allocated may be padded to fall on long word or larger boundaries for performance. If your code wants to advance row by row, use   and do not assume the data is packed. Passing in a non-zero value allows you to specify exact row advances.
- `pBits`: If you specify 0 for this parameter, the object interprets the number of bits per pixel using the values in the   and   parameters, as described in the preceding paragraph, without any meaningless bits.

## See Also

- [class func imageReps(with: Data) -> [NSImageRep]](nsbitmapimagerep/imagereps(with:).md)
  Creates and returns an array of bitmap image representation objects that correspond to the images in the specified data.
- [func colorize(byMappingGray: CGFloat, to: NSColor?, blackMapping: NSColor?, whiteMapping: NSColor?)](nsbitmapimagerep/colorize(bymappinggray:to:blackmapping:whitemapping:).md)
  Colorizes a grayscale image.
- [init?(bitmapDataPlanes: UnsafeMutablePointer<UnsafeMutablePointer<UInt8>?>?, pixelsWide: Int, pixelsHigh: Int, bitsPerSample: Int, samplesPerPixel: Int, hasAlpha: Bool, isPlanar: Bool, colorSpaceName: NSColorSpaceName, bytesPerRow: Int, bitsPerPixel: Int)](nsbitmapimagerep/init(bitmapdataplanes:pixelswide:pixelshigh:bitspersample:samplesperpixel:hasalpha:isplanar:colorspacename:bytesperrow:bitsperpixel:).md)
  Initializes a newly allocated bitmap image representation so it can render the specified image.
- [init(cgImage: CGImage)](nsbitmapimagerep/init(cgimage:).md)
  Returns a bitmap image representation from a Core Graphics image object.
- [init(ciImage: CIImage)](nsbitmapimagerep/init(ciimage:).md)
  Returns a bitmap image representation from a Core Image object.
- [init?(data: Data)](nsbitmapimagerep/init(data:).md)
  Initializes a newly allocated bitmap image representation from the specified data.
- [init(forIncrementalLoad: ())](nsbitmapimagerep/init(forincrementalload:).md)
  Initializes a newly allocated bitmap image representation for incremental loading.
- [init?(focusedViewRect: NSRect)](nsbitmapimagerep/init(focusedviewrect:).md)
  Initializes a newly allocated bitmap image representation with bitmap data from a rendered image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/init(bitmapdataplanes:pixelswide:pixelshigh:bitspersample:samplesperpixel:hasalpha:isplanar:colorspacename:bitmapformat:bytesperrow:bitsperpixel:))*