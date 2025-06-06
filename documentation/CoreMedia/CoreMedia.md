# Core Media

**Framework**: Core Media  
**Kind**: module

Represent time-based audio-visual assets with essential data types.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

#### Overview

The Core Media framework defines the media pipeline used by AVFoundation and other high-level media frameworks found on Apple platforms. Use Core Media’s low-level data types and interfaces to efficiently process media samples and manage queues of media data.

## Topics

### Sample Processing
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
- [CMAttachment APIs](cmattachment-api.md)
  Add supporting metadata to sample buffers.
### Time Representation
- [CMTime APIs](cmtime-api.md)
  A structure that represents time.
- [CMTimeRange APIs](cmtimerange-api.md)
  A structure that represents a range of time.
- [CMTimeMapping APIs](cmtimemapping-api.md)
  A structure that maps a segment of a source time range to a target time range.
### Media Synchronization
- [CMClock APIs](cmclock-api.md)
  A reference clock you use to synchronize applications and devices.
- [CMAudioClock APIs](cmaudioclock-api.md)
  A specialized reference clock that synchronizes with audio sources.
- [CMTimebase APIs](cmtimebase-api.md)
  A model of a timeline under application control.
### Text Markup
- [CMTextMarkup](cmtextmarkup.md)
  Attributes that specify text markup in legible media.
### Metadata
- [CMMetadata APIs](cmmetadata.md)
  The APIs for working with the framework’s Metadata Identifier Services and Metadata Data Type Registry.
- [CMTag APIs](cmtag-api.md)
  Types and interfaces for working with Core Media tags.
- [class CMTag](cmtag-swift.class.md)
  A tag to set additional metadata on media buffers.
- [class CMTypedTag](cmtypedtag.md)
  A tag to set additional metadata on media buffers, with an associated Swift type for its value.
- [CMTagCollection APIs](cmtagcollection.md)
  Objective-C types and interfaces for working with Core Media tag collections.
- [enum CMProjectionType](cmprojectiontype.md)
  Constants describing the projection surface information in a 3D video buffer or channel.
- [struct CMStereoViewComponents](cmstereoviewcomponents.md)
  Constants describing the stereo views contained within a buffer or channel.
- [struct CMStereoViewInterpretationOptions](cmstereoviewinterpretationoptions.md)
  Create a set of stereo view interpretation options from a constant.
- [enum CMPackingType](cmpackingtype.md)
  The type of packing within each video frame, if any.
### Queues
- [CMSimpleQueue APIs](cmsimplequeue-api.md)
  A simple, lockless FIFO queue of elements.
- [CMBufferQueue APIs](cmbufferqueue-api.md)
  A queue of timed buffers.
- [CMMemoryPool APIs](cmmemorypool-api.md)
  An object that optimizes memory allocation when working with large blocks of memory.
### Reference
- [Core Media Constants](core-media-constants.md)
- [Core Media Functions](core-media-functions.md)
- [Core Media Type Aliases](core-media-type-aliases.md)
### Variables
- [let kCMFormatDescriptionProjectionKind_Equirectangular: CFString](kcmformatdescriptionprojectionkind_equirectangular.md)
- [let kCMFormatDescriptionProjectionKind_HalfEquirectangular: CFString](kcmformatdescriptionprojectionkind_halfequirectangular.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreMedia)*