# relativeTemperatureSetting

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A relative temperature setting.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var relativeTemperatureSetting: INRelativeSetting { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INRelativeSetting relativeTemperatureSetting;
```

*macOS*

```objc
@property (atomic, assign, readonly) INRelativeSetting relativeTemperatureSetting;
```

#### Discussion

Use this property to adjust the temperature up or down based relative to its current position. When adjusting temperatures up or down to the next setting, you define the number of degrees to add or subtract from the current setting. The value of this property is [`INRelativeSetting.unknown`](../inrelativesetting/unknown.md) when the user modified a different climate control setting.

## See Also

### Getting the Climate Control Settings
- [var enableClimateControl: Bool?](./enableclimatecontrol-4y9iz.md)
  A Boolean value indicating whether to turn on the climate control system.
- [var enableAutoMode: Bool?](./enableautomode-31bzq.md)
  A Boolean value indicating whether to enable automatic mode for the climate control system.
- [var airCirculationMode: INCarAirCirculationMode](./aircirculationmode.md)
  The air circulation mode for the climate control system.
- [var temperature: Measurement<UnitTemperature>?](./temperature.md)
  The specific temperature to set for the climate control system.
- [var climateZone: INCarSeat](./climatezone.md)
  The seat position to have its climate settings modified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetclimatesettingsincarintent/relativetemperaturesetting)*