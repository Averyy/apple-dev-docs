# climateZone

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The seat position to have its climate settings modified.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var climateZone: INCarSeat { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INCarSeat climateZone;
```

*macOS*

```objc
@property (atomic, assign, readonly) INCarSeat climateZone;
```

#### Discussion

If your climate control system supports different settings for different parts of the car, use this property to determine which zone’s settings you need to adjust. If your vehicle supports only one climate control zone, you can ignore the value in this property.

The value of this property is [`INCarSeat.unknown`](../incarseat/unknown.md) when the user modified a different climate control setting or didn’t specify a seat position.

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
- [var relativeTemperatureSetting: INRelativeSetting](./relativetemperaturesetting.md)
  A relative temperature setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetclimatesettingsincarintent/climatezone)*