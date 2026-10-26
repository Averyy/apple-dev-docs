# callRecordToCallBack

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

Details about a call to redial a missed call.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@NSCopying
var callRecordToCallBack: INCallRecord? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INCallRecord * callRecordToCallBack;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INCallRecord * callRecordToCallBack;
```

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
- [var recordTypeForRedialing: INCallRecordType](./recordtypeforredialing.md)
  The category of past call record contact information used for redialing.
- [var callRecordFilter: INCallRecordFilter?](./callrecordfilter.md)
  Filters specified by the user to redial a call.
- [enum INCallAudioRoute](../incallaudioroute.md)
  Constants that describe the audio route for the call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallintent/callrecordtocallback)*