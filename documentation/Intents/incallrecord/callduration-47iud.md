# callDuration

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The duration (measured in seconds) of the call.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- watchOS 4.0+

## Declaration

```swift
@nonobjc
final var callDuration: Double? { get }
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
- [var unseen: Bool?](./unseen-2m7sz.md)
  A Boolean value indicating whether the user has seen the call.
- [var numberOfCalls: Int?](./numberofcalls-r8kl.md)
  The number of calls in the call record.
- [var participants: [INPerson]?](./participants.md)
  The recipient of the user’s call request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecord/callduration-47iud)*