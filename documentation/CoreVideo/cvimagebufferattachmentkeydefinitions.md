# CVImageBufferAttachmentKeyDefinitions

**Framework**: Core Video  
**Kind**: protocol

A namespace for image buffer attachment keys.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
protocol CVImageBufferAttachmentKeyDefinitions : CVAttachmentKeyDefinitions
```

## Topics

### Type Properties
- [static var alphaChannelIsOpaque: CVAttachmentKeyDefinition<Self.ShouldPropagate, Bool>](cvimagebufferattachmentkeydefinitions/alphachannelisopaque.md)
  True if the alpha channel in the image data is fully opaque.
- [static var alphaChannelMode: CVAttachmentKeyDefinition<Self.ShouldPropagate, CVImageAlphaChannelMode>](cvimagebufferattachmentkeydefinitions/alphachannelmode.md)
  Determines how the alpha channel should be rendered.
- [static var ambientViewingEnvironment: CVAttachmentKeyDefinition<Self.ShouldPropagate, Data>](cvimagebufferattachmentkeydefinitions/ambientviewingenvironment.md)
  The ambient viewing environment for the image. The value for this key is an 8 byte big-endian data sequence to match the payload of the Ambient Viewing Environment SEI message.
- [static var chromaField: CVAttachmentCompositeKeyDefinition<Self.ShouldPropagate, CVImageChromaField>](cvimagebufferattachmentkeydefinitions/chromafield.md)
  The chroma field information for the image buffer.
- [static var cleanAperture: CVAttachmentKeyDefinition<Self.ShouldPropagate, CVImageCleanAperture>](cvimagebufferattachmentkeydefinitions/cleanaperture.md)
  Clean aperture of the image buffer.
- [static var colorPrimaries: CVAttachmentKeyDefinition<Self.ShouldPropagate, CVImageColorPrimaries>](cvimagebufferattachmentkeydefinitions/colorprimaries.md)
  The color primaries gamut for the image buffer.
- [static var colorSpace: CVAttachmentKeyDefinition<Self.ShouldPropagate, CGColorSpace>](cvimagebufferattachmentkeydefinitions/colorspace.md)
  Color space of the image buffer.
- [static var contentLightLevelInfo: CVAttachmentKeyDefinition<Self.ShouldPropagate, Data>](cvimagebufferattachmentkeydefinitions/contentlightlevelinfo.md)
  The content light level information for the image.
- [static var displayDimensions: CVAttachmentKeyDefinition<Self.ShouldPropagate, CGSize>](cvimagebufferattachmentkeydefinitions/displaydimensions.md)
  Display dimensions for the image buffer.
- [static var displayMaskRectangle: CVAttachmentKeyDefinition<Self.ShouldPropagate, CVImageDisplayMaskRectangle>](cvimagebufferattachmentkeydefinitions/displaymaskrectangle.md)
  Specifies the rectangular display area within the image.
- [static var fieldDetail: CVAttachmentKeyDefinition<Self.ShouldPropagate, CVImageFieldDetail>](cvimagebufferattachmentkeydefinitions/fielddetail.md)
  The order of interlaced video data in the image buffer.
- [static var gammaLevel: CVAttachmentKeyDefinition<Self.ShouldPropagate, Double>](cvimagebufferattachmentkeydefinitions/gammalevel.md)
  The gamma level for the image buffer.
- [static var horizontalDisparityAdjustment: CVAttachmentKeyDefinitionWithDefault<Self.ShouldPropagate, Int32>](cvimagebufferattachmentkeydefinitions/horizontaldisparityadjustment.md)
  Indicates a relative shift of the left and right images, which changes the zero parallax plane.
- [static var iccProfile: CVAttachmentKeyDefinition<Self.ShouldPropagate, Data>](cvimagebufferattachmentkeydefinitions/iccprofile.md)
  ICC color profile for the image buffer.
- [static var leftStereoDisplayMaskRectangle: CVAttachmentKeyDefinition<Self.ShouldPropagate, CVImageStereoDisplayMaskRectangle>](cvimagebufferattachmentkeydefinitions/leftstereodisplaymaskrectangle.md)
  Specifies the rectangular display area within the left eye view of stereo images.
- [static var logTransferFunction: CVAttachmentKeyDefinition<Self.ShouldPropagate, CVImageLogTransferFunction>](cvimagebufferattachmentkeydefinitions/logtransferfunction.md)
  Indicates that the transfer function or gamma of the content is a log format and identifies the specific log curve.
- [static var masteringDisplayColorVolume: CVAttachmentKeyDefinition<Self.ShouldPropagate, Data>](cvimagebufferattachmentkeydefinitions/masteringdisplaycolorvolume.md)
  Mastering display color volume of the image.
- [static var pixelAspectRatio: CVAttachmentKeyDefinition<Self.ShouldPropagate, CVImagePixelAspectRatio>](cvimagebufferattachmentkeydefinitions/pixelaspectratio.md)
  Pixel aspect ratio for the image buffer.
- [static var postDecodeProcessingFrameMetadata: CVAttachmentKeyDefinition<Self.ShouldPropagate, Data>](cvimagebufferattachmentkeydefinitions/postdecodeprocessingframemetadata.md)
- [static var postDecodeProcessingSequenceMetadata: CVAttachmentKeyDefinition<Self.ShouldPropagate, Data>](cvimagebufferattachmentkeydefinitions/postdecodeprocessingsequencemetadata.md)
- [static var regionOfInterest: CVAttachmentKeyDefinition<Self.ShouldPropagate, CGRect>](cvimagebufferattachmentkeydefinitions/regionofinterest.md)
  Specifies region of interest that image statistics cover.
- [static var rightStereoDisplayMaskRectangle: CVAttachmentKeyDefinition<Self.ShouldPropagate, CVImageStereoDisplayMaskRectangle>](cvimagebufferattachmentkeydefinitions/rightstereodisplaymaskrectangle.md)
  Specifies the rectangular display area within the right eye view of stereo images.
- [static var sceneIllumination: CVAttachmentKeyDefinition<Self.ShouldPropagate, Int>](cvimagebufferattachmentkeydefinitions/sceneillumination.md)
  Scene illumination measured in millilux.
- [static var transferFunction: CVAttachmentKeyDefinition<Self.ShouldPropagate, CVImageTransferFunction>](cvimagebufferattachmentkeydefinitions/transferfunction.md)
  The transfer characteristic for the image buffer.
- [static var yCbCrMatrix: CVAttachmentKeyDefinition<Self.ShouldPropagate, CVImageYCbCrMatrix>](cvimagebufferattachmentkeydefinitions/ycbcrmatrix.md)
  The matrix to convert from YCbCr to the RGB color space.

## Relationships

### Inherits From
- [CVAttachmentKeyDefinitions](cvattachmentkeydefinitions.md)
### Conforming Types
- [CVPixelBufferAttachmentKeyDefinitions](cvpixelbufferattachmentkeydefinitions.md)

## See Also

- [protocol CVImageBufferRepresentable](cvimagebufferrepresentable.md)
  CVImageBufferRepresentable protocol is a sealed protocol intended to be implemented by the types in CoreVideo framework. This protocol facilitates Swift types that wrap a value of CVImageBuffer type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagebufferattachmentkeydefinitions)*