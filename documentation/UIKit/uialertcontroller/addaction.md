# addAction(_:)

**Framework**: UIKit  
**Kind**: method

Attaches an action object to the alert or action sheet.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addAction(_ action: UIAlertAction)
```

#### Discussion

If your alert has multiple actions, the order in which you add those actions determines their order in the resulting alert or action sheet.

## Parameters

- `action`: The action object to display as part of the alert. Actions are displayed as buttons in the alert. The action object provides the button text and the action to be performed when that button is tapped.

## See Also

- [var actions: [UIAlertAction]](uialertcontroller/actions.md)
  The actions that the user can take in response to the alert or action sheet.
- [var preferredAction: UIAlertAction?](uialertcontroller/preferredaction.md)
  The preferred action for the user to take from an alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertcontroller/addaction(_:))*