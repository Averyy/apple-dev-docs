# INCallAudioRoute

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the audio route for the call.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum INCallAudioRoute
```

```c
enum INCallAudioRoute : NSInteger;
```

## Topics

### Audio Routes
- [INCallAudioRoute.unknown](./incallaudioroute/unknown.md)
  An unknown audio route.
- [INCallAudioRoute.speakerphoneAudioRoute](./incallaudioroute/speakerphoneaudioroute.md)
  The device’s speakerphone mode.
- [INCallAudioRoute.bluetoothAudioRoute](./incallaudioroute/bluetoothaudioroute.md)
  A connected Bluetooth device.
### Initializers
- [init?(rawValue: Int)](./incallaudioroute/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Call Details
- [var callCapability: INCallCapability](./instartcallintent/callcapability.md)
  The type of call the user initiated.
- [var contacts: [INPerson]?](./instartcallintent/contacts.md)
  The users to call.
- [var destinationType: INCallDestinationType](./instartcallintent/destinationtype.md)
  The type of call to place.
- [var audioRoute: INCallAudioRoute](./instartcallintent/audioroute.md)
  The audio route the call is using.
- [var recordTypeForRedialing: INCallRecordType](./instartcallintent/recordtypeforredialing.md)
  The category of past call record contact information used for redialing.
- [var callRecordFilter: INCallRecordFilter?](./instartcallintent/callrecordfilter.md)
  Filters specified by the user to redial a call.
- [var callRecordToCallBack: INCallRecord?](./instartcallintent/callrecordtocallback.md)
  Details about a call to redial a missed call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallaudioroute)*