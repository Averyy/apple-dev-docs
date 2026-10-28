# recordTypeForRedialing

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The category of past call record contact information used for redialing.

**Availability**:
- iOS 13.0+ - Deprecated in 14.0
- iPadOS 13.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 7.0

## Declaration

```swift
var recordTypeForRedialing: INCallRecordType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INCallRecordType recordTypeForRedialing;
```

*macOS*

```objc
@property (atomic, assign, readonly) INCallRecordType recordTypeForRedialing;
```

## Discussion

This value indicates which past call record your app should use in determining which contact or contacts to call. For example, if the user asks Siri to redial their last missed call, the system provides your intent handler with a start call intent whose [`recordTypeForRedialing`](./recordtypeforredialing.md) is [`INCallRecordType.missed`](../incallrecordtype/missed.md).

## See Also

### Getting the Call Details
- [var callCapability: INCallCapability](./callcapability.md)
  The type of call the user initiated.
- [var contacts: [INPerson]?](./contacts.md)
  The users to call.
- [var destinationType: INCallDestinationType](./destinationtype.md)
  The type of call to place.
- [var audioRoute: INCallAudioRoute](./audioroute.md)
  The audio route the call is using.
- [var callRecordFilter: INCallRecordFilter?](./callrecordfilter.md)
  Filters specified by the user to redial a call.
- [var callRecordToCallBack: INCallRecord?](./callrecordtocallback.md)
  Details about a call to redial a missed call.
- [enum INCallAudioRoute](../incallaudioroute.md)
  Constants that describe the audio route for the call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallintent/recordtypeforredialing)*