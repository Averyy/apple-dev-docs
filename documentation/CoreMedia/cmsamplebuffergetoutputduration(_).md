# CMSampleBufferGetOutputDuration(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns the output duration of a sample buffer.

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
func CMSampleBufferGetOutputDuration(_ sbuf: CMSampleBuffer) -> CMTime
```

```c
extern CMTime CMSampleBufferGetOutputDuration(CMSampleBufferRef sbuf);
```

## Return Value

The output duration of the `CMSampleBuffer` or `kCMTimeInvalid` if there is an error.

## Discussion

The output duration is the duration minus any trimmed duration, all divided by the speed multiplier:

`(Duration - TrimDurationAtStart - TrimDurationAtEnd) / SpeedMultiplier`

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
- [func CMSampleBufferGetOutputDecodeTimeStamp(CMSampleBuffer) -> CMTime](./cmsamplebuffergetoutputdecodetimestamp%28_%29.md)
  Returns the output decode timestamp of a sample buffer.
- [func CMSampleBufferGetOutputPresentationTimeStamp(CMSampleBuffer) -> CMTime](./cmsamplebuffergetoutputpresentationtimestamp%28_%29.md)
  Returns the output presentation timestamp of a sample buffer.
- [func CMSampleBufferSetOutputPresentationTimeStamp(CMSampleBuffer, newValue: CMTime) -> OSStatus](./cmsamplebuffersetoutputpresentationtimestamp%28_,newvalue%29.md)
  Sets an output presentation timestamp to use in place of a calculated value.
- [func CMSampleBufferGetSampleTimingInfo(CMSampleBuffer, at: CMItemIndex, timingInfoOut: UnsafeMutablePointer<CMSampleTimingInfo>) -> OSStatus](./cmsamplebuffergetsampletiminginfo%28_,at,timinginfoout%29.md)
  Retrieves a timing information structure that describes a specified sample in a sample buffer.
- [func CMSampleBufferGetSampleTimingInfoArray(CMSampleBuffer, entryCount: CMItemCount, arrayToFill: UnsafeMutablePointer<CMSampleTimingInfo>?, entriesNeededOut: UnsafeMutablePointer<CMItemCount>?) -> OSStatus](./cmsamplebuffergetsampletiminginfoarray%28_,entrycount,arraytofill,entriesneededout%29.md)
  Retrieves an array of sample timing information structures that represents each sample in a sample buffer.
- [func CMSampleBufferGetOutputSampleTimingInfoArray(CMSampleBuffer, entryCount: CMItemCount, arrayToFill: UnsafeMutablePointer<CMSampleTimingInfo>?, entriesNeededOut: UnsafeMutablePointer<CMItemCount>?) -> OSStatus](./cmsamplebuffergetoutputsampletiminginfoarray%28_,entrycount,arraytofill,entriesneededout%29.md)
  Retrieves an array of output timing information structures that represents each sample in a sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffergetoutputduration(_:))*