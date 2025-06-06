# CMSampleBufferGetDuration(_:)

**Framework**: Core Media  
**Kind**: func

Returns the total duration of a sample buffer.

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
func CMSampleBufferGetDuration(_ sbuf: CMSampleBuffer) -> CMTime
```

#### Return Value

The duration of the `CMSampleBuffer` or `kCMTimeInvalid` if there is an error.

#### Discussion

If the buffer contains out-of-presentation-order samples, any gaps in the presentation timeline aren’t represented in the returned duration. The returned duration is the sum of all the individual sample durations.

## Parameters

- `sbuf`: The   being interrogated .

## See Also

- [func CMSampleBufferGetDecodeTimeStamp(CMSampleBuffer) -> CMTime](cmsamplebuffergetdecodetimestamp(_:).md)
  Returns the decode timestamp that’s the earliest numerically of all the samples in a sample buffer.
- [func CMSampleBufferGetPresentationTimeStamp(CMSampleBuffer) -> CMTime](cmsamplebuffergetpresentationtimestamp(_:).md)
  Returns the presentation timestamp that’s the earliest numerically of all the samples in a sample buffer.
- [func CMSampleBufferGetOutputDuration(CMSampleBuffer) -> CMTime](cmsamplebuffergetoutputduration(_:).md)
  Returns the output duration of a sample buffer.
- [func CMSampleBufferGetOutputDecodeTimeStamp(CMSampleBuffer) -> CMTime](cmsamplebuffergetoutputdecodetimestamp(_:).md)
  Returns the output decode timestamp of a sample buffer.
- [func CMSampleBufferGetOutputPresentationTimeStamp(CMSampleBuffer) -> CMTime](cmsamplebuffergetoutputpresentationtimestamp(_:).md)
  Returns the output presentation timestamp of a sample buffer.
- [func CMSampleBufferSetOutputPresentationTimeStamp(CMSampleBuffer, newValue: CMTime) -> OSStatus](cmsamplebuffersetoutputpresentationtimestamp(_:newvalue:).md)
  Sets an output presentation timestamp to use in place of a calculated value.
- [func CMSampleBufferGetSampleTimingInfo(CMSampleBuffer, at: CMItemIndex, timingInfoOut: UnsafeMutablePointer<CMSampleTimingInfo>) -> OSStatus](cmsamplebuffergetsampletiminginfo(_:at:timinginfoout:).md)
  Retrieves a timing information structure that describes a specified sample in a sample buffer.
- [func CMSampleBufferGetSampleTimingInfoArray(CMSampleBuffer, entryCount: CMItemCount, arrayToFill: UnsafeMutablePointer<CMSampleTimingInfo>?, entriesNeededOut: UnsafeMutablePointer<CMItemCount>?) -> OSStatus](cmsamplebuffergetsampletiminginfoarray(_:entrycount:arraytofill:entriesneededout:).md)
  Retrieves an array of sample timing information structures that represents each sample in a sample buffer.
- [func CMSampleBufferGetOutputSampleTimingInfoArray(CMSampleBuffer, entryCount: CMItemCount, arrayToFill: UnsafeMutablePointer<CMSampleTimingInfo>?, entriesNeededOut: UnsafeMutablePointer<CMItemCount>?) -> OSStatus](cmsamplebuffergetoutputsampletiminginfoarray(_:entrycount:arraytofill:entriesneededout:).md)
  Retrieves an array of output timing information structures that represents each sample in a sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffergetduration(_:))*