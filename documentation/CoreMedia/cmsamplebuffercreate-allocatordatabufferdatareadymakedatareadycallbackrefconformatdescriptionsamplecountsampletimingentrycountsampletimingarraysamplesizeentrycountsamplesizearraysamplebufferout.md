# CMSampleBufferCreate(allocator:dataBuffer:dataReady:makeDataReadyCallback:refcon:formatDescription:sampleCount:sampleTimingEntryCount:sampleTimingArray:sampleSizeEntryCount:sampleSizeArray:sampleBufferOut:)

**Framework**: Core Media  
**Kind**: func

Creates a sample buffer with a callback to make the data ready for use.

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
func CMSampleBufferCreate(allocator: CFAllocator?, dataBuffer: CMBlockBuffer?, dataReady: Bool, makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback?, refcon makeDataReadyRefcon: UnsafeMutableRawPointer?, formatDescription: CMFormatDescription?, sampleCount numSamples: CMItemCount, sampleTimingEntryCount numSampleTimingEntries: CMItemCount, sampleTimingArray: UnsafePointer<CMSampleTimingInfo>?, sampleSizeEntryCount numSampleSizeEntries: CMItemCount, sampleSizeArray: UnsafePointer<Int>?, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus
```

#### Return Value

A result code. See [`Sample Buffer Error Codes`](sample-buffer-errors.md).

#### Discussion

Array parameters (`sampleSizeArray`, `sampleTimingArray`) should have only one element if that same element applies to all samples. All parameters are copied. On return, the caller can release them, free them or reuse them. On return, the caller owns the returned `CMSampleBuffer`, and must release it when done with it.

Example of usage for in-display-order video frames:

- dataBuffer: contains 7 Motion JPEG frames
- dataFormatDescription: describes Motion JPEG video
- dataFormatDescription: describes Motion JPEG video
- numSamples: 7
- numSampleTimingEntries: 1
- sampleTimingArray: one entry = {duration = 1001/30000, presentationTimeStamp = 0/30000, decodeTimeStamp = invalid }
- numSampleSizeEntries: 7
- sampleSizeArray: [105840, 104456, 103464, 116460, 100412, 94808, 120400]

Example of usage for video frames in out-of-display-order :

- dataBuffer: contains 6 H.264 frames in decode order (P2,B0,B1,I5,B3,B4)
- dataFormatDescription: describes H.264 video
- numSamples: 6
- numSampleTimingEntries: 6
- sampleTimingArray: 6 entries = {
- {duration = 1001/30000, presentationTimeStamp = 12012/30000, decodeTimeStamp = 10010/30000},
- {duration = 1001/30000, presentationTimeStamp = 10010/30000, decodeTimeStamp = 11011/30000},
- {duration = 1001/30000, presentationTimeStamp = 11011/30000, decodeTimeStamp = 12012/30000},
- {duration = 1001/30000, presentationTimeStamp = 15015/30000, decodeTimeStamp = 13013/30000},
- {duration = 1001/30000, presentationTimeStamp = 13013/30000, decodeTimeStamp = 14014/30000},
- {duration = 1001/30000, presentationTimeStamp = 13013/30000, decodeTimeStamp = 14014/30000}}
- numSampleSizeEntries: 6
- sampleSizeArray: [10580, 1234, 1364, 75660, 1012, 988]

Example of usage for compressed audio:

- dataBuffer: contains 24 compressed AAC packets
- dataFormatDescription: describes 44.1kHz AAC audio
- numSamples: 24
- numSampleTimingEntries: 1
- sampleTimingArray: one entry = {{duration = 1024/44100, presentationTimeStamp = 0/44100, decodeTimeStamp = invalid }}
- numSampleSizeEntries: 24
- sampleSizeArray:[191, 183, 208, 213, 202, 206, 209, 206, 204, 192, 202, 277, 282, 240, 209, 194, 193, 197, 196, 198, 168, 199, 171, 194]

Example of usage for uncompressed interleaved audio:

- dataBuffer: contains 24000 uncompressed interleaved stereo frames, each containing 2 Float32s =
- {{L,R},
- {L,R},
- {L,R}, …}
- dataFormatDescription: describes 48kHz Float32 interleaved audio
- numSamples: 24000
- numSampleTimingEntries: 1
- sampleTimingArray: one entry = {{duration = 1/48000, presentationTimeStamp = 0/48000, decodeTimeStamp = invalid }}
- numSampleSizeEntries: 1
- sampleSizeArray: {8}

Example of usage for uncompressed non-interleaved audio:

- dataBuffer: contains 24000 uncompressed non-interleaved stereo frames, each containing 2 (non-contiguous) Float32s =
- {{L,L,L,L,L,…},
- {R,R,R,R,R,…}}
- dataFormatDescription: describes 48kHz Float32 non-interleaved audio
- numSamples: 24000
- numSampleTimingEntries: 1
- sampleTimingArray: one entry = {duration = 1/48000, presentationTimeStamp = 0/48000, decodeTimeStamp = invalid }
- numSampleSizeEntries: 0
- sampleSizeArray: `NULL` (because the samples aren’t contiguous)

## Parameters

- `allocator`: The allocator to use for allocating the   object. Pass   to use the default allocator.
- `dataBuffer`:   for the media data. This can be  , a   with no backing memory, a   with backing memory but no data yet, or a   that already contains the media data. If   contains the media data,   should be  . The Boolean   should also be   if the   is   and   is 0.
- `dataReady`: Indicates whether or not the block buffer already contains the media data.
- `makeDataReadyCallback`: Callback that   should call to make the data ready. Can be  .
- `makeDataReadyRefcon`: Refcon   should pass to the callback.
- `formatDescription`: A description of the media data’s format. Can be  .
- `numSamples`: Number of samples in the  . Can be zero.
- `numSampleTimingEntries`: Number of entries in  . Must be 0, 1, or  .
- `sampleTimingArray`: Array of   structs, one struct per sample. If all samples have the same duration and are in presentation order, you can pass a single   struct with duration set to the duration of one sample,   set to the presentation time of the numerically earliest sample, and   set to  . Behavior is undefined if samples in a   (or even in multiple buffers in the same stream) have the same  . Can be  .
- `numSampleSizeEntries`: Number of entries in  . Must be 0, 1, or  .
- `sampleSizeArray`: Array of size entries, one entry per sample. If all samples have the same size, you can pass a single size entry containing the size of one sample. Can be  . Must be   if the samples are non-contiguous in the buffer (for example, non-interleaved audio, where the channel values for a single sample are scattered through the buffer).
- `sampleBufferOut`: On output, points to the newly created  .

## Topics

### Callbacks
- [typealias CMSampleBufferMakeDataReadyCallback](cmsamplebuffermakedatareadycallback.md)
  Client callback called by [`CMSampleBufferMakeDataReady(_:)`](cmsamplebuffermakedataready(_:).md).

## See Also

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
- [func CMSampleBufferCreateForImageBuffer(allocator: CFAllocator?, imageBuffer: CVImageBuffer, dataReady: Bool, makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback?, refcon: UnsafeMutableRawPointer?, formatDescription: CMVideoFormatDescription, sampleTiming: UnsafePointer<CMSampleTimingInfo>, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](cmsamplebuffercreateforimagebuffer(allocator:imagebuffer:dataready:makedatareadycallback:refcon:formatdescription:sampletiming:samplebufferout:).md)
  Creates a sample buffer with an image buffer and a callback to make the data ready for use.
- [func CMAudioSampleBufferCreateWithPacketDescriptions(allocator: CFAllocator?, dataBuffer: CMBlockBuffer?, dataReady: Bool, makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback?, refcon: UnsafeMutableRawPointer?, formatDescription: CMFormatDescription, sampleCount: CMItemCount, presentationTimeStamp: CMTime, packetDescriptions: UnsafePointer<AudioStreamPacketDescription>?, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](cmaudiosamplebuffercreatewithpacketdescriptions(allocator:databuffer:dataready:makedatareadycallback:refcon:formatdescription:samplecount:presentationtimestamp:packetdescriptions:samplebufferout:).md)
  Creates a sample buffer with packet descriptions and a callback to make the data ready for use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffercreate(allocator:databuffer:dataready:makedatareadycallback:refcon:formatdescription:samplecount:sampletimingentrycount:sampletimingarray:samplesizeentrycount:samplesizearray:samplebufferout:))*