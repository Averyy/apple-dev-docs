# temperature

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The specific temperature to set for the climate control system.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var temperature: Measurement<UnitTemperature>? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSMeasurement<NSUnitTemperature *> * temperature;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSMeasurement<NSUnitTemperature *> * temperature;
```

## Discussion

Use this property to get the precise temperature requested by the user. This property is `nil` when the user modified a different climate control setting.

## See Also

### Getting the Climate Control Settings
- [var enableClimateControl: Bool?](./enableclimatecontrol-4y9iz.md)
  A Boolean value indicating whether to turn on the climate control system.
- [var enableAutoMode: Bool?](./enableautomode-31bzq.md)
  A Boolean value indicating whether to enable automatic mode for the climate control system.
- [var airCirculationMode: INCarAirCirculationMode](./aircirculationmode.md)
  The air circulation mode for the climate control system.
- [var relativeTemperatureSetting: INRelativeSetting](./relativetemperaturesetting.md)
  A relative temperature setting.
- [var climateZone: INCarSeat](./climatezone.md)
  The seat position to have its climate settings modified.
- [enableClimateControl](./enableclimatecontrol-tviy.md)
  A Boolean value indicating whether to turn on the climate control system.
- [enableAutoMode](./enableautomode-6ye2n.md)
  A Boolean value indicating whether to enable automatic mode for the climate control system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetclimatesettingsincarintent/temperature)*