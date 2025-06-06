# CMTimeRangeShow(_:)

**Framework**: Core Media  
**Kind**: func

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

#### Discussion

This is most useful from within LLDB.

## Parameters

- `range`: The time range to print.

## See Also

- [func CMTimeClampToRange(CMTime, range: CMTimeRange) -> CMTime](cmtimeclamptorange(_:range:).md)
  Returns the nearest time value inside the time range.
- [func CMTimeMapDurationFromRangeToRange(CMTime, fromRange: CMTimeRange, toRange: CMTimeRange) -> CMTime](cmtimemapdurationfromrangetorange(_:fromrange:torange:).md)
  Translates a duration through a mapping from two time ranges.
- [func CMTimeMapTimeFromRangeToRange(CMTime, fromRange: CMTimeRange, toRange: CMTimeRange) -> CMTime](cmtimemaptimefromrangetorange(_:fromrange:torange:).md)
  Translates a time through a mapping from two time ranges.
- [func CMTimeRangeCopyAsDictionary(CMTimeRange, allocator: CFAllocator?) -> CFDictionary?](cmtimerangecopyasdictionary(_:allocator:).md)
  Returns a dictionary representation of a time range.
- [func CMTimeRangeCopyDescription(allocator: CFAllocator?, range: CMTimeRange) -> CFString?](cmtimerangecopydescription(allocator:range:).md)
  Returns a string with a description of a time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerangeshow(_:))*