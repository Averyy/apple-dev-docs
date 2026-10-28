# actionSheet(_:didDismissWithButtonIndex:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate after an action sheet is dismissed from the screen.

**Availability**:
- iOS 2.0+ - Deprecated in 8.3
- iPadOS 2.0+ - Deprecated in 8.3
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIActionSheet`](../uiactionsheet.md).

## Declaration

```swift
optional func actionSheet(_ actionSheet: UIActionSheet, didDismissWithButtonIndex buttonIndex: Int)
```

```objc
- (void) actionSheet:(UIActionSheet *) actionSheet didDismissWithButtonIndex:(NSInteger) buttonIndex;
```

## Discussion

This method is invoked after the animation ends and the view is hidden.

## Parameters

- `actionSheet`: The action sheet that was dismissed.
- `buttonIndex`: The index of the button that was clicked. The button indices start at `0`. If this is the cancel button index, the action sheet is canceling. If `-1`, the cancel button index is not set.

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
- [func actionSheetCancel(UIActionSheet)](./actionsheetcancel%28_%29.md)
  Sent to the delegate before an action sheet is canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/actionsheet(_:diddismisswithbuttonindex:))*