# CMFormatDescription.Extensions.Key

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct Key
```

## Topics

### Extension Keys
- [static let alphaChannelMode: CMFormatDescription.Extensions.Key](./key/alphachannelmode.md)
- [static let alternativeTransferCharacteristics: CMFormatDescription.Extensions.Key](./key/alternativetransfercharacteristics.md)
- [static let ambientViewingEnvironment: CMFormatDescription.Extensions.Key](./key/ambientviewingenvironment.md)
- [static let auxiliaryTypeInfo: CMFormatDescription.Extensions.Key](./key/auxiliarytypeinfo.md)
- [static let backgroundColor: CMFormatDescription.Extensions.Key](./key/backgroundcolor.md)
- [static let bitsPerComponent: CMFormatDescription.Extensions.Key](./key/bitspercomponent.md)
- [static let bytesPerRow: CMFormatDescription.Extensions.Key](./key/bytesperrow.md)
- [static let chromaLocationBottomField: CMFormatDescription.Extensions.Key](./key/chromalocationbottomfield.md)
- [static let chromaLocationTopField: CMFormatDescription.Extensions.Key](./key/chromalocationtopfield.md)
- [static let cleanAperture: CMFormatDescription.Extensions.Key](./key/cleanaperture.md)
- [static let colorPrimaries: CMFormatDescription.Extensions.Key](./key/colorprimaries.md)
- [static let conformsToMPEG2VideoProfile: CMFormatDescription.Extensions.Key](./key/conformstompeg2videoprofile.md)
- [static let containsAlphaChannel: CMFormatDescription.Extensions.Key](./key/containsalphachannel.md)
- [static let contentLightLevelInfo: CMFormatDescription.Extensions.Key](./key/contentlightlevelinfo.md)
- [static let defaultFontName: CMFormatDescription.Extensions.Key](./key/defaultfontname.md)
- [static let defaultStyle: CMFormatDescription.Extensions.Key](./key/defaultstyle.md)
- [static let defaultTextBox: CMFormatDescription.Extensions.Key](./key/defaulttextbox.md)
- [static let depth: CMFormatDescription.Extensions.Key](./key/depth.md)
- [static let displayFlags: CMFormatDescription.Extensions.Key](./key/displayflags.md)
- [static let fieldCount: CMFormatDescription.Extensions.Key](./key/fieldcount.md)
- [static let fieldDetail: CMFormatDescription.Extensions.Key](./key/fielddetail.md)
- [static let fontTable: CMFormatDescription.Extensions.Key](./key/fonttable.md)
- [static let formatName: CMFormatDescription.Extensions.Key](./key/formatname.md)
- [static let fullRangeVideo: CMFormatDescription.Extensions.Key](./key/fullrangevideo.md)
- [static let gammaLevel: CMFormatDescription.Extensions.Key](./key/gammalevel.md)
- [static let horizontalJustification: CMFormatDescription.Extensions.Key](./key/horizontaljustification.md)
- [static let iccProfile: CMFormatDescription.Extensions.Key](./key/iccprofile.md)
- [static let masteringDisplayColorVolume: CMFormatDescription.Extensions.Key](./key/masteringdisplaycolorvolume.md)
- [static let metadataKeyTable: CMFormatDescription.Extensions.Key](./key/metadatakeytable.md)
- [static let originalCompressionSettings: CMFormatDescription.Extensions.Key](./key/originalcompressionsettings.md)
- [static let pixelAspectRatio: CMFormatDescription.Extensions.Key](./key/pixelaspectratio.md)
- [static let revisionLevel: CMFormatDescription.Extensions.Key](./key/revisionlevel.md)
- [static let sampleDescriptionExtensionAtoms: CMFormatDescription.Extensions.Key](./key/sampledescriptionextensionatoms.md)
- [static let sourceReferenceName: CMFormatDescription.Extensions.Key](./key/sourcereferencename.md)
- [static let spatialQuality: CMFormatDescription.Extensions.Key](./key/spatialquality.md)
- [static let temporalQuality: CMFormatDescription.Extensions.Key](./key/temporalquality.md)
- [static let textJustification: CMFormatDescription.Extensions.Key](./key/textjustification.md)
- [static let transferFunction: CMFormatDescription.Extensions.Key](./key/transferfunction.md)
- [static let vendor: CMFormatDescription.Extensions.Key](./key/vendor.md)
- [static let verbatimISOSampleEntry: CMFormatDescription.Extensions.Key](./key/verbatimisosampleentry.md)
- [static let verbatimSampleDescription: CMFormatDescription.Extensions.Key](./key/verbatimsampledescription.md)
- [static let version: CMFormatDescription.Extensions.Key](./key/version.md)
- [static let verticalJustification: CMFormatDescription.Extensions.Key](./key/verticaljustification.md)
- [static let yCbCrMatrix: CMFormatDescription.Extensions.Key](./key/ycbcrmatrix.md)
### Initializers
- [init(rawValue: CFString)](./key/init%28rawvalue%29.md)
  Creates a new `Key` backed by `rawValue`
### Type Properties
- [static let cameraCalibrationDataLensCollection: CMFormatDescription.Extensions.Key](./key/cameracalibrationdatalenscollection.md)
  Specifies intrinsic and extrinsic parameters for single or multiple lenses. The value for this key is represented by [`CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection`](./value/cameracalibrationdatalenscollection.md) type.
- [static var contentColorVolume: CMFormatDescription.Extensions.Key](./key/contentcolorvolume.md)
  Matches payload of ITU-T-H.265:11/2019, D.2.40 Content Colour Volume SEI message. The value of this key is of [`CMFormatDescription.Extensions.Value.ContentColorVolume`](./value/contentcolorvolume.md) type.
- [static let convertedFromExternalSphericalTags: CMFormatDescription.Extensions.Key](./key/convertedfromexternalsphericaltags.md)
  Indicates that the image description contains projected media data converted from an external format.
- [static var hasAdditionalViews: CMFormatDescription.Extensions.Key](./key/hasadditionalviews.md)
  A boolean indicating that one or more additional views may be present beyond stereo left and stereo right eyes (e.g,. a “centerline” view).
- [static var hasLeftStereoEyeView: CMFormatDescription.Extensions.Key](./key/hasleftstereoeyeview.md)
  A boolean indicating the stereo left eye is present in video frames.
- [static var hasRightStereoEyeView: CMFormatDescription.Extensions.Key](./key/hasrightstereoeyeview.md)
  A boolean indicating the stereo right eye is present in video frames.
- [static var heroEye: CMFormatDescription.Extensions.Key](./key/heroeye.md)
  Indicates which of the two eyes should be used as the primary when rendering in 2D. It is usually perpendicular to the target image surface.
- [static var horizontalDisparityAdjustment: CMFormatDescription.Extensions.Key](./key/horizontaldisparityadjustment.md)
  Indicates a relative shift of the left and right images, which changes the zero parallax plane.
- [static var horizontalFieldOfView: CMFormatDescription.Extensions.Key](./key/horizontalfieldofview.md)
  Horizontal field of view in thousandths of a degree (i.e., 123456 is 123.456 degrees).
- [static var logTransferFunction: CMFormatDescription.Extensions.Key](./key/logtransferfunction.md)
  Indicates that the transfer function or gamma of the content is a log format and identifies the specific log curve.
- [static var projectionKind: CMFormatDescription.Extensions.Key](./key/projectionkind.md)
  Indicates the projection that should be applied to presented decoded video frames.
- [static var protectedContentOriginalFormat: CMFormatDescription.Extensions.Key](./key/protectedcontentoriginalformat.md)
  FourCharCode number representing the original format
- [static var stereoCameraBaseline: CMFormatDescription.Extensions.Key](./key/stereocamerabaseline.md)
  Indicates the distance between centers of the lenses of the camera system.
- [static let viewPackingKind: CMFormatDescription.Extensions.Key](./key/viewpackingkind.md)
  Indicates the packing type of stereoscopic video frames.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Constants
- [CMFormatDescription.Extensions.Value](./value.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/extensions-swift.struct/key)*