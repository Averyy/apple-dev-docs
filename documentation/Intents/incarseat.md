# INCarSeat

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating a seat position.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
enum INCarSeat
```

```c
enum INCarSeat : NSInteger;
```

## Topics

### Constants
- [INCarSeat.unknown](./incarseat/unknown.md)
  An unknown seat position.
- [INCarSeat.driver](./incarseat/driver.md)
  The driver’s seat.
- [INCarSeat.passenger](./incarseat/passenger.md)
  The front passenger’s seat.
- [INCarSeat.frontLeft](./incarseat/frontleft.md)
  The front-left car seat.
- [INCarSeat.frontRight](./incarseat/frontright.md)
  The front-right car seat.
- [INCarSeat.front](./incarseat/front.md)
  The front seats.
- [INCarSeat.rearLeft](./incarseat/rearleft.md)
  The rear-left car seat.
- [INCarSeat.rearRight](./incarseat/rearright.md)
  The rear-right car seat.
- [INCarSeat.rear](./incarseat/rear.md)
  The rear seats.
- [INCarSeat.thirdRowLeft](./incarseat/thirdrowleft.md)
  The left seat in third-row seating.
- [INCarSeat.thirdRowRight](./incarseat/thirdrowright.md)
  The right seat in third-row seating.
- [INCarSeat.thirdRow](./incarseat/thirdrow.md)
  The third row seats.
- [INCarSeat.all](./incarseat/all.md)
  All seats in the car.
### Initializers
- [init?(rawValue: Int)](./incarseat/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### CarPlay Data Objects
- [enum INCarDefroster](./incardefroster.md)
  Constants indicating the defroster type.
- [enum INCarAudioSource](./incaraudiosource.md)
  Constants indicating the source of audio.
- [enum INCarAirCirculationMode](./incaraircirculationmode.md)
  Constants indicating the circulation mode for the climate system.
- [enum INRadioType](./inradiotype.md)
  Constants indicating the type of radio.
- [enum INRelativeReference](./inrelativereference.md)
  Constants indicating relative positions.
- [enum INRelativeSetting](./inrelativesetting.md)
  Constants indicating relative settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incarseat)*