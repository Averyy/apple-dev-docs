# delegate

**Framework**: UIKit  
**Kind**: property

The delegate you want to receive popover controller messages.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
weak var delegate: (any UIPopoverControllerDelegate)? { get set }
```

#### Discussion

The popover controller uses its delegate to determine whether it should dismiss the popover and provides a notification when such an event occurs. For more information about the methods you can implement in your delegate, see [`UIPopoverControllerDelegate`](uipopovercontrollerdelegate.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/delegate)*