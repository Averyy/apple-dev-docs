# CMSampleBufferGetSampleTimingInfo(_:at:timingInfoOut:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Retrieves a timing information structure that describes a specified sample in a sample buffer.

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
func CMSampleBufferGetSampleTimingInfo(_ sbuf: CMSampleBuffer, at sampleIndex: CMItemIndex, timingInfoOut: UnsafeMutablePointer<CMSampleTimingInfo>) -> OSStatus
```

```c
extern OSStatus CMSampleBufferGetSampleTimingInfo(CMSampleBufferRef sbuf, CMItemIndex sampleIndex, CMSampleTimingInfo *timingInfoOut);
```

## Return Value

A result code. See [Sample Buffer Error Codes](./sample-buffer-errors.md).

## Discussion

A sample-specific [`CMSampleTimingInfo`](./cmsampletiminginfo.md) struct will be returned with a sample-specific `presentationTimeStamp` and `decodeTimeStamp`, even if a single `CMSampleTimingInfo` struct was used during creation to describe all the samples in the buffer. The timing info struct must be allocated by the caller. If the sample index isn’t in the range 0…numSamples-1, [`CMSampleBuffer`](./cmsamplebuffer.md) will be returned. If there’s no `timingInfo` in this `CMSampleBuffer`, [`CMSampleBuffer`](./cmsamplebuffer.md) will be returned.

## Parameters

- `sbuf`: The `CMSampleBuffer` being interrogated.
- `sampleIndex`: Sample index (0 is the first sample in `sbuf`).
- `timingInfoOut`: On output, points to a single `CMSampleTimingInfo` struct to receive the timing info.

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
- [func CMSampleBufferGetOutputPresentationTimeStamp(CMSampleBuffer) -> CMTime](./cmsamplebuffergetoutputpresentationtimestamp%28_%29.md)
  Returns the output presentation timestamp of a sample buffer.
- [func CMSampleBufferSetOutputPresentationTimeStamp(CMSampleBuffer, newValue: CMTime) -> OSStatus](./cmsamplebuffersetoutputpresentationtimestamp%28_,newvalue%29.md)
  Sets an output presentation timestamp to use in place of a calculated value.
- [func CMSampleBufferGetSampleTimingInfoArray(CMSampleBuffer, entryCount: CMItemCount, arrayToFill: UnsafeMutablePointer<CMSampleTimingInfo>?, entriesNeededOut: UnsafeMutablePointer<CMItemCount>?) -> OSStatus](./cmsamplebuffergetsampletiminginfoarray%28_,entrycount,arraytofill,entriesneededout%29.md)
  Retrieves an array of sample timing information structures that represents each sample in a sample buffer.
- [func CMSampleBufferGetOutputSampleTimingInfoArray(CMSampleBuffer, entryCount: CMItemCount, arrayToFill: UnsafeMutablePointer<CMSampleTimingInfo>?, entriesNeededOut: UnsafeMutablePointer<CMItemCount>?) -> OSStatus](./cmsamplebuffergetoutputsampletiminginfoarray%28_,entrycount,arraytofill,entriesneededout%29.md)
  Retrieves an array of output timing information structures that represents each sample in a sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffergetsampletiminginfo(_:at:timinginfoout:))*