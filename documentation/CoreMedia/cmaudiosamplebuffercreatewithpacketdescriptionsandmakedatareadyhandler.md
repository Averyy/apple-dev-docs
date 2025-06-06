# CMAudioSampleBufferCreateWithPacketDescriptionsAndMakeDataReadyHandler(_:_:_:_:_:_:_:_:_:)

**Framework**: Core Media  
**Kind**: func

Creates a sample buffer with packet descriptions and a handler to make the data ready for use.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 13.1+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMAudioSampleBufferCreateWithPacketDescriptionsAndMakeDataReadyHandler(_ allocator: CFAllocator?, _ dataBuffer: CMBlockBuffer?, _ dataReady: Bool, _ formatDescription: CMFormatDescription, _ numSamples: CMItemCount, _ presentationTimeStamp: CMTime, _ packetDescriptions: UnsafePointer<AudioStreamPacketDescription>?, _ sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>, _ makeDataReadyHandler: CMSampleBufferMakeDataReadyHandler?) -> OSStatus
```

## Parameters

- `allocator`: The allocator to use to create a sample buffer object. Pass   to use the default allocator.
- `dataBuffer`: A block buffer that contains the media data. This argument can be  , such as for a block buffer that doesn’t yet have backing memory or data.
- `dataReady`: A Boolean value that indicates whether the buffer already contains the data.
- `formatDescription`: A description of the media data’s format. Must not be  .
- `numSamples`: The number of samples in the sample buffer. Must not be  .
- `presentationTimeStamp`: The timestamp of the first sample in the buffer. Must be a numeric  .
- `packetDescriptions`: An array of packet descriptions, one for each of sample. This value may   if you know the samples have a constant size and number of frames per packet.
- `sampleBufferOut`: On return, a new   object.
- `makeDataReadyHandler`: A block for the system to call to make the data ready for use. This argument can be  .

## Topics

### Handlers
- [typealias CMSampleBufferMakeDataReadyHandler](cmsamplebuffermakedatareadyhandler.md)
  A block the system calls to make the sample buffer ready for use.

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
- [func CMSampleBufferCreate(allocator: CFAllocator?, dataBuffer: CMBlockBuffer?, dataReady: Bool, makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback?, refcon: UnsafeMutableRawPointer?, formatDescription: CMFormatDescription?, sampleCount: CMItemCount, sampleTimingEntryCount: CMItemCount, sampleTimingArray: UnsafePointer<CMSampleTimingInfo>?, sampleSizeEntryCount: CMItemCount, sampleSizeArray: UnsafePointer<Int>?, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](cmsamplebuffercreate(allocator:databuffer:dataready:makedatareadycallback:refcon:formatdescription:samplecount:sampletimingentrycount:sampletimingarray:samplesizeentrycount:samplesizearray:samplebufferout:).md)
  Creates a sample buffer with a callback to make the data ready for use.
- [func CMSampleBufferCreateForImageBuffer(allocator: CFAllocator?, imageBuffer: CVImageBuffer, dataReady: Bool, makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback?, refcon: UnsafeMutableRawPointer?, formatDescription: CMVideoFormatDescription, sampleTiming: UnsafePointer<CMSampleTimingInfo>, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](cmsamplebuffercreateforimagebuffer(allocator:imagebuffer:dataready:makedatareadycallback:refcon:formatdescription:sampletiming:samplebufferout:).md)
  Creates a sample buffer with an image buffer and a callback to make the data ready for use.
- [func CMAudioSampleBufferCreateWithPacketDescriptions(allocator: CFAllocator?, dataBuffer: CMBlockBuffer?, dataReady: Bool, makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback?, refcon: UnsafeMutableRawPointer?, formatDescription: CMFormatDescription, sampleCount: CMItemCount, presentationTimeStamp: CMTime, packetDescriptions: UnsafePointer<AudioStreamPacketDescription>?, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](cmaudiosamplebuffercreatewithpacketdescriptions(allocator:databuffer:dataready:makedatareadycallback:refcon:formatdescription:samplecount:presentationtimestamp:packetdescriptions:samplebufferout:).md)
  Creates a sample buffer with packet descriptions and a callback to make the data ready for use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmaudiosamplebuffercreatewithpacketdescriptionsandmakedatareadyhandler(_:_:_:_:_:_:_:_:_:))*