# UIAlertAction

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An action that can be taken when the user taps a button in an alert.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIAlertAction
```

```objc
@interface UIAlertAction : NSObject
```

## Mentions

- [Getting the user’s attention with alerts and action sheets](./getting-the-user-s-attention-with-alerts-and-action-sheets.md)

#### Overview

You use this class to configure information about a single action, including the title to display in the button, any styling information, and a handler to execute when the user taps the button. After creating an alert action object, add it to a [`UIAlertController`](./uialertcontroller.md) object before displaying the corresponding alert to the user.

## Topics

### Creating an alert action
- [convenience init(title: String?, style: UIAlertAction.Style, handler: ((UIAlertAction) -> Void)?)](./uialertaction/init%28title,style,handler%29.md)
  Create and return an action with the specified title and behavior.
### Getting the action’s attributes
- [var title: String?](./uialertaction/title.md)
  The title of the action’s button.
- [var style: UIAlertAction.Style](./uialertaction/style-swift.property.md)
  The style that applies to the action’s button.
- [var isEnabled: Bool](./uialertaction/isenabled.md)
  A Boolean value indicating whether the action is currently enabled.
### Constants
- [UIAlertAction.Style](./uialertaction/style-swift.enum.md)
  Styles to apply to action buttons in an alert.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [UIAccessibilityIdentification](./uiaccessibilityidentification.md)

## See Also

### Alerts
- [Getting the user’s attention with alerts and action sheets](./getting-the-user-s-attention-with-alerts-and-action-sheets.md)
  Present important information to a person or prompt them about an important choice.
- [class UIAlertController](./uialertcontroller.md)
  An object that displays an alert message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uialertaction)*