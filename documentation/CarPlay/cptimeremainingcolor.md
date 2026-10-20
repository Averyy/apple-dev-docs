# CPTimeRemainingColor

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

The color the system uses when displaying the time remaining for a trip.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum CPTimeRemainingColor
```

```c
enum CPTimeRemainingColor : NSUInteger;
```

#### Overview

The system determines the shade of each color based on the [`tripEstimateStyle`](./cpmaptemplate/tripestimatestyle.md) for the map template.

## Topics

### Colors
- [CPTimeRemainingColor.default](./cptimeremainingcolor/default.md)
  The system default color.
- [CPTimeRemainingColor.green](./cptimeremainingcolor/green.md)
  A shade of green.
- [CPTimeRemainingColor.orange](./cptimeremainingcolor/orange.md)
  A shade of orange.
- [CPTimeRemainingColor.red](./cptimeremainingcolor/red.md)
  A shade of red.
### Initializers
- [init?(rawValue: UInt)](./cptimeremainingcolor/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Providing Trip Estimates
- [func updateEstimates(CPTravelEstimates, for: CPTrip)](./cpmaptemplate/updateestimates%28_,for%29.md)
  Updates travel estimates, such as arrival time and the remaining time and distance for a trip.
- [func update(CPTravelEstimates, for: CPTrip, with: CPTimeRemainingColor)](./cpmaptemplate/update%28_,for,with%29.md)
  Updates travel estimates, such as arrival time and the remaining time and distance for a trip, with the specified time-remaining color.
- [var tripEstimateStyle: CPTripEstimateStyle](./cpmaptemplate/tripestimatestyle.md)
  The style that the map template uses when displaying trip estimates during active nagivation.
- [enum CPTripEstimateStyle](./cptripestimatestyle.md)
  The set of display styles for trip estimates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptimeremainingcolor)*