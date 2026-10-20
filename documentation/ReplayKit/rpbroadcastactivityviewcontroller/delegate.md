# delegate

**Framework**: ReplayKit  
**Kind**: property  
**Role**: Instance Property

The delegate for the broadcast activity view controller.

**Availability**:
- iOS 10.0+ - Deprecated in 27.0
- iPadOS 10.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: No longer supported

## Declaration

```swift
weak var delegate: (any RPBroadcastActivityViewControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<RPBroadcastActivityViewControllerDelegate> delegate;
```

## See Also

### Getting the Delegate
- [protocol RPBroadcastActivityViewControllerDelegate](../rpbroadcastactivityviewcontrollerdelegate.md)
  The protocol you implement to respond to changes to a broadcast activity user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontroller/delegate)*