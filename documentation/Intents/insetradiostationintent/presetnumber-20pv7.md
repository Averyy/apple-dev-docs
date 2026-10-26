# presetNumber

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The programmable preset assigned to the station.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * presetNumber;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSNumber * presetNumber;
```

#### Discussion

For most entertainment systems, users can assign favorite radio stations to one or more programmable presets. If the user specified a preset when asking to change the radio station, this property contains the specified preset number.

When the [`channel`](./channel.md) property contains a valid value, this property `nil`.

## See Also

### Getting Details About the Radio Station to Set
- [var radioType: INRadioType](./radiotype.md)
  The type of radio tuner to use.
- [frequency](./frequency-63rbb.md)
  The broadcast frequency of the radio station.
- [var stationName: String?](./stationname.md)
  The name associated with the radio station.
- [var channel: String?](./channel.md)
  The channel number of the station.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetradiostationintent/presetnumber-20pv7)*