# message

**Framework**: UIKit  
**Kind**: property

Descriptive text that provides more details about the reason for the alert.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var message: String? { get set }
```

#### Discussion

The message string is displayed below the title string and is less prominent. Use this string to provide additional context about the reason for the alert or about the actions that the user might take.

## See Also

- [var title: String?](uialertcontroller/title.md)
  The title of the alert.
- [var preferredStyle: UIAlertController.Style](uialertcontroller/preferredstyle.md)
  The style of the alert controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertcontroller/message)*