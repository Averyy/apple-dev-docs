# audioRoute

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The audio route the call is using.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var audioRoute: INCallAudioRoute { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INCallAudioRoute audioRoute;
```

*macOS*

```objc
@property (atomic, assign, readonly) INCallAudioRoute audioRoute;
```

## Discussion

The property contains the call’s audio route. For example, when the value of this property is [`INCallAudioRoute.bluetoothAudioRoute`](../incallaudioroute/bluetoothaudioroute.md), the user is attempting to use a bluetooth device for the call.

## See Also

### Getting the Call Details
- [var callCapability: INCallCapability](./callcapability.md)
  The type of call the user initiated.
- [var contacts: [INPerson]?](./contacts.md)
  The users to call.
- [var destinationType: INCallDestinationType](./destinationtype.md)
  The type of call to place.
- [var recordTypeForRedialing: INCallRecordType](./recordtypeforredialing.md)
  The category of past call record contact information used for redialing.
- [var callRecordFilter: INCallRecordFilter?](./callrecordfilter.md)
  Filters specified by the user to redial a call.
- [var callRecordToCallBack: INCallRecord?](./callrecordtocallback.md)
  Details about a call to redial a missed call.
- [enum INCallAudioRoute](../incallaudioroute.md)
  Constants that describe the audio route for the call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallintent/audioroute)*