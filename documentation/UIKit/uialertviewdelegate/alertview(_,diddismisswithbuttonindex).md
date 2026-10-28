# alertView(_:didDismissWithButtonIndex:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate after an alert view is dismissed from the screen.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIAlertView`](../uialertview.md).

## Declaration

```swift
optional func alertView(_ alertView: UIAlertView, didDismissWithButtonIndex buttonIndex: Int)
```

```objc
- (void) alertView:(UIAlertView *) alertView didDismissWithButtonIndex:(NSInteger) buttonIndex;
```

## Discussion

This method is invoked after the animation ends and the view is hidden.

## Parameters

- `alertView`: The alert view that was dismissed.
- `buttonIndex`: The index of the button that was clicked. The button indices start at `0`. If this is the cancel button index, the alert view is canceling. If `-1`, the cancel button index is not set.

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
- [func alertViewCancel(UIAlertView)](./alertviewcancel%28_%29.md)
  Sent to the delegate before an alert view is canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertviewdelegate/alertview(_:diddismisswithbuttonindex:))*