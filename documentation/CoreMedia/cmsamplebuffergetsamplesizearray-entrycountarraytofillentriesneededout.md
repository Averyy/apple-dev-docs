# CMSampleBufferGetSampleSizeArray(_:entryCount:arrayToFill:entriesNeededOut:)

**Framework**: Core Media  
**Kind**: func

Retrieves an array of sample sizes that represents each sample in a sample buffer.

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
func CMSampleBufferGetSampleSizeArray(_ sbuf: CMSampleBuffer, entryCount sizeArrayEntries: CMItemCount, arrayToFill sizeArrayOut: UnsafeMutablePointer<Int>?, entriesNeededOut sizeArrayEntriesNeededOut: UnsafeMutablePointer<CMItemCount>?) -> OSStatus
```

#### Return Value

A result code. See [`Sample Buffer Error Codes`](sample-buffer-errors.md).

#### Discussion

If only one size entry is returned, all samples in the buffer are of this size. The `sizeArrayOut` must be allocated by the caller, and the number of entries allocated must be passed in `sizeArrayEntries`. If `sizeArrayOut` is NULL, sizeArrayEntriesNeededOut will return the required number of entries. Similarly, if `sizeArrayEntries` is too small, [`CMSampleBuffer`](cmsamplebuffer.md) will be returned, and `sizeArrayEntriesNeededOut` will return the required number of entries. The caller can then make an appropriately-sized `sizeArrayOut` and call again. For example, the caller might pass the address of a `size_t` variable on the stack (as sizeArrayOut), and 1 as `sizeArrayEntries`. If all samples are the same size (or there’s only one sample in the `CMSampleBuffer`), this call would succeed. If not, it will fail, and will return the number of entries required in `sizeArrayEntriesNeededOut`. Only in this case (multiple samples of different sizes) will the caller need to allocate an array. 0 entries will be returned if the samples in the buffer are non-contiguous (for example, non-interleaved audio, where the channel values for a single sample are scattered through the buffer). If there are no sample sizes in this `CMSampleBuffer`, [`CMSampleBuffer`](cmsamplebuffer.md) will be returned, and `*sizeArrayEntriesNeededOut` will be set to 0. This will be true, for example, if the samples in the buffer are non-contiguous (for example, non-interleaved audio, where the channel values for a single sample are scattered through the buffer), or if this `CMSampleBuffer` contains a `CVImageBuffer`.

## Parameters

- `sbuf`: The   being interrogated.
- `sizeArrayEntries`: Number of entries in  .
- `sizeArrayOut`: Reference to an array of   values to receive the sample sizes.
- `sizeArrayEntriesNeededOut`: Number of entries needed for the result.

## See Also

- [func CMSampleBufferGetNumSamples(CMSampleBuffer) -> CMItemCount](cmsamplebuffergetnumsamples(_:).md)
  Returns the number of media samples in a sample buffer.
- [func CMSampleBufferGetTotalSampleSize(CMSampleBuffer) -> Int](cmsamplebuffergettotalsamplesize(_:).md)
  Returns the total size in bytes of sample data in a sample buffer.
- [func CMSampleBufferGetSampleSize(CMSampleBuffer, at: CMItemIndex) -> Int](cmsamplebuffergetsamplesize(_:at:).md)
  Returns the size in bytes of a specified sample in a sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffergetsamplesizearray(_:entrycount:arraytofill:entriesneededout:))*