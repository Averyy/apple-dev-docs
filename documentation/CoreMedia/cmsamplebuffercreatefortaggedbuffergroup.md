# CMSampleBufferCreateForTaggedBufferGroup

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a new sample buffer from a tagged buffer group.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```c
extern OSStatus CMSampleBufferCreateForTaggedBufferGroup(CFAllocatorRef allocator, CMTaggedBufferGroupRef taggedBufferGroup, CMTime sbufPTS, CMTime sbufDuration, CMTaggedBufferGroupFormatDescriptionRef formatDescription, CMSampleBufferRef*sBufOut);
```

#### Return Value

Returns `0` on success and a value from [Sample Buffer Error Codes](./sample-buffer-errors.md) on failure.

## Parameters

- `allocator`: The allocator to use for the new tag collection. Pass `kCFAllocatorDefault` to use the default global allocator.
- `taggedBufferGroup`: The tagged buffer group to create a new sample buffer from.
- `sbufPTS`: The presentation time, in seconds, for the sample buffer.
- `sbufDuration`: The duration, in seconds, of the sample buffer.
- `formatDescription`: The format description for the tagged buffer group.
- `sBufOut`: The output destination for the new sample buffer.

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
- [func CMAudioSampleBufferCreateWithPacketDescriptionsAndMakeDataReadyHandler(CFAllocator?, CMBlockBuffer?, Bool, CMFormatDescription, CMItemCount, CMTime, UnsafePointer<AudioStreamPacketDescription>?, UnsafeMutablePointer<CMSampleBuffer?>, CMSampleBufferMakeDataReadyHandler?) -> OSStatus](./cmaudiosamplebuffercreatewithpacketdescriptionsandmakedatareadyhandler%28_,_,_,_,_,_,_,_,_%29.md)
  Creates a sample buffer with packet descriptions and a handler to make the data ready for use.
- [func CMSampleBufferCreate(allocator: CFAllocator?, dataBuffer: CMBlockBuffer?, dataReady: Bool, makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback?, refcon: UnsafeMutableRawPointer?, formatDescription: CMFormatDescription?, sampleCount: CMItemCount, sampleTimingEntryCount: CMItemCount, sampleTimingArray: UnsafePointer<CMSampleTimingInfo>?, sampleSizeEntryCount: CMItemCount, sampleSizeArray: UnsafePointer<Int>?, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](./cmsamplebuffercreate%28allocator,databuffer,dataready,makedatareadycallback,refcon,formatdescription,samplecount,sampletimingentrycount,sampletimingarray,samplesizeentrycount,samplesizearray,samplebufferout%29.md)
  Creates a sample buffer with a callback to make the data ready for use.
- [func CMSampleBufferCreateForImageBuffer(allocator: CFAllocator?, imageBuffer: CVImageBuffer, dataReady: Bool, makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback?, refcon: UnsafeMutableRawPointer?, formatDescription: CMVideoFormatDescription, sampleTiming: UnsafePointer<CMSampleTimingInfo>, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](./cmsamplebuffercreateforimagebuffer%28allocator,imagebuffer,dataready,makedatareadycallback,refcon,formatdescription,sampletiming,samplebufferout%29.md)
  Creates a sample buffer with an image buffer and a callback to make the data ready for use.
- [func CMAudioSampleBufferCreateWithPacketDescriptions(allocator: CFAllocator?, dataBuffer: CMBlockBuffer?, dataReady: Bool, makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback?, refcon: UnsafeMutableRawPointer?, formatDescription: CMFormatDescription, sampleCount: CMItemCount, presentationTimeStamp: CMTime, packetDescriptions: UnsafePointer<AudioStreamPacketDescription>?, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](./cmaudiosamplebuffercreatewithpacketdescriptions%28allocator,databuffer,dataready,makedatareadycallback,refcon,formatdescription,samplecount,presentationtimestamp,packetdescriptions,samplebufferout%29.md)
  Creates a sample buffer with packet descriptions and a callback to make the data ready for use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffercreatefortaggedbuffergroup)*