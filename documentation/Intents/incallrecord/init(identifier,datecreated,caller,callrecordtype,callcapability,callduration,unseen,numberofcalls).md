# init(identifier:dateCreated:caller:callRecordType:callCapability:callDuration:unseen:numberOfCalls:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a call record with the details about the call.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- watchOS 6.0+

## Declaration

```swift
@nonobjc
convenience init(identifier: String, dateCreated: Date? = nil, caller: INPerson? = nil, callRecordType: INCallRecordType = .unknown, callCapability: INCallCapability = .unknown, callDuration: Double? = nil, unseen: Bool? = nil, numberOfCalls: Int? = nil)
```

#### Return Value

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecord/init(identifier:datecreated:caller:callrecordtype:callcapability:callduration:unseen:numberofcalls:))*