# CMSampleBufferCreateReady(allocator:dataBuffer:formatDescription:sampleCount:sampleTimingEntryCount:sampleTimingArray:sampleSizeEntryCount:sampleSizeArray:sampleBufferOut:)

**Framework**: Core Media  
**Kind**: func

Creates a sample buffer with media data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMSampleBufferCreateReady(allocator: CFAllocator?, dataBuffer: CMBlockBuffer?, formatDescription: CMFormatDescription?, sampleCount numSamples: CMItemCount, sampleTimingEntryCount numSampleTimingEntries: CMItemCount, sampleTimingArray: UnsafePointer<CMSampleTimingInfo>?, sampleSizeEntryCount numSampleSizeEntries: CMItemCount, sampleSizeArray: UnsafePointer<Int>?, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus
```

#### Discussion

This function is identical to [`CMSampleBufferCreate(allocator:dataBuffer:dataReady:makeDataReadyCallback:refcon:formatDescription:sampleCount:sampleTimingEntryCount:sampleTimingArray:sampleSizeEntryCount:sampleSizeArray:sampleBufferOut:)`](cmsamplebuffercreate(allocator:databuffer:dataready:makedatareadycallback:refcon:formatdescription:samplecount:sampletimingentrycount:sampletimingarray:samplesizeentrycount:samplesizearray:samplebufferout:).md) except that `dataReady` is always `true`, and so no `makeDataReadyCallback` or `refcon` needs to be passed.

## Parameters

- `allocator`: The allocator to use for allocating the `CMSampleBuffer` object. Pass `kCFAllocatorDefault` to use the default allocator.
- `dataBuffer`: `CMBlockBuffer` that already contains the media data. Must not be `NULL`.
- `formatDescription`: A description of the media data’s format. Can be `NULL`.
- `numSamples`: Number of samples in the `CMSampleBuffer`. Can be 0.
- `numSampleTimingEntries`: Number of entries in sampleTimingArray. Must be 0, 1, or `numSamples`.
- `sampleTimingArray`: Array of `CMSampleTimingInfo` structs, one struct per sample. If all samples have the same duration and are in presentation order, you can pass a single `CMSampleTimingInfo` struct with duration set to the duration of one sample, `presentationTimeStamp` set to the presentation time of the numerically earliest sample, and `decodeTimeStamp` set to `kCMTimeInvalid`. The behavior is undefined if samples in a `CMSampleBuffer` (or even in multiple buffers in the same stream) have the same `presentationTimeStamp`. Can be `NULL`.
- `numSampleSizeEntries`: Number of entries in `sampleSizeArray`. Must be 0, 1, or `numSamples`.
- `sampleSizeArray`: Array of size entries, one entry per sample. If all samples have the same size, you can pass a single size entry containing the size of one sample. Can be `NULL`. Must be `NULL` if the samples are non-contiguous in the buffer (eg. non-interleaved audio, where the channel values for a single sample are scattered through the buffer).
- `sampleBufferOut`: Returned newly created `CMSampleBuffer`.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffercreateready(allocator:databuffer:formatdescription:samplecount:sampletimingentrycount:sampletimingarray:samplesizeentrycount:samplesizearray:samplebufferout:))*