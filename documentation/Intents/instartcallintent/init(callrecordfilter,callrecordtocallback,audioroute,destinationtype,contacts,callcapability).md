# init(callRecordFilter:callRecordToCallBack:audioRoute:destinationType:contacts:callCapability:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a start call intent object with the specified parameters.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(callRecordFilter: INCallRecordFilter?, callRecordToCallBack: INCallRecord?, audioRoute: INCallAudioRoute, destinationType: INCallDestinationType, contacts: [INPerson]?, callCapability: INCallCapability)
```

```objc
- (instancetype) initWithCallRecordFilter:(INCallRecordFilter *) callRecordFilter callRecordToCallBack:(INCallRecord *) callRecordToCallBack audioRoute:(INCallAudioRoute) audioRoute destinationType:(INCallDestinationType) destinationType contacts:(NSArray<INPerson *> *) contacts callCapability:(INCallCapability) callCapability;
```

#### Return Value

An initialized intent or `nil` if it couldn’t create the object.

## Parameters

- `callRecordFilter`: Filters specified by the user to redial a call.
- `callRecordToCallBack`: Details about a call to redial a missed call.
- `audioRoute`: The audio route for the call.
- `destinationType`: The target type of the call to place.
- `contacts`: An array of [`INPerson`](../inperson.md) objects representing the users to call.
- `callCapability`: The type of call to place.

## See Also

### Initializing the Intent Object
- [convenience init(audioRoute: INCallAudioRoute, destinationType: INCallDestinationType, contacts: [INPerson]?, recordTypeForRedialing: INCallRecordType, callCapability: INCallCapability)](./init%28audioroute,destinationtype,contacts,recordtypeforredialing,callcapability%29.md)
  Creates a start call intent object with the specified parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallintent/init(callrecordfilter:callrecordtocallback:audioroute:destinationtype:contacts:callcapability:))*