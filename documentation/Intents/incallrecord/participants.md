# participants

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The recipient of the user’s call request.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 12.0+
- visionOS 1.0+
- watchOS 7.3+

## Declaration

```swift
var participants: [INPerson]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<INPerson *> * participants;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<INPerson *> * participants;
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
- [var callDuration: Double?](./callduration-47iud.md)
  The duration (measured in seconds) of the call.
- [var unseen: Bool?](./unseen-2m7sz.md)
  A Boolean value indicating whether the user has seen the call.
- [var numberOfCalls: Int?](./numberofcalls-r8kl.md)
  The number of calls in the call record.
- [callDuration](./callduration-2d9u1.md)
  The duration (measured in seconds) of the call.
- [unseen](./unseen-8qab3.md)
  A Boolean value indicating whether the user has seen the call.
- [numberOfCalls](./numberofcalls-7vv6o.md)
  The number of calls in the call record.
- [isCallerIdBlocked](./iscalleridblocked.md)
  A Boolean value indicating if user’s callerID is showing during a call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecord/participants)*