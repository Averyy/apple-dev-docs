# kCMSampleAttachmentKey_CryptorSubsampleAuxiliaryData

**Framework**: Core Media  
**Kind**: var

An attachment that describes the ranges of protected and unprotected data within a protected sample buffer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let kCMSampleAttachmentKey_CryptorSubsampleAuxiliaryData: CFString
```

## See Also

- [var kCMAttachmentMode_ShouldNotPropagate: CMAttachmentMode](kcmattachmentmode_shouldnotpropagate.md)
  A mode that doesn’t propagate attachments to another object.
- [var kCMAttachmentMode_ShouldPropagate: CMAttachmentMode](kcmattachmentmode_shouldpropagate.md)
  A mode that propagates attachments to another object.
- [let kCMSampleAttachmentKey_HEVCTemporalLevelInfo: CFString](kcmsampleattachmentkey_hevctemporallevelinfo.md)
  An attachment that indicates a video frame’s level within a hierarchical frame dependency structure.
- [let kCMSampleAttachmentKey_HEVCTemporalSubLayerAccess: CFString](kcmsampleattachmentkey_hevctemporalsublayeraccess.md)
  An attachment that indicates a temporal sublayer access grouping.
- [let kCMSampleAttachmentKey_HEVCStepwiseTemporalSubLayerAccess: CFString](kcmsampleattachmentkey_hevcstepwisetemporalsublayeraccess.md)
  An attachment that indicates a step-wise temporal sublayer access (STSA) sample grouping.
- [let kCMSampleAttachmentKey_HEVCSyncSampleNALUnitType: CFString](kcmsampleattachmentkey_hevcsyncsamplenalunittype.md)
  An attachment that indicates a sync sample NAL unit type.
- [let kCMSampleAttachmentKey_AudioIndependentSampleDecoderRefreshCount: CFString](kcmsampleattachmentkey_audioindependentsampledecoderrefreshcount.md)
  An attachment that’s only present if the audio sample is an independent frame or immediate playout frame.
- [let kCMSampleBufferAttachmentKey_CameraIntrinsicMatrix: CFString](kcmsamplebufferattachmentkey_cameraintrinsicmatrix.md)
  An attachment that indicates a 3x3 camera intrinsic matrix to apply to the current sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmsampleattachmentkey_cryptorsubsampleauxiliarydata)*