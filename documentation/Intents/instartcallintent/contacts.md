# contacts

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The users to call.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var contacts: [INPerson]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<INPerson *> * contacts;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<INPerson *> * contacts;
```

#### Discussion

The property contains the users to call. Use the information in each [`INPerson`](../inperson.md) object to look for a matching contact in your app.

## See Also

### Getting the Call Details
- [var callCapability: INCallCapability](./callcapability.md)
  The type of call the user initiated.
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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallintent/contacts)*