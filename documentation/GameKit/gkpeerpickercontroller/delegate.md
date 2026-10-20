# delegate

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The delegate of the peer picker controller.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: No longer supported

## Declaration

```swift
weak var delegate: (any GKPeerPickerControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<GKPeerPickerControllerDelegate> delegate;
```

#### Discussion

The delegate must adopt the [`GKPeerPickerControllerDelegate`](../gkpeerpickercontrollerdelegate.md) formal protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkpeerpickercontroller/delegate)*