# CMTimeRangeFromTimeToTime(start:end:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a valid time range from a start and end time.

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
func CMTimeRangeFromTimeToTime(start: CMTime, end: CMTime) -> CMTimeRange
```

```c
extern CMTimeRange CMTimeRangeFromTimeToTime(CMTime start, CMTime end);
```

## Return Value

A valid time range structure.

## Parameters

- `start`: The start time of the range.
- `end`: The end time of the range.

## See Also

### Creating Time Ranges
- [func CMTimeRangeMake(start: CMTime, duration: CMTime) -> CMTimeRange](./cmtimerangemake%28start,duration%29.md)
  Creates a valid time range with a start time and duration.
- [func CMTimeRangeMakeFromDictionary(CFDictionary) -> CMTimeRange](./cmtimerangemakefromdictionary%28_%29.md)
  Creates a time range from a dictionary representation of its fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerangefromtimetotime(start:end:))*