# distanceRemainingToDisplay

**Framework**: CarPlay  
**Kind**: property

The distance remaining that the framework displays to a person, in the default units of measurement.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var distanceRemainingToDisplay: Measurement<UnitLength> { get }
```

#### Discussion

If not set, falls back to `distanceRemaining`.

## See Also

- [var distanceRemaining: Measurement<UnitLength>](cptravelestimates/distanceremaining.md)
  The remaining distance for the travel estimate.
- [var timeRemaining: TimeInterval](cptravelestimates/timeremaining.md)
  The remaining time for the travel estimate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptravelestimates/distanceremainingtodisplay)*