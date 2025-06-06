# CMTimeRange APIs

**Framework**: Core Media

A structure that represents a range of time.

#### Overview

This document describes the API for creating and manipulating `CMTimeRange` structures.

The system represents a `CMTimeRange` as a non-opaque, mutable structure by using two [`CMTime`](cmtime.md) values that specify the start time and duration of the range. A time range doesn’t include the end time because you calculate it by adding the duration to the start time.

```objc
// An expression that evaluates to false.
CMTimeRangeContainsTime(range, CMTimeRangeGetEnd(range))
```

Convert `CMTimeRanges` to and from `CFDictionaries` (see [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary)) using [`CMTimeRangeCopyAsDictionary(_:allocator:)`](cmtimerangecopyasdictionary(_:allocator:).md) and [`CMTimeRangeMakeFromDictionary(_:)`](cmtimerangemakefromdictionary(_:).md) to use in annotations and various Core Foundation containers.

The epoch in a `CMTime` that represents a duration must be `0`, and the value must be nonnegative. The epoch in a `CMTime` that represents a timestamp can be nonzero, but functions (such as [`CMTimeRangeGetUnion(_:otherRange:)`](cmtimerangegetunion(_:otherrange:).md)) can only perform operations on ranges whose start fields have the same epoch. `CMTimeRanges` can’t span different epochs.

For information about additional functions for managing dates and times, see [`Time Utilities`](https://developer.apple.com/documentation/CoreFoundation/time-utilities).

## Topics

### Creating Time Ranges
- [func CMTimeRangeMake(start: CMTime, duration: CMTime) -> CMTimeRange](cmtimerangemake(start:duration:).md)
  Creates a valid time range with a start time and duration.
- [func CMTimeRangeMakeFromDictionary(CFDictionary) -> CMTimeRange](cmtimerangemakefromdictionary(_:).md)
  Creates a time range from a dictionary representation of its fields.
- [func CMTimeRangeFromTimeToTime(start: CMTime, end: CMTime) -> CMTimeRange](cmtimerangefromtimetotime(start:end:).md)
  Creates a valid time range from a start and end time.
### Comparing Time Ranges
- [func CMTimeRangeEqual(CMTimeRange, CMTimeRange) -> Bool](cmtimerangeequal(_:_:).md)
  Returns a Boolean value that indicates whether two time ranges are equal.
- [func CMTimeRangeContainsTime(CMTimeRange, time: CMTime) -> Bool](cmtimerangecontainstime(_:time:).md)
  Returns a Boolean value that indicates whether a time range contains a time.
- [func CMTimeRangeContainsTimeRange(CMTimeRange, otherRange: CMTimeRange) -> Bool](cmtimerangecontainstimerange(_:otherrange:).md)
  Returns a Boolean value that indicates whether a time range contains another time range.
### Inspecting Time Ranges
- [func CMTIMERANGE_IS_EMPTY(CMTimeRange) -> Bool](cmtimerange_is_empty(_:).md)
  Returns a Boolean value that indicates whether a time range has a duration of zero.
- [func CMTIMERANGE_IS_INDEFINITE(CMTimeRange) -> Bool](cmtimerange_is_indefinite(_:).md)
  Returns a Boolean value that indicates whether a time range is indefinite.
- [func CMTIMERANGE_IS_INVALID(CMTimeRange) -> Bool](cmtimerange_is_invalid(_:).md)
  Returns a Boolean value that indicates whether a time range is invalid.
- [func CMTIMERANGE_IS_VALID(CMTimeRange) -> Bool](cmtimerange_is_valid(_:).md)
  Returns a Boolean value that indicates whether a time range is valid.
- [func CMTimeRangeGetEnd(CMTimeRange) -> CMTime](cmtimerangegetend(_:).md)
  Returns a time value that represents the end of a time range.
- [func CMTimeRangeGetIntersection(CMTimeRange, otherRange: CMTimeRange) -> CMTimeRange](cmtimerangegetintersection(_:otherrange:).md)
  Returns a new time range with the time elements that are common between the input.
- [func CMTimeRangeGetUnion(CMTimeRange, otherRange: CMTimeRange) -> CMTimeRange](cmtimerangegetunion(_:otherrange:).md)
  Returns a new time range with the time elements of the input.
### Utility Functions
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
- [func CMTimeRangeShow(CMTimeRange)](cmtimerangeshow(_:).md)
  Prints a description of the time range to standard error.
### Data Types
- [struct CMTimeRange](cmtimerange.md)
  A structure that represents a time range.
### Constants
- [Dictionary Keys](cmtimerange-dictionary-keys.md)
  Keys to use when working with dictionary representations of a time range.
- [Pre-Specified Time Ranges](pre-specified-time-ranges.md)
  Constants that specify zero and invalid time ranges.

## See Also

- [CMTime APIs](cmtime-api.md)
  A structure that represents time.
- [CMTimeMapping APIs](cmtimemapping-api.md)
  A structure that maps a segment of a source time range to a target time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerange-api)*