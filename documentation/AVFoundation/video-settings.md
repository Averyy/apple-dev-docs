# Video settings

**Framework**: AVFoundation

Configure video processing settings using standard key and value constants.

## Topics

### Clean aperture
- [let AVVideoCleanApertureKey: String](avvideocleanaperturekey.md)
  A key that defines the region within the video dimension displayed during playback.
- [let AVVideoCleanApertureWidthKey: String](avvideocleanaperturewidthkey.md)
  A key to access the width of video that’s free from transition artifacts caused by signal encoding.
- [let AVVideoCleanApertureHeightKey: String](avvideocleanapertureheightkey.md)
  A key to access the height of video that’s free from transition artifacts caused by signal encoding.
- [let AVVideoCleanApertureVerticalOffsetKey: String](avvideocleanapertureverticaloffsetkey.md)
  A key to access the vertical offset of video that’s free from transition artifacts caused by signal encoding.
- [let AVVideoCleanApertureHorizontalOffsetKey: String](avvideocleanaperturehorizontaloffsetkey.md)
  A key to access the horizontal offset of video that’s free from transition artifacts caused by signal encoding.
### Video codecs
- [let AVVideoCodecKey: String](avvideocodeckey.md)
  A key to access the name of the codec for compressing video.
- [struct AVVideoCodecType](avvideocodectype.md)
  A set of constants that describe the codecs the system supports for video capture.
### Color properties
- [Setting color properties for a specific resolution](setting-color-properties-for-a-specific-resolution.md)
  Choose the proper color property keys for the desired color range.
- [let AVVideoAllowWideColorKey: String](avvideoallowwidecolorkey.md)
  The key for a dictionary that indicates whether the client can process wide color.
- [let AVVideoColorPrimariesKey: String](avvideocolorprimarieskey.md)
  The key to identify color primaries in a color properties dictionary.
- [let AVVideoColorPrimaries_EBU_3213: String](avvideocolorprimaries_ebu_3213.md)
  The color primary is in the EBU Tech. 3213 color space.
- [let AVVideoColorPrimaries_ITU_R_2020: String](avvideocolorprimaries_itu_r_2020.md)
  The color primary is in the ITU_R BT.2020 color space for ultra high definition television.
- [let AVVideoColorPrimaries_ITU_R_709_2: String](avvideocolorprimaries_itu_r_709_2.md)
  The color primary is in the ITU_R BT.709 color space.
- [let AVVideoColorPrimaries_P3_D65: String](avvideocolorprimaries_p3_d65.md)
  The color primary uses the DCI-P3 D65 color space.
- [let AVVideoColorPrimaries_SMPTE_C: String](avvideocolorprimaries_smpte_c.md)
  The color primary uses the SMPTE C color space.
- [let AVVideoColorPropertiesKey: String](avvideocolorpropertieskey.md)
  The key for a dictionary that contains properties specifying video color.
- [let AVVideoTransferFunctionKey: String](avvideotransferfunctionkey.md)
  The key to identify the transfer function in a color properties dictionary.
- [let AVVideoTransferFunction_IEC_sRGB: String](avvideotransferfunction_iec_srgb.md)
  The transfer function for the IEC sRGB color space.
- [let AVVideoTransferFunction_ITU_R_2100_HLG: String](avvideotransferfunction_itu_r_2100_hlg.md)
  The transfer function for the ITU_R BT.2100 color space.
- [let AVVideoTransferFunction_ITU_R_709_2: String](avvideotransferfunction_itu_r_709_2.md)
  The transfer function for the ITU_R BT.709 color space.
- [let AVVideoTransferFunction_Linear: String](avvideotransferfunction_linear.md)
  The transfer function for the linear color space.
- [let AVVideoTransferFunction_SMPTE_240M_1995: String](avvideotransferfunction_smpte_240m_1995.md)
  The transfer function for the SMPTE 240M color space.
- [let AVVideoTransferFunction_SMPTE_ST_2084_PQ: String](avvideotransferfunction_smpte_st_2084_pq.md)
  The transfer function for the SMPTE 2084 color space.
- [let AVVideoYCbCrMatrixKey: String](avvideoycbcrmatrixkey.md)
  The key to identify the Y’CbCr matrix in a color properties dictionary.
- [let AVVideoYCbCrMatrix_ITU_R_2020: String](avvideoycbcrmatrix_itu_r_2020.md)
  The Y’CbCr color matrix for ITU-R BT.2020 conversion.
- [let AVVideoYCbCrMatrix_ITU_R_601_4: String](avvideoycbcrmatrix_itu_r_601_4.md)
  The Y’CbCr color matrix for ITU-R BT.601 conversion.
- [let AVVideoYCbCrMatrix_ITU_R_709_2: String](avvideoycbcrmatrix_itu_r_709_2.md)
  The Y’CbCr color matrix for ITU-R BT.709 conversion.
- [let AVVideoYCbCrMatrix_SMPTE_240M_1995: String](avvideoycbcrmatrix_smpte_240m_1995.md)
  The Y’CbCr color matrix for SMPTE 240M conversion.
### Compression
- [let AVVideoCompressionPropertiesKey: String](avvideocompressionpropertieskey.md)
  A key to access the dictionary of compression properties for a video asset.
- [let AVVideoDecompressionPropertiesKey: String](avvideodecompressionpropertieskey.md)
  The key that indicates the video decompression properties to pass to the video decoder.
- [let AVVideoAverageBitRateKey: String](avvideoaveragebitratekey.md)
  A key to access the average bit rate—as bits per second—used in compressing video.
- [let AVVideoQualityKey: String](avvideoqualitykey.md)
  A key to set the JPEG compression quality of the video.
- [let AVVideoMaxKeyFrameIntervalKey: String](avvideomaxkeyframeintervalkey.md)
  A key to access the maximum interval between keyframes.
- [let AVVideoMaxKeyFrameIntervalDurationKey: String](avvideomaxkeyframeintervaldurationkey.md)
  A key to access the maximum interval duration between keyframes.
- [let AVVideoAllowFrameReorderingKey: String](avvideoallowframereorderingkey.md)
  A key to access permission to reorder frames.
- [let AVVideoAppleProRAWBitDepthKey: String](avvideoappleprorawbitdepthkey.md)
  A key to access the Apple ProRAW bit depth.
### Entropy mode
- [let AVVideoH264EntropyModeKey: String](avvideoh264entropymodekey.md)
  The entropy encoding mode for H.264 compression.
- [let AVVideoH264EntropyModeCABAC: String](avvideoh264entropymodecabac.md)
  The encoder uses Context-based Adaptive Binary Arithmetic Coding.
- [let AVVideoH264EntropyModeCAVLC: String](avvideoh264entropymodecavlc.md)
  The encoder uses Context-based Adaptive Variable Length Coding.
### FairPlay
- [let AVStreamingKeyDeliveryContentKeyType: String](avstreamingkeydeliverycontentkeytype.md)
  A URL for a content key.
- [let AVStreamingKeyDeliveryPersistentContentKeyType: String](avstreamingkeydeliverypersistentcontentkeytype.md)
  A URL for a persistent content key.
### Frame rate
- [let AVVideoExpectedSourceFrameRateKey: String](avvideoexpectedsourceframeratekey.md)
  The expected source frame rate.
- [let AVVideoAverageNonDroppableFrameRateKey: String](avvideoaveragenondroppableframeratekey.md)
  The desired average number of non-droppable frames to be encoded for each second of video.
### Geometry
- [let AVVideoWidthKey: String](avvideowidthkey.md)
  A key to access the width of the video in pixels.
- [let AVVideoHeightKey: String](avvideoheightkey.md)
  A key to access the height of the video in pixels.
- [let AVVideoPixelAspectRatioKey: String](avvideopixelaspectratiokey.md)
  A key to access the video’s pixel aspect ratio.
- [let AVVideoPixelAspectRatioVerticalSpacingKey: String](avvideopixelaspectratioverticalspacingkey.md)
  A key to access the pixel aspect ratio vertical spacing.
- [let AVVideoPixelAspectRatioHorizontalSpacingKey: String](avvideopixelaspectratiohorizontalspacingkey.md)
  A key to access the pixel aspect ratio horizontal spacing.
### Profile level
- [let AVVideoProfileLevelKey: String](avvideoprofilelevelkey.md)
  A key to access the video profile.
- [let AVVideoProfileLevelH264High40: String](avvideoprofilelevelh264high40.md)
  A high-level 4.0 profile.
- [let AVVideoProfileLevelH264High41: String](avvideoprofilelevelh264high41.md)
  A high-level 4.1 profile.
- [let AVVideoProfileLevelH264Main30: String](avvideoprofilelevelh264main30.md)
  A main-level 3.0 profile.
- [let AVVideoProfileLevelH264Main31: String](avvideoprofilelevelh264main31.md)
  A main-level 3.1 profile.
- [let AVVideoProfileLevelH264Main32: String](avvideoprofilelevelh264main32.md)
  A main-level 3.2 profile.
- [let AVVideoProfileLevelH264Main41: String](avvideoprofilelevelh264main41.md)
  A main-level 4.1 profile.
- [let AVVideoProfileLevelH264Baseline30: String](avvideoprofilelevelh264baseline30.md)
  A baseline-level 3.0 profile.
- [let AVVideoProfileLevelH264Baseline31: String](avvideoprofilelevelh264baseline31.md)
  A baseline-level 3.1 profile.
- [let AVVideoProfileLevelH264Baseline41: String](avvideoprofilelevelh264baseline41.md)
  A baseline-level 4.1 profile.
- [let AVVideoProfileLevelH264HighAutoLevel: String](avvideoprofilelevelh264highautolevel.md)
  A high profile auto level profile.
- [let AVVideoProfileLevelH264MainAutoLevel: String](avvideoprofilelevelh264mainautolevel.md)
  A main profile auto level profile.
- [let AVVideoProfileLevelH264BaselineAutoLevel: String](avvideoprofilelevelh264baselineautolevel.md)
  A baseline auto level profile.
### Scaling mode
- [let AVVideoScalingModeFit: String](avvideoscalingmodefit.md)
  The string identifier for scaling a video to fit the surrounding view’s dimensions.
- [let AVVideoScalingModeKey: String](avvideoscalingmodekey.md)
  A key to retrieve the video scaling mode from a dictionary.
- [let AVVideoScalingModeResize: String](avvideoscalingmoderesize.md)
  The string identifier for resizing a video to fit the surrounding view’s dimensions.
- [let AVVideoScalingModeResizeAspect: String](avvideoscalingmoderesizeaspect.md)
  The string identifier for resizing a video to its surrounding view’s shorter dimension while preserving its aspect ratio.
- [let AVVideoScalingModeResizeAspectFill: String](avvideoscalingmoderesizeaspectfill.md)
  The string identifier for resizing a video to fit the surrounding view’s longer dimension while preserving aspect ratio.
### VideoToolbox options
- [let AVVideoEncoderSpecificationKey: String](avvideoencoderspecificationkey.md)
  The video encoder specification includes options for choosing a specific video encoder.

## See Also

- [Media assets](media-assets.md)
  Load media assets from files and streams to inspect their attributes, tracks, and embedded metadata.
- [Media reading and writing](media-reading-and-writing.md)
  Read images from video, export to alternative formats, and perform sample-level reading and writing of media data.
- [Media types and utilities](media-types-and-utilities.md)
  Identify the types of content and file formats that AVFoundation supports.
- [Audio settings](audio-settings.md)
  Configure audio processing settings using standard key and value constants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/video-settings)*