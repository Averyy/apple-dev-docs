# destinationType

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The type of call to place.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var destinationType: INCallDestinationType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INCallDestinationType destinationType;
```

*macOS*

```objc
@property (atomic, assign, readonly) INCallDestinationType destinationType;
```

## Discussion

This property contains the call destination type. Use it to differentiate regular calls from specialized types of calls. For example, when the value of this property is [`voicemailDestination`](../incalldestinationtype/voicemaildestination.md), the user is attempting to connect to their voicemail messages.

## See Also

### Getting the Call Details
- [var callCapability: INCallCapability](./callcapability.md)
  The type of call the user initiated.
- [var contacts: [INPerson]?](./contacts.md)
  The users to call.
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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallintent/destinationtype)*