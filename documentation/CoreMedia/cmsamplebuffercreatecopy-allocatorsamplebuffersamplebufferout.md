# CMSampleBufferCreateCopy(allocator:sampleBuffer:sampleBufferOut:)

**Framework**: Core Media  
**Kind**: func

Creates a copy of a sample buffer.

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
func CMSampleBufferCreateCopy(allocator: CFAllocator?, sampleBuffer sbuf: CMSampleBuffer, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus
```

#### Return Value

A result code. See [`Sample Buffer Error Codes`](sample-buffer-errors.md).

#### Discussion

The copy is shallow: scalar properties (sizes and timing) are copied directly, the data buffer and format description are retained, and the attachments that can be propagated are retained by the copy’s dictionary. If `sbuf’s` data isn’t ready, the copy will be set to track its readiness.

## Parameters

- `allocator`: The allocator to use for allocating the   object. Pass   to use the default allocator.
- `sbuf`:   being copied.
- `sampleBufferOut`: On output, points to the newly created copy of  .

## See Also

- [func CMSampleBufferCreateCopyWithNewTiming(allocator: CFAllocator?, sampleBuffer: CMSampleBuffer, sampleTimingEntryCount: CMItemCount, sampleTimingArray: UnsafePointer<CMSampleTimingInfo>?, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](cmsamplebuffercreatecopywithnewtiming(allocator:samplebuffer:sampletimingentrycount:sampletimingarray:samplebufferout:).md)
  Creates a copy of a sample buffer with new timing information.
- [func CMSampleBufferCopySampleBufferForRange(allocator: CFAllocator?, sampleBuffer: CMSampleBuffer, sampleRange: CFRange, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](cmsamplebuffercopysamplebufferforrange(allocator:samplebuffer:samplerange:samplebufferout:).md)
  Creates a sample buffer that contains a range of samples from an existing sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffercreatecopy(allocator:samplebuffer:samplebufferout:))*