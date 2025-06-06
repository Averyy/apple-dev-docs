# CMTimeRangeCopyDescription(allocator:range:)

**Framework**: Core Media  
**Kind**: func

Returns a string with a description of a time range.

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
func CMTimeRangeCopyDescription(allocator: CFAllocator?, range: CMTimeRange) -> CFString?
```

#### Return Value

A string description.

#### Discussion

You use this from within `CFShow` on an object that contains `CMTimeRange` fields. It is also useful from other client debugging code.  The caller owns the `CFString` this function returns and is responsible for releasing it. Pass `kCFAllocatorDefault` to use the default allocator.

## Parameters

- `allocator`: The allocator the function uses when allocating memory for the description.
- `range`: The time range to describe.

## See Also

- [func CMTimeClampToRange(CMTime, range: CMTimeRange) -> CMTime](cmtimeclamptorange(_:range:).md)
  Returns the nearest time value inside the time range.
- [func CMTimeMapDurationFromRangeToRange(CMTime, fromRange: CMTimeRange, toRange: CMTimeRange) -> CMTime](cmtimemapdurationfromrangetorange(_:fromrange:torange:).md)
  Translates a duration through a mapping from two time ranges.
- [func CMTimeMapTimeFromRangeToRange(CMTime, fromRange: CMTimeRange, toRange: CMTimeRange) -> CMTime](cmtimemaptimefromrangetorange(_:fromrange:torange:).md)
  Translates a time through a mapping from two time ranges.
- [func CMTimeRangeCopyAsDictionary(CMTimeRange, allocator: CFAllocator?) -> CFDictionary?](cmtimerangecopyasdictionary(_:allocator:).md)
  Returns a dictionary representation of a time range.
- [func CMTimeRangeShow(CMTimeRange)](cmtimerangeshow(_:).md)
  Prints a description of the time range to standard error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerangecopydescription(allocator:range:))*