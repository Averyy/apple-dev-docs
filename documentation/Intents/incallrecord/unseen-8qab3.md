# unseen

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the user has seen the call.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * unseen;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSNumber * unseen;
```

## See Also

### Getting the Call Details
- [var callRecordType: INCallRecordType](./callrecordtype.md)
  The type of call that resulted from the attempt.
- [var callCapability: INCallCapability](./callcapability.md)
  The audio and video capabilities of the call.
- [enum INCallCapability](../incallcapability.md)
  Constants indicating the capabilities of the call.
- [var dateCreated: Date?](./datecreated.md)
  The date and time at which the call was initiated.
- [callDuration](./callduration-2d9u1.md)
  The duration (measured in seconds) of the call.
- [numberOfCalls](./numberofcalls-7vv6o.md)
  The number of calls in the call record.
- [var participants: [INPerson]?](./participants.md)
  The recipient of the user’s call request.
- [isCallerIdBlocked](./iscalleridblocked.md)
  A Boolean value indicating if user’s callerID is showing during a call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecord/unseen-8qab3)*