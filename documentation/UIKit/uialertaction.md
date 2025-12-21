# UIAlertAction

**Framework**: UIKit  
**Kind**: class

An action that can be taken when the user taps a button in an alert.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIAlertAction
```

## Mentions

- [Getting the user’s attention with alerts and action sheets](getting-the-user-s-attention-with-alerts-and-action-sheets.md)

#### Overview

You use this class to configure information about a single action, including the title to display in the button, any styling information, and a handler to execute when the user taps the button. After creating an alert action object, add it to a [`UIAlertController`](uialertcontroller.md) object before displaying the corresponding alert to the user.

## Topics

### Creating an alert action
- [convenience init(title: String?, style: UIAlertAction.Style, handler: ((UIAlertAction) -> Void)?)](uialertaction/init(title:style:handler:).md)
  Create and return an action with the specified title and behavior.
### Getting the action’s attributes
- [var title: String?](uialertaction/title.md)
  The title of the action’s button.
- [var style: UIAlertAction.Style](uialertaction/style-swift.property.md)
  The style that applies to the action’s button.
- [var isEnabled: Bool](uialertaction/isenabled.md)
  A Boolean value indicating whether the action is currently enabled.
### Constants
- [UIAlertAction.Style](uialertaction/style-swift.enum.md)
  Styles to apply to action buttons in an alert.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)

## See Also

- [Getting the user’s attention with alerts and action sheets](getting-the-user-s-attention-with-alerts-and-action-sheets.md)
  Present important information to a person or prompt them about an important choice.
- [class UIAlertController](uialertcontroller.md)
  An object that displays an alert message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertaction)*