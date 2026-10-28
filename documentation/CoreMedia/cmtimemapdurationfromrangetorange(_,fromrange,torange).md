# CMTimeMapDurationFromRangeToRange(_:fromRange:toRange:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

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

```c
extern CMTime CMTimeMapDurationFromRangeToRange(CMTime dur, CMTimeRange fromRange, CMTimeRange toRange);
```

## Return Value

A time structure that represents the translated duration.

## Discussion

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

### Utility Functions
- [func CMTimeClampToRange(CMTime, range: CMTimeRange) -> CMTime](./cmtimeclamptorange%28_,range%29.md)
  Returns the nearest time value inside the time range.
- [func CMTimeMapTimeFromRangeToRange(CMTime, fromRange: CMTimeRange, toRange: CMTimeRange) -> CMTime](./cmtimemaptimefromrangetorange%28_,fromrange,torange%29.md)
  Translates a time through a mapping from two time ranges.
- [func CMTimeRangeCopyAsDictionary(CMTimeRange, allocator: CFAllocator?) -> CFDictionary?](./cmtimerangecopyasdictionary%28_,allocator%29.md)
  Returns a dictionary representation of a time range.
- [func CMTimeRangeCopyDescription(allocator: CFAllocator?, range: CMTimeRange) -> CFString?](./cmtimerangecopydescription%28allocator,range%29.md)
  Returns a string with a description of a time range.
- [func CMTimeRangeShow(CMTimeRange)](./cmtimerangeshow%28_%29.md)
  Prints a description of the time range to standard error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimemapdurationfromrangetorange(_:fromrange:torange:))*