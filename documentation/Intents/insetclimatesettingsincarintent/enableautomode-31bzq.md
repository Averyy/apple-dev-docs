# enableAutoMode

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether to enable automatic mode for the climate control system.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 10.0+ - Deprecated in 15.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
@nonobjc
final var enableAutoMode: Bool? { get }
```

## Discussion

This property is `nil` when the user modified a different climate control setting.

## See Also

### Getting the Climate Control Settings
- [var enableClimateControl: Bool?](./enableclimatecontrol-4y9iz.md)
  A Boolean value indicating whether to turn on the climate control system.
- [var airCirculationMode: INCarAirCirculationMode](./aircirculationmode.md)
  The air circulation mode for the climate control system.
- [var temperature: Measurement<UnitTemperature>?](./temperature.md)
  The specific temperature to set for the climate control system.
- [var relativeTemperatureSetting: INRelativeSetting](./relativetemperaturesetting.md)
  A relative temperature setting.
- [var climateZone: INCarSeat](./climatezone.md)
  The seat position to have its climate settings modified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetclimatesettingsincarintent/enableautomode-31bzq)*