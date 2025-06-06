# Image Properties

**Framework**: Image I/O

Properties that apply to the container in general, and not necessarily to an individual image in the container.

#### Overview

Access these properties using the [`CGImageSourceCopyProperties(_:_:)`](cgimagesourcecopyproperties(_:_:).md) function.

## Topics

### Dictionary
- [let kCGImagePropertyFileContentsDictionary: CFString](kcgimagepropertyfilecontentsdictionary.md)
  A dictionary of properties related to the image’s on-disk file.
### Container File Size
- [let kCGImagePropertyFileSize: CFString](kcgimagepropertyfilesize.md)
  The size of the image file in bytes, if known.
### Image Information
- [let kCGImagePropertyImageCount: CFString](kcgimagepropertyimagecount.md)
  The number of images in the file.
- [let kCGImagePropertyIsIndexed: CFString](kcgimagepropertyisindexed.md)
  A Boolean value that indicates whether the image contains indexed pixel samples.
- [let kCGImagePropertyImages: CFString](kcgimagepropertyimages.md)
  An array of dictionaries, each of which contains metadata for one of the images in the file.
- [let kCGImagePropertyThumbnailImages: CFString](kcgimagepropertythumbnailimages.md)
- [let kCGImagePropertyPrimaryImage: CFString](kcgimagepropertyprimaryimage.md)
  The index of the primary image in the file.
- [let kCGImagePropertyIsFloat: CFString](kcgimagepropertyisfloat.md)
  A Boolean value that indicates whether the image contains floating-point pixel samples.
- [let kCGImagePropertyOrientation: CFString](kcgimagepropertyorientation.md)
  The intended display orientation of the image.
- [Individual Image Properties](individual-image-properties.md)
  Properties that apply to an individual image in an image source.
- [enum CGImagePropertyOrientation](cgimagepropertyorientation.md)
  A value describing the intended display orientation for an image.
### Pixel Information
- [let kCGImagePropertyPixelFormat: CFString](kcgimagepropertypixelformat.md)
  The format of the image’s individual pixels.
- [let kCGImagePropertyPixelWidth: CFString](kcgimagepropertypixelwidth.md)
  The number of pixels along the x-axis of the image.
- [let kCGImagePropertyPixelHeight: CFString](kcgimagepropertypixelheight.md)
  The number of pixels along the y-axis of the image.
- [let kCGImagePropertyDPIHeight: CFString](kcgimagepropertydpiheight.md)
  The resolution, in dots per inch, in the y dimension.
- [let kCGImagePropertyDPIWidth: CFString](kcgimagepropertydpiwidth.md)
  The resolution, in dots per inch, in the x dimension.
- [let kCGImagePropertyDepth: CFString](kcgimagepropertydepth.md)
  The number of bits in the color sample of a pixel.
### Color Information
- [let kCGImagePropertyHasAlpha: CFString](kcgimagepropertyhasalpha.md)
  A Boolean value that indicates whether the image has an alpha channel.
- [let kCGImagePropertyNamedColorSpace: CFString](kcgimagepropertynamedcolorspace.md)
  The name of the image’s color space.
- [let kCGImagePropertyProfileName: CFString](kcgimagepropertyprofilename.md)
  The name of the optional International Color Consortium (ICC) profile embedded in the image, if known.
- [let kCGImagePropertyColorModel: CFString](kcgimagepropertycolormodel.md)
  The color model of the image, such as RGB, CMYK, grayscale, or Lab.
- [let kCGImagePropertyColorModelRGB: CFString](kcgimagepropertycolormodelrgb.md)
  A Red Green Blue (RGB) color model.
- [let kCGImagePropertyColorModelCMYK: CFString](kcgimagepropertycolormodelcmyk.md)
  A Cyan Magenta Yellow Black (CMYK) color model.
- [let kCGImagePropertyColorModelGray: CFString](kcgimagepropertycolormodelgray.md)
  A grayscale color model.
- [let kCGImagePropertyColorModelLab: CFString](kcgimagepropertycolormodellab.md)
  A Lab color model, where color values contain the amount of light and the amounts of four human-perceivable colors.

## See Also

- [EXIF Dictionary Keys](exif-dictionary-keys.md)
  Metadata keys for Exchangeable Image File Format (EXIF) data.
- [IPTC Dictionary Keys](iptc-dictionary-keys.md)
  Metadata keys for International Press Telecommunications Council (IPTC) data.
- [GPS Dictionary Keys](gps-dictionary-keys.md)
  Keys for Global Positioning System (GPS) information.
- [WebP Data](webp-data.md)
  Metadata keys for WebP metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/image-properties)*