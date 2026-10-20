# alertView(_:clickedButtonAt:)

**Framework**: UIKit  
**Kind**: method

Sent to the delegate when the user clicks a button on an alert view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func alertView(_ alertView: UIAlertView, clickedButtonAt buttonIndex: Int)
```

#### Discussion

The receiver is automatically dismissed after this method is invoked.

## Parameters

- `alertView`: The alert view containing the button.
- `buttonIndex`: The index of the button that was clicked. The button indices start at `0`.

## See Also

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
- [func alertViewCancel(UIAlertView)](uialertviewdelegate/alertviewcancel(_:).md)
  Sent to the delegate before an alert view is canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertviewdelegate/alertview(_:clickedbuttonat:))*