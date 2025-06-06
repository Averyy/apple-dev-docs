# HEIC Image Properties

**Framework**: Image I/O

Metadata keys for the High Efficiency Image Container (HEIC) format.

## Topics

### Dictionary
- [let kCGImagePropertyHEICSDictionary: CFString](kcgimagepropertyheicsdictionary.md)
  A dictionary of properties related to an HEIC container.
### Image Properties
- [let kCGImagePropertyHEICSCanvasPixelHeight: CFString](kcgimagepropertyheicscanvaspixelheight.md)
  The height of the main image, in pixels.
- [let kCGImagePropertyHEICSCanvasPixelWidth: CFString](kcgimagepropertyheicscanvaspixelwidth.md)
  The width of the main image, in pixels.
- [let kCGImagePropertyNamedColorSpace: CFString](kcgimagepropertynamedcolorspace.md)
  The name of the image’s color space.
### Sequence Timing
- [let kCGImagePropertyHEICSFrameInfoArray: CFString](kcgimagepropertyheicsframeinfoarray.md)
  An array of dictionaries that contain timing information for the image sequence.
- [let kCGImagePropertyHEICSDelayTime: CFString](kcgimagepropertyheicsdelaytime.md)
  The number of seconds to wait before displaying the next image in the sequence, clamped to a minimum of `0.1` seconds.
- [let kCGImagePropertyHEICSUnclampedDelayTime: CFString](kcgimagepropertyheicsunclampeddelaytime.md)
  The unclamped number of seconds to wait before displaying the next image in the sequence.
- [let kCGImagePropertyHEICSLoopCount: CFString](kcgimagepropertyheicsloopcount.md)
  The number of times to play the sequence.

## See Also

- [CIFF Image Properties](ciff-image-properties.md)
  Metadata keys for the Camera Image File Format (CIFF) image format.
- [DNG Image Properties](dng-image-properties.md)
  Metadata keys for the Digital Negative (DNG) archival format.
- [GIF Image Properties](gif-image-properties.md)
  Metadata keys for the Graphics Interchange Format (GIF).
- [JFIF Image Properties](jfif-image-properties.md)
  Metadata keys for the JPEG File Interchange Format (JFIF).
- [PNG Image Properties](png-image-properties.md)
  Metadata keys for the Portable Network Graphics (PNG) format.
- [TGA Image Properties](tga-image-properties.md)
  Metadata keys for the Truevision Graphics Adapter (TGA) format.
- [TIFF Image Properties](tiff-image-properties.md)
  Metadata keys for the Tagged Image File Format (TIFF).
- [8BIM Image Properties](8bim-image-properties.md)
  Metadata keys for the Adobe Photoshop image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/heic-image-properties)*