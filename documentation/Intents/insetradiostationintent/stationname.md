# stationName

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The name associated with the radio station.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var stationName: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * stationName;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * stationName;
```

## Discussion

For stations that are identifiable by name, this property contains that name. If the user doesn’t provide other identifying information, use the station name to look up the appropriate channel or frequency information.

## See Also

### Getting Details About the Radio Station to Set
- [var radioType: INRadioType](./radiotype.md)
  The type of radio tuner to use.
- [var frequency: Double?](./frequency-2ctw6.md)
  The broadcast frequency of the radio station.
- [var channel: String?](./channel.md)
  The channel number of the station.
- [var presetNumber: Int?](./presetnumber-2dub4.md)
  The programmable preset assigned to the station.
- [frequency](./frequency-63rbb.md)
  The broadcast frequency of the radio station.
- [presetNumber](./presetnumber-20pv7.md)
  The programmable preset assigned to the station.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetradiostationintent/stationname)*