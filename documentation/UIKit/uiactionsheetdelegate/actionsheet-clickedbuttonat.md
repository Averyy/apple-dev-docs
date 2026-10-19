# actionSheet(_:clickedButtonAt:)

**Framework**: UIKit  
**Kind**: method

Sent to the delegate when the user clicks a button on an action sheet.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func actionSheet(_ actionSheet: UIActionSheet, clickedButtonAt buttonIndex: Int)
```

#### Discussion

The receiver is automatically dismissed after this method is invoked.

## Parameters

- `actionSheet`: The action sheet containing the button.
- `buttonIndex`: The position of the clicked button. The button indices start at `0`.

## See Also

- [func willPresent(UIActionSheet)](uiactionsheetdelegate/willpresent(_:).md)
  Sent to the delegate before an action sheet is presented to the user.
- [func didPresent(UIActionSheet)](uiactionsheetdelegate/didpresent(_:).md)
  Sent to the delegate after an action sheet is presented to the user.
- [func actionSheet(UIActionSheet, willDismissWithButtonIndex: Int)](uiactionsheetdelegate/actionsheet(_:willdismisswithbuttonindex:).md)
  Sent to the delegate before an action sheet is dismissed.
- [func actionSheet(UIActionSheet, didDismissWithButtonIndex: Int)](uiactionsheetdelegate/actionsheet(_:diddismisswithbuttonindex:).md)
  Sent to the delegate after an action sheet is dismissed from the screen.
- [func actionSheetCancel(UIActionSheet)](uiactionsheetdelegate/actionsheetcancel(_:).md)
  Sent to the delegate before an action sheet is canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/actionsheet(_:clickedbuttonat:))*