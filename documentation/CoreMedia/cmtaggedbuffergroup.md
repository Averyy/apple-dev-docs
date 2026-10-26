# CMTaggedBufferGroup

**Framework**: Core Media  
**Role**: API Collection

Objective-C types and interfaces for working with Core Media tagged buffer groups.

## Topics

### Types
- [typealias CMTaggedBufferGroupFormatDescription](./cmtaggedbuffergroupformatdescription.md)
  A type for tagged buffer format descriptions.
- [typealias CMTaggedBufferGroupFormatType](./cmtaggedbuffergroupformattype.md)
  A type for tagged buffer format information.
- [CMTaggedBufferGroupRef](./cmtaggedbuffergroupref.md)
  A reference to a tagged buffer group instance.
### Creating Tagged Buffer Groups
- [CMTaggedBufferGroupCreate](./cmtaggedbuffergroupcreate.md)
  Creates a new tagged buffer group from a pair of buffers and the tags to associate with them.
- [CMTaggedBufferGroupCreateCombined](./cmtaggedbuffergroupcreatecombined.md)
  Creates a new tagged buffer group from an array of existing tagged buffer groups.
### Inspecting Tagged Buffer Groups
- [CMTaggedBufferGroupGetCount](./cmtaggedbuffergroupgetcount.md)
  Gets the number of buffers contained within a tagged buffer group.
- [CMTaggedBufferGroupGetNumberOfMatchesForTagCollection](./cmtaggedbuffergroupgetnumberofmatchesfortagcollection.md)
  Gets the number of buffers in the group associated with a given tag collection.
- [CMTaggedBufferGroupGetTagCollectionAtIndex](./cmtaggedbuffergroupgettagcollectionatindex.md)
  Gets the collection of tags for a buffer at a given index in the group.
- [CMTaggedBufferGroupGetTypeID](./cmtaggedbuffergroupgettypeid.md)
  Gets the internal type ID for a tagged buffer group.
### Accessing Sample Buffers
- [CMTaggedBufferGroupGetCMSampleBufferAtIndex](./cmtaggedbuffergroupgetcmsamplebufferatindex.md)
  Gets the sample buffer at a given index in the buffer group.
- [CMTaggedBufferGroupGetCMSampleBufferForTag](./cmtaggedbuffergroupgetcmsamplebufferfortag.md)
  Gets the single sample buffer in a group which contains a given tag, if present.
- [CMTaggedBufferGroupGetCMSampleBufferForTagCollection](./cmtaggedbuffergroupgetcmsamplebufferfortagcollection.md)
  Gets the single sample buffer in a group which contains a given tag collection, if present.
### Accessing Pixel Buffers
- [CMTaggedBufferGroupGetCVPixelBufferAtIndex](./cmtaggedbuffergroupgetcvpixelbufferatindex.md)
  Gets the pixel buffer at a given index in the buffer group.
- [CMTaggedBufferGroupGetCVPixelBufferForTag](./cmtaggedbuffergroupgetcvpixelbufferfortag.md)
  Gets the single pixel buffer in a group which contains a given tag, if present.
- [CMTaggedBufferGroupGetCVPixelBufferForTagCollection](./cmtaggedbuffergroupgetcvpixelbufferfortagcollection.md)
  Gets the single pixel buffer in a group which contains a given tag collection, if present.
### Inspecting Buffer Format
- [CMTaggedBufferGroupFormatDescriptionCreateForTaggedBufferGroup](./cmtaggedbuffergroupformatdescriptioncreatefortaggedbuffergroup.md)
  Creates a new format description for a tagged buffer group.
- [CMTaggedBufferGroupFormatDescriptionMatchesTaggedBufferGroup](./cmtaggedbuffergroupformatdescriptionmatchestaggedbuffergroup.md)
  Checks to see if a tagged buffer group’s format matches an existing format description.
### Errors
- [CMTaggedBufferGroupError](./cmtaggedbuffergrouperror.md)
  Error codes returned by Core Media when working with tagged buffer groups.

## See Also

### Sample Processing
- [CMSampleBuffer](./cmsamplebuffer-api.md)
  An object that contains zero or more media samples of a uniform media type.
- [CMBlockBuffer](./cmblockbuffer-api.md)
  An object the system uses to move blocks of memory through a processing system.
- [CMFormatDescription](./cmformatdescription-api.md)
  A media format descriptor that describes the samples in a sample buffer.
- [CMAttachment](./cmattachment-api.md)
  Add supporting metadata to sample buffers.
- [struct CMTaggedBuffer](./cmtaggedbuffer.md)
  An instance of a media buffer containing metadata tags.
- [struct CMMutableDataBlockBuffer](./cmmutabledatablockbuffer.md)
  A block buffer that provides read-write access to a range of bytes.
- [struct CMReadOnlyDataBlockBuffer](./cmreadonlydatablockbuffer.md)
  A block buffer that provides read-only access to the a range of bytes.
- [struct CMReadySampleBuffer](./cmreadysamplebuffer.md)
  Buffer carrying readily available samples of media data.
- [struct CMSampleDataReference](./cmsampledatareference.md)
  References sample data in at a URL.
- [struct CMTaggedDynamicBuffer](./cmtaggeddynamicbuffer.md)
  Contains a collection of tags associated with a read-only media buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtaggedbuffergroup)*