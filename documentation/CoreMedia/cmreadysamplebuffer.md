# CMReadySampleBuffer

**Framework**: Core Media  
**Kind**: struct

Buffer carrying readily available samples of media data.

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
struct CMReadySampleBuffer<Content> where Content : CMSampleBuffer.Content
```

## Topics

### Initializers
- [init(CMReadySampleBuffer<some CMSampleBuffer.Content>)](cmreadysamplebuffer/init(_:)-35rzo.md)
  Convert a ready sample buffer to dynamic content.
- [init?(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>)](cmreadysamplebuffer/init(_:)-3rj25.md)
  Converts dynamic sample buffer to a marker sample buffer.
- [init?(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>)](cmreadysamplebuffer/init(_:)-3tjyq.md)
  Converts dynamic sample buffer to a sample buffer containing pixel buffer.
- [init?(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>)](cmreadysamplebuffer/init(_:)-4j97d.md)
  Converts dynamic sample buffer to a sample buffer containing data buffer.
- [init?(CMReadySampleBuffer<CMSampleBuffer.DynamicContent>)](cmreadysamplebuffer/init(_:)-6uyu8.md)
  Converts dynamic sample buffer to a sample buffer containing tagged buffers.
- [init(audioDataBuffer: Content, formatDescription: CMAudioFormatDescription, sampleCount: Int, presentationTimeStamp: CMTime)](cmreadysamplebuffer/init(audiodatabuffer:formatdescription:samplecount:presentationtimestamp:).md)
  Creates a sample buffer carrying audio media data.
- [init(compressedAudioDataBuffer: Content, formatDescription: CMAudioFormatDescription, presentationTimeStamp: CMTime, packetDescriptions: [AudioStreamPacketDescription])](cmreadysamplebuffer/init(compressedaudiodatabuffer:formatdescription:presentationtimestamp:packetdescriptions:).md)
  Creates a sample buffer carrying compressed audio media data.
- [init(dataBuffer: Content, formatDescription: CMFormatDescription, sampleProperties: CMSampleBuffer.SamplePropertiesCollection)](cmreadysamplebuffer/init(databuffer:formatdescription:sampleproperties:).md)
  Creates a sample buffer with media data.
- [init(markerAt: CMTime, duration: CMTime)](cmreadysamplebuffer/init(markerat:duration:).md)
  Creates a marker-only sample buffer with no payload and no format description.
- [init(pixelBuffer: Content, formatDescription: CMVideoFormatDescription?, presentationTimeStamp: CMTime, duration: CMTime)](cmreadysamplebuffer/init(pixelbuffer:formatdescription:presentationtimestamp:duration:).md)
  Creates a sample buffer carrying image buffer.
- [init(sampleDataReference: Content, formatDescription: CMFormatDescription, sampleProperties: CMSampleBuffer.SamplePropertiesCollection)](cmreadysamplebuffer/init(sampledatareference:formatdescription:sampleproperties:).md)
  Creates a sample buffer with references to sample data.
- [init(taggedBuffers: Content, formatDescription: CMTaggedBufferGroupFormatDescription?, presentationTimeStamp: CMTime, duration: CMTime)](cmreadysamplebuffer/init(taggedbuffers:formatdescription:presentationtimestamp:duration:).md)
  Creates a sample buffer carrying tagged buffers.
- [init(unsafeBuffer: sending CMSampleBuffer)](cmreadysamplebuffer/init(unsafebuffer:).md)
  Create a ready sample buffer with dynamic content from an existing sample buffer.
- [init(unsafeMarkerOnlySampleBuffer: sending CMSampleBuffer)](cmreadysamplebuffer/init(unsafemarkeronlysamplebuffer:).md)
  Create a ready sample buffer with marker content from an existing sample buffer.
- [init(unsafeSampleDataReferenceBuffer: sending CMSampleBuffer)](cmreadysamplebuffer/init(unsafesampledatareferencebuffer:).md)
  Create a ready sample buffer with data reference content from an existing sample buffer.
- [init(unsafeWithDataBuffer: sending CMSampleBuffer)](cmreadysamplebuffer/init(unsafewithdatabuffer:).md)
  Creates a ready sample buffer with data buffer content from an existing sample buffer.
- [init(unsafeWithPixelBuffer: sending CMSampleBuffer)](cmreadysamplebuffer/init(unsafewithpixelbuffer:).md)
  Creates a ready sample buffer with pixel buffer content from an existing sample buffer.
- [init(unsafeWithTaggedBuffers: sending CMSampleBuffer)](cmreadysamplebuffer/init(unsafewithtaggedbuffers:).md)
  Create a ready sample buffer with tagged buffers content from an existing sample buffer.
### Instance Properties
- [var audioStreamPacketDescriptions: [AudioStreamPacketDescription]?](cmreadysamplebuffer/audiostreampacketdescriptions.md)
  Get an array of AudioStreamPacketDescriptions describing audio samples in the buffer.
- [var content: CMSampleBuffer.DynamicContent](cmreadysamplebuffer/content-14qb7.md)
  Payload containing the samples.
- [var content: CVReadOnlyPixelBuffer](cmreadysamplebuffer/content-4peot.md)
  Payload containing the samples.
- [var content: Array<CMTaggedDynamicBuffer>](cmreadysamplebuffer/content-5fko2.md)
  Payload containing the samples.
- [var content: CMReadOnlyDataBlockBuffer](cmreadysamplebuffer/content-6ihvr.md)
  Payload containing the samples.
- [var contentType: CMSampleBuffer.ContentType](cmreadysamplebuffer/contenttype.md)
  Type of the content carried by this sample buffer
- [var decodeTimeStamp: CMTime](cmreadysamplebuffer/decodetimestamp.md)
  Numerically earliest sample decode timestamp in the sample buffer.
- [var duration: CMTime](cmreadysamplebuffer/duration-2ssr4.md)
  The unmodified sum of the durations of all samples in the sample buffer.
- [var duration: CMTime](cmreadysamplebuffer/duration-54778.md)
  Duration of the sample buffer.
- [var duration: CMTime](cmreadysamplebuffer/duration-94fnq.md)
  Duration of the sample buffer.
- [var duration: CMTime](cmreadysamplebuffer/duration-9lx3g.md)
  Duration of the sample buffer.
- [var formatDescription: CMFormatDescription](cmreadysamplebuffer/formatdescription-6rp0o.md)
  The format description of the samples in the sample buffer.
- [var formatDescription: CMFormatDescription?](cmreadysamplebuffer/formatdescription-9i48t.md)
  The format description of the samples in the sample buffer.
- [var markerTimeStamp: CMTime](cmreadysamplebuffer/markertimestamp.md)
  Presentation timestamp of the sample buffer.
- [var outputDecodeTimeStamp: CMTime](cmreadysamplebuffer/outputdecodetimestamp.md)
  The output decode timestamp of the sample buffer.
- [var outputDuration: CMTime](cmreadysamplebuffer/outputduration.md)
  The output duration of the sample buffer.
- [var outputPresentationTimeStamp: CMTime](cmreadysamplebuffer/outputpresentationtimestamp.md)
  The output presentation timestamp of the sample buffer.
- [var outputSampleTimings: CMSampleBuffer.TimingPerSample?](cmreadysamplebuffer/outputsampletimings.md)
  Output timing information of each sample in the sample buffer.
- [var presentationTimeStamp: CMTime](cmreadysamplebuffer/presentationtimestamp-19vwq.md)
  Presentation timestamp of the sample buffer.
- [var presentationTimeStamp: CMTime](cmreadysamplebuffer/presentationtimestamp-266ka.md)
  Presentation timestamp of the sample buffer.
- [var presentationTimeStamp: CMTime](cmreadysamplebuffer/presentationtimestamp-7ea7z.md)
  Numerically earliest sample presentation timestamp in the sample buffer.
- [var sampleAttachments: CMSampleBuffer.SampleAttachments](cmreadysamplebuffer/sampleattachments-8g6nm.md)
  Attachments for the sample in this buffer.
- [var sampleAttachments: CMSampleBuffer.SampleAttachments](cmreadysamplebuffer/sampleattachments-9g3d5.md)
  Attachments for the sample in this buffer.
- [var sampleCount: Int](cmreadysamplebuffer/samplecount.md)
  Number of samples in the sample buffer.
- [var sampleProperties: CMSampleBuffer.SamplePropertiesCollection](cmreadysamplebuffer/sampleproperties.md)
  Information about the samples in the sample buffer.
- [var totalSampleSize: Int](cmreadysamplebuffer/totalsamplesize.md)
  Total size in bytes of all samples in the sample buffer.
### Instance Methods
- [func attach(contentKey: AVContentKey) throws](cmreadysamplebuffer/attach(contentkey:).md)
  Attaches an AVContentKey to a CMReadySampleBuffer for the purpose of content decryption. The client is expected to attach AVContentKeys to CMReadySampleBuffers that have been created by the client for enqueueing with AVSampleBufferDisplayLayer or AVSampleBufferAudioRenderer, for which the AVContentKeySpecifier matches indications of suitability that are available to the client according to the content key system that’s in use.
- [func copyPCMData(fromRange: Range<Int>, into: UnsafeMutablePointer<AudioBufferList>) throws](cmreadysamplebuffer/copypcmdata(fromrange:into:).md)
  Copies PCM audio data from the sample buffer into a pre-allocated `AudioBufferList`.
- [func splitSamples() -> [CMReadySampleBuffer<Content>]](cmreadysamplebuffer/splitsamples.md)
  Split sample buffer into a smaller representation, ideally carrying a single sample per resulting sample buffer.
- [func withUnsafeSampleBuffer<R>((CMSampleBuffer) throws -> sending R) rethrows -> sending R](cmreadysamplebuffer/withunsafesamplebuffer(_:).md)
  Access the underlying CMSampleBuffer instance.

## Relationships

### Conforms To
- [AVAssetReaderOutput.SupportedPayload](../AVFoundation/AVAssetReaderOutput/SupportedPayload.md)
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadysamplebuffer)*