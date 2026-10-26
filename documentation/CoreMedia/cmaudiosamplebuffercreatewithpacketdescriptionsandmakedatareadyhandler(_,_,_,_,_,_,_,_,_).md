# CMAudioSampleBufferCreateWithPacketDescriptionsAndMakeDataReadyHandler(_:_:_:_:_:_:_:_:_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus CMAudioSampleBufferCreateWithPacketDescriptionsAndMakeDataReadyHandler(CFAllocatorRef allocator, CMBlockBufferRef dataBuffer, Boolean dataReady, CMFormatDescriptionRef formatDescription, CMItemCount numSamples, CMTime presentationTimeStamp, const AudioStreamPacketDescription *packetDescriptions, CMSampleBufferRef*sampleBufferOut, CMSampleBufferMakeDataReadyHandler makeDataReadyHandler);
```

## Parameters

- `allocator`: The allocator to use to create a sample buffer object. Pass [`kCFAllocatorDefault`](../CoreFoundation/kcfallocatordefault.md) to use the default allocator.
- `dataBuffer`: A block buffer that contains the media data. This argument can be `NULL`, such as for a block buffer that doesn’t yet have backing memory or data.
- `dataReady`: A Boolean value that indicates whether the buffer already contains the data.
- `formatDescription`: A description of the media data’s format. Must not be `NULL`.
- `numSamples`: The number of samples in the sample buffer. Must not be `0`.
- `presentationTimeStamp`: The timestamp of the first sample in the buffer. Must be a numeric [`CMTime`](./cmtime.md).
- `packetDescriptions`: An array of packet descriptions, one for each of sample. This value may `NULL` if you know the samples have a constant size and number of frames per packet.
- `sampleBufferOut`: On return, a new [`CMSampleBuffer`](./cmsamplebuffer.md) object.
- `makeDataReadyHandler`: A block for the system to call to make the data ready for use. This argument can be `NULL`.

## Topics

### Handlers
- [typealias CMSampleBufferMakeDataReadyHandler](./cmsamplebuffermakedatareadyhandler.md)
  A block the system calls to make the sample buffer ready for use.

## See Also

### Creating Sample Buffers
- [func CMSampleBufferCreateReady(allocator: CFAllocator?, dataBuffer: CMBlockBuffer?, formatDescription: CMFormatDescription?, sampleCount: CMItemCount, sampleTimingEntryCount: CMItemCount, sampleTimingArray: UnsafePointer<CMSampleTimingInfo>?, sampleSizeEntryCount: CMItemCount, sampleSizeArray: UnsafePointer<Int>?, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](./cmsamplebuffercreateready%28allocator,databuffer,formatdescription,samplecount,sampletimingentrycount,sampletimingarray,samplesizeentrycount,samplesizearray,samplebufferout%29.md)
  Creates a sample buffer with media data.
- [func CMSampleBufferCreateReadyWithImageBuffer(allocator: CFAllocator?, imageBuffer: CVImageBuffer, formatDescription: CMVideoFormatDescription, sampleTiming: UnsafePointer<CMSampleTimingInfo>, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](./cmsamplebuffercreatereadywithimagebuffer%28allocator,imagebuffer,formatdescription,sampletiming,samplebufferout%29.md)
  Creates a sample buffer with image data.
- [func CMAudioSampleBufferCreateReadyWithPacketDescriptions(allocator: CFAllocator?, dataBuffer: CMBlockBuffer, formatDescription: CMFormatDescription, sampleCount: CMItemCount, presentationTimeStamp: CMTime, packetDescriptions: UnsafePointer<AudioStreamPacketDescription>?, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](./cmaudiosamplebuffercreatereadywithpacketdescriptions%28allocator,databuffer,formatdescription,samplecount,presentationtimestamp,packetdescriptions,samplebufferout%29.md)
  Creates a sample buffer with packet descriptions.
- [func CMSampleBufferCreateWithMakeDataReadyHandler(CFAllocator?, CMBlockBuffer?, Bool, CMFormatDescription?, CMItemCount, CMItemCount, UnsafePointer<CMSampleTimingInfo>?, CMItemCount, UnsafePointer<Int>?, UnsafeMutablePointer<CMSampleBuffer?>, CMSampleBufferMakeDataReadyHandler?) -> OSStatus](./cmsamplebuffercreatewithmakedatareadyhandler%28_,_,_,_,_,_,_,_,_,_,_%29.md)
  Creates a sample buffer with a handler to make the data ready for use.
- [func CMSampleBufferCreateForImageBufferWithMakeDataReadyHandler(CFAllocator?, CVImageBuffer, Bool, CMVideoFormatDescription, UnsafePointer<CMSampleTimingInfo>, UnsafeMutablePointer<CMSampleBuffer?>, CMSampleBufferMakeDataReadyHandler?) -> OSStatus](./cmsamplebuffercreateforimagebufferwithmakedatareadyhandler%28_,_,_,_,_,_,_%29.md)
  Creates a sample buffer with an image buffer and a handler to make the data ready for use.
- [func CMSampleBufferCreate(allocator: CFAllocator?, dataBuffer: CMBlockBuffer?, dataReady: Bool, makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback?, refcon: UnsafeMutableRawPointer?, formatDescription: CMFormatDescription?, sampleCount: CMItemCount, sampleTimingEntryCount: CMItemCount, sampleTimingArray: UnsafePointer<CMSampleTimingInfo>?, sampleSizeEntryCount: CMItemCount, sampleSizeArray: UnsafePointer<Int>?, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](./cmsamplebuffercreate%28allocator,databuffer,dataready,makedatareadycallback,refcon,formatdescription,samplecount,sampletimingentrycount,sampletimingarray,samplesizeentrycount,samplesizearray,samplebufferout%29.md)
  Creates a sample buffer with a callback to make the data ready for use.
- [func CMSampleBufferCreateForImageBuffer(allocator: CFAllocator?, imageBuffer: CVImageBuffer, dataReady: Bool, makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback?, refcon: UnsafeMutableRawPointer?, formatDescription: CMVideoFormatDescription, sampleTiming: UnsafePointer<CMSampleTimingInfo>, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](./cmsamplebuffercreateforimagebuffer%28allocator,imagebuffer,dataready,makedatareadycallback,refcon,formatdescription,sampletiming,samplebufferout%29.md)
  Creates a sample buffer with an image buffer and a callback to make the data ready for use.
- [func CMAudioSampleBufferCreateWithPacketDescriptions(allocator: CFAllocator?, dataBuffer: CMBlockBuffer?, dataReady: Bool, makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback?, refcon: UnsafeMutableRawPointer?, formatDescription: CMFormatDescription, sampleCount: CMItemCount, presentationTimeStamp: CMTime, packetDescriptions: UnsafePointer<AudioStreamPacketDescription>?, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](./cmaudiosamplebuffercreatewithpacketdescriptions%28allocator,databuffer,dataready,makedatareadycallback,refcon,formatdescription,samplecount,presentationtimestamp,packetdescriptions,samplebufferout%29.md)
  Creates a sample buffer with packet descriptions and a callback to make the data ready for use.
- [CMSampleBufferCreateForTaggedBufferGroup](./cmsamplebuffercreatefortaggedbuffergroup.md)
  Creates a new sample buffer from a tagged buffer group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmaudiosamplebuffercreatewithpacketdescriptionsandmakedatareadyhandler(_:_:_:_:_:_:_:_:_:))*