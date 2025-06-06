# preferredAction

**Framework**: UIKit  
**Kind**: property

The preferred action for the user to take from an alert.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var preferredAction: UIAlertAction? { get set }
```

#### Discussion

The preferred action is relevant for the [`UIAlertController.Style.alert`](uialertcontroller/style/alert.md) style only; it isn’t used by action sheets. When you specify a preferred action, the alert controller highlights the text of that action to give it emphasis. (If the alert also contains a cancel button, the preferred action receives the highlighting instead of the cancel button.) If the iOS device is connected to a physical keyboard, pressing the Return key triggers the preferred action.

The action object you assign to this property must have already been added to the alert controller’s list of actions. Assigning an object to this property before adding it with the [`addAction(_:)`](uialertcontroller/addaction(_:).md) method is a programmer error.

The default value of this property is `nil`.

## See Also

- [func addAction(UIAlertAction)](uialertcontroller/addaction(_:).md)
  Attaches an action object to the alert or action sheet.
- [var actions: [UIAlertAction]](uialertcontroller/actions.md)
  The actions that the user can take in response to the alert or action sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertcontroller/preferredaction)*