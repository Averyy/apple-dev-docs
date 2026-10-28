# actionSheet(_:willDismissWithButtonIndex:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate before an action sheet is dismissed.

**Availability**:
- iOS 2.0+ - Deprecated in 8.3
- iPadOS 2.0+ - Deprecated in 8.3
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIActionSheet`](../uiactionsheet.md).

## Declaration

```swift
optional func actionSheet(_ actionSheet: UIActionSheet, willDismissWithButtonIndex buttonIndex: Int)
```

```objc
- (void) actionSheet:(UIActionSheet *) actionSheet willDismissWithButtonIndex:(NSInteger) buttonIndex;
```

## Discussion

This method is invoked before the animation begins and the view is hidden.

## Parameters

- `actionSheet`: The action sheet that is about to be dismissed.
- `buttonIndex`: The index of the button that was clicked. If this is the cancel button index, the action sheet is canceling. If `-1`, the cancel button index is not set.

## See Also

### Deprecated methods
- [func actionSheet(UIActionSheet, clickedButtonAt: Int)](./actionsheet%28_,clickedbuttonat%29.md)
  Sent to the delegate when the user clicks a button on an action sheet.
- [func willPresent(UIActionSheet)](./willpresent%28_%29.md)
  Sent to the delegate before an action sheet is presented to the user.
- [func didPresent(UIActionSheet)](./didpresent%28_%29.md)
  Sent to the delegate after an action sheet is presented to the user.
- [func actionSheet(UIActionSheet, didDismissWithButtonIndex: Int)](./actionsheet%28_,diddismisswithbuttonindex%29.md)
  Sent to the delegate after an action sheet is dismissed from the screen.
- [func actionSheetCancel(UIActionSheet)](./actionsheetcancel%28_%29.md)
  Sent to the delegate before an action sheet is canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/actionsheet(_:willdismisswithbuttonindex:))*