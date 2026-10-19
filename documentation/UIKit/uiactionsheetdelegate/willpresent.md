# willPresent(_:)

**Framework**: UIKit  
**Kind**: method

Sent to the delegate before an action sheet is presented to the user.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func willPresent(_ actionSheet: UIActionSheet)
```

## Parameters

- `actionSheet`: The action sheet that is about to be displayed.

## See Also

- [func actionSheet(UIActionSheet, clickedButtonAt: Int)](uiactionsheetdelegate/actionsheet(_:clickedbuttonat:).md)
  Sent to the delegate when the user clicks a button on an action sheet.
- [func didPresent(UIActionSheet)](uiactionsheetdelegate/didpresent(_:).md)
  Sent to the delegate after an action sheet is presented to the user.
- [func actionSheet(UIActionSheet, willDismissWithButtonIndex: Int)](uiactionsheetdelegate/actionsheet(_:willdismisswithbuttonindex:).md)
  Sent to the delegate before an action sheet is dismissed.
- [func actionSheet(UIActionSheet, didDismissWithButtonIndex: Int)](uiactionsheetdelegate/actionsheet(_:diddismisswithbuttonindex:).md)
  Sent to the delegate after an action sheet is dismissed from the screen.
- [func actionSheetCancel(UIActionSheet)](uiactionsheetdelegate/actionsheetcancel(_:).md)
  Sent to the delegate before an action sheet is canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/willpresent(_:))*