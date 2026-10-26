# init(audioRoute:destinationType:contacts:recordTypeForRedialing:callCapability:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a start call intent object with the specified parameters.

**Availability**:
- iOS 13.0+ - Deprecated in 14.0
- iPadOS 13.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 7.0

## Declaration

```swift
convenience init(audioRoute: INCallAudioRoute, destinationType: INCallDestinationType, contacts: [INPerson]?, recordTypeForRedialing: INCallRecordType, callCapability: INCallCapability)
```

```objc
- (instancetype) initWithAudioRoute:(INCallAudioRoute) audioRoute destinationType:(INCallDestinationType) destinationType contacts:(NSArray<INPerson *> *) contacts recordTypeForRedialing:(INCallRecordType) recordTypeForRedialing callCapability:(INCallCapability) callCapability;
```

#### Return Value

An initialized intent or `nil` if it couldn’t create the object.

#### Discussion

Typically, you don’t create instances of this class yourself. Instead, Siri creates instances when the user asks to place a call to another user. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `audioRoute`: The audio route for the call.
- `destinationType`: The target type of the call to place.
- `contacts`: An array of [`INPerson`](../inperson.md) objects representing the users to call.
- `recordTypeForRedialing`: The category of past call record contact information used for redialing.
- `callCapability`: The type of call to place.

## See Also

### Initializing the Intent Object
- [init(callRecordFilter: INCallRecordFilter?, callRecordToCallBack: INCallRecord?, audioRoute: INCallAudioRoute, destinationType: INCallDestinationType, contacts: [INPerson]?, callCapability: INCallCapability)](./init%28callrecordfilter,callrecordtocallback,audioroute,destinationtype,contacts,callcapability%29.md)
  Creates a start call intent object with the specified parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallintent/init(audioroute:destinationtype:contacts:recordtypeforredialing:callcapability:))*