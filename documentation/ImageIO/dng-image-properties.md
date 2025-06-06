# DNG Image Properties

**Framework**: Image I/O

Metadata keys for the Digital Negative (DNG) archival format.

#### Overview

For more information about the DNG format, see  at [`www.adobe.com`](https://developer.apple.comhttps://www.adobe.com).

## Topics

### Dictionary
- [let kCGImagePropertyDNGDictionary: CFString](kcgimagepropertydngdictionary.md)
  A dictionary of key-value pairs for an image that uses the Digital Negative (DNG) archival format. See [`DNG Image Properties`](dng-image-properties.md).
### Quality
- [let kCGImagePropertyDNGBaselineSharpness: CFString](kcgimagepropertydngbaselinesharpness.md)
  The amount of sharpening required for this camera model.
- [let kCGImagePropertyDNGLinearResponseLimit: CFString](kcgimagepropertydnglinearresponselimit.md)
  The fraction of the encoding range, above which the response may become significantly non-linear.
- [let kCGImagePropertyDNGChromaBlurRadius: CFString](kcgimagepropertydngchromablurradius.md)
  A hint to the DNG reader about how much chroma blur to apply to the image.
- [let kCGImagePropertyDNGAntiAliasStrength: CFString](kcgimagepropertydngantialiasstrength.md)
  A hint to the DNG reader about how strong the camera’s antialias filter is.
- [let kCGImagePropertyDNGShadowScale: CFString](kcgimagepropertydngshadowscale.md)
  A tag that Adobe Camera Raw uses to control the sensitivity of its Shadows slider.
- [let kCGImagePropertyDNGBestQualityScale: CFString](kcgimagepropertydngbestqualityscale.md)
  The scale factor to apply to the default scale to achieve the best quality image size.
- [let kCGImagePropertyDNGDefaultScale: CFString](kcgimagepropertydngdefaultscale.md)
  The default scale factors for each direction to convert the image to square pixels.
- [let kCGImagePropertyDNGLinearizationTable: CFString](kcgimagepropertydnglinearizationtable.md)
  A lookup table that maps stored values into linear values.
### Exposure
- [let kCGImagePropertyDNGBaselineExposure: CFString](kcgimagepropertydngbaselineexposure.md)
  The amount by which to adjust the zero point of the exposure, specified in EV units.
- [let kCGImagePropertyDNGBaselineNoise: CFString](kcgimagepropertydngbaselinenoise.md)
  The relative noise level of the camera model at an ISO of 100.
- [let kCGImagePropertyDNGBaselineExposureOffset: CFString](kcgimagepropertydngbaselineexposureoffset.md)
  The amount of EV units to add to the baseline exposure during image rendering.
### Color Balance
- [let kCGImagePropertyDNGAnalogBalance: CFString](kcgimagepropertydnganalogbalance.md)
  The analog or digital gain that applies to the stored raw values.
- [let kCGImagePropertyDNGAsShotNeutral: CFString](kcgimagepropertydngasshotneutral.md)
  The selected white balance at the time of capture, encoded as the coordinates of a neutral color in linear reference space values.
- [let kCGImagePropertyDNGAsShotWhiteXY: CFString](kcgimagepropertydngasshotwhitexy.md)
  The selected white balance at the time of capture, encoded as x-y chromaticity coordinates.
- [let kCGImagePropertyDNGBayerGreenSplit: CFString](kcgimagepropertydngbayergreensplit.md)
  A value that specifies how closely green pixels in the blue/green rows track the green pixels in red/green rows.
- [let kCGImagePropertyDNGForwardMatrix1: CFString](kcgimagepropertydngforwardmatrix1.md)
  A matrix that maps white balanced camera colors to XYZ D50 colors.
- [let kCGImagePropertyDNGForwardMatrix2: CFString](kcgimagepropertydngforwardmatrix2.md)
  A matrix that maps white balanced camera colors to XYZ D50 colors.
- [let kCGImagePropertyDNGDefaultBlackRender: CFString](kcgimagepropertydngdefaultblackrender.md)
  A hint to the raw converter about how to handle the black point during rendering.
### Color Calibration
- [let kCGImagePropertyDNGBlackLevelRepeatDim: CFString](kcgimagepropertydngblacklevelrepeatdim.md)
  The repeat pattern size for the black level tag.
- [let kCGImagePropertyDNGBlackLevel: CFString](kcgimagepropertydngblacklevel.md)
  The zero light encoding level, specified as a repeating pattern.
- [let kCGImagePropertyDNGBlackLevelDeltaH: CFString](kcgimagepropertydngblackleveldeltah.md)
  The difference between the zero-light encoding level for each column and the baseline zero-light encoding level.
- [let kCGImagePropertyDNGBlackLevelDeltaV: CFString](kcgimagepropertydngblackleveldeltav.md)
  The difference between the zero-light encodoing level for each row and the baseline zero-light encoding level.
- [let kCGImagePropertyDNGWhiteLevel: CFString](kcgimagepropertydngwhitelevel.md)
  The saturated encoding level for the raw sample values.
- [let kCGImagePropertyDNGCalibrationIlluminant1: CFString](kcgimagepropertydngcalibrationilluminant1.md)
  The illuminant for the first set of color calibration tags.
- [let kCGImagePropertyDNGCalibrationIlluminant2: CFString](kcgimagepropertydngcalibrationilluminant2.md)
  The illuminant for an optional second set of color calibration tags.
- [let kCGImagePropertyDNGColorMatrix1: CFString](kcgimagepropertydngcolormatrix1.md)
  A transformation matrix that converts XYZ values to reference camera native color spaces, under the first calibration illuminant.
- [let kCGImagePropertyDNGColorMatrix2: CFString](kcgimagepropertydngcolormatrix2.md)
  A transformation matrix that converts XYZ values to reference camera native color spaces, under the second calibration illuminant.
- [let kCGImagePropertyDNGCameraCalibration1: CFString](kcgimagepropertydngcameracalibration1.md)
  A matrix that transforms reference camera native space values to camera-native space values under the first calibration illuminant.
- [let kCGImagePropertyDNGCameraCalibration2: CFString](kcgimagepropertydngcameracalibration2.md)
  A matrix that transforms reference camera native space values to camera-native space values under the second calibration illuminant.
- [let kCGImagePropertyDNGReductionMatrix1: CFString](kcgimagepropertydngreductionmatrix1.md)
  A reduction matrix that converts color camera-native space values to XYZ values, under the first calibration illuminant.
- [let kCGImagePropertyDNGReductionMatrix2: CFString](kcgimagepropertydngreductionmatrix2.md)
  A reduction matrix that converts color camera-native space values to XYZ values, under the second calibration illuminant.
- [let kCGImagePropertyDNGAsShotICCProfile: CFString](kcgimagepropertydngasshoticcprofile.md)
  A profile that specifies default color rendering from camera color-space coordinates into the ICC profile space.
- [let kCGImagePropertyDNGAsShotPreProfileMatrix: CFString](kcgimagepropertydngasshotpreprofilematrix.md)
  A matrix to apply to the camera color-space coordinates before processing values through the ICC profile.
- [let kCGImagePropertyDNGCurrentICCProfile: CFString](kcgimagepropertydngcurrenticcprofile.md)
  A profile that specifies default color rendering from camera color-space coordinates into the ICC profile space.
- [let kCGImagePropertyDNGCurrentPreProfileMatrix: CFString](kcgimagepropertydngcurrentpreprofilematrix.md)
  A matrix to apply to the current camera color-space coordinates before processing values through the ICC profile.
- [let kCGImagePropertyDNGColorimetricReference: CFString](kcgimagepropertydngcolorimetricreference.md)
  The colorimetric reference for the CIE XYZ values.
- [let kCGImagePropertyDNGCameraCalibrationSignature: CFString](kcgimagepropertydngcameracalibrationsignature.md)
  A string to match against the profile calibration signature for the selected camera profile.
- [let kCGImagePropertyDNGProfileCalibrationSignature: CFString](kcgimagepropertydngprofilecalibrationsignature.md)
  A string that describes the calibration for the current profile.
### Crop Data
- [let kCGImagePropertyDNGActiveArea: CFString](kcgimagepropertydngactivearea.md)
  The rectangle that defines the non-masked pixels of the sensor.
- [let kCGImagePropertyDNGMaskedAreas: CFString](kcgimagepropertydngmaskedareas.md)
  A list of non-overlapping rectangles that contain fully masked pixels in the image.
- [let kCGImagePropertyDNGDefaultCropOrigin: CFString](kcgimagepropertydngdefaultcroporigin.md)
  The origin of the final image area, relative to the top-left corner of the active area rectangle.
- [let kCGImagePropertyDNGDefaultCropSize: CFString](kcgimagepropertydngdefaultcropsize.md)
  The size of the final image area, in raw image coordinates.
- [let kCGImagePropertyDNGDefaultUserCrop: CFString](kcgimagepropertydngdefaultusercrop.md)
  A default user-crop rectangle in relative coordinates.
### RAW Data
- [let kCGImagePropertyDNGOriginalRawFileName: CFString](kcgimagepropertydngoriginalrawfilename.md)
  The file name of the original raw file.
- [let kCGImagePropertyDNGOriginalRawFileData: CFString](kcgimagepropertydngoriginalrawfiledata.md)
  The compressed contents of the original raw file.
- [let kCGImagePropertyDNGNoiseReductionApplied: CFString](kcgimagepropertydngnoisereductionapplied.md)
  The amount of noise reduction applied to the raw data on a scale of 0.0 to 1.0.
- [let kCGImagePropertyDNGNewRawImageDigest: CFString](kcgimagepropertydngnewrawimagedigest.md)
  An MD5 digest of the raw image data.
- [let kCGImagePropertyDNGOriginalRawFileDigest: CFString](kcgimagepropertydngoriginalrawfiledigest.md)
  An MD5 digest of the data stored for the original raw file data.
- [let kCGImagePropertyDNGRawImageDigest: CFString](kcgimagepropertydngrawimagedigest.md)
  A modified MD5 digest of the raw image data.
- [let kCGImagePropertyDNGOriginalDefaultFinalSize: CFString](kcgimagepropertydngoriginaldefaultfinalsize.md)
  THe default final size of the larger original file that was the source of this proxy.
- [let kCGImagePropertyDNGOriginalBestQualityFinalSize: CFString](kcgimagepropertydngoriginalbestqualityfinalsize.md)
  The best-quality final size of the larger original file that was the source of this proxy.
- [let kCGImagePropertyDNGOriginalDefaultCropSize: CFString](kcgimagepropertydngoriginaldefaultcropsize.md)
  The default crop size of the larger original file that was the source of this proxy.
- [let kCGImagePropertyDNGRawToPreviewGain: CFString](kcgimagepropertydngrawtopreviewgain.md)
  The gain between the main raw IFD and the preview IFD that contains this tag.
- [let kCGImagePropertyDNGNoiseProfile: CFString](kcgimagepropertydngnoiseprofile.md)
  The amount of noise in the raw image.
- [let kCGImagePropertyDNGCFALayout: CFString](kcgimagepropertydngcfalayout.md)
  The spatial layout of the CFA.
- [let kCGImagePropertyDNGCFAPlaneColor: CFString](kcgimagepropertydngcfaplanecolor.md)
  A mapping between the values in the CFA pattern tag and the plane numbers in linear raw space.
- [let kCGImagePropertyDNGOpcodeList1: CFString](kcgimagepropertydngopcodelist1.md)
  The list of opcodes to apply to the raw image, as read directly from the file.
- [let kCGImagePropertyDNGOpcodeList2: CFString](kcgimagepropertydngopcodelist2.md)
  THe list of opcodes to apply to the raw image, after mapping it to linear reference values.
- [let kCGImagePropertyDNGOpcodeList3: CFString](kcgimagepropertydngopcodelist3.md)
  The list of opcodes to apply to the raw image, after demosaicing it.
- [let kCGImagePropertyDNGWarpRectilinear: CFString](kcgimagepropertydngwarprectilinear.md)
  An opcode to apply a warp to an image to correct for geometric distortion and lateral chromatic aberration for rectilinear lenses.
- [let kCGImagePropertyDNGWarpFisheye: CFString](kcgimagepropertydngwarpfisheye.md)
  An opcode to unwrap an image captued with a fisheye lens and map it to a perspective projection.
- [let kCGImagePropertyDNGFixVignetteRadial: CFString](kcgimagepropertydngfixvignetteradial.md)
  An opcode to apply a gain function to an image to correct vignetting.
### Image File Data
- [let kCGImagePropertyDNGPrivateData: CFString](kcgimagepropertydngprivatedata.md)
  Private data that manufacturers may store with an image and use in their own converters.
- [let kCGImagePropertyDNGMakerNoteSafety: CFString](kcgimagepropertydngmakernotesafety.md)
  A Boolean value that tells the DNG reader whether the EXIF MakerNote tag is safe to preserve.
- [let kCGImagePropertyDNGRawDataUniqueID: CFString](kcgimagepropertydngrawdatauniqueid.md)
  A 16-byte unique identifier for the raw image data.
- [let kCGImagePropertyDNGSubTileBlockSize: CFString](kcgimagepropertydngsubtileblocksize.md)
  The size of rectangular blocks that tiles use to group pixels.
- [let kCGImagePropertyDNGRowInterleaveFactor: CFString](kcgimagepropertydngrowinterleavefactor.md)
  The number of interleaved fields for the rows of the image.
- [let kCGImagePropertyDNGBackwardVersion: CFString](kcgimagepropertydngbackwardversion.md)
  The oldest version for which a file is compatible.
- [let kCGImagePropertyDNGVersion: CFString](kcgimagepropertydngversion.md)
  An encoding of the four-tier version number.
### Profile Data
- [let kCGImagePropertyDNGExtraCameraProfiles: CFString](kcgimagepropertydngextracameraprofiles.md)
  A list of file offsets to extra camera profiles.
- [let kCGImagePropertyDNGAsShotProfileName: CFString](kcgimagepropertydngasshotprofilename.md)
  A string containing the name of the “as shot” camera profile, if any.
- [let kCGImagePropertyDNGProfileHueSatMapDims: CFString](kcgimagepropertydngprofilehuesatmapdims.md)
  The number of input samples in each dimension of the hue/saturation/value mapping tables.
- [let kCGImagePropertyDNGProfileHueSatMapData1: CFString](kcgimagepropertydngprofilehuesatmapdata1.md)
  The data for the first hue/saturation/value mapping table.
- [let kCGImagePropertyDNGProfileHueSatMapData2: CFString](kcgimagepropertydngprofilehuesatmapdata2.md)
  The data for the second hue/saturation/value mapping table.
- [let kCGImagePropertyDNGProfileHueSatMapEncoding: CFString](kcgimagepropertydngprofilehuesatmapencoding.md)
  The encoding option to use when indexing into a 3D look table during raw conversion.
- [let kCGImagePropertyDNGProfileToneCurve: CFString](kcgimagepropertydngprofiletonecurve.md)
  The default tone curve to apply when processing the image as a starting point for user adjustments.
- [let kCGImagePropertyDNGProfileName: CFString](kcgimagepropertydngprofilename.md)
  A string containing the name of the camera profile.
- [let kCGImagePropertyDNGProfileEmbedPolicy: CFString](kcgimagepropertydngprofileembedpolicy.md)
  The usage rules for the camera profile.
- [let kCGImagePropertyDNGProfileCopyright: CFString](kcgimagepropertydngprofilecopyright.md)
  The copyright information for the camera profile.
- [let kCGImagePropertyDNGProfileLookTableDims: CFString](kcgimagepropertydngprofilelooktabledims.md)
  The number of input samples in each dimentsion of a default “look” table.
- [let kCGImagePropertyDNGProfileLookTableData: CFString](kcgimagepropertydngprofilelooktabledata.md)
  The default “look” table to apply when processing the image as a starting point for user adjustment.
- [let kCGImagePropertyDNGProfileLookTableEncoding: CFString](kcgimagepropertydngprofilelooktableencoding.md)
  The encoding option to use when indexing into a 3D look table during raw conversion.
### Preview
- [let kCGImagePropertyDNGPreviewApplicationName: CFString](kcgimagepropertydngpreviewapplicationname.md)
  The name of the app that created the preview stored in the IFD.
- [let kCGImagePropertyDNGPreviewApplicationVersion: CFString](kcgimagepropertydngpreviewapplicationversion.md)
  The version number of the app that created the preview stored in the IFD.
- [let kCGImagePropertyDNGPreviewSettingsName: CFString](kcgimagepropertydngpreviewsettingsname.md)
  The name of the conversion settings for the preview.
- [let kCGImagePropertyDNGPreviewSettingsDigest: CFString](kcgimagepropertydngpreviewsettingsdigest.md)
  A unique ID of the conversion settings used to render the preview.
- [let kCGImagePropertyDNGPreviewColorSpace: CFString](kcgimagepropertydngpreviewcolorspace.md)
  The color space associated with the rendered preview.
- [let kCGImagePropertyDNGPreviewDateTime: CFString](kcgimagepropertydngpreviewdatetime.md)
  The date and time for the render of the preview.
### Camera Details
- [let kCGImagePropertyDNGLensInfo: CFString](kcgimagepropertydnglensinfo.md)
  Information about the lens used for the image.
- [let kCGImagePropertyDNGUniqueCameraModel: CFString](kcgimagepropertydnguniquecameramodel.md)
  A unique, nonlocalized name for the camera model.
- [let kCGImagePropertyDNGLocalizedCameraModel: CFString](kcgimagepropertydnglocalizedcameramodel.md)
  The localized camera model name.
- [let kCGImagePropertyDNGCameraSerialNumber: CFString](kcgimagepropertydngcameraserialnumber.md)
  The camera serial number.

## See Also

- [CIFF Image Properties](ciff-image-properties.md)
  Metadata keys for the Camera Image File Format (CIFF) image format.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/dng-image-properties)*