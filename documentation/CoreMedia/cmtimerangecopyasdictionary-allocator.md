# CMTimeRangeCopyAsDictionary(_:allocator:)

**Framework**: Core Media  
**Kind**: func

Returns a dictionary representation of a time range.

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
func CMTimeRangeCopyAsDictionary(_ range: CMTimeRange, allocator: CFAllocator?) -> CFDictionary?
```

#### Return Value

A dictionary that represents the time range.

#### Discussion

This is useful when putting `CMTimeRanges` in Core Foundation container types. Pass `kCFAllocatorDefault` to use the default allocator.

For keys in the dictionary, see [`Dictionary Keys`](cmtimerange-dictionary-keys.md).

## Parameters

- `range`: The time range from which to create a dictionary.
- `allocator`: The allocator with which to create a dictionary.

## See Also

- [func CMTimeClampToRange(CMTime, range: CMTimeRange) -> CMTime](cmtimeclamptorange(_:range:).md)
  Returns the nearest time value inside the time range.
- [func CMTimeMapDurationFromRangeToRange(CMTime, fromRange: CMTimeRange, toRange: CMTimeRange) -> CMTime](cmtimemapdurationfromrangetorange(_:fromrange:torange:).md)
  Translates a duration through a mapping from two time ranges.
- [func CMTimeMapTimeFromRangeToRange(CMTime, fromRange: CMTimeRange, toRange: CMTimeRange) -> CMTime](cmtimemaptimefromrangetorange(_:fromrange:torange:).md)
  Translates a time through a mapping from two time ranges.
- [func CMTimeRangeCopyDescription(allocator: CFAllocator?, range: CMTimeRange) -> CFString?](cmtimerangecopydescription(allocator:range:).md)
  Returns a string with a description of a time range.
- [func CMTimeRangeShow(CMTimeRange)](cmtimerangeshow(_:).md)
  Prints a description of the time range to standard error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerangecopyasdictionary(_:allocator:))*