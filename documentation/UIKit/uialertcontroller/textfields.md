# textFields

**Framework**: UIKit  
**Kind**: property

The array of text fields displayed by the alert.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var textFields: [UITextField]? { get }
```

#### Discussion

Use this property to access the text fields displayed by the alert. The text fields are in the order in which you added them to the alert controller. This order also corresponds to the order in which they are displayed in the alert.

## See Also

- [func addTextField(configurationHandler: ((UITextField) -> Void)?)](uialertcontroller/addtextfield(configurationhandler:).md)
  Adds a text field to an alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertcontroller/textfields)*