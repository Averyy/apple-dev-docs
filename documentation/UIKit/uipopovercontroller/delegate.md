# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The delegate you want to receive popover controller messages.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 9.0

> **Deprecated**: For more information, see [`UIPopoverController`](../uipopovercontroller.md).

## Declaration

```swift
weak var delegate: (any UIPopoverControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UIPopoverControllerDelegate> delegate;
```

#### Discussion

The popover controller uses its delegate to determine whether it should dismiss the popover and provides a notification when such an event occurs. For more information about the methods you can implement in your delegate, see [`UIPopoverControllerDelegate`](../uipopovercontrollerdelegate.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/delegate)*