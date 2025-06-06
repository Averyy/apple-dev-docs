# ControlWidget

**Framework**: SwiftUI  
**Kind**: protocol

The configuration and content of a control widget to display in system spaces such as Control Center, the Lock Screen, and the Action Button.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol ControlWidget
```

#### Overview

Controls allow users to quickly read the state of your app or its accessories, and take quick actions, without having to open your app. Users can add, configure, and arrange controls to suit their individual needs. You can provide multiple types of controls, each representing a specific kind of action.

There are three key components to a control:

- A configuration that determines whether the control is configurable, identifies the control, and defines the SwiftUI template that provides the control’s content.
- A value provider that defines the value of the control when being previewed and when being actually rendered
- The template used by WidgetKit to display the control.

Controls are defined using templates in order to ensure that they control will work at all sizes and in all system spaces in which they might be displayed. These templates define images (specifically, symbol images) and text using simple SwiftUI views like [`Label`](label.md), [`Text`](text.md), and [`Image`](image.md); and tint colors using the [`tint(_:)`](controlwidgettemplate/tint(_:).md) modifier.

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Topics

### Associated Types
- [associatedtype Body : ControlWidgetConfiguration](controlwidget/body-swift.associatedtype.md)
  The type of configuration representing the content of this control.
### Initializers
- [init()](controlwidget/init.md)
  Creates a control using `body` as its content.
### Instance Properties
- [var body: Self.Body](controlwidget/body-swift.property.md)
  The content and behavior of the control.
### Type Methods
- [static func main()](controlwidget/main.md)

## See Also

- [protocol ControlWidgetConfiguration](controlwidgetconfiguration.md)
  A type that describes a control widget’s content.
- [struct EmptyControlWidgetConfiguration](emptycontrolwidgetconfiguration.md)
  An empty control widget configuration.
- [struct ControlWidgetConfigurationBuilder](controlwidgetconfigurationbuilder.md)
  A custom attribute that constructs a control widget’s body.
- [protocol ControlWidgetTemplate](controlwidgettemplate.md)
  A type that describes a control widget’s content.
- [struct EmptyControlWidgetTemplate](emptycontrolwidgettemplate.md)
  An empty control widget template.
- [struct ControlWidgetTemplateBuilder](controlwidgettemplatebuilder.md)
  A custom attribute that constructs a control widget template’s body.
- [func controlWidgetActionHint(_:)](view/controlwidgetactionhint(_:).md)
  The action hint of the control described by the modified label.
- [func controlWidgetStatus(_:)](view/controlwidgetstatus(_:).md)
  The status of the control described by the modified label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlwidget)*