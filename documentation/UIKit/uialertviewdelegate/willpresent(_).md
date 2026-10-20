# willPresent(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate before a model view is presented to the user.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIAlertView`](../uialertview.md).

## Declaration

```swift
optional func willPresent(_ alertView: UIAlertView)
```

```objc
- (void) willPresentAlertView:(UIAlertView *) alertView;
```

## Parameters

- `alertView`: The alert view that is about to be displayed.

## See Also

### Deprecated methods
- [func alertView(UIAlertView, clickedButtonAt: Int)](./alertview%28_,clickedbuttonat%29.md)
  Sent to the delegate when the user clicks a button on an alert view.
- [func alertViewShouldEnableFirstOtherButton(UIAlertView) -> Bool](./alertviewshouldenablefirstotherbutton%28_%29.md)
  Sent to the delegate to determine whether the first non-cancel button in the alert should be enabled.
- [func didPresent(UIAlertView)](./didpresent%28_%29.md)
  Sent to the delegate after an alert view is presented to the user.
- [func alertView(UIAlertView, willDismissWithButtonIndex: Int)](./alertview%28_,willdismisswithbuttonindex%29.md)
  Sent to the delegate before an alert view is dismissed.
- [func alertView(UIAlertView, didDismissWithButtonIndex: Int)](./alertview%28_,diddismisswithbuttonindex%29.md)
  Sent to the delegate after an alert view is dismissed from the screen.
- [func alertViewCancel(UIAlertView)](./alertviewcancel%28_%29.md)
  Sent to the delegate before an alert view is canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertviewdelegate/willpresent(_:))*