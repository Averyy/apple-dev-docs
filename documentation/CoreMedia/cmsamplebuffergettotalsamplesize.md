# CMSampleBufferGetTotalSampleSize(_:)

**Framework**: Core Media  
**Kind**: func

Returns the total size in bytes of sample data in a sample buffer.

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
func CMSampleBufferGetTotalSampleSize(_ sbuf: CMSampleBuffer) -> Int
```

#### Return Value

Total size in bytes of sample data in the `CMSampleBuffer`. If there are no sample sizes in this `CMSampleBuffer`, a size of 0 will be returned.

## Parameters

- `sbuf`: The   being interrogated.

## See Also

- [func CMSampleBufferGetNumSamples(CMSampleBuffer) -> CMItemCount](cmsamplebuffergetnumsamples(_:).md)
  Returns the number of media samples in a sample buffer.
- [func CMSampleBufferGetSampleSize(CMSampleBuffer, at: CMItemIndex) -> Int](cmsamplebuffergetsamplesize(_:at:).md)
  Returns the size in bytes of a specified sample in a sample buffer.
- [func CMSampleBufferGetSampleSizeArray(CMSampleBuffer, entryCount: CMItemCount, arrayToFill: UnsafeMutablePointer<Int>?, entriesNeededOut: UnsafeMutablePointer<CMItemCount>?) -> OSStatus](cmsamplebuffergetsamplesizearray(_:entrycount:arraytofill:entriesneededout:).md)
  Retrieves an array of sample sizes that represents each sample in a sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffergettotalsamplesize(_:))*