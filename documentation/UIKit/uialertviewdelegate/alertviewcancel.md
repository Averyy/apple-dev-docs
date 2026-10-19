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
optional func alertViewCancel(_ alertView: UIAlertView)
```

#### Discussion

If the alert view’s delegate does not implement this method, clicking the cancel button is simulated and the alert view is dismissed. Implement this method if you need to perform some actions before an alert view is canceled. An alert view can be canceled at any time by the system—for example, when the user taps the Home button. The [`alertView(_:willDismissWithButtonIndex:)`](uialertviewdelegate/alertview(_:willdismisswithbuttonindex:).md) and [`alertView(_:didDismissWithButtonIndex:)`](uialertviewdelegate/alertview(_:diddismisswithbuttonindex:).md) methods are invoked after this method.

## Parameters

- `alertView`: The alert view that will be canceled.

## See Also

- [func alertView(UIAlertView, clickedButtonAt: Int)](uialertviewdelegate/alertview(_:clickedbuttonat:).md)
  Sent to the delegate when the user clicks a button on an alert view.
- [func alertViewShouldEnableFirstOtherButton(UIAlertView) -> Bool](uialertviewdelegate/alertviewshouldenablefirstotherbutton(_:).md)
  Sent to the delegate to determine whether the first non-cancel button in the alert should be enabled.
- [func willPresent(UIAlertView)](uialertviewdelegate/willpresent(_:).md)
  Sent to the delegate before a model view is presented to the user.
- [func didPresent(UIAlertView)](uialertviewdelegate/didpresent(_:).md)
  Sent to the delegate after an alert view is presented to the user.
- [func alertView(UIAlertView, willDismissWithButtonIndex: Int)](uialertviewdelegate/alertview(_:willdismisswithbuttonindex:).md)
  Sent to the delegate before an alert view is dismissed.
- [func alertView(UIAlertView, didDismissWithButtonIndex: Int)](uialertviewdelegate/alertview(_:diddismisswithbuttonindex:).md)
  Sent to the delegate after an alert view is dismissed from the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertviewdelegate/alertviewcancel(_:))*