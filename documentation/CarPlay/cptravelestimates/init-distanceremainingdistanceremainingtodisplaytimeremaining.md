# init(distanceRemaining:distanceRemainingToDisplay:timeRemaining:)

**Framework**: CarPlay  
**Kind**: init

Creates a travel estimates instance with the distance remaining that the framework displays to a person.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
init(distanceRemaining: Measurement<UnitLength>, distanceRemainingToDisplay: Measurement<UnitLength>, timeRemaining time: TimeInterval)
```

#### Return Value

A newly initialized travel estimates object.

#### Discussion

If not set, falls back to `distanceRemaining`.

## Parameters

- `distanceRemaining`: The distance remaining in   units.   distanceRemainingToDisplay: the disance remaining to dfisk to a person, in   units.   time: `TimeInterval

## See Also

- [init(distanceRemaining: Measurement<UnitLength>, timeRemaining: TimeInterval)](cptravelestimates/init(distanceremaining:timeremaining:).md)
  Creates travel estimates with the remaining distance and time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptravelestimates/init(distanceremaining:distanceremainingtodisplay:timeremaining:))*