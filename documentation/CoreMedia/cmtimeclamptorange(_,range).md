# CMTimeClampToRange(_:range:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns the nearest time value inside the time range.

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
func CMTimeClampToRange(_ time: CMTime, range: CMTimeRange) -> CMTime
```

```c
extern CMTime CMTimeClampToRange(CMTime time, CMTimeRange range);
```

#### Return Value

A time structure inside the time range.

#### Discussion

The function returns the times inside the range you specify unmodified. Times before the start and after the end time of the time range return the start and end time of the range. If the `CMTimeRange` argument is empty, this function returns an invalid `CMTime`. If the given `CMTime` is invalid, the function returns an invalid `CMTime`.

## Parameters

- `time`: The time to clamp.
- `range`: The time range to examine.

## See Also

### Utility Functions
- [func CMTimeMapDurationFromRangeToRange(CMTime, fromRange: CMTimeRange, toRange: CMTimeRange) -> CMTime](./cmtimemapdurationfromrangetorange%28_,fromrange,torange%29.md)
  Translates a duration through a mapping from two time ranges.
- [func CMTimeMapTimeFromRangeToRange(CMTime, fromRange: CMTimeRange, toRange: CMTimeRange) -> CMTime](./cmtimemaptimefromrangetorange%28_,fromrange,torange%29.md)
  Translates a time through a mapping from two time ranges.
- [func CMTimeRangeCopyAsDictionary(CMTimeRange, allocator: CFAllocator?) -> CFDictionary?](./cmtimerangecopyasdictionary%28_,allocator%29.md)
  Returns a dictionary representation of a time range.
- [func CMTimeRangeCopyDescription(allocator: CFAllocator?, range: CMTimeRange) -> CFString?](./cmtimerangecopydescription%28allocator,range%29.md)
  Returns a string with a description of a time range.
- [func CMTimeRangeShow(CMTimeRange)](./cmtimerangeshow%28_%29.md)
  Prints a description of the time range to standard error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimeclamptorange(_:range:))*