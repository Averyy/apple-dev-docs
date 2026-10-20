# willPresent(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate before an action sheet is presented to the user.

**Availability**:
- iOS 2.0+ - Deprecated in 8.3
- iPadOS 2.0+ - Deprecated in 8.3
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIActionSheet`](../uiactionsheet.md).

## Declaration

```swift
optional func willPresent(_ actionSheet: UIActionSheet)
```

```objc
- (void) willPresentActionSheet:(UIActionSheet *) actionSheet;
```

## Parameters

- `actionSheet`: The action sheet that is about to be displayed.

## See Also

### Deprecated methods
- [func actionSheet(UIActionSheet, clickedButtonAt: Int)](./actionsheet%28_,clickedbuttonat%29.md)
  Sent to the delegate when the user clicks a button on an action sheet.
- [func didPresent(UIActionSheet)](./didpresent%28_%29.md)
  Sent to the delegate after an action sheet is presented to the user.
- [func actionSheet(UIActionSheet, willDismissWithButtonIndex: Int)](./actionsheet%28_,willdismisswithbuttonindex%29.md)
  Sent to the delegate before an action sheet is dismissed.
- [func actionSheet(UIActionSheet, didDismissWithButtonIndex: Int)](./actionsheet%28_,diddismisswithbuttonindex%29.md)
  Sent to the delegate after an action sheet is dismissed from the screen.
- [func actionSheetCancel(UIActionSheet)](./actionsheetcancel%28_%29.md)
  Sent to the delegate before an action sheet is canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/willpresent(_:))*