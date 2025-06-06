# actionSheet(_:willDismissWithButtonIndex:)

**Framework**: UIKit  
**Kind**: method

Sent to the delegate before an action sheet is dismissed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func actionSheet(_ actionSheet: UIActionSheet, willDismissWithButtonIndex buttonIndex: Int)
```

#### Discussion

This method is invoked before the animation begins and the view is hidden.

## Parameters

- `actionSheet`: The action sheet that is about to be dismissed.
- `buttonIndex`: The index of the button that was clicked. If this is the cancel button index, the action sheet is canceling. If  , the cancel button index is not set.

## See Also

- [func willPresent(UIActionSheet)](uiactionsheetdelegate/willpresent(_:).md)
  Sent to the delegate before an action sheet is presented to the user.
- [func didPresent(UIActionSheet)](uiactionsheetdelegate/didpresent(_:).md)
  Sent to the delegate after an action sheet is presented to the user.
- [func actionSheet(UIActionSheet, didDismissWithButtonIndex: Int)](uiactionsheetdelegate/actionsheet(_:diddismisswithbuttonindex:).md)
  Sent to the delegate after an action sheet is dismissed from the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/actionsheet(_:willdismisswithbuttonindex:))*