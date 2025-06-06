# init(distanceRemaining:timeRemaining:)

**Framework**: CarPlay  
**Kind**: init

Creates travel estimates with the remaining distance and time.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(distanceRemaining distance: Measurement<UnitLength>, timeRemaining time: TimeInterval)
```

#### Return Value

A newly initialized travel estimates object.

## Parameters

- `distance`: The remaining distance for the travel estimate.
- `time`: The remaining time for the travel estimate.

## See Also

- [init(distanceRemaining: Measurement<UnitLength>, distanceRemainingToDisplay: Measurement<UnitLength>, timeRemaining: TimeInterval)](cptravelestimates/init(distanceremaining:distanceremainingtodisplay:timeremaining:).md)
  Creates a travel estimates instance with the distance remaining that the framework displays to a person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptravelestimates/init(distanceremaining:timeremaining:))*