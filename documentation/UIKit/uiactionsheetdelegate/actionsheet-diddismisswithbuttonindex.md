# actionSheet(_:didDismissWithButtonIndex:)

**Framework**: UIKit  
**Kind**: method

Sent to the delegate after an action sheet is dismissed from the screen.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func actionSheet(_ actionSheet: UIActionSheet, didDismissWithButtonIndex buttonIndex: Int)
```

#### Discussion

This method is invoked after the animation ends and the view is hidden.

## Parameters

- `actionSheet`: The action sheet that was dismissed.
- `buttonIndex`: The index of the button that was clicked. The button indices start at  . If this is the cancel button index, the action sheet is canceling. If  , the cancel button index is not set.

## See Also

- [func willPresent(UIActionSheet)](uiactionsheetdelegate/willpresent(_:).md)
  Sent to the delegate before an action sheet is presented to the user.
- [func didPresent(UIActionSheet)](uiactionsheetdelegate/didpresent(_:).md)
  Sent to the delegate after an action sheet is presented to the user.
- [func actionSheet(UIActionSheet, willDismissWithButtonIndex: Int)](uiactionsheetdelegate/actionsheet(_:willdismisswithbuttonindex:).md)
  Sent to the delegate before an action sheet is dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/actionsheet(_:diddismisswithbuttonindex:))*