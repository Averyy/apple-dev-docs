# callCapability

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The audio and video capabilities of the call.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var callCapability: INCallCapability { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INCallCapability callCapability;
```

*macOS*

```objc
@property (atomic, assign, readonly) INCallCapability callCapability;
```

## See Also

### Getting the Call Details
- [var callRecordType: INCallRecordType](./callrecordtype.md)
  The type of call that resulted from the attempt.
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
- [var participants: [INPerson]?](./participants.md)
  The recipient of the user’s call request.
- [callDuration](./callduration-2d9u1.md)
  The duration (measured in seconds) of the call.
- [unseen](./unseen-8qab3.md)
  A Boolean value indicating whether the user has seen the call.
- [numberOfCalls](./numberofcalls-7vv6o.md)
  The number of calls in the call record.
- [isCallerIdBlocked](./iscalleridblocked.md)
  A Boolean value indicating if user’s callerID is showing during a call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecord/callcapability)*