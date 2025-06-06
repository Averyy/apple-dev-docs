# willPresent(_:)

**Framework**: UIKit  
**Kind**: method

Sent to the delegate before a model view is presented to the user.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func willPresent(_ alertView: UIAlertView)
```

## Parameters

- `alertView`: The alert view that is about to be displayed.

## See Also

- [func alertViewShouldEnableFirstOtherButton(UIAlertView) -> Bool](uialertviewdelegate/alertviewshouldenablefirstotherbutton(_:).md)
  Sent to the delegate to determine whether the first non-cancel button in the alert should be enabled.
- [func didPresent(UIAlertView)](uialertviewdelegate/didpresent(_:).md)
  Sent to the delegate after an alert view is presented to the user.
- [func alertView(UIAlertView, willDismissWithButtonIndex: Int)](uialertviewdelegate/alertview(_:willdismisswithbuttonindex:).md)
  Sent to the delegate before an alert view is dismissed.
- [func alertView(UIAlertView, didDismissWithButtonIndex: Int)](uialertviewdelegate/alertview(_:diddismisswithbuttonindex:).md)
  Sent to the delegate after an alert view is dismissed from the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertviewdelegate/willpresent(_:))*