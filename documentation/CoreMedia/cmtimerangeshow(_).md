# CMTimeRangeShow(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Prints a description of the time range to standard error.

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
func CMTimeRangeShow(_ range: CMTimeRange)
```

```c
extern void CMTimeRangeShow(CMTimeRange range);
```

## Discussion

This is most useful from within LLDB.

## Parameters

- `range`: The time range to print.

## See Also

### Utility Functions
- [func CMTimeClampToRange(CMTime, range: CMTimeRange) -> CMTime](./cmtimeclamptorange%28_,range%29.md)
  Returns the nearest time value inside the time range.
- [func CMTimeMapDurationFromRangeToRange(CMTime, fromRange: CMTimeRange, toRange: CMTimeRange) -> CMTime](./cmtimemapdurationfromrangetorange%28_,fromrange,torange%29.md)
  Translates a duration through a mapping from two time ranges.
- [func CMTimeMapTimeFromRangeToRange(CMTime, fromRange: CMTimeRange, toRange: CMTimeRange) -> CMTime](./cmtimemaptimefromrangetorange%28_,fromrange,torange%29.md)
  Translates a time through a mapping from two time ranges.
- [func CMTimeRangeCopyAsDictionary(CMTimeRange, allocator: CFAllocator?) -> CFDictionary?](./cmtimerangecopyasdictionary%28_,allocator%29.md)
  Returns a dictionary representation of a time range.
- [func CMTimeRangeCopyDescription(allocator: CFAllocator?, range: CMTimeRange) -> CFString?](./cmtimerangecopydescription%28allocator,range%29.md)
  Returns a string with a description of a time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerangeshow(_:))*