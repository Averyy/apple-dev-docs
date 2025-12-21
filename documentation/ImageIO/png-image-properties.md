# PNG Image Properties

**Framework**: Image I/O

Metadata keys for the Portable Network Graphics (PNG) format.

## Topics

### Dictionary
- [let kCGImagePropertyPNGDictionary: CFString](kcgimagepropertypngdictionary.md)
  A dictionary of key-value pairs for an image that uses Portable Network Graphics (PNG) format.
### Properties
- [let kCGImagePropertyPNGSource: CFString](kcgimagepropertypngsource.md)
### Image Properties
- [let kCGImagePropertyAPNGCanvasPixelHeight: CFString](kcgimagepropertyapngcanvaspixelheight.md)
  The height of the main image, in pixels.
- [let kCGImagePropertyAPNGCanvasPixelWidth: CFString](kcgimagepropertyapngcanvaspixelwidth.md)
  The width of the main image, in pixels.
- [let kCGImagePropertyPNGXPixelsPerMeter: CFString](kcgimagepropertypngxpixelspermeter.md)
  The number of x pixels per meter.
- [let kCGImagePropertyPNGYPixelsPerMeter: CFString](kcgimagepropertypngypixelspermeter.md)
  The number of y pixels per meter.
- [let kCGImagePropertyPNGGamma: CFString](kcgimagepropertypnggamma.md)
  The gamma value.
- [let kCGImagePropertyPNGInterlaceType: CFString](kcgimagepropertypnginterlacetype.md)
  The interlace type.
- [let kCGImagePropertyPNGsRGBIntent: CFString](kcgimagepropertypngsrgbintent.md)
  The sRGB intent.
- [let kCGImagePropertyPNGChromaticities: CFString](kcgimagepropertypngchromaticities.md)
  The chromaticities.
### Sequence Timing
- [let kCGImagePropertyAPNGFrameInfoArray: CFString](kcgimagepropertyapngframeinfoarray.md)
  An array of dictionaries that contain timing information for the image sequence.
- [let kCGImagePropertyAPNGDelayTime: CFString](kcgimagepropertyapngdelaytime.md)
  The number of seconds to wait before displaying the next image in an animated sequence.
- [let kCGImagePropertyAPNGUnclampedDelayTime: CFString](kcgimagepropertyapngunclampeddelaytime.md)
  The number of seconds to wait before displaying the next image in an animated sequence.
- [let kCGImagePropertyAPNGLoopCount: CFString](kcgimagepropertyapngloopcount.md)
  The number of times that an animated PNG should play through its frames before stopping.
### Descriptive Information
- [let kCGImagePropertyPNGTitle: CFString](kcgimagepropertypngtitle.md)
  A string that holds the image’s title.
- [let kCGImagePropertyPNGDescription: CFString](kcgimagepropertypngdescription.md)
  A string that describes the image.
- [let kCGImagePropertyPNGComment: CFString](kcgimagepropertypngcomment.md)
  A string that contains image comments.
- [let kCGImagePropertyPNGDisclaimer: CFString](kcgimagepropertypngdisclaimer.md)
  A disclaimer string.
- [let kCGImagePropertyPNGWarning: CFString](kcgimagepropertypngwarning.md)
  A warning string.
- [let kCGImagePropertyPNGAuthor: CFString](kcgimagepropertypngauthor.md)
  A string that identifies the author of the image.
- [let kCGImagePropertyPNGCopyright: CFString](kcgimagepropertypngcopyright.md)
  A string that identifies the copyright of the image.
- [let kCGImagePropertyPNGCreationTime: CFString](kcgimagepropertypngcreationtime.md)
  A string that identifies the date and time the image was created.
- [let kCGImagePropertyPNGModificationTime: CFString](kcgimagepropertypngmodificationtime.md)
  A string that identifies the last date and time the image was modified.
- [let kCGImagePropertyPNGSoftware: CFString](kcgimagepropertypngsoftware.md)
  A string that identifies the software used to create the image.
### Pre-Compression Filters
- [let kCGImagePropertyPNGCompressionFilter: CFString](kcgimagepropertypngcompressionfilter.md)
  The PNG filter to apply prior to compression.
- [var IMAGEIO_PNG_NO_FILTERS: Int32](imageio_png_no_filters.md)
  No PNG filters.
- [var IMAGEIO_PNG_FILTER_NONE: Int32](imageio_png_filter_none.md)
  A filter in which each byte is unchanged.
- [var IMAGEIO_PNG_FILTER_SUB: Int32](imageio_png_filter_sub.md)
  A filter in which each byte is replaced with the difference between it and the corresponding byte to its left.
- [var IMAGEIO_PNG_FILTER_UP: Int32](imageio_png_filter_up.md)
  A filter in which each byte is replaced with the difference between it and the byte above it.
- [var IMAGEIO_PNG_FILTER_AVG: Int32](imageio_png_filter_avg.md)
  A filter in which each byte is replaced with the difference between it and the average of the bytes above it and to its left.
- [var IMAGEIO_PNG_FILTER_PAETH: Int32](imageio_png_filter_paeth.md)
  A filter in which each byte is replaced with the difference between it and the Paeth predictor of the bytes to its left, above, and upper left.

## See Also

- [CIFF Image Properties](ciff-image-properties.md)
  Metadata keys for the Camera Image File Format (CIFF) image format.
- [DNG Image Properties](dng-image-properties.md)
  Metadata keys for the Digital Negative (DNG) archival format.
- [GIF Image Properties](gif-image-properties.md)
  Metadata keys for the Graphics Interchange Format (GIF).
- [HEIC Image Properties](heic-image-properties.md)
  Metadata keys for the High Efficiency Image Container (HEIC) format.
- [JFIF Image Properties](jfif-image-properties.md)
  Metadata keys for the JPEG File Interchange Format (JFIF).
- [TGA Image Properties](tga-image-properties.md)
  Metadata keys for the Truevision Graphics Adapter (TGA) format.
- [TIFF Image Properties](tiff-image-properties.md)
  Metadata keys for the Tagged Image File Format (TIFF).
- [8BIM Image Properties](8bim-image-properties.md)
  Metadata keys for the Adobe Photoshop image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/png-image-properties)*