# ButtonBorderShape

**Framework**: SwiftUI  
**Kind**: struct

A shape used to draw a button’s border.

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
struct ButtonBorderShape
```

#### Overview

Use the [`buttonBorderShape(_:)`](view/buttonbordershape(_:).md) view modifier to apply the shape to bordered buttons within a view hierarchy.

## Topics

### Getting border shapes
- [static let automatic: ButtonBorderShape](buttonbordershape/automatic.md)
  A shape that defers to the system to determine an appropriate shape for the given context and platform.
- [static let capsule: ButtonBorderShape](buttonbordershape/capsule.md)
  A capsule shape.
- [static let circle: ButtonBorderShape](buttonbordershape/circle.md)
  A circular shape.
- [static let roundedRectangle: ButtonBorderShape](buttonbordershape/roundedrectangle.md)
  A rounded rectangle shape.
- [static func roundedRectangle(radius: CGFloat) -> ButtonBorderShape](buttonbordershape/roundedrectangle(radius:).md)
  A rounded rectangle shape.

## Relationships

### Conforms To
- [Animatable](animatable.md)
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [InsettableShape](insettableshape.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [Shape](shape.md)
- [View](view.md)

## See Also

- [struct Button](button.md)
  A control that initiates an action.
- [func buttonStyle(_:)](view/buttonstyle(_:).md)
  Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [func buttonBorderShape(ButtonBorderShape) -> some View](view/buttonbordershape(_:).md)
  Sets the border shape for buttons in this view.
- [func buttonRepeatBehavior(ButtonRepeatBehavior) -> some View](view/buttonrepeatbehavior(_:).md)
  Sets whether buttons in this view should repeatedly trigger their actions on prolonged interactions.
- [struct ButtonRepeatBehavior](buttonrepeatbehavior.md)
  The options for controlling the repeatability of button actions.
- [var buttonRepeatBehavior: ButtonRepeatBehavior](environmentvalues/buttonrepeatbehavior.md)
  Whether buttons with this associated environment should repeatedly trigger their actions on prolonged interactions.
- [func buttonSizing(ButtonSizing) -> some View](view/buttonsizing(_:).md)
  The preferred sizing behavior of buttons in the view hierarchy.
- [struct ButtonSizing](buttonsizing.md)
  The sizing behavior of `Button`s and other button-like controls.
- [struct ButtonRole](buttonrole.md)
  A value that describes the purpose of a button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/buttonbordershape)*