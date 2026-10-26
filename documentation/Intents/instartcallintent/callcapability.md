# callCapability

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The type of call the user initiated.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var callCapability: INCallCapability { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INCallCapability callCapability;
```

*macOS*

```objc
@property (atomic, assign, readonly) INCallCapability callCapability;
```

#### Discussion

This property contains the user-initiated call type. If the type of call isn’t known, the value of this property is [`INCallCapability.unknown`](../incallcapability/unknown.md).

## See Also

### Getting the Call Details
- [var contacts: [INPerson]?](./contacts.md)
  The users to call.
- [var destinationType: INCallDestinationType](./destinationtype.md)
  The type of call to place.
- [var audioRoute: INCallAudioRoute](./audioroute.md)
  The audio route the call is using.
- [var recordTypeForRedialing: INCallRecordType](./recordtypeforredialing.md)
  The category of past call record contact information used for redialing.
- [var callRecordFilter: INCallRecordFilter?](./callrecordfilter.md)
  Filters specified by the user to redial a call.
- [var callRecordToCallBack: INCallRecord?](./callrecordtocallback.md)
  Details about a call to redial a missed call.
- [enum INCallAudioRoute](../incallaudioroute.md)
  Constants that describe the audio route for the call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallintent/callcapability)*