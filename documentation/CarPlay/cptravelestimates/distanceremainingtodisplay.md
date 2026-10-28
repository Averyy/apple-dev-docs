# distanceRemainingToDisplay

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The distance remaining that the framework displays to a person, in the default units of measurement.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var distanceRemainingToDisplay: Measurement<UnitLength> { get }
```

```objc
@property (nonatomic, copy, readonly) NSMeasurement<NSUnitLength *> * distanceRemainingToDisplay;
```

## Discussion

If not set, falls back to `distanceRemaining`.

## See Also

### Getting Travel Estimates
- [var distanceRemaining: Measurement<UnitLength>](./distanceremaining.md)
  The remaining distance for the travel estimate.
- [var timeRemaining: TimeInterval](./timeremaining.md)
  The remaining time for the travel estimate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptravelestimates/distanceremainingtodisplay)*