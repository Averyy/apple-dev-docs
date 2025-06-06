# alertViewCancel(_:)

**Framework**: UIKit  
**Kind**: method

Sent to the delegate before an alert view is canceled.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func alertViewCancel(_ alertView: UIAlertView)
```

#### Discussion

If the alert view’s delegate does not implement this method, clicking the cancel button is simulated and the alert view is dismissed. Implement this method if you need to perform some actions before an alert view is canceled. An alert view can be canceled at any time by the system—for example, when the user taps the Home button. The [`alertView(_:willDismissWithButtonIndex:)`](uialertviewdelegate/alertview(_:willdismisswithbuttonindex:).md) and [`alertView(_:didDismissWithButtonIndex:)`](uialertviewdelegate/alertview(_:diddismisswithbuttonindex:).md) methods are invoked after this method.

## Parameters

- `alertView`: The alert view that will be canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertviewdelegate/alertviewcancel(_:))*