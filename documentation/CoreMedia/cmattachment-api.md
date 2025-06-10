# CMAttachment APIs

**Framework**: Core Media

Add supporting metadata to sample buffers.

#### Overview

An attachment bearer is a Core Foundation type object that supports the suite of key, value, and mode attachment APIs. You can attach any Core Foundation object to an attachment bearer to store additional information.

## Topics

### Processing Attachments
- [func CMGetAttachment(CMAttachmentBearer, key: CFString, attachmentModeOut: UnsafeMutablePointer<CMAttachmentMode>?) -> CFTypeRef?](cmgetattachment(_:key:attachmentmodeout:).md)
  Returns an attachment from an attachment bearer object.
- [func CMCopyDictionaryOfAttachments(allocator: CFAllocator?, target: CMAttachmentBearer, attachmentMode: CMAttachmentMode) -> sending CFDictionary?](cmcopydictionaryofattachments(allocator:target:attachmentmode:).md)
  Returns a dictionary of all attachments for an attachment bearer object.
- [func CMSetAttachment(CMAttachmentBearer, key: CFString, value: CFTypeRef?, attachmentMode: CMAttachmentMode)](cmsetattachment(_:key:value:attachmentmode:).md)
  Sets or adds an attachment to an attachment bearer object.
- [func CMSetAttachments(CMAttachmentBearer, attachments: CFDictionary, attachmentMode: CMAttachmentMode)](cmsetattachments(_:attachments:attachmentmode:).md)
  Sets a dictionary of attachments on an attachment bearer object.
- [func CMRemoveAttachment(CMAttachmentBearer, key: CFString)](cmremoveattachment(_:key:).md)
  Removes a specific attachment from an attachment bearer object.
- [func CMRemoveAllAttachments(CMAttachmentBearer)](cmremoveallattachments(_:).md)
  Removes all attachments from an attachment bearer object.
- [func CMPropagateAttachments(CMAttachmentBearer, destination: CMAttachmentBearer)](cmpropagateattachments(_:destination:).md)
  Copies all propagable attachments from one attachment bearer object to another.
### Data Types
- [protocol CMAttachmentBearerProtocol](cmattachmentbearerprotocol.md)
  A protocol for objects that can carry attachments.
- [typealias CMAttachmentBearer](cmattachmentbearer.md)
  An object that can carry attachments.
- [typealias CMAttachmentMode](cmattachmentmode.md)
  The mode to use when propagating attachments.
### Constants
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
- [let kCMSampleAttachmentKey_CryptorSubsampleAuxiliaryData: CFString](kcmsampleattachmentkey_cryptorsubsampleauxiliarydata.md)
  An attachment that describes the ranges of protected and unprotected data within a protected sample buffer.
- [let kCMSampleAttachmentKey_AudioIndependentSampleDecoderRefreshCount: CFString](kcmsampleattachmentkey_audioindependentsampledecoderrefreshcount.md)
  An attachment that’s only present if the audio sample is an independent frame or immediate playout frame.
- [let kCMSampleBufferAttachmentKey_CameraIntrinsicMatrix: CFString](kcmsamplebufferattachmentkey_cameraintrinsicmatrix.md)
  An attachment that indicates a 3x3 camera intrinsic matrix to apply to the current sample buffer.

## See Also

- [CMSampleBuffer APIs](cmsamplebuffer-api.md)
  An object that contains zero or more media samples of a uniform media type.
- [CMBlockBuffer APIs](cmblockbuffer-api.md)
  An object the system uses to move blocks of memory through a processing system.
- [struct CMTaggedBuffer](cmtaggedbuffer.md)
  An instance of a media buffer containing metadata tags.
- [CMTaggedBufferGroup APIs](cmtaggedbuffergroup.md)
  Objective-C types and interfaces for working with Core Media tagged buffer groups.
- [CMFormatDescription APIs](cmformatdescription-api.md)
  A media format descriptor that describes the samples in a sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmattachment-api)*