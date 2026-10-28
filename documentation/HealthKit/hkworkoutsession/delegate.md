# delegate

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The workout session’s delegate.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
weak var delegate: (any HKWorkoutSessionDelegate)? { get set }
```

```objc
@property (weak, nullable) id<HKWorkoutSessionDelegate> delegate;
```

## Discussion

The delegate receives notifications when a workout session’s state changes or when a workout session fails.

## See Also

### Monitoring the session
- [protocol HKWorkoutSessionDelegate](../hkworkoutsessiondelegate.md)
  The session delegate protocol that defines an interface for receiving notifications about errors and changes in the workout session’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/delegate)*