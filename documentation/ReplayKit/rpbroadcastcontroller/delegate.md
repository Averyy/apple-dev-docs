# delegate

**Framework**: ReplayKit  
**Kind**: property  
**Role**: Instance Property

The delegate for the broadcast controller.

**Availability**:
- iOS 10.0+ - Deprecated in 27.0
- iPadOS 10.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: No longer supported

## Declaration

```swift
weak var delegate: (any RPBroadcastControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak) id<RPBroadcastControllerDelegate> delegate;
```

## See Also

### Getting the Delegate
- [protocol RPBroadcastControllerDelegate](../rpbroadcastcontrollerdelegate.md)
  The protocol you implement to respond to changes in a live broadcast.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastcontroller/delegate)*