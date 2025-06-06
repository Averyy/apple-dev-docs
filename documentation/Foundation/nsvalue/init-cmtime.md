# init(CMTime:)

**Framework**: Foundation  
**Kind**: init

Creates a new value object containing the specified CoreMedia time structure.

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
init(time: CMTime)
```

#### Return Value

A new value object that contains the media time information.

## Parameters

- `time`: The value for the new object.

## See Also

- [struct CMTime](../CoreMedia/CMTime.md)
  A structure that represents time.
- [init(CMTimeRange: CMTimeRange)](nsvalue/init(cmtimerange:).md)
  Creates a new value object containing the specified CoreMedia time range structure.
- [init(CMTimeMapping: CMTimeMapping)](nsvalue/init(cmtimemapping:).md)
  Creates a new value object containing the specified CoreMedia time mapping structure.
- [var timeValue: CMTime](nsvalue/timevalue.md)
  The CoreMedia time structure representation of the value.
- [var timeRangeValue: CMTimeRange](nsvalue/timerangevalue.md)
  The CoreMedia time range structure representation of the value.
- [var timeMappingValue: CMTimeMapping](nsvalue/timemappingvalue.md)
  The CoreMedia time mapping structure representation of the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/init(cmtime:))*