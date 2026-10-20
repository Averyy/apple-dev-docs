# actionSheet(_:clickedButtonAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate when the user clicks a button on an action sheet.

**Availability**:
- iOS 2.0+ - Deprecated in 8.3
- iPadOS 2.0+ - Deprecated in 8.3
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIActionSheet`](../uiactionsheet.md).

## Declaration

```swift
optional func actionSheet(_ actionSheet: UIActionSheet, clickedButtonAt buttonIndex: Int)
```

```objc
- (void) actionSheet:(UIActionSheet *) actionSheet clickedButtonAtIndex:(NSInteger) buttonIndex;
```

#### Discussion

The receiver is automatically dismissed after this method is invoked.

## Parameters

- `actionSheet`: The action sheet containing the button.
- `buttonIndex`: The position of the clicked button. The button indices start at `0`.

## See Also

### Deprecated methods
- [func willPresent(UIActionSheet)](./willpresent%28_%29.md)
  Sent to the delegate before an action sheet is presented to the user.
- [func didPresent(UIActionSheet)](./didpresent%28_%29.md)
  Sent to the delegate after an action sheet is presented to the user.
- [func actionSheet(UIActionSheet, willDismissWithButtonIndex: Int)](./actionsheet%28_,willdismisswithbuttonindex%29.md)
  Sent to the delegate before an action sheet is dismissed.
- [func actionSheet(UIActionSheet, didDismissWithButtonIndex: Int)](./actionsheet%28_,diddismisswithbuttonindex%29.md)
  Sent to the delegate after an action sheet is dismissed from the screen.
- [func actionSheetCancel(UIActionSheet)](./actionsheetcancel%28_%29.md)
  Sent to the delegate before an action sheet is canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/actionsheet(_:clickedbuttonat:))*