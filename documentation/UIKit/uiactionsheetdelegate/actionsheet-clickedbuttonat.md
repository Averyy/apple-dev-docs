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
@MainActor
optional func actionSheet(_ actionSheet: UIActionSheet, clickedButtonAt buttonIndex: Int)
```

#### Discussion

The receiver is automatically dismissed after this method is invoked.

## Parameters

- `actionSheet`: The action sheet containing the button.
- `buttonIndex`: The position of the clicked button. The button indices start at  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheetdelegate/actionsheet(_:clickedbuttonat:))*