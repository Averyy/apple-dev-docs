# CMSampleBufferGetSampleSize(_:at:)

**Framework**: Core Media  
**Kind**: func

Returns the size in bytes of a specified sample in a sample buffer.

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
func CMSampleBufferGetSampleSize(_ sbuf: CMSampleBuffer, at sampleIndex: CMItemIndex) -> Int
```

#### Return Value

The size in bytes of the specified sample in the sample buffer. If the sample index is not in the range 0 to `numSamples`-1, a size of 0 will be returned.If there are no sample sizes in this sample buffer, a size of 0 will be returned.This will be true, for example, if the samples in the buffer are non-contiguous (eg. non-interleaved audio, where the channel values for a single sample are scattered through the buffer), or if this sample buffer contains a `CVImageBuffer`.

## Parameters

- `sbuf`: The sample buffer to inspect.
- `sampleIndex`: The zero-based sample index.

## See Also

- [func CMSampleBufferGetNumSamples(CMSampleBuffer) -> CMItemCount](cmsamplebuffergetnumsamples(_:).md)
  Returns the number of media samples in a sample buffer.
- [func CMSampleBufferGetTotalSampleSize(CMSampleBuffer) -> Int](cmsamplebuffergettotalsamplesize(_:).md)
  Returns the total size in bytes of sample data in a sample buffer.
- [func CMSampleBufferGetSampleSizeArray(CMSampleBuffer, entryCount: CMItemCount, arrayToFill: UnsafeMutablePointer<Int>?, entriesNeededOut: UnsafeMutablePointer<CMItemCount>?) -> OSStatus](cmsamplebuffergetsamplesizearray(_:entrycount:arraytofill:entriesneededout:).md)
  Retrieves an array of sample sizes that represents each sample in a sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffergetsamplesize(_:at:))*