# CMTimeRange

**Framework**: Core Media  
**Role**: API Collection

A structure that represents a range of time.

## Overview

This document describes the API for creating and manipulating `CMTimeRange` structures.

The system represents a `CMTimeRange` as a non-opaque, mutable structure by using two [`CMTime`](./cmtime.md) values that specify the start time and duration of the range. A time range doesn’t include the end time because you calculate it by adding the duration to the start time.

```objc
// An expression that evaluates to false.
CMTimeRangeContainsTime(range, CMTimeRangeGetEnd(range))
```

Convert `CMTimeRanges` to and from `CFDictionaries` (see [`CFDictionary`](../CoreFoundation/cfdictionary.md)) using [`CMTimeRangeCopyAsDictionary(_:allocator:)`](./cmtimerangecopyasdictionary%28_,allocator%29.md) and [`CMTimeRangeMakeFromDictionary(_:)`](./cmtimerangemakefromdictionary%28_%29.md) to use in annotations and various Core Foundation containers.

The epoch in a `CMTime` that represents a duration must be `0`, and the value must be nonnegative. The epoch in a `CMTime` that represents a timestamp can be nonzero, but functions (such as [`CMTimeRangeGetUnion(_:otherRange:)`](./cmtimerangegetunion%28_,otherrange%29.md)) can only perform operations on ranges whose start fields have the same epoch. `CMTimeRanges` can’t span different epochs.

For information about additional functions for managing dates and times, see [Time Utilities](../CoreFoundation/time-utilities.md).

## Topics

### Creating Time Ranges
- [func CMTimeRangeMake(start: CMTime, duration: CMTime) -> CMTimeRange](./cmtimerangemake%28start,duration%29.md)
  Creates a valid time range with a start time and duration.
- [func CMTimeRangeMakeFromDictionary(CFDictionary) -> CMTimeRange](./cmtimerangemakefromdictionary%28_%29.md)
  Creates a time range from a dictionary representation of its fields.
- [func CMTimeRangeFromTimeToTime(start: CMTime, end: CMTime) -> CMTimeRange](./cmtimerangefromtimetotime%28start,end%29.md)
  Creates a valid time range from a start and end time.
### Comparing Time Ranges
- [func CMTimeRangeEqual(CMTimeRange, CMTimeRange) -> Bool](./cmtimerangeequal%28_,_%29.md)
  Returns a Boolean value that indicates whether two time ranges are equal.
- [func CMTimeRangeContainsTime(CMTimeRange, time: CMTime) -> Bool](./cmtimerangecontainstime%28_,time%29.md)
  Returns a Boolean value that indicates whether a time range contains a time.
- [func CMTimeRangeContainsTimeRange(CMTimeRange, otherRange: CMTimeRange) -> Bool](./cmtimerangecontainstimerange%28_,otherrange%29.md)
  Returns a Boolean value that indicates whether a time range contains another time range.
### Inspecting Time Ranges
- [func CMTIMERANGE_IS_EMPTY(CMTimeRange) -> Bool](./cmtimerange_is_empty%28_%29.md)
  Returns a Boolean value that indicates whether a time range has a duration of zero.
- [func CMTIMERANGE_IS_INDEFINITE(CMTimeRange) -> Bool](./cmtimerange_is_indefinite%28_%29.md)
  Returns a Boolean value that indicates whether a time range is indefinite.
- [func CMTIMERANGE_IS_INVALID(CMTimeRange) -> Bool](./cmtimerange_is_invalid%28_%29.md)
  Returns a Boolean value that indicates whether a time range is invalid.
- [func CMTIMERANGE_IS_VALID(CMTimeRange) -> Bool](./cmtimerange_is_valid%28_%29.md)
  Returns a Boolean value that indicates whether a time range is valid.
- [func CMTimeRangeGetEnd(CMTimeRange) -> CMTime](./cmtimerangegetend%28_%29.md)
  Returns a time value that represents the end of a time range.
- [func CMTimeRangeGetIntersection(CMTimeRange, otherRange: CMTimeRange) -> CMTimeRange](./cmtimerangegetintersection%28_,otherrange%29.md)
  Returns a new time range with the time elements that are common between the input.
- [func CMTimeRangeGetUnion(CMTimeRange, otherRange: CMTimeRange) -> CMTimeRange](./cmtimerangegetunion%28_,otherrange%29.md)
  Returns a new time range with the time elements of the input.
- [CMTIMERANGE_IS_EMPTY](./cmtimerange_is_empty.md)
  Returns a Boolean value that indicates whether a time range has a duration of zero.
- [CMTIMERANGE_IS_INDEFINITE](./cmtimerange_is_indefinite.md)
  Returns a Boolean value that indicates whether a time range is indefinite.
- [CMTIMERANGE_IS_INVALID](./cmtimerange_is_invalid.md)
  Returns a Boolean value that indicates whether a time range is invalid.
- [CMTIMERANGE_IS_VALID](./cmtimerange_is_valid.md)
  Returns a Boolean value that indicates whether a time range is valid.
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
- [func CMTimeRangeShow(CMTimeRange)](./cmtimerangeshow%28_%29.md)
  Prints a description of the time range to standard error.
### Data Types
- [struct CMTimeRange](./cmtimerange.md)
  A structure that represents a time range.
### Constants
- [Dictionary Keys](./cmtimerange-dictionary-keys.md)
  Keys to use when working with dictionary representations of a time range.
- [Pre-Specified Time Ranges](./pre-specified-time-ranges.md)
  Constants that specify zero and invalid time ranges.

## See Also

### Time Representation
- [CMTime](./cmtime-api.md)
  A structure that represents time.
- [CMTimeMapping](./cmtimemapping-api.md)
  A structure that maps a segment of a source time range to a target time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerange-api)*