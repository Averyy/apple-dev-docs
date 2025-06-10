# Image I/O

**Framework**: Image I/O  
**Kind**: module

Read and write most image file formats, and access an image’s metadata.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

#### Overview

The Image I/O framework allows applications to read and write most image file formats. This framework offers high efficiency, color management, and access to image metadata.

For more information, see [`Image I/O Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/ImageIOGuide/imageio_intro/ikpg_intro.html#//apple_ref/doc/uid/TP40005462).

## Topics

### Image Management
- [class CGImageSource](cgimagesource.md)
  An opaque type that you use to read image data from a URL, data object, or data consumer.
- [class CGImageDestination](cgimagedestination.md)
  An opaque type that you use to write image data to a URL, data object, or data consumer.
### XMP Metadata
- [class CGImageMetadata](cgimagemetadata.md)
  An immutable object that contains the XMP metadata associated with an image.
- [class CGMutableImageMetadata](cgmutableimagemetadata.md)
  An opaque type for adding or modifying image metadata.
- [class CGImageMetadataTag](cgimagemetadatatag.md)
  An immutable type that contains information about a single piece of image metadata.
- [XMP Namespaces and Prefixes](xmp-namespaces-and-prefixes.md)
  Discover the public namespaces and prefixes that exist in XMP metadata tags.
- [let kCFErrorDomainCGImageMetadata: CFString](kcferrordomaincgimagemetadata.md)
  The domain for metadata-related errors that originate in the Image I/O framework.
- [enum CGImageMetadataErrors](cgimagemetadataerrors.md)
  Constants for errors that occur when getting or setting metadata information.
### Common Image Properties
- [Image Properties](image-properties.md)
  Properties that apply to the container in general, and not necessarily to an individual image in the container.
- [EXIF Dictionary Keys](exif-dictionary-keys.md)
  Metadata keys for Exchangeable Image File Format (EXIF) data.
- [IPTC Dictionary Keys](iptc-dictionary-keys.md)
  Metadata keys for International Press Telecommunications Council (IPTC) data.
- [GPS Dictionary Keys](gps-dictionary-keys.md)
  Keys for Global Positioning System (GPS) information.
- [WebP Data](webp-data.md)
  Metadata keys for WebP metadata.
### Format-Specific Properties
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
- [PNG Image Properties](png-image-properties.md)
  Metadata keys for the Portable Network Graphics (PNG) format.
- [TGA Image Properties](tga-image-properties.md)
  Metadata keys for the Truevision Graphics Adapter (TGA) format.
- [TIFF Image Properties](tiff-image-properties.md)
  Metadata keys for the Tagged Image File Format (TIFF).
- [8BIM Image Properties](8bim-image-properties.md)
  Metadata keys for the Adobe Photoshop image format.
### Manufacturer-Specific Properties
- [Nikon Camera Dictionary Keys](nikon-camera-dictionary-keys.md)
  Metadata keys for an image from a Nikon camera.
- [Canon Camera Dictionary Keys](canon-camera-dictionary-keys.md)
  Metadata keys for an image from a Canon camera.
- [let kCGImagePropertyMakerAppleDictionary: CFString](kcgimagepropertymakerappledictionary.md)
  A dictionary of key-value pairs for an image from an Apple camera.
- [let kCGImagePropertyMakerMinoltaDictionary: CFString](kcgimagepropertymakerminoltadictionary.md)
  A dictionary of key-value pairs for an image from a Minolta camera.
- [let kCGImagePropertyMakerFujiDictionary: CFString](kcgimagepropertymakerfujidictionary.md)
  A dictionary of key-value pairs for an image from a Fuji camera.
- [let kCGImagePropertyMakerOlympusDictionary: CFString](kcgimagepropertymakerolympusdictionary.md)
  A dictionary of key-value pairs for an image from a Olympus camera.
- [let kCGImagePropertyMakerPentaxDictionary: CFString](kcgimagepropertymakerpentaxdictionary.md)
  A dictionary of key-value pairs for an image from a Pentax camera.
- [let kCGImagePropertyRawDictionary: CFString](kcgimagepropertyrawdictionary.md)
  A dictionary of key-value pairs for an image that contains minimally processed, or raw, data.
### Spatial Photos
- [Writing spatial photos](writing-spatial-photos.md)
  Create spatial photos for visionOS by packaging a pair of left- and right-eye images as a stereo HEIC file with related spatial metadata.
- [Creating spatial photos and videos with spatial metadata](creating-spatial-photos-and-videos-with-spatial-metadata.md)
  Add spatial metadata to stereo photos and videos to create spatial media for viewing on Apple Vision Pro.
### Animations
- [func CGAnimateImageAtURLWithBlock(CFURL, CFDictionary?, CGImageSourceAnimationBlock) -> OSStatus](cganimateimageaturlwithblock(_:_:_:).md)
  Animate the sequence of images in the Graphics Interchange Format (GIF) or Animated Portable Network Graphics (APNG) file at the specified URL.
- [func CGAnimateImageDataWithBlock(CFData, CFDictionary?, CGImageSourceAnimationBlock) -> OSStatus](cganimateimagedatawithblock(_:_:_:).md)
  Animate the sequence of images using data from a Graphics Interchange Format (GIF) or Animated Portable Network Graphics (APNG) file file.
- [typealias CGImageSourceAnimationBlock](cgimagesourceanimationblock.md)
  The block to execute for each frame of an image animation.
- [let kCGImageAnimationStartIndex: CFString](kcgimageanimationstartindex.md)
  A property that specifies the index of the first frame of an animation.
- [let kCGImageAnimationDelayTime: CFString](kcgimageanimationdelaytime.md)
  The number of seconds to wait before displaying the next image in an animated sequence.
- [let kCGImageAnimationLoopCount: CFString](kcgimageanimationloopcount.md)
  The number of times to repeat the animated sequence.
- [enum CGImageAnimationStatus](cgimageanimationstatus.md)
  Constants that indicate the result of animating an image sequence.
### Reference
- [Image I/O Constants](image-i-o-constants.md)
- [Image I/O Functions](image-i-o-functions.md)
- [Image I/O Macros](image-i-o-macros.md)
### Variables
- [let kCGComputeHDRStats: CFString](kcgcomputehdrstats.md)
- [let kCGImageDestinationEncodeAlternateColorSpace: CFString](kcgimagedestinationencodealternatecolorspace.md)
- [let kCGImageDestinationEncodeBaseColorSpace: CFString](kcgimagedestinationencodebasecolorspace.md)
- [let kCGImageDestinationEncodeBaseIsSDR: CFString](kcgimagedestinationencodebaseissdr.md)
- [let kCGImageDestinationEncodeBasePixelFormatRequest: CFString](kcgimagedestinationencodebasepixelformatrequest.md)
- [let kCGImageDestinationEncodeGainMapPixelFormatRequest: CFString](kcgimagedestinationencodegainmappixelformatrequest.md)
- [let kCGImageDestinationEncodeGainMapSubsampleFactor: CFString](kcgimagedestinationencodegainmapsubsamplefactor.md)
- [let kCGImageDestinationEncodeGenerateGainMapWithBaseImage: CFString](kcgimagedestinationencodegenerategainmapwithbaseimage.md)
- [let kCGImageDestinationEncodeIsBaseImage: CFString](kcgimagedestinationencodeisbaseimage.md)
- [let kCGImageDestinationEncodeRequest: CFString](kcgimagedestinationencoderequest.md)
- [let kCGImageDestinationEncodeRequestOptions: CFString](kcgimagedestinationencoderequestoptions.md)
- [let kCGImageDestinationEncodeToISOGainmap: CFString](kcgimagedestinationencodetoisogainmap.md)
- [let kCGImageDestinationEncodeToISOHDR: CFString](kcgimagedestinationencodetoisohdr.md)
- [let kCGImageDestinationEncodeToSDR: CFString](kcgimagedestinationencodetosdr.md)
- [let kCGImageDestinationEncodeTonemapMode: CFString](kcgimagedestinationencodetonemapmode.md)
- [let kCGImagePropertyASTCBlockSize: CFString](kcgimagepropertyastcblocksize.md)
- [let kCGImagePropertyASTCBlockSize4x4: CFString](kcgimagepropertyastcblocksize4x4.md)
- [let kCGImagePropertyASTCBlockSize8x8: CFString](kcgimagepropertyastcblocksize8x8.md)
- [let kCGImagePropertyASTCEncoder: CFString](kcgimagepropertyastcencoder.md)
- [let kCGImagePropertyBCEncoder: CFString](kcgimagepropertybcencoder.md)
- [let kCGImagePropertyBCFormat: CFString](kcgimagepropertybcformat.md)
- [let kCGImagePropertyEncoder: CFString](kcgimagepropertyencoder.md)
- [let kCGImagePropertyOpenEXRCompression: CFString](kcgimagepropertyopenexrcompression.md)
- [let kCGImagePropertyPVREncoder: CFString](kcgimagepropertypvrencoder.md)
- [let kCGImageSourceGenerateImageSpecificLumaScaling: CFString](kcgimagesourcegenerateimagespecificlumascaling.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/ImageIO)*