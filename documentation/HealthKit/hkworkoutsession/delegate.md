# delegate

**Framework**: HealthKit  
**Kind**: property

The workout session’s delegate.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
weak var delegate: (any HKWorkoutSessionDelegate)? { get set }
```

#### Discussion

The delegate receives notifications when a workout session’s state changes or when a workout session fails.

## See Also

- [protocol HKWorkoutSessionDelegate](hkworkoutsessiondelegate.md)
  The session delegate protocol that defines an interface for receiving notifications about errors and changes in the workout session’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/delegate)*