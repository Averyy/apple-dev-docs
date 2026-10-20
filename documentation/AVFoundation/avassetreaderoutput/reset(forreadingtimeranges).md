# reset(forReadingTimeRanges:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Restarts reading with a new set of time ranges.

**Availability**:
- iOS 8.0+ - Deprecated in 27.0
- iPadOS 8.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use RandomAccessController.resetForReading(timeRanges:) instead

## Declaration

```swift
func reset(forReadingTimeRanges timeRanges: [NSValue])
```

```objc
- (void) resetForReadingTimeRanges:(NSArray<NSValue *> *) timeRanges;
```

#### Discussion

You may only call this method if the value of the [`supportsRandomAccess`](./supportsrandomaccess.md) property is [`true`](../../Swift/true.md). You can’t call it after invoking [`markConfigurationAsFinal()`](./markconfigurationasfinal%28%29.md).

A typical time to call this method is when performing multi-pass encoding using an instance of [`AVAssetWriter`](../avassetwriter.md). In this case, call the [`copyNextSampleBuffer()`](./copynextsamplebuffer%28%29.md) method until it returns `nil`, and then ask the asset writer’s input for a set of time ranges to reencode. You pass the time ranges to this method to prepare the output for the next pass.

The time ranges that you set here override the value of the asset reader’s [`timeRange`](../avassetreader/timerange.md) property. If the start times of the time range in the array don’t strictly increase, or if two or more time ranges in the array overlap, the system throws an exception. It’s an error to include a time range with a nonnumeric start time or duration, unless the duration is [`positiveInfinity`](../../CoreMedia/cmtime/positiveinfinity.md).

If you call this method while the asset reader is in an [`AVAssetReader.Status.failed`](../avassetreader/status-swift.enum/failed.md) or [`AVAssetReader.Status.cancelled`](../avassetreader/status-swift.enum/cancelled.md) state, its [`status`](../avassetreader/status-swift.property.md) property value doesn’t change, and the result of the next call to [`copyNextSampleBuffer()`](./copynextsamplebuffer%28%29.md) is `nil`.

If you call this method while there’s still media data to read, the system throws an exception. You can only call it after the asset reader starts reading.

## Parameters

- `timeRanges`: An array of [`NSValue`](../../Foundation/nsvalue.md) objects, each representing a single [`CMTimeRange`](../../CoreMedia/cmtimerange.md) structure.

## See Also

### Configuring reading
- [var alwaysCopiesSampleData: Bool](./alwayscopiessampledata.md)
  A Boolean value that indicates whether the output vends copied sample data.
- [var supportsRandomAccess: Bool](./supportsrandomaccess.md)
  A Boolean value that indicates whether the output supports reconfiguring the time ranges it reads.
- [func markConfigurationAsFinal()](./markconfigurationasfinal%28%29.md)
  Tells the output that it’s finished reconfiguring time ranges, and allows the asset reader to advance to a completed state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/reset(forreadingtimeranges:))*