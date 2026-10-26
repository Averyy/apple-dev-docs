# phase

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The current status of the ride.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var phase: INRidePhase { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readwrite) INRidePhase phase;
```

*macOS*

```objc
@property (atomic, assign, readwrite) INRidePhase phase;
```

## Mentions

- [Providing Live Status Updates](../../SiriKit/providing-live-status-updates.md)

#### Discussion

Use this property to convey the current status of the ride. When doing the initial confirmation of details with the user, you typically set this property to [`INRidePhase.unknown`](../inridephase/unknown.md). When the user books the ride, set the phase to [`INRidePhase.received`](../inridephase/received.md) if you have received the request but not yet assigned a driver to handle the request. After assigning a driver, change the status to [`INRidePhase.confirmed`](../inridephase/confirmed.md) until the driver picks up the user, at which point you should change the phase to values indicating the pickup status.

When the ride is complete or canceled, change the value to [`INRidePhase.completed`](../inridephase/completed.md) and update the [`completionStatus`](./completionstatus.md) property with additional details about how the ride ended.

The default value of this property is [`INRidePhase.unknown`](../inridephase/unknown.md).

## See Also

### Specifying the Ride Status
- [enum INRidePhase](../inridephase.md)
  Constants indicating the current ride status.
- [var completionStatus: INRideCompletionStatus?](./completionstatus.md)
  Information about how the ride ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridestatus/phase)*