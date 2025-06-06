# CMSampleBufferGetOutputSampleTimingInfoArray(_:entryCount:arrayToFill:entriesNeededOut:)

**Framework**: Core Media  
**Kind**: func

Retrieves an array of output timing information structures that represents each sample in a sample buffer.

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
func CMSampleBufferGetOutputSampleTimingInfoArray(_ sbuf: CMSampleBuffer, entryCount timingArrayEntries: CMItemCount, arrayToFill timingArrayOut: UnsafeMutablePointer<CMSampleTimingInfo>?, entriesNeededOut timingArrayEntriesNeededOut: UnsafeMutablePointer<CMItemCount>?) -> OSStatus
```

#### Return Value

A result code. See [`Sample Buffer Error Codes`](sample-buffer-errors.md).

#### Discussion

If only one [`CMSampleTimingInfo`](cmsampletiminginfo.md) struct is returned, it applies to all samples in the buffer.See documentation of [`CMSampleTimingInfo`](cmsampletiminginfo.md) for details of how a single `CMSampleTimingInfo` struct can apply to multiple samples. The `timingArrayOut` must be allocated by the caller, and the number of entries allocated must be passed in `timingArrayEntries`. If `timingArrayOut` is `NULL`, `timingArrayEntriesNeededOut` will return the required number of entries. Similarly, if `*timingArrayEntriesNeededOut` is too small, [`CMSampleBuffer`](cmsamplebuffer.md) will be returned, and `timingArrayEntriesNeededOut` will return the required number of entries. In either case, the caller can then make an appropriately-sized `timingArrayOut` and call again. For example, the caller might pass the address of a `CMSampleTimingInfo` struct on the stack (as timingArrayOut), and 1 as `timingArrayEntries`. If all samples are describable with a single `CMSampleTimingInfo` struct (or there’s only one sample in the `CMSampleBuffer`), this call will succeed. If not, it will fail, and will return the number of entries required in `timingArrayEntriesNeededOut`. Only in this case will the caller actually need to allocate an array. If there’s no timingInfo in this `CMSampleBuffer`, [`CMSampleBuffer`](cmsamplebuffer.md) will be returned, and `*timingArrayEntriesNeededOut` will be set to 0.

## Parameters

- `sbuf`: The   being interrogated.
- `timingArrayEntries`: Number of entries in timing array.
- `timingArrayOut`: On output, points to an array of   structs to receive the timing info.
- `timingArrayEntriesNeededOut`: Number of entries needed for the result.

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
- [func CMSampleBufferSetOutputPresentationTimeStamp(CMSampleBuffer, newValue: CMTime) -> OSStatus](cmsamplebuffersetoutputpresentationtimestamp(_:newvalue:).md)
  Sets an output presentation timestamp to use in place of a calculated value.
- [func CMSampleBufferGetSampleTimingInfo(CMSampleBuffer, at: CMItemIndex, timingInfoOut: UnsafeMutablePointer<CMSampleTimingInfo>) -> OSStatus](cmsamplebuffergetsampletiminginfo(_:at:timinginfoout:).md)
  Retrieves a timing information structure that describes a specified sample in a sample buffer.
- [func CMSampleBufferGetSampleTimingInfoArray(CMSampleBuffer, entryCount: CMItemCount, arrayToFill: UnsafeMutablePointer<CMSampleTimingInfo>?, entriesNeededOut: UnsafeMutablePointer<CMItemCount>?) -> OSStatus](cmsamplebuffergetsampletiminginfoarray(_:entrycount:arraytofill:entriesneededout:).md)
  Retrieves an array of sample timing information structures that represents each sample in a sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffergetoutputsampletiminginfoarray(_:entrycount:arraytofill:entriesneededout:))*