# alertViewCancel(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate before an alert view is canceled.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIAlertView`](../uialertview.md).

## Declaration

```swift
optional func alertViewCancel(_ alertView: UIAlertView)
```

```objc
- (void) alertViewCancel:(UIAlertView *) alertView;
```

#### Discussion

If the alert view’s delegate does not implement this method, clicking the cancel button is simulated and the alert view is dismissed. Implement this method if you need to perform some actions before an alert view is canceled. An alert view can be canceled at any time by the system—for example, when the user taps the Home button. The [`alertView(_:willDismissWithButtonIndex:)`](./alertview%28_,willdismisswithbuttonindex%29.md) and [`alertView(_:didDismissWithButtonIndex:)`](./alertview%28_,diddismisswithbuttonindex%29.md) methods are invoked after this method.

## Parameters

- `alertView`: The alert view that will be canceled.

## See Also

### Deprecated methods
- [func alertView(UIAlertView, clickedButtonAt: Int)](./alertview%28_,clickedbuttonat%29.md)
  Sent to the delegate when the user clicks a button on an alert view.
- [func alertViewShouldEnableFirstOtherButton(UIAlertView) -> Bool](./alertviewshouldenablefirstotherbutton%28_%29.md)
  Sent to the delegate to determine whether the first non-cancel button in the alert should be enabled.
- [func willPresent(UIAlertView)](./willpresent%28_%29.md)
  Sent to the delegate before a model view is presented to the user.
- [func didPresent(UIAlertView)](./didpresent%28_%29.md)
  Sent to the delegate after an alert view is presented to the user.
- [func alertView(UIAlertView, willDismissWithButtonIndex: Int)](./alertview%28_,willdismisswithbuttonindex%29.md)
  Sent to the delegate before an alert view is dismissed.
- [func alertView(UIAlertView, didDismissWithButtonIndex: Int)](./alertview%28_,diddismisswithbuttonindex%29.md)
  Sent to the delegate after an alert view is dismissed from the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertviewdelegate/alertviewcancel(_:))*