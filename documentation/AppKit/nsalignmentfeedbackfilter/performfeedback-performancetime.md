# performFeedback(_:performanceTime:)

**Framework**: AppKit  
**Kind**: method

Performs the haptic feedback described by one or more alignment feedback tokens.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func performFeedback(_ alignmentFeedbackTokens: [any NSAlignmentFeedbackToken], performanceTime: NSHapticFeedbackManager.PerformanceTime)
```

#### Discussion

Call this method to initiate haptic feedback to the user. Pass it one or more alignment feedback tokens of type `NSAlignmentFeedbackToken` and a time to execute of type `NSHapticFeedbackPerformanceTime`. Call this method immediately before moving the object to its new aligned position.

## Parameters

- `alignmentFeedbackTokens`: One or more feedback tokens prepared for specific alignment locations by calling  ,  , or  . Typically, no more than one feedback token per dimension (horizontal/vertical) should be provided.
- `performanceTime`: The time, of type  , when the feedback should be provided to the user.

## See Also

- [protocol NSHapticFeedbackPerformer](nshapticfeedbackperformer.md)
  A set of methods and constants that a haptic feedback performer implements.
- [NSHapticFeedbackManager.PerformanceTime](nshapticfeedbackmanager/performancetime.md)
  A time at which to provide haptic feedback to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalignmentfeedbackfilter/performfeedback(_:performancetime:))*