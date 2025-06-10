# CMSampleBuffer.SampleAttachments

**Framework**: Core Media  
**Kind**: struct

Attachments applicable to each sample within a sample buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct SampleAttachments
```

#### Overview

Each property of this struct is represented as a key in the [`dictionaryRepresentation`](cmsamplebuffer/sampleattachments-swift.struct/dictionaryrepresentation.md).

## Topics

### Initializers
- [init([String : any Sendable])](cmsamplebuffer/sampleattachments-swift.struct/init(_:).md)
### Instance Properties
- [var audioIndependentSampleDecoderRefreshCount: Int?](cmsamplebuffer/sampleattachments-swift.struct/audioindependentsampledecoderrefreshcount.md)
  Only present if the audio sample is an independent frame or immediate playout frame.
- [var cryptorSubsampleAuxiliaryData: Data?](cmsamplebuffer/sampleattachments-swift.struct/cryptorsubsampleauxiliarydata.md)
  Describes the ranges of protected and unprotected data within a protected sample buffer.
- [var dependsOnOthers: Bool?](cmsamplebuffer/sampleattachments-swift.struct/dependsonothers.md)
  Indicates whether the sample depends on other samples for decoding.
- [var dictionaryRepresentation: [String : any Sendable]](cmsamplebuffer/sampleattachments-swift.struct/dictionaryrepresentation.md)
  Dictionary representation of the sample attachments.
- [var displayImmediately: Bool](cmsamplebuffer/sampleattachments-swift.struct/displayimmediately.md)
  Indicates whether the sample should be displayed immediately.
- [var doNotDisplay: Bool](cmsamplebuffer/sampleattachments-swift.struct/donotdisplay.md)
  Indicates whether the sample should be decoded but not displayed.
- [var earlierDisplayTimesAllowed: Bool?](cmsamplebuffer/sampleattachments-swift.struct/earlierdisplaytimesallowed.md)
  Indicates whether later samples may have earlier display times.
- [var hasRedundantCoding: Bool?](cmsamplebuffer/sampleattachments-swift.struct/hasredundantcoding.md)
  Indicates whether the sample has redundant coding.
- [var hdr10PlusPerFrameData: Data?](cmsamplebuffer/sampleattachments-swift.struct/hdr10plusperframedata.md)
  HDR10+ per frame metadata.
- [var hevcStepwiseTemporalSubLayerAccess: Bool](cmsamplebuffer/sampleattachments-swift.struct/hevcstepwisetemporalsublayeraccess.md)
  Indicates a step-wise temporal sublayer access (STSA) sample grouping.
- [var hevcSyncSampleNALUnitType: Int?](cmsamplebuffer/sampleattachments-swift.struct/hevcsyncsamplenalunittype.md)
  Indicates sync sample NAL unit type.
- [var hevcTemporalInfo: CMSampleBuffer.HEVCTemporalInfo?](cmsamplebuffer/sampleattachments-swift.struct/hevctemporalinfo.md)
  Indicates a video frame’s level within a hierarchical frame dependency structure.
- [var hevcTemporalSubLayerAccess: Bool](cmsamplebuffer/sampleattachments-swift.struct/hevctemporalsublayeraccess.md)
  Indicates a temporal sublayer access grouping.
- [var isDependedOnByOthers: Bool?](cmsamplebuffer/sampleattachments-swift.struct/isdependedonbyothers.md)
  Indicates whether other samples depend on this sample for decoding.
- [var isNotSync: Bool](cmsamplebuffer/sampleattachments-swift.struct/isnotsync.md)
  Indicates whether the sample is a sync sample.
- [var isPartialSync: Bool](cmsamplebuffer/sampleattachments-swift.struct/ispartialsync.md)
  Indicates whether the sample is a partial sync sample.
- [var postDecodeProcessingMetadata: [String : any Sendable]?](cmsamplebuffer/sampleattachments-swift.struct/postdecodeprocessingmetadata.md)
  Represents the sequence and frame level metadata for post decode processing. This attachment is used to pass sequence and frame level metadata from a format reader to a decoder or RAW processor. The value should only contain plist types.
### Subscripts
- [subscript(rawAttachment _: String) -> (any Sendable)?](cmsamplebuffer/sampleattachments-swift.struct/subscript(rawattachment:).md)
  Get or set a custom attachment value. The value must be a plist type.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/sampleattachments-swift.struct)*