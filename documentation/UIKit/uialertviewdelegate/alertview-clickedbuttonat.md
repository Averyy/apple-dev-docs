# alertView(_:clickedButtonAt:)

**Framework**: UIKit  
**Kind**: method

Sent to the delegate when the user clicks a button on an alert view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func alertView(_ alertView: UIAlertView, clickedButtonAt buttonIndex: Int)
```

#### Discussion

The receiver is automatically dismissed after this method is invoked.

## Parameters

- `alertView`: The alert view containing the button.
- `buttonIndex`: The index of the button that was clicked. The button indices start at  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertviewdelegate/alertview(_:clickedbuttonat:))*