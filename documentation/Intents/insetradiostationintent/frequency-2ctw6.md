# frequency

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The broadcast frequency of the radio station.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 10.0+ - Deprecated in 15.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
@nonobjc
final var frequency: Double? { get }
```

## Discussion

This property contains a floating-point number indicating the frequency for AM or FM stations. For example, the value might be 88.5 for an FM station or 660.0 for an AM station.

## See Also

### Getting Details About the Radio Station to Set
- [var radioType: INRadioType](./radiotype.md)
  The type of radio tuner to use.
- [var stationName: String?](./stationname.md)
  The name associated with the radio station.
- [var channel: String?](./channel.md)
  The channel number of the station.
- [var presetNumber: Int?](./presetnumber-2dub4.md)
  The programmable preset assigned to the station.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetradiostationintent/frequency-2ctw6)*