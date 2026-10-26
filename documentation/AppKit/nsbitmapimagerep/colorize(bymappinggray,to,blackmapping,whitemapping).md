# colorize(byMappingGray:to:blackMapping:whiteMapping:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Colorizes a grayscale image.

**Availability**:
- macOS

## Declaration

```swift
func colorize(byMappingGray midPoint: CGFloat, to midPointColor: NSColor?, blackMapping shadowColor: NSColor?, whiteMapping lightColor: NSColor?)
```

```objc
- (void) colorizeByMappingGray:(CGFloat) midPoint toColor:(NSColor *) midPointColor blackMapping:(NSColor *) shadowColor whiteMapping:(NSColor *) lightColor;
```

#### Discussion

This method maps the receiver such that:

- Gray value of `midPoint` –>  `midPointColor`;
- black –> `shadowColor`;
- white –> `lightColor`.

It works on images with 8-bit SPP, and thus supports either 8-bit gray or 24-bit color (with optional alpha).

## Parameters

- `midPoint`: A float value representing the midpoint of the grayscale image.
- `midPointColor`: A color object representing the midpoint of the color to map the image to.
- `shadowColor`: A color object representing the black mapping to use for shadows.
- `lightColor`: A color object representing the white mapping to be used in the image.

## See Also

### Creating Bitmap Representations of Images
- [class func imageReps(with: Data) -> [NSImageRep]](./imagereps%28with%29.md)
  Creates and returns an array of bitmap image representation objects that correspond to the images in the specified data.
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
- [+ imageRepWithData:](./imagerepwithdata_.md)
  Creates and returns a bitmap image representation with the first image in the specified data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/colorize(bymappinggray:to:blackmapping:whitemapping:))*