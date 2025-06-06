# preferredStyle

**Framework**: UIKit  
**Kind**: property

The style of the alert controller.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var preferredStyle: UIAlertController.Style { get }
```

#### Discussion

The value of this property is set to the value you specified in the [`init(title:message:preferredStyle:)`](uialertcontroller/init(title:message:preferredstyle:).md) method. This value determines how the alert is displayed onscreen.

## See Also

- [var title: String?](uialertcontroller/title.md)
  The title of the alert.
- [var message: String?](uialertcontroller/message.md)
  Descriptive text that provides more details about the reason for the alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertcontroller/preferredstyle)*