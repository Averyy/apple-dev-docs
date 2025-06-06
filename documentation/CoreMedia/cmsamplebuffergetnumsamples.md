# CMSampleBufferGetNumSamples(_:)

**Framework**: Core Media  
**Kind**: func

Returns the number of media samples in a sample buffer.

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
func CMSampleBufferGetNumSamples(_ sbuf: CMSampleBuffer) -> CMItemCount
```

#### Return Value

The number of media samples in the `CMSampleBuffer`. 0 is returned if there is an error.

## Parameters

- `sbuf`: The   being interrogated.

## See Also

- [func CMSampleBufferGetTotalSampleSize(CMSampleBuffer) -> Int](cmsamplebuffergettotalsamplesize(_:).md)
  Returns the total size in bytes of sample data in a sample buffer.
- [func CMSampleBufferGetSampleSize(CMSampleBuffer, at: CMItemIndex) -> Int](cmsamplebuffergetsamplesize(_:at:).md)
  Returns the size in bytes of a specified sample in a sample buffer.
- [func CMSampleBufferGetSampleSizeArray(CMSampleBuffer, entryCount: CMItemCount, arrayToFill: UnsafeMutablePointer<Int>?, entriesNeededOut: UnsafeMutablePointer<CMItemCount>?) -> OSStatus](cmsamplebuffergetsamplesizearray(_:entrycount:arraytofill:entriesneededout:).md)
  Retrieves an array of sample sizes that represents each sample in a sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffergetnumsamples(_:))*