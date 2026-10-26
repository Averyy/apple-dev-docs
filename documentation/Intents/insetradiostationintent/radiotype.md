# radioType

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The type of radio tuner to use.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var radioType: INRadioType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INRadioType radioType;
```

*macOS*

```objc
@property (atomic, assign, readonly) INRadioType radioType;
```

## See Also

### Getting Details About the Radio Station to Set
- [var frequency: Double?](./frequency-2ctw6.md)
  The broadcast frequency of the radio station.
- [var stationName: String?](./stationname.md)
  The name associated with the radio station.
- [var channel: String?](./channel.md)
  The channel number of the station.
- [var presetNumber: Int?](./presetnumber-2dub4.md)
  The programmable preset assigned to the station.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetradiostationintent/radiotype)*