# CMTimeMapTimeFromRangeToRange(_:fromRange:toRange:)

**Framework**: Core Media  
**Kind**: func

Translates a time through a mapping from two time ranges.

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
func CMTimeMapTimeFromRangeToRange(_ t: CMTime, fromRange: CMTimeRange, toRange: CMTimeRange) -> CMTime
```

#### Return Value

A time structure that represents the translated time.

#### Discussion

The start and end time of `fromRange` maps to the start and end time of `toRange` respectively. The function maps other times linearly using the formula:

```objc
result = (t-fromRange.start)*(toRange.duration/fromRange.duration)+toRange.start
```

If either `CMTimeRange` argument is empty, the function returns an invalid `CMTime`. If `t` doesn’t have the same epoch as `fromRange.start`, the function returns an invalid `CMTime`. If both `fromRange` and `toRange` have duration `kCMTimePositiveInfinity`, the function offsets `t` relative to the differences between their starts, but not scaled.

## Parameters

- `t`: The time value to translate.
- `fromRange`: The time range from which the function translates the time range.
- `toRange`: The time range to which the function maps the time value.

## See Also

- [func CMTimeClampToRange(CMTime, range: CMTimeRange) -> CMTime](cmtimeclamptorange(_:range:).md)
  Returns the nearest time value inside the time range.
- [func CMTimeMapDurationFromRangeToRange(CMTime, fromRange: CMTimeRange, toRange: CMTimeRange) -> CMTime](cmtimemapdurationfromrangetorange(_:fromrange:torange:).md)
  Translates a duration through a mapping from two time ranges.
- [func CMTimeRangeCopyAsDictionary(CMTimeRange, allocator: CFAllocator?) -> CFDictionary?](cmtimerangecopyasdictionary(_:allocator:).md)
  Returns a dictionary representation of a time range.
- [func CMTimeRangeCopyDescription(allocator: CFAllocator?, range: CMTimeRange) -> CFString?](cmtimerangecopydescription(allocator:range:).md)
  Returns a string with a description of a time range.
- [func CMTimeRangeShow(CMTimeRange)](cmtimerangeshow(_:).md)
  Prints a description of the time range to standard error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimemaptimefromrangetorange(_:fromrange:torange:))*