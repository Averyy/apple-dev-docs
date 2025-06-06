# CMSampleBufferCopySampleBufferForRange(allocator:sampleBuffer:sampleRange:sampleBufferOut:)

**Framework**: Core Media  
**Kind**: func

Creates a sample buffer that contains a range of samples from an existing sample buffer.

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
func CMSampleBufferCopySampleBufferForRange(allocator: CFAllocator?, sampleBuffer sbuf: CMSampleBuffer, sampleRange: CFRange, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus
```

#### Return Value

A result code. See [`Sample Buffer Error Codes`](sample-buffer-errors.md).

#### Discussion

> **Note**:  Samples containing non-interleaved audio aren’t supported.

 Samples containing non-interleaved audio aren’t supported.

## Parameters

- `allocator`: The allocator to use for allocating the   object. Pass   to use the default allocator.
- `sbuf`: The sample buffer containing the original samples.
- `sampleRange`: The range of samples to copy from  , where sample 0 is the first sample in the  .``
- `sampleBufferOut`: On output, points to the newly created  .

## See Also

- [func CMSampleBufferCreateCopy(allocator: CFAllocator?, sampleBuffer: CMSampleBuffer, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](cmsamplebuffercreatecopy(allocator:samplebuffer:samplebufferout:).md)
  Creates a copy of a sample buffer.
- [func CMSampleBufferCreateCopyWithNewTiming(allocator: CFAllocator?, sampleBuffer: CMSampleBuffer, sampleTimingEntryCount: CMItemCount, sampleTimingArray: UnsafePointer<CMSampleTimingInfo>?, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](cmsamplebuffercreatecopywithnewtiming(allocator:samplebuffer:sampletimingentrycount:sampletimingarray:samplebufferout:).md)
  Creates a copy of a sample buffer with new timing information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffercopysamplebufferforrange(allocator:samplebuffer:samplerange:samplebufferout:))*