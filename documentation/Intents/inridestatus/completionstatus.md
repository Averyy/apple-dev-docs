# completionStatus

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

Information about how the ride ended.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var completionStatus: INRideCompletionStatus? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INRideCompletionStatus * completionStatus;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INRideCompletionStatus * completionStatus;
```

## Mentions

- [Providing Live Status Updates](../../SiriKit/providing-live-status-updates.md)

## Discussion

When the value of the [`phase`](./phase.md) property is [`INRidePhase.completed`](../inridephase/completed.md), SiriKit checks this property for additional information about how the ride ended. Use this property to specify whether the ride ended successfully or the user canceled the ride.. You can also include information about the amount paid or the reason for any cancellation.

## See Also

### Specifying the Ride Status
- [var phase: INRidePhase](./phase.md)
  The current status of the ride.
- [enum INRidePhase](../inridephase.md)
  Constants indicating the current ride status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridestatus/completionstatus)*