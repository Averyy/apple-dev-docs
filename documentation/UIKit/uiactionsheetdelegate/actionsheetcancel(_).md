# actionSheetCancel(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate before an action sheet is canceled.

**Availability**:
- iOS 2.0+ - Deprecated in 8.3
- iPadOS 2.0+ - Deprecated in 8.3
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIActionSheet`](../uiactionsheet.md).

## Declaration

```swift
optional func actionSheetCancel(_ actionSheet: UIActionSheet)
```

```objc
- (void) actionSheetCancel:(UIActionSheet *) actionSheet;
```

## Discussion

If the action sheet’s delegate does not implement this method, clicking the cancel button is simulated and the action sheet is dismissed. Implement this method if you need to perform some actions before an action sheet is canceled. An action sheet can be canceled at any time by the system—for example, when the user taps the Home button. The [`actionSheet(_:willDismissWithButtonIndex:)`](./actionsheet%28_,willdismisswithbuttonindex%29.md) and [`actionSheet(_:didDismissWithButtonIndex:)`](./actionsheet%28_,diddismisswithbuttonindex%29.md) methods are invoked after this method.

## Parameters

- `actionSheet`: The action sheet that will be canceled.

## See Also

### Deprecated methods
- [func actionSheet(UIActionSheet, clickedButtonAt: Int)](./actionsheet%28_,clickedbuttonat%29.md)
  Sent to the delegate when the user clicks a button on an action sheet.
- [func willPresent(UIActionSheet)](./willpresent%28_%29.md)
  Sent to the delegate before an action sheet is presented to the user.
- [func didPresent(UIActionSheet)](./didpresent%28_%29.md)
  Sent to the delegate after an action sheet is presented to the user.
- [func actionSheet(UIActionSheet, willDismissWithButtonIndex: Int)](./actionsheet%28_,willdismisswithbuttonindex%29.md)
  Sent to the delegate before an action sheet is dismissed.
- [func actionSheet(UIActionSheet, didDismissWithButtonIndex: Int)](./actionsheet%28_,diddismisswithbuttonindex%29.md)
  Sent to the delegate after an action sheet is dismissed from the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/actionsheetcancel(_:))*