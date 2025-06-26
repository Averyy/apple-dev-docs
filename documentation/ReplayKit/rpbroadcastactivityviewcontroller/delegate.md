# delegate

**Framework**: ReplayKit  
**Kind**: property

The delegate for the broadcast activity view controller.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var delegate: (any RPBroadcastActivityViewControllerDelegate)? { get set }
```

## See Also

- [protocol RPBroadcastActivityViewControllerDelegate](rpbroadcastactivityviewcontrollerdelegate.md)
  The protocol you implement to respond to changes to a broadcast activity user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontroller/delegate)*