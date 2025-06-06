# CMSampleBufferSetOutputPresentationTimeStamp(_:newValue:)

**Framework**: Core Media  
**Kind**: func

Sets an output presentation timestamp to use in place of a calculated value.

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
func CMSampleBufferSetOutputPresentationTimeStamp(_ sbuf: CMSampleBuffer, newValue outputPresentationTimeStamp: CMTime) -> OSStatus
```

#### Return Value

A result code. See [`Sample Buffer Error Codes`](sample-buffer-errors.md).

#### Discussion

The output presentation timestamp is the time at which the decoded, trimmed, stretched and possibly reversed samples should commence being presented. By default, this is calculated by calling `CMSampleBufferGetOutputPresentationTimeStamp`. Call `CMSampleBufferSetOutputPresentationTimeStamp` to explicitly set the value for `CMSampleBufferGetOutputPresentationTimeStamp` to return.

For general forward playback in a scaled edit, the OutputPresentationTimeStamp should be set to:

`((PresentationTimeStamp + TrimDurationAtStart - EditStartMediaTime) / EditSpeedMultiplier) + EditStartTrackTime.`

For general reversed playback `OutputPresentationTimeStamp` should be set to:

`((PresentationTimeStamp + Duration - TrimDurationAtEnd - EditStartMediaTime) / EditSpeedMultiplier) + EditStartTrackTime`.

## Parameters

- `sbuf`: The sample buffer being interrogated
- `outputPresentationTimeStamp`: New value for  . Pass   to go back to the default calculation.

## See Also

- [func CMSampleBufferGetDuration(CMSampleBuffer) -> CMTime](cmsamplebuffergetduration(_:).md)
  Returns the total duration of a sample buffer.
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
- [func CMSampleBufferGetSampleTimingInfo(CMSampleBuffer, at: CMItemIndex, timingInfoOut: UnsafeMutablePointer<CMSampleTimingInfo>) -> OSStatus](cmsamplebuffergetsampletiminginfo(_:at:timinginfoout:).md)
  Retrieves a timing information structure that describes a specified sample in a sample buffer.
- [func CMSampleBufferGetSampleTimingInfoArray(CMSampleBuffer, entryCount: CMItemCount, arrayToFill: UnsafeMutablePointer<CMSampleTimingInfo>?, entriesNeededOut: UnsafeMutablePointer<CMItemCount>?) -> OSStatus](cmsamplebuffergetsampletiminginfoarray(_:entrycount:arraytofill:entriesneededout:).md)
  Retrieves an array of sample timing information structures that represents each sample in a sample buffer.
- [func CMSampleBufferGetOutputSampleTimingInfoArray(CMSampleBuffer, entryCount: CMItemCount, arrayToFill: UnsafeMutablePointer<CMSampleTimingInfo>?, entriesNeededOut: UnsafeMutablePointer<CMItemCount>?) -> OSStatus](cmsamplebuffergetoutputsampletiminginfoarray(_:entrycount:arraytofill:entriesneededout:).md)
  Retrieves an array of output timing information structures that represents each sample in a sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffersetoutputpresentationtimestamp(_:newvalue:))*