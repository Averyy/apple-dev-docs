# CMSampleBufferCreateCopyWithNewTiming(allocator:sampleBuffer:sampleTimingEntryCount:sampleTimingArray:sampleBufferOut:)

**Framework**: Core Media  
**Kind**: func

Creates a copy of a sample buffer with new timing information.

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
func CMSampleBufferCreateCopyWithNewTiming(allocator: CFAllocator?, sampleBuffer originalSBuf: CMSampleBuffer, sampleTimingEntryCount numSampleTimingEntries: CMItemCount, sampleTimingArray: UnsafePointer<CMSampleTimingInfo>?, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus
```

#### Return Value

A result code. See [`Sample Buffer Error Codes`](sample-buffer-errors.md).

#### Discussion

This emulates `CMSampleBufferCreateCopy`, but changes the timing. The array parameters, `sampleTimingArray`, should have only one element if that same element applies to all samples.

All parameters are copied; on return, the caller can release them, free them, or reuse them. Any `outputPresentationTimestamp` that has been set on the original buffer isn’t copied because it’s no longer relevant. On return, the caller owns the returned `CMSampleBuffer`, and must release it when done with it.

## Parameters

- `allocator`: The allocator to use for allocating the   object. Pass   to use the default allocator.
- `originalSBuf`:   containing the original samples.
- `numSampleTimingEntries`: Number of entries in  . Must be 0, 1, or the number of samples in  .
- `sampleTimingArray`: Array of   structs, one struct per sample. If all samples have the same duration and are in presentation order, you can pass a single   struct with duration set to the duration of one sample,   set to the presentation time of the numerically earliest sample, and   set to  . Behavior is undefined if samples in a   (or even in multiple buffers in the same stream) have the same  . Can be  .
- `sampleBufferOut`: On output, points to the newly created copy of  .

## See Also

- [func CMSampleBufferCreateCopy(allocator: CFAllocator?, sampleBuffer: CMSampleBuffer, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](cmsamplebuffercreatecopy(allocator:samplebuffer:samplebufferout:).md)
  Creates a copy of a sample buffer.
- [func CMSampleBufferCopySampleBufferForRange(allocator: CFAllocator?, sampleBuffer: CMSampleBuffer, sampleRange: CFRange, sampleBufferOut: UnsafeMutablePointer<CMSampleBuffer?>) -> OSStatus](cmsamplebuffercopysamplebufferforrange(allocator:samplebuffer:samplerange:samplebufferout:).md)
  Creates a sample buffer that contains a range of samples from an existing sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffercreatecopywithnewtiming(allocator:samplebuffer:sampletimingentrycount:sampletimingarray:samplebufferout:))*