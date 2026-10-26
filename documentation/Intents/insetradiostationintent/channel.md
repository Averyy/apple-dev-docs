# channel

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The channel number of the station.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var channel: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * channel;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * channel;
```

#### Discussion

This property contains the channel number (if any) you can use to locate the radio station. You use this property to identify satellite radio stations or any radio station with a unique integer identifier in your system.

When the [`presetNumber`](./presetnumber-20pv7.md) property contains a valid value, this property is `nil`.

## See Also

### Getting Details About the Radio Station to Set
- [var radioType: INRadioType](./radiotype.md)
  The type of radio tuner to use.
- [var frequency: Double?](./frequency-2ctw6.md)
  The broadcast frequency of the radio station.
- [var stationName: String?](./stationname.md)
  The name associated with the radio station.
- [var presetNumber: Int?](./presetnumber-2dub4.md)
  The programmable preset assigned to the station.
- [frequency](./frequency-63rbb.md)
  The broadcast frequency of the radio station.
- [presetNumber](./presetnumber-20pv7.md)
  The programmable preset assigned to the station.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetradiostationintent/channel)*