# initWithIdentifier:dateCreated:caller:callRecordType:callCapability:callDuration:unseen:numberOfCalls:

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Initializes a call record with the details about the call.

**Availability**:
- iOS 13.0+ - Deprecated in 14.5
- iPadOS 13.0+ - Deprecated in 14.5
- Mac Catalyst 13.1+ - Deprecated in 14.5
- macOS 10.15+ - Deprecated in 11.3
- tvOS 13.0+ - Deprecated in 14.5
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 7.3

## Declaration

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier dateCreated:(NSDate *) dateCreated caller:(INPerson *) caller callRecordType:(INCallRecordType) callRecordType callCapability:(INCallCapability) callCapability callDuration:(NSNumber *) callDuration unseen:(NSNumber *) unseen numberOfCalls:(NSNumber *) numberOfCalls;
```

## Return Value

An initialized [`INCallRecord`](../incallrecord.md) object or `nil` if the object could not be initialized.

## Parameters

- `identifier`: A unique string that you can use to identify the call in your app.
- `dateCreated`: The date and time at which the call started.
- `caller`: The person who participated in the call with the current user.
- `callRecordType`: The type of call. Use this parameter to specify whether the call was incoming, was outgoing, corresponds to a voicemail, and so on.
- `callCapability`: An indicator of whether the call supports audio or video.
- `callDuration`: The duration of the call, measured in seconds.
- `unseen`: A Boolean indicating whether the user saw the call.
- `numberOfCalls`: The number of calls associated with the call record.

## See Also

### Initializing a Call Record
- [- initWithIdentifier:dateCreated:caller:callRecordType:callCapability:callDuration:unseen:](./initwithidentifier_datecreated_caller_callrecordtype_callcapability_callduration_unseen_.md)
  Initializes a call record with the details about the call.
- [- initWithIdentifier:dateCreated:callRecordType:callCapability:callDuration:unseen:](./initwithidentifier_datecreated_callrecordtype_callcapability_callduration_unseen_.md)
  Creates a call record with the details about the call.
- [- initWithIdentifier:dateCreated:callRecordType:callCapability:callDuration:unseen:numberOfCalls:](./initwithidentifier_datecreated_callrecordtype_callcapability_callduration_unseen_numberofcalls_.md)
  Creates a call record with the details about the call.
- [- initWithIdentifier:dateCreated:callRecordType:callCapability:callDuration:unseen:participants:numberOfCalls:isCallerIdBlocked:](./initwithidentifier_datecreated_callrecordtype_callcapability_callduration_unseen_participants_numberofcalls_iscalleridblocked_.md)
  Creates a call record with the details about the call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecord/initwithidentifier:datecreated:caller:callrecordtype:callcapability:callduration:unseen:numberofcalls:)*