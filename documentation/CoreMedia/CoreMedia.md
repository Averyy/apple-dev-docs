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
- [CMSampleBuffer](cmsamplebuffer-api.md)
  An object that contains zero or more media samples of a uniform media type.
- [CMBlockBuffer](cmblockbuffer-api.md)
  An object the system uses to move blocks of memory through a processing system.
- [CMTaggedBufferGroup](cmtaggedbuffergroup.md)
  Objective-C types and interfaces for working with Core Media tagged buffer groups.
- [CMFormatDescription](cmformatdescription-api.md)
  A media format descriptor that describes the samples in a sample buffer.
- [CMAttachment](cmattachment-api.md)
  Add supporting metadata to sample buffers.
- [struct CMTaggedBuffer](cmtaggedbuffer.md)
  An instance of a media buffer containing metadata tags.
- [struct CMMutableDataBlockBuffer](cmmutabledatablockbuffer.md)
  A block buffer that provides read-write access to a range of bytes.
- [struct CMReadOnlyDataBlockBuffer](cmreadonlydatablockbuffer.md)
  A block buffer that provides read-only access to the a range of bytes.
- [struct CMReadySampleBuffer](cmreadysamplebuffer.md)
  Buffer carrying readily available samples of media data.
- [struct CMSampleDataReference](cmsampledatareference.md)
  References sample data in at a URL.
- [struct CMTaggedDynamicBuffer](cmtaggeddynamicbuffer.md)
  Contains a collection of tags associated with a read-only media buffer.
### Time Representation
- [CMTime](cmtime-api.md)
  A structure that represents time.
- [CMTimeRange](cmtimerange-api.md)
  A structure that represents a range of time.
- [CMTimeMapping](cmtimemapping-api.md)
  A structure that maps a segment of a source time range to a target time range.
### Media Synchronization
- [CMClock](cmclock-api.md)
  A reference clock you use to synchronize applications and devices.
- [CMAudioClock](cmaudioclock-api.md)
  A specialized reference clock that synchronizes with audio sources.
- [CMTimebase](cmtimebase-api.md)
  A model of a timeline under application control.
### Text Markup
- [CMTextMarkup](cmtextmarkup.md)
  Attributes that specify text markup in legible media.
### Metadata
- [CMMetadata](cmmetadata.md)
  The APIs for working with the framework’s Metadata Identifier Services and Metadata Data Type Registry.
- [CMTag](cmtag-api.md)
  Types and interfaces for working with Core Media tags.
- [class CMTag](cmtag-swift.class.md)
  A tag to set additional metadata on media buffers.
- [class CMTypedTag](cmtypedtag.md)
  A tag to set additional metadata on media buffers, with an associated Swift type for its value.
- [CMTagCollection](cmtagcollection.md)
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
- [CMSimpleQueue](cmsimplequeue-api.md)
  A simple, lockless FIFO queue of elements.
- [CMBufferQueue](cmbufferqueue-api.md)
  A queue of timed buffers.
- [CMMemoryPool](cmmemorypool-api.md)
  An object that optimizes memory allocation when working with large blocks of memory.
### Reference
- [Core Media Constants](core-media-constants.md)
- [Core Media Functions](core-media-functions.md)
- [Core Media Type Aliases](core-media-type-aliases.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreMedia)*