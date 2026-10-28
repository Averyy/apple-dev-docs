# CMSampleBufferGetOutputPresentationTimeStamp(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns the output presentation timestamp of a sample buffer.

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
func CMSampleBufferGetOutputPresentationTimeStamp(_ sbuf: CMSampleBuffer) -> CMTime
```

```c
extern CMTime CMSampleBufferGetOutputPresentationTimeStamp(CMSampleBufferRef sbuf);
```

## Return Value

The output presentation timestamp of the `CMSampleBuffer` or `kCMTimeInvalid` if there is an error.

## Discussion

The output presentation timestamp is the time at which the decoded, trimmed, stretched, and possibly reversed samples should start being presented. If [`CMSampleBufferGetOutputPresentationTimeStamp(_:)`](./cmsamplebuffergetoutputpresentationtimestamp%28_%29.md) has been called to explicitly set the output PTS, [`CMSampleBufferGetOutputPresentationTimeStamp(_:)`](./cmsamplebuffergetoutputpresentationtimestamp%28_%29.md) returns it. If not, [`CMSampleBufferGetOutputPresentationTimeStamp(_:)`](./cmsamplebuffergetoutputpresentationtimestamp%28_%29.md) calculates its result as `(PresentationTimeStamp + TrimDurationAtStart)` unless `kCMSampleBufferAttachmentKey_Reverse` is `kCFBooleanTrue`, in which case it calculates the result as  `(PresentationTimeStamp + Duration - TrimDurationAtEnd)`. These are generally correct for un-stretched, un-shifted playback.

For general forward playback in a scaled edit, the `OutputPresentationTimeStamp` should be set to:

`((PresentationTimeStamp + TrimDurationAtStart - EditStartMediaTime) / EditSpeedMultiplier) + EditStartTrackTime`

For general reversed playback:

`((PresentationTimeStamp + Duration - TrimDurationAtEnd - EditStartMediaTime) / EditSpeedMultiplier) + EditStartTrackTime`

## Parameters

- `sbuf`: The `CMSampleBuffer` being interrogated.

## See Also

### Inspecting Duration and Timing
- [func CMSampleBufferGetDuration(CMSampleBuffer) -> CMTime](./cmsamplebuffergetduration%28_%29.md)
  Returns the total duration of a sample buffer.
- [func CMSampleBufferGetDecodeTimeStamp(CMSampleBuffer) -> CMTime](./cmsamplebuffergetdecodetimestamp%28_%29.md)
  Returns the decode timestamp that’s the earliest numerically of all the samples in a sample buffer.
- [func CMSampleBufferGetPresentationTimeStamp(CMSampleBuffer) -> CMTime](./cmsamplebuffergetpresentationtimestamp%28_%29.md)
  Returns the presentation timestamp that’s the earliest numerically of all the samples in a sample buffer.
- [func CMSampleBufferGetOutputDuration(CMSampleBuffer) -> CMTime](./cmsamplebuffergetoutputduration%28_%29.md)
  Returns the output duration of a sample buffer.
- [func CMSampleBufferGetOutputDecodeTimeStamp(CMSampleBuffer) -> CMTime](./cmsamplebuffergetoutputdecodetimestamp%28_%29.md)
  Returns the output decode timestamp of a sample buffer.
- [func CMSampleBufferSetOutputPresentationTimeStamp(CMSampleBuffer, newValue: CMTime) -> OSStatus](./cmsamplebuffersetoutputpresentationtimestamp%28_,newvalue%29.md)
  Sets an output presentation timestamp to use in place of a calculated value.
- [func CMSampleBufferGetSampleTimingInfo(CMSampleBuffer, at: CMItemIndex, timingInfoOut: UnsafeMutablePointer<CMSampleTimingInfo>) -> OSStatus](./cmsamplebuffergetsampletiminginfo%28_,at,timinginfoout%29.md)
  Retrieves a timing information structure that describes a specified sample in a sample buffer.
- [func CMSampleBufferGetSampleTimingInfoArray(CMSampleBuffer, entryCount: CMItemCount, arrayToFill: UnsafeMutablePointer<CMSampleTimingInfo>?, entriesNeededOut: UnsafeMutablePointer<CMItemCount>?) -> OSStatus](./cmsamplebuffergetsampletiminginfoarray%28_,entrycount,arraytofill,entriesneededout%29.md)
  Retrieves an array of sample timing information structures that represents each sample in a sample buffer.
- [func CMSampleBufferGetOutputSampleTimingInfoArray(CMSampleBuffer, entryCount: CMItemCount, arrayToFill: UnsafeMutablePointer<CMSampleTimingInfo>?, entriesNeededOut: UnsafeMutablePointer<CMItemCount>?) -> OSStatus](./cmsamplebuffergetoutputsampletiminginfoarray%28_,entrycount,arraytofill,entriesneededout%29.md)
  Retrieves an array of output timing information structures that represents each sample in a sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffergetoutputpresentationtimestamp(_:))*