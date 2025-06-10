# ButtonRole

**Framework**: SwiftUI  
**Kind**: struct

A value that describes the purpose of a button.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct ButtonRole
```

#### Overview

A button role provides a description of a button’s purpose.  For example, the [`destructive`](buttonrole/destructive.md) role indicates that a button performs a destructive action, like delete user data:

```swift
Button("Delete", role: .destructive) { delete() }
```

## Topics

### Getting button roles
- [static let cancel: ButtonRole](buttonrole/cancel.md)
  A role that indicates a button that cancels an operation.
- [static let destructive: ButtonRole](buttonrole/destructive.md)
  A role that indicates a destructive button.
### Type Properties
- [static let close: ButtonRole](buttonrole/close.md)
  A role that indicates a button that closes the current operation.
- [static let confirm: ButtonRole](buttonrole/confirm.md)
  A role that indicates a button that confirms an operation.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct Button](button.md)
  A control that initiates an action.
- [func buttonStyle(_:)](view/buttonstyle(_:).md)
  Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [func buttonBorderShape(ButtonBorderShape) -> some View](view/buttonbordershape(_:).md)
  Sets the border shape for buttons in this view.
- [func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View](view/buttonrepeatbehavior(_:).md)
  Sets whether buttons in this view should repeatedly trigger their actions on prolonged interactions.
- [var buttonRepeatBehavior: ButtonRepeatBehavior](environmentvalues/buttonrepeatbehavior.md)
  Whether buttons with this associated environment should repeatedly trigger their actions on prolonged interactions.
- [struct ButtonBorderShape](buttonbordershape.md)
  A shape used to draw a button’s border.
- [struct ButtonRepeatBehavior](buttonrepeatbehavior.md)
  The options for controlling the repeatability of button actions.
- [struct ButtonSizing](buttonsizing.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/buttonrole)*