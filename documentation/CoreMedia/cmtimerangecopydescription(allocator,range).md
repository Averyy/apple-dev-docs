# CMTimeRangeCopyDescription(allocator:range:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

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

```c
extern CFStringRefCMTimeRangeCopyDescription(CFAllocatorRef allocator, CMTimeRange range);
```

#### Return Value

A string description.

#### Discussion

You use this from within `CFShow` on an object that contains `CMTimeRange` fields. It is also useful from other client debugging code.  The caller owns the `CFString` this function returns and is responsible for releasing it. Pass `kCFAllocatorDefault` to use the default allocator.

## Parameters

- `allocator`: The allocator the function uses when allocating memory for the description.
- `range`: The time range to describe.

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
- [func CMTimeRangeShow(CMTimeRange)](./cmtimerangeshow%28_%29.md)
  Prints a description of the time range to standard error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerangecopydescription(allocator:range:))*