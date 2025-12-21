# CMSampleBuffer

**Framework**: Core Media

An object that contains zero or more media samples of a uniform media type.

#### Overview

Sample buffers are Core Foundation objects that the system uses to move media sample data through the media pipeline. An instance of `CMSampleBuffer` contains zero or more compressed (or uncompressed) samples of a particular media type and contains one of the following:

- A [`CMBlockBuffer`](cmblockbuffer.md) of one or more media samples
- A [`CVImageBuffer`](https://developer.apple.com/documentation/CoreVideo/cvimagebuffer-q40), a reference to the format description for the stream of `CMSampleBuffers`, size and timing information for each of the contained media samples, and both buffer-level and sample-level attachments

A sample buffer can contain both sample-level and buffer-level attachments. Each individual sample in a buffer may provide attachments that include information such as timestamps and video frame dependencies. You read and write sample-level attachments using the [`CMSampleBufferGetSampleAttachmentsArray(_:createIfNecessary:)`](cmsamplebuffergetsampleattachmentsarray(_:createifnecessary:).md) function. Buffer-level attachments provide information about the buffer as a whole, such as playback speed and actions to perform upon consuming the buffer. You can read and write buffer-level attachments using the APIs described in [`CMAttachment`](cmattachment-api.md) and the keys listed under [`Sample Attachment Keys`](sample-attachment-keys.md).

It’s possible for a sample buffer to describe samples it doesn’t yet contain. For example, some media services may have access to sample size, timing, and format information before they read the data. Such services may create sample buffers with that information and insert them into queues early, and attach (or fill) the buffer of media data later, when it becomes ready. Sample buffers have the concept of data-readiness, which means you can test, set, and force them to become ready “now.” It’s also possible for a sample buffer to contain nothing but a special buffer-level attachment that describes a media stream event (for example, “discontinuity: drain and reset decoder before processing the next `CMSampleBuffer`”).

## Topics

### Creating Sample Buffers
- [func CMSampleBufferCreateReady(allocator: CFAllocator?, dataBuffer: CMBlockBuffer?, formatDescription: CMFormatDescription?, sampleCount: CMItemCount, sampleTimingEntryCount: CMItemCount, sampleTimingArray: UnsafePointer<CMSampleTimingInfo>?, sampleSizeEntryCount: CMItemCount, sampleSizeArray: UnsafePointer<Int>?, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](cmsamplebuffercreateready(allocator:databuffer:formatdescription:samplecount:sampletimingentrycount:sampletimingarray:samplesizeentrycount:samplesizearray:samplebufferout:).md)
  Creates a sample buffer with media data.
- [func CMSampleBufferCreateReadyWithImageBuffer(allocator: CFAllocator?, imageBuffer: CVImageBuffer, formatDescription: CMVideoFormatDescription, sampleTiming: UnsafePointer<CMSampleTimingInfo>, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](cmsamplebuffercreatereadywithimagebuffer(allocator:imagebuffer:formatdescription:sampletiming:samplebufferout:).md)
  Creates a sample buffer with image data.
- [func CMAudioSampleBufferCreateReadyWithPacketDescriptions(allocator: CFAllocator?, dataBuffer: CMBlockBuffer, formatDescription: CMFormatDescription, sampleCount: CMItemCount, presentationTimeStamp: CMTime, packetDescriptions: UnsafePointer<AudioStreamPacketDescription>?, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](cmaudiosamplebuffercreatereadywithpacketdescriptions(allocator:databuffer:formatdescription:samplecount:presentationtimestamp:packetdescriptions:samplebufferout:).md)
  Creates a sample buffer with packet descriptions.
- [func CMSampleBufferCreateWithMakeDataReadyHandler(CFAllocator?, CMBlockBuffer?, Bool, CMFormatDescription?, CMItemCount, CMItemCount, UnsafePointer<CMSampleTimingInfo>?, CMItemCount, UnsafePointer<Int>?, UnsafeMutablePointer<CMSampleBuffer?>, CMSampleBufferMakeDataReadyHandler?) -> OSStatus](cmsamplebuffercreatewithmakedatareadyhandler(_:_:_:_:_:_:_:_:_:_:_:).md)
  Creates a sample buffer with a handler to make the data ready for use.
- [func CMSampleBufferCreateForImageBufferWithMakeDataReadyHandler(CFAllocator?, CVImageBuffer, Bool, CMVideoFormatDescription, UnsafePointer<CMSampleTimingInfo>, UnsafeMutablePointer<CMSampleBuffer?>, CMSampleBufferMakeDataReadyHandler?) -> OSStatus](cmsamplebuffercreateforimagebufferwithmakedatareadyhandler(_:_:_:_:_:_:_:).md)
  Creates a sample buffer with an image buffer and a handler to make the data ready for use.
- [func CMAudioSampleBufferCreateWithPacketDescriptionsAndMakeDataReadyHandler(CFAllocator?, CMBlockBuffer?, Bool, CMFormatDescription, CMItemCount, CMTime, UnsafePointer<AudioStreamPacketDescription>?, UnsafeMutablePointer<CMSampleBuffer?>, CMSampleBufferMakeDataReadyHandler?) -> OSStatus](cmaudiosamplebuffercreatewithpacketdescriptionsandmakedatareadyhandler(_:_:_:_:_:_:_:_:_:).md)
  Creates a sample buffer with packet descriptions and a handler to make the data ready for use.
- [func CMSampleBufferCreate(allocator: CFAllocator?, dataBuffer: CMBlockBuffer?, dataReady: Bool, makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback?, refcon: UnsafeMutableRawPointer?, formatDescription: CMFormatDescription?, sampleCount: CMItemCount, sampleTimingEntryCount: CMItemCount, sampleTimingArray: UnsafePointer<CMSampleTimingInfo>?, sampleSizeEntryCount: CMItemCount, sampleSizeArray: UnsafePointer<Int>?, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](cmsamplebuffercreate(allocator:databuffer:dataready:makedatareadycallback:refcon:formatdescription:samplecount:sampletimingentrycount:sampletimingarray:samplesizeentrycount:samplesizearray:samplebufferout:).md)
  Creates a sample buffer with a callback to make the data ready for use.
- [func CMSampleBufferCreateForImageBuffer(allocator: CFAllocator?, imageBuffer: CVImageBuffer, dataReady: Bool, makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback?, refcon: UnsafeMutableRawPointer?, formatDescription: CMVideoFormatDescription, sampleTiming: UnsafePointer<CMSampleTimingInfo>, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](cmsamplebuffercreateforimagebuffer(allocator:imagebuffer:dataready:makedatareadycallback:refcon:formatdescription:sampletiming:samplebufferout:).md)
  Creates a sample buffer with an image buffer and a callback to make the data ready for use.
- [func CMAudioSampleBufferCreateWithPacketDescriptions(allocator: CFAllocator?, dataBuffer: CMBlockBuffer?, dataReady: Bool, makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback?, refcon: UnsafeMutableRawPointer?, formatDescription: CMFormatDescription, sampleCount: CMItemCount, presentationTimeStamp: CMTime, packetDescriptions: UnsafePointer<AudioStreamPacketDescription>?, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](cmaudiosamplebuffercreatewithpacketdescriptions(allocator:databuffer:dataready:makedatareadycallback:refcon:formatdescription:samplecount:presentationtimestamp:packetdescriptions:samplebufferout:).md)
  Creates a sample buffer with packet descriptions and a callback to make the data ready for use.
### Copying Sample Buffers
- [func CMSampleBufferCreateCopy(allocator: CFAllocator?, sampleBuffer: CMSampleBuffer, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](cmsamplebuffercreatecopy(allocator:samplebuffer:samplebufferout:).md)
  Creates a copy of a sample buffer.
- [func CMSampleBufferCreateCopyWithNewTiming(allocator: CFAllocator?, sampleBuffer: CMSampleBuffer, sampleTimingEntryCount: CMItemCount, sampleTimingArray: UnsafePointer<CMSampleTimingInfo>?, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](cmsamplebuffercreatecopywithnewtiming(allocator:samplebuffer:sampletimingentrycount:sampletimingarray:samplebufferout:).md)
  Creates a copy of a sample buffer with new timing information.
- [func CMSampleBufferCopySampleBufferForRange(allocator: CFAllocator?, sampleBuffer: CMSampleBuffer, sampleRange: CFRange, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](cmsamplebuffercopysamplebufferforrange(allocator:samplebuffer:samplerange:samplebufferout:).md)
  Creates a sample buffer that contains a range of samples from an existing sample buffer.
### Determining Readiness
- [func CMSampleBufferDataIsReady(CMSampleBuffer) -> Bool](cmsamplebufferdataisready(_:).md)
  Returns a Boolean value that indicates whether the sample buffer’s data is ready for use.
- [func CMSampleBufferSetDataReady(CMSampleBuffer) -> OSStatus](cmsamplebuffersetdataready(_:).md)
  Marks a sample buffer’s data as ready for use.
- [func CMSampleBufferSetDataFailed(CMSampleBuffer, status: OSStatus) -> OSStatus](cmsamplebuffersetdatafailed(_:status:).md)
  Marks the sample buffer’s data as failed to indicate that it won’t become ready.
- [func CMSampleBufferHasDataFailed(CMSampleBuffer, statusOut: UnsafeMutablePointer<OSStatus>?) -> Bool](cmsamplebufferhasdatafailed(_:statusout:).md)
  Returns a Boolean value that indicates whether the sample buffer’s data loading request failed.
- [func CMSampleBufferMakeDataReady(CMSampleBuffer) -> OSStatus](cmsamplebuffermakedataready(_:).md)
  Makes the sample buffer’s data ready for use by invoking its callback to load the data.
- [func CMSampleBufferTrackDataReadiness(CMSampleBuffer, sampleBufferToTrack: CMSampleBuffer) -> OSStatus](cmsamplebuffertrackdatareadiness(_:samplebuffertotrack:).md)
  Associates a sample buffer’s data readiness with that of another sample buffer.
### Invalidating Sample Buffers
- [func CMSampleBufferSetInvalidateHandler(CMSampleBuffer, invalidateHandler: CMSampleBufferInvalidateHandler) -> OSStatus](cmsamplebuffersetinvalidatehandler(_:invalidatehandler:).md)
  Sets the sample buffer’s invalidation handler.
- [func CMSampleBufferInvalidate(CMSampleBuffer) -> OSStatus](cmsamplebufferinvalidate(_:).md)
  Invalidates a sample buffer by calling its invalidation callback.
- [func CMSampleBufferIsValid(CMSampleBuffer) -> Bool](cmsamplebufferisvalid(_:).md)
  Returns a Boolean value that indicates whether a sample buffer is valid.
- [func CMSampleBufferSetInvalidateCallback(CMSampleBuffer, callback: CMSampleBufferInvalidateCallback, refcon: UInt64) -> OSStatus](cmsamplebuffersetinvalidatecallback(_:callback:refcon:).md)
  Sets the sample buffer’s invalidation callback.
### Inspecting Size Information
- [func CMSampleBufferGetNumSamples(CMSampleBuffer) -> CMItemCount](cmsamplebuffergetnumsamples(_:).md)
  Returns the number of media samples in a sample buffer.
- [func CMSampleBufferGetTotalSampleSize(CMSampleBuffer) -> Int](cmsamplebuffergettotalsamplesize(_:).md)
  Returns the total size in bytes of sample data in a sample buffer.
- [func CMSampleBufferGetSampleSize(CMSampleBuffer, at: CMItemIndex) -> Int](cmsamplebuffergetsamplesize(_:at:).md)
  Returns the size in bytes of a specified sample in a sample buffer.
- [func CMSampleBufferGetSampleSizeArray(CMSampleBuffer, entryCount: CMItemCount, arrayToFill: UnsafeMutablePointer<Int>?, entriesNeededOut: UnsafeMutablePointer<CMItemCount>?) -> OSStatus](cmsamplebuffergetsamplesizearray(_:entrycount:arraytofill:entriesneededout:).md)
  Retrieves an array of sample sizes that represents each sample in a sample buffer.
### Inspecting Duration and Timing
- [func CMSampleBufferGetDuration(CMSampleBuffer) -> CMTime](cmsamplebuffergetduration(_:).md)
  Returns the total duration of a sample buffer.
- [func CMSampleBufferGetDecodeTimeStamp(CMSampleBuffer) -> CMTime](cmsamplebuffergetdecodetimestamp(_:).md)
  Returns the decode timestamp that’s the earliest numerically of all the samples in a sample buffer.
- [func CMSampleBufferGetPresentationTimeStamp(CMSampleBuffer) -> CMTime](cmsamplebuffergetpresentationtimestamp(_:).md)
  Returns the presentation timestamp that’s the earliest numerically of all the samples in a sample buffer.
- [func CMSampleBufferGetOutputDuration(CMSampleBuffer) -> CMTime](cmsamplebuffergetoutputduration(_:).md)
  Returns the output duration of a sample buffer.
- [func CMSampleBufferGetOutputDecodeTimeStamp(CMSampleBuffer) -> CMTime](cmsamplebuffergetoutputdecodetimestamp(_:).md)
  Returns the output decode timestamp of a sample buffer.
- [func CMSampleBufferGetOutputPresentationTimeStamp(CMSampleBuffer) -> CMTime](cmsamplebuffergetoutputpresentationtimestamp(_:).md)
  Returns the output presentation timestamp of a sample buffer.
- [func CMSampleBufferSetOutputPresentationTimeStamp(CMSampleBuffer, newValue: CMTime) -> OSStatus](cmsamplebuffersetoutputpresentationtimestamp(_:newvalue:).md)
  Sets an output presentation timestamp to use in place of a calculated value.
- [func CMSampleBufferGetSampleTimingInfo(CMSampleBuffer, at: CMItemIndex, timingInfoOut: UnsafeMutablePointer<CMSampleTimingInfo>) -> OSStatus](cmsamplebuffergetsampletiminginfo(_:at:timinginfoout:).md)
  Retrieves a timing information structure that describes a specified sample in a sample buffer.
- [func CMSampleBufferGetSampleTimingInfoArray(CMSampleBuffer, entryCount: CMItemCount, arrayToFill: UnsafeMutablePointer<CMSampleTimingInfo>?, entriesNeededOut: UnsafeMutablePointer<CMItemCount>?) -> OSStatus](cmsamplebuffergetsampletiminginfoarray(_:entrycount:arraytofill:entriesneededout:).md)
  Retrieves an array of sample timing information structures that represents each sample in a sample buffer.
- [func CMSampleBufferGetOutputSampleTimingInfoArray(CMSampleBuffer, entryCount: CMItemCount, arrayToFill: UnsafeMutablePointer<CMSampleTimingInfo>?, entriesNeededOut: UnsafeMutablePointer<CMItemCount>?) -> OSStatus](cmsamplebuffergetoutputsampletiminginfoarray(_:entrycount:arraytofill:entriesneededout:).md)
  Retrieves an array of output timing information structures that represents each sample in a sample buffer.
### Accessing the Format Description
- [func CMSampleBufferGetFormatDescription(CMSampleBuffer) -> CMFormatDescription?](cmsamplebuffergetformatdescription(_:).md)
  Returns the format description of the samples in a sample buffer.
### Modifying Sample Buffers
- [func CMSampleBufferGetDataBuffer(CMSampleBuffer) -> CMBlockBuffer?](cmsamplebuffergetdatabuffer(_:).md)
  Returns a block buffer that contains the media data.
- [func CMSampleBufferSetDataBuffer(CMSampleBuffer, newValue: CMBlockBuffer) -> OSStatus](cmsamplebuffersetdatabuffer(_:newvalue:).md)
  Sets a block buffer of media data on a sample buffer.
- [func CMSampleBufferGetImageBuffer(CMSampleBuffer) -> CVImageBuffer?](cmsamplebuffergetimagebuffer(_:).md)
  Returns an image buffer that contains the media data.
- [func CMSampleBufferGetAudioBufferListWithRetainedBlockBuffer(CMSampleBuffer, bufferListSizeNeededOut: UnsafeMutablePointer<Int>?, bufferListOut: UnsafeMutablePointer<AudioBufferList>?, bufferListSize: Int, blockBufferAllocator: CFAllocator?, blockBufferMemoryAllocator: CFAllocator?, flags: UInt32, blockBufferOut: UnsafeMutablePointer<CMBlockBuffer?>?) -> OSStatus](cmsamplebuffergetaudiobufferlistwithretainedblockbuffer(_:bufferlistsizeneededout:bufferlistout:bufferlistsize:blockbufferallocator:blockbuffermemoryallocator:flags:blockbufferout:).md)
  Returns an audio buffer list that contains the media data.
- [func CMSampleBufferSetDataBufferFromAudioBufferList(CMSampleBuffer, blockBufferAllocator: CFAllocator?, blockBufferMemoryAllocator: CFAllocator?, flags: UInt32, bufferList: UnsafePointer<AudioBufferList>) -> OSStatus](cmsamplebuffersetdatabufferfromaudiobufferlist(_:blockbufferallocator:blockbuffermemoryallocator:flags:bufferlist:).md)
  Creates a block buffer that contains a copy of the data from an audio buffer list.
- [func CMSampleBufferCopyPCMDataIntoAudioBufferList(CMSampleBuffer, at: Int32, frameCount: Int32, into: UnsafeMutablePointer<AudioBufferList>) -> OSStatus](cmsamplebuffercopypcmdataintoaudiobufferlist(_:at:framecount:into:).md)
  Copies PCM audio data from a sample buffer into an audio buffer list.
- [func CMSampleBufferGetAudioStreamPacketDescriptions(CMSampleBuffer, allocatedSize: Int, packetDescriptionsOut: UnsafeMutablePointer<AudioStreamPacketDescription>?, packetDescriptionsSizeNeededOut: UnsafeMutablePointer<Int>?) -> OSStatus](cmsamplebuffergetaudiostreampacketdescriptions(_:allocatedsize:packetdescriptionsout:packetdescriptionssizeneededout:).md)
  Creates an array of audio stream packet descriptions.
- [func CMSampleBufferGetAudioStreamPacketDescriptionsPtr(CMSampleBuffer, packetDescriptionsPointerOut: UnsafeMutablePointer<UnsafePointer<AudioStreamPacketDescription>?>?, sizeOut: UnsafeMutablePointer<Int>?) -> OSStatus](cmsamplebuffergetaudiostreampacketdescriptionsptr(_:packetdescriptionspointerout:sizeout:).md)
  Returns a pointer to a constant array of audio stream packet descriptions.
### Managing Attachments
- [func CMSampleBufferGetSampleAttachmentsArray(CMSampleBuffer, createIfNecessary: Bool) -> CFArray?](cmsamplebuffergetsampleattachmentsarray(_:createifnecessary:).md)
  Retrieves an array of sample attachment dictionaries that represents each sample in a sample buffer.
- [Sample Attachment Keys](sample-attachment-keys.md)
  Keys that specify attachments to individual samples in a buffer.
### Processing Samples
- [func CMSampleBufferCallBlockForEachSample(CMSampleBuffer, (CMSampleBuffer, CMItemCount) -> OSStatus) -> OSStatus](cmsamplebuffercallblockforeachsample(_:_:).md)
  Calls a block for every individual sample in a sample buffer.
- [func CMSampleBufferCallForEachSample(CMSampleBuffer, callback: (CMSampleBuffer, CMItemCount, UnsafeMutableRawPointer?) -> OSStatus, refcon: UnsafeMutableRawPointer?) -> OSStatus](cmsamplebuffercallforeachsample(_:callback:refcon:).md)
  Calls a function for every individual sample in a sample buffer.
### Accessing the Type Identifier
- [func CMSampleBufferGetTypeID() -> CFTypeID](cmsamplebuffergettypeid().md)
  Returns the type identifier of sample buffer objects.
### Data Types
- [class CMSampleBuffer](cmsamplebuffer.md)
  A reference to a buffer of media data.
- [Sample Buffer Flags](sample-buffer-flags.md)
  Flags that customize the behavior of framework operations.
- [struct CMSampleTimingInfo](cmsampletiminginfo.md)
  A collection of timing information for a sample in a sample buffer.
- [typealias CMBuffer](cmbuffer.md)
  A reference to a buffer object.
- [typealias CMBufferGetSizeCallback](cmbuffergetsizecallback.md)
  A client callback that returns a size.
- [typealias CMItemIndex](cmitemindex.md)
  A datatype that represents an item index.
- [typealias CMItemCount](cmitemcount.md)
  A datatype that represents an item count.
- [typealias CMPersistentTrackID](cmpersistenttrackid.md)
  A datatype that represents a persistent track identifier.
- [typealias CMMuxedStreamType](cmmuxedstreamtype.md)
  A datatype that represents a muxed stream of data.
### Notifications
- [Sample Buffer Notifications](sample-buffer-notifications.md)
  Notifications the system posts when processing sample buffer objects.
### Errors
- [Sample Buffer Error Codes](sample-buffer-errors.md)
  Errors that occur when processing sample buffer objects.
- [var kCMPersistentTrackID_Invalid: CMPersistentTrackID](kcmpersistenttrackid_invalid.md)
  Indicates an invalid track ID.
### Functions
- [func CMTimeFoldIntoRange(CMTime, foldRange: CMTimeRange) -> CMTime](cmtimefoldintorange(_:foldrange:).md)
  Folds a time into a time range.
- [func CMVideoFormatDescriptionGetHEVCParameterSetAtIndex(CMFormatDescription, parameterSetIndex: Int, parameterSetPointerOut: UnsafeMutablePointer<UnsafePointer<UInt8>?>?, parameterSetSizeOut: UnsafeMutablePointer<Int>?, parameterSetCountOut: UnsafeMutablePointer<Int>?, nalUnitHeaderLengthOut: UnsafeMutablePointer<Int32>?) -> OSStatus](cmvideoformatdescriptiongethevcparametersetatindex(_:parametersetindex:parametersetpointerout:parametersetsizeout:parametersetcountout:nalunitheaderlengthout:).md)
  Returns a parameter set contained in an HEVC (H.265) format description.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer-api)*