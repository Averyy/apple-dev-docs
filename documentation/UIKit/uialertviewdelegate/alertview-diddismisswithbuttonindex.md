# alertView(_:didDismissWithButtonIndex:)

**Framework**: UIKit  
**Kind**: method

Sent to the delegate after an alert view is dismissed from the screen.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func alertView(_ alertView: UIAlertView, didDismissWithButtonIndex buttonIndex: Int)
```

#### Discussion

This method is invoked after the animation ends and the view is hidden.

## Parameters

- `alertView`: The alert view that was dismissed.
- `buttonIndex`: The index of the button that was clicked. The button indices start at  . If this is the cancel button index, the alert view is canceling. If  , the cancel button index is not set.

## See Also

- [func alertViewShouldEnableFirstOtherButton(UIAlertView) -> Bool](uialertviewdelegate/alertviewshouldenablefirstotherbutton(_:).md)
  Sent to the delegate to determine whether the first non-cancel button in the alert should be enabled.
- [func willPresent(UIAlertView)](uialertviewdelegate/willpresent(_:).md)
  Sent to the delegate before a model view is presented to the user.
- [func didPresent(UIAlertView)](uialertviewdelegate/didpresent(_:).md)
  Sent to the delegate after an alert view is presented to the user.
- [func alertView(UIAlertView, willDismissWithButtonIndex: Int)](uialertviewdelegate/alertview(_:willdismisswithbuttonindex:).md)
  Sent to the delegate before an alert view is dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertviewdelegate/alertview(_:diddismisswithbuttonindex:))*