# CMTimeRangeMakeFromDictionary(_:)

**Framework**: Core Media  
**Kind**: func

Creates a time range from a dictionary representation of its fields.

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
func CMTimeRangeMakeFromDictionary(_ dictionaryRepresentation: CFDictionary) -> CMTimeRange
```

#### Return Value

A valid time range structure, or an invalid time range if `dict` doesn’t have the necessary values.

#### Discussion

This is useful when getting Core Media time ranges from Core Foundation container types. For keys in the dictionary, see [`Dictionary Keys`](cmtimerange-dictionary-keys.md).

## Parameters

- `dictionaryRepresentation`: A dictionary from which to create the time range.

## See Also

- [func CMTimeRangeMake(start: CMTime, duration: CMTime) -> CMTimeRange](cmtimerangemake(start:duration:).md)
  Creates a valid time range with a start time and duration.
- [func CMTimeRangeFromTimeToTime(start: CMTime, end: CMTime) -> CMTimeRange](cmtimerangefromtimetotime(start:end:).md)
  Creates a valid time range from a start and end time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerangemakefromdictionary(_:))*