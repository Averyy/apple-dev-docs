# title

**Framework**: UIKit  
**Kind**: property

The title of the alert.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var title: String? { get set }
```

#### Discussion

The title string is displayed prominently in the alert or action sheet. You should use this string to get the user’s attention and communicate the reason for displaying the alert.

## See Also

- [var message: String?](uialertcontroller/message.md)
  Descriptive text that provides more details about the reason for the alert.
- [var preferredStyle: UIAlertController.Style](uialertcontroller/preferredstyle.md)
  The style of the alert controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertcontroller/title)*