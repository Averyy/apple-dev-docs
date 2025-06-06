# CMSampleBufferCreateForImageBuffer(allocator:imageBuffer:dataReady:makeDataReadyCallback:refcon:formatDescription:sampleTiming:sampleBufferOut:)

**Framework**: Core Media  
**Kind**: func

Creates a sample buffer with an image buffer and a callback to make the data ready for use.

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
func CMSampleBufferCreateForImageBuffer(allocator: CFAllocator?, imageBuffer: CVImageBuffer, dataReady: Bool, makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback?, refcon makeDataReadyRefcon: UnsafeMutableRawPointer?, formatDescription: CMVideoFormatDescription, sampleTiming: UnsafePointer<CMSampleTimingInfo>, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus
```

#### Return Value

A result code. See [`Sample Buffer Error Codes`](sample-buffer-errors.md).

#### Discussion

Unlike a `CMBlockBuffer` which can reference many samples, a `CVImageBuffer` is defined to reference only one sample; therefore this routine has fewer parameters than `CMSampleBufferCreate`. Sample timing information, which is a vector for `CMSampleBufferCreate`, consists of only one value for this routine. The concept of sample size doesn’t apply to `CVImageBuffers`. As such, [`CMSampleBufferGetSampleSizeArray(_:entryCount:arrayToFill:entriesNeededOut:)`](cmsamplebuffergetsamplesizearray(_:entrycount:arraytofill:entriesneededout:).md) returns `kCMSampleBufferError_BufferHasNoSampleSizes`, and [`CMSampleBufferGetSampleSize(_:at:)`](cmsamplebuffergetsamplesize(_:at:).md) returns 0.

Because `CVImageBuffers` hold visual data, the format description provided is a `CMVideoFormatDescription`. The format description must be consistent with the attributes and formatting information attached to the `CVImageBuffer`. The width, height, and `codecType` must match (for `CVPixelBuffers` the codec type is given by `CVPixelBufferGetPixelFormatType`(pixelBuffer); for other `CVImageBuffers`, the codecType must be 0). The format description extensions must match the image buffer attachments for all the keys in the list returned by `CMVideoFormatDescriptionGetExtensionKeysCommonWithImageBuffers`. If absent in either they must be absent in both.

## Parameters

- `allocator`: The allocator to use for allocating the   object. Pass   to use the default allocator.
- `imageBuffer`:   for the media data. This can be a   whose content hasn’t yet been rendered, or a   that already contains the media data (in which case   should be true). May not be  .
- `dataReady`: Indicates whether or not the   already contains the media data.
- `makeDataReadyCallback`: Callback that   should call to make the data ready. Can be  .
- `makeDataReadyRefcon`: Refcon   should pass to the callback.
- `formatDescription`: A description of the media data’s format. See discussion above for constraints. May not be  .
- `sampleTiming`: A   struct that provides the timing information for the media represented by the  .
- `sampleBufferOut`: On output, points to the newly created   that contains a  .

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
- [func CMSampleBufferCreate(allocator: CFAllocator?, dataBuffer: CMBlockBuffer?, dataReady: Bool, makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback?, refcon: UnsafeMutableRawPointer?, formatDescription: CMFormatDescription?, sampleCount: CMItemCount, sampleTimingEntryCount: CMItemCount, sampleTimingArray: UnsafePointer<CMSampleTimingInfo>?, sampleSizeEntryCount: CMItemCount, sampleSizeArray: UnsafePointer<Int>?, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](cmsamplebuffercreate(allocator:databuffer:dataready:makedatareadycallback:refcon:formatdescription:samplecount:sampletimingentrycount:sampletimingarray:samplesizeentrycount:samplesizearray:samplebufferout:).md)
  Creates a sample buffer with a callback to make the data ready for use.
- [func CMAudioSampleBufferCreateWithPacketDescriptions(allocator: CFAllocator?, dataBuffer: CMBlockBuffer?, dataReady: Bool, makeDataReadyCallback: CMSampleBufferMakeDataReadyCallback?, refcon: UnsafeMutableRawPointer?, formatDescription: CMFormatDescription, sampleCount: CMItemCount, presentationTimeStamp: CMTime, packetDescriptions: UnsafePointer<AudioStreamPacketDescription>?, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](cmaudiosamplebuffercreatewithpacketdescriptions(allocator:databuffer:dataready:makedatareadycallback:refcon:formatdescription:samplecount:presentationtimestamp:packetdescriptions:samplebufferout:).md)
  Creates a sample buffer with packet descriptions and a callback to make the data ready for use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffercreateforimagebuffer(allocator:imagebuffer:dataready:makedatareadycallback:refcon:formatdescription:sampletiming:samplebufferout:))*