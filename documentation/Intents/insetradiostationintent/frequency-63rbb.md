# frequency

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The broadcast frequency of the radio station.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * frequency;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSNumber * frequency;
```

#### Discussion

This property contains a floating-point number indicating the frequency for AM or FM stations. For example, the value might be 88.5 for an FM station or 660.0 for an AM station.

## See Also

### Getting Details About the Radio Station to Set
- [var radioType: INRadioType](./radiotype.md)
  The type of radio tuner to use.
- [var stationName: String?](./stationname.md)
  The name associated with the radio station.
- [var channel: String?](./channel.md)
  The channel number of the station.
- [presetNumber](./presetnumber-20pv7.md)
  The programmable preset assigned to the station.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetradiostationintent/frequency-63rbb)*