# init(ciImage:)

**Framework**: AppKit  
**Kind**: init

Returns a bitmap image representation from a Core Image object.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init(ciImage: CIImage)
```

#### Return Value

An [`NSBitmapImageRep`](nsbitmapimagerep.md) object initialized from the contents of the Core Image ([`CIImage`](https://developer.apple.com/documentation/coreimage/ciimage)) object.

#### Discussion

The image in the `ciImage` parameter must be fully rendered before the receiver can be initialized. If you specify an object whose rendering was deferred (and thus does not have any pixels available now), this method forces the image to be rendered immediately. Rendering the image could result in a performance penalty if the image has a complex rendering chain or accelerated rendering hardware is not available. Rendering uses the current graphics context in the thread from which this method is called; to ensure consistent results across multiple threads, set the current context using the [`NSGraphicsContext`](nsgraphicscontext.md) class before calling this method.

By the time this method returns, the resultant [`NSBitmapImageRep`](nsbitmapimagerep.md) object can have its raw pixel data inspected, can be put on the pasteboard, and can be encoded to any of the standard image formats that [`NSBitmapImageRep`](nsbitmapimagerep.md) supports (JPEG, TIFF, and so on.)

If you pass in a [`CIImage`](https://developer.apple.com/documentation/coreimage/ciimage) object whose extents are not finite, this method raises an exception.

## Parameters

- `ciImage`: A Core Image object whose contents are to be copied to the receiver. This image rectangle must be of a finite size.

## See Also

- [init?(bitmapImageRep: NSBitmapImageRep)](../coreimage/ciimage/1535335-init.md)
  Initializes an image object with the specified bitmap image representation.
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
- [init?(data: Data)](nsbitmapimagerep/init(data:).md)
  Initializes a newly allocated bitmap image representation from the specified data.
- [init(forIncrementalLoad: ())](nsbitmapimagerep/init(forincrementalload:).md)
  Initializes a newly allocated bitmap image representation for incremental loading.
- [init?(focusedViewRect: NSRect)](nsbitmapimagerep/init(focusedviewrect:).md)
  Initializes a newly allocated bitmap image representation with bitmap data from a rendered image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/init(ciimage:))*