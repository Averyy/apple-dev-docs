# CMTimeRangeMake(start:duration:)

**Framework**: Core Media  
**Kind**: func

Creates a valid time range with a start time and duration.

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
func CMTimeRangeMake(start: CMTime, duration: CMTime) -> CMTimeRange
```

#### Return Value

A valid time range structure, or an invalid time range if the duration’s epoch isn’t `0`.

## Parameters

- `start`: The start of the time range.
- `duration`: The duration of the time range.

## See Also

- [func CMTimeRangeMakeFromDictionary(CFDictionary) -> CMTimeRange](cmtimerangemakefromdictionary(_:).md)
  Creates a time range from a dictionary representation of its fields.
- [func CMTimeRangeFromTimeToTime(start: CMTime, end: CMTime) -> CMTimeRange](cmtimerangefromtimetotime(start:end:).md)
  Creates a valid time range from a start and end time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerangemake(start:duration:))*