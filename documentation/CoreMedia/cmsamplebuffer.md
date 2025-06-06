# CMSampleBuffer

**Framework**: Core Media  
**Kind**: class

A reference to a buffer of media data.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class CMSampleBuffer
```

#### Overview

A sample buffer is a Core Foundation object that contains zero or more media samples of a particular type (audio, video, muxed, and so on).

## Topics

### Determining Readiness
- [var dataReadiness: CMSampleBuffer.DataReadiness](cmsamplebuffer/datareadiness-swift.property.md)
  A value that indicates the status of the data the sample buffer contains.
- [func setDataReadiness(CMSampleBuffer.DataReadiness) throws](cmsamplebuffer/setdatareadiness(_:).md)
  Sets the status of the sample buffer’s data.
- [CMSampleBuffer.DataReadiness](cmsamplebuffer/datareadiness-swift.enum.md)
  Constants that indicate the readiness of a sample buffer’s data.
- [func makeDataReady() throws](cmsamplebuffer/makedataready.md)
  Makes the sample buffer’s data ready for use by calling its handler closure.
- [func trackDataReadiness(CMSampleBuffer) throws](cmsamplebuffer/trackdatareadiness(_:).md)
  Associates a sample buffer’s data readiness with that of another sample buffer.
### Invalidating Sample Buffers
- [var isValid: Bool](cmsamplebuffer/isvalid.md)
  A Boolean value that indicates whether the sample buffer is valid.
- [func setInvalidateHandler((CMSampleBuffer) throws -> Void) throws](cmsamplebuffer/setinvalidatehandler(_:).md)
  Sets a closure for the sample buffer to call when it’s invalidated.
- [func invalidate() throws](cmsamplebuffer/invalidate.md)
  Invalidates a sample buffer by calling its invalidation handler.
### Inspecting Size Information
- [var numSamples: Int](cmsamplebuffer/numsamples.md)
  The number of media samples the buffer contains.
- [func sampleSizes() throws -> [Int]](cmsamplebuffer/samplesizes.md)
  Retrieves an array of sample sizes that represents each sample in a sample buffer.
- [func sampleSize(at: Int) -> Int](cmsamplebuffer/samplesize(at:).md)
  Returns the size of a sample in bytes.
- [var totalSampleSize: Int](cmsamplebuffer/totalsamplesize.md)
  The total size in bytes of sample data in the buffer.
### Inspecting Duration and Timing
- [var duration: CMTime](cmsamplebuffer/duration.md)
  The total duration of a sample buffer.
- [var decodeTimeStamp: CMTime](cmsamplebuffer/decodetimestamp.md)
  The decode timestamp of the first sample in the buffer.
- [var presentationTimeStamp: CMTime](cmsamplebuffer/presentationtimestamp.md)
  The sample presentation timestamp that’s the earliest numerically in the sample buffer.
- [var outputDuration: CMTime](cmsamplebuffer/outputduration.md)
  The output duration of the sample buffer.
- [var outputDecodeTimeStamp: CMTime](cmsamplebuffer/outputdecodetimestamp.md)
  The output decode timestamp for a sample buffer.
- [var outputPresentationTimeStamp: CMTime](cmsamplebuffer/outputpresentationtimestamp.md)
  The output presentation timestamp of a sample buffer.
- [func setOutputPresentationTimeStamp(CMTime) throws](cmsamplebuffer/setoutputpresentationtimestamp(_:).md)
  Sets an output presentation timestamp to use in place of a calculated value.
- [func sampleTimingInfos() throws -> [CMSampleTimingInfo]](cmsamplebuffer/sampletiminginfos.md)
  Retrieves an array of sample timing information structures that represents each sample in a sample buffer.
- [func sampleTimingInfo(at: CMItemIndex) throws -> CMSampleTimingInfo](cmsamplebuffer/sampletiminginfo(at:).md)
  Returns sample timing information for a sample at the specified index.
- [func outputSampleTimingInfos() throws -> [CMSampleTimingInfo]](cmsamplebuffer/outputsampletiminginfos.md)
  Retrieves an array of output sample timing information structures that represents each sample in a sample buffer.
### Accessing the Format Description
- [var formatDescription: CMFormatDescription?](cmsamplebuffer/formatdescription.md)
  An object that describes the details of the media data.
### Modifying Sample Buffers
- [var dataBuffer: CMBlockBuffer?](cmsamplebuffer/databuffer.md)
  A block buffer that contains the media data.
- [func setDataBuffer(CMBlockBuffer) throws](cmsamplebuffer/setdatabuffer(_:).md)
  Associates a block buffer of media data with a sample buffer.
- [var imageBuffer: CVImageBuffer?](cmsamplebuffer/imagebuffer.md)
  An image buffer that contains the media data.
- [func withAudioBufferList<R>(blockBufferMemoryAllocator: CFAllocator?, flags: CMSampleBuffer.Flags, body: (UnsafeMutableAudioBufferListPointer, CMBlockBuffer) throws -> R) throws -> R](cmsamplebuffer/withaudiobufferlist(blockbuffermemoryallocator:flags:body:).md)
  Calls a closure with an audio buffer list that contains the data from a sample buffer and a block buffer backing the audio buffers.
- [func setDataBuffer(fromAudioBufferList: UnsafePointer<AudioBufferList>, blockBufferMemoryAllocator: CFAllocator?, flags: CMSampleBuffer.Flags) throws](cmsamplebuffer/setdatabuffer(fromaudiobufferlist:blockbuffermemoryallocator:flags:).md)
  Creates a block buffer that contains a copy of the data from an audio buffer list, and sets it as the sample buffer’s data.
- [func copyPCMData(fromRange: Range<Int>, into: UnsafeMutablePointer<AudioBufferList>) throws](cmsamplebuffer/copypcmdata(fromrange:into:).md)
  Copies PCM audio data from a sample buffer into a prepopulated audio buffer list.
- [func audioStreamPacketDescriptions() throws -> [AudioStreamPacketDescription]](cmsamplebuffer/audiostreampacketdescriptions.md)
  Creates an array of audio stream packet descriptions for the variable bytes per packet or variable frames per packet audio data in a sample buffer.
- [func withUnsafeAudioStreamPacketDescriptions<R>((UnsafeBufferPointer<AudioStreamPacketDescription>) throws -> R) throws -> R](cmsamplebuffer/withunsafeaudiostreampacketdescriptions(_:).md)
  Calls a closure with an audio stream packet description.
- [func singleSampleBuffers() throws -> CMSampleBuffer.SingleSampleBuffers](cmsamplebuffer/singlesamplebuffers.md)
  Returns all samples in a sample buffer.
- [CMSampleBuffer.SingleSampleBuffers](cmsamplebuffer/singlesamplebuffers.md)
  A structure that holds all samples in a sample buffer.
### Managing Attachments
- [CMSampleBuffer.AttachmentKey](cmsamplebuffer/attachmentkey.md)
  Keys that identify sample buffer attachments.
- [var sampleAttachments: CMSampleBuffer.SampleAttachmentsArray](cmsamplebuffer/sampleattachments.md)
  An array of sample attachments.
- [CMSampleBuffer.SampleAttachmentsArray](cmsamplebuffer/sampleattachmentsarray.md)
  A structure that defines an array of sample attachments.
- [CMSampleBuffer.PerSampleAttachmentsDictionary](cmsamplebuffer/persampleattachmentsdictionary.md)
  A structure that defines keys to identify per-sample attachments.
### Accessing the Type Identifier
- [static var typeID: CFTypeID](cmsamplebuffer/typeid.md)
  Returns the type identifier of sample buffer objects.
### Accessing Tagged Buffers
- [var taggedBuffers: [CMTaggedBuffer]?](cmsamplebuffer/taggedbuffers.md)
  Returns the tagged buffers associated with this buffer.
### Constants
- [CMSampleBuffer.Error](cmsamplebuffer/error.md)
  A structure that defines errors that occur during framework operations.
- [CMSampleBuffer.Flags](cmsamplebuffer/flags.md)
  Flags that customize the behavior of framework operations.
- [CMSampleBuffer.NotificationKey](cmsamplebuffer/notificationkey.md)
  A key for sample buffer notifications.
### Notifications
- [static let dataBecameReady: NSNotification.Name](cmsamplebuffer/databecameready.md)
  A notification the system posts when a sample buffer’s data becomes ready.
- [static let dataFailed: NSNotification.Name](cmsamplebuffer/datafailed.md)
  A notification the system posts when a sample buffer fails to load its data.

## Relationships

### Conforms To
- [CMAttachmentBearerProtocol](cmattachmentbearerprotocol.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer)*