# init(CMTimeMapping:)

**Framework**: Foundation  
**Kind**: init

Creates a new value object containing the specified CoreMedia time mapping structure.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
init(timeMapping: CMTimeMapping)
```

#### Return Value

A new value object that contains the time mapping information.

## Parameters

- `timeMapping`: The value for the new object.

## See Also

- [struct CMTimeMapping](../CoreMedia/CMTimeMapping.md)
  A structure that maps a segment of a source time range to a target time range.
- [init(CMTime: CMTime)](nsvalue/init(cmtime:).md)
  Creates a new value object containing the specified CoreMedia time structure.
- [init(CMTimeRange: CMTimeRange)](nsvalue/init(cmtimerange:).md)
  Creates a new value object containing the specified CoreMedia time range structure.
- [var timeValue: CMTime](nsvalue/timevalue.md)
  The CoreMedia time structure representation of the value.
- [var timeRangeValue: CMTimeRange](nsvalue/timerangevalue.md)
  The CoreMedia time range structure representation of the value.
- [var timeMappingValue: CMTimeMapping](nsvalue/timemappingvalue.md)
  The CoreMedia time mapping structure representation of the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/init(cmtimemapping:))*