# CMTimeMapDurationFromRangeToRange(_:fromRange:toRange:)

**Framework**: Core Media  
**Kind**: func

Translates a duration through a mapping from two time ranges.

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
func CMTimeMapDurationFromRangeToRange(_ dur: CMTime, fromRange: CMTimeRange, toRange: CMTimeRange) -> CMTime
```

#### Return Value

A time structure that represents the translated duration.

#### Discussion

The function scales the duration in proportion to the ratio between the ranges’ durations:

```objc
result = dur*(toRange.duration/fromRange.duration)
```

If `dur` doesn’t have the epoch `0`, the function returns an invalid `CMTime`.

## Parameters

- `dur`: The duration to translate.
- `fromRange`: The time range from which the function translates the duration.
- `toRange`: The time range to which the function maps the duration.

## See Also

- [func CMTimeClampToRange(CMTime, range: CMTimeRange) -> CMTime](cmtimeclamptorange(_:range:).md)
  Returns the nearest time value inside the time range.
- [func CMTimeMapTimeFromRangeToRange(CMTime, fromRange: CMTimeRange, toRange: CMTimeRange) -> CMTime](cmtimemaptimefromrangetorange(_:fromrange:torange:).md)
  Translates a time through a mapping from two time ranges.
- [func CMTimeRangeCopyAsDictionary(CMTimeRange, allocator: CFAllocator?) -> CFDictionary?](cmtimerangecopyasdictionary(_:allocator:).md)
  Returns a dictionary representation of a time range.
- [func CMTimeRangeCopyDescription(allocator: CFAllocator?, range: CMTimeRange) -> CFString?](cmtimerangecopydescription(allocator:range:).md)
  Returns a string with a description of a time range.
- [func CMTimeRangeShow(CMTimeRange)](cmtimerangeshow(_:).md)
  Prints a description of the time range to standard error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimemapdurationfromrangetorange(_:fromrange:torange:))*