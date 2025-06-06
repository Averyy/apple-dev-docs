# actionSheetCancel(_:)

**Framework**: UIKit  
**Kind**: method

Sent to the delegate before an action sheet is canceled.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func actionSheetCancel(_ actionSheet: UIActionSheet)
```

#### Discussion

If the action sheet’s delegate does not implement this method, clicking the cancel button is simulated and the action sheet is dismissed. Implement this method if you need to perform some actions before an action sheet is canceled. An action sheet can be canceled at any time by the system—for example, when the user taps the Home button. The [`actionSheet(_:willDismissWithButtonIndex:)`](uiactionsheetdelegate/actionsheet(_:willdismisswithbuttonindex:).md) and [`actionSheet(_:didDismissWithButtonIndex:)`](uiactionsheetdelegate/actionsheet(_:diddismisswithbuttonindex:).md) methods are invoked after this method.

## Parameters

- `actionSheet`: The action sheet that will be canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/actionsheetcancel(_:))*