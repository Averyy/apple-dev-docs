# dateCreated

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The date and time at which the call was initiated.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var dateCreated: Date? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSDate * dateCreated;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSDate * dateCreated;
```

## See Also

### Getting the Call Details
- [var callRecordType: INCallRecordType](./callrecordtype.md)
  The type of call that resulted from the attempt.
- [var callCapability: INCallCapability](./callcapability.md)
  The audio and video capabilities of the call.
- [enum INCallCapability](../incallcapability.md)
  Constants indicating the capabilities of the call.
- [var callDuration: Double?](./callduration-47iud.md)
  The duration (measured in seconds) of the call.
- [var unseen: Bool?](./unseen-2m7sz.md)
  A Boolean value indicating whether the user has seen the call.
- [var numberOfCalls: Int?](./numberofcalls-r8kl.md)
  The number of calls in the call record.
- [var participants: [INPerson]?](./participants.md)
  The recipient of the user’s call request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallrecord/datecreated)*