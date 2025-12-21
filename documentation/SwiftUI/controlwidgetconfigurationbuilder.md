# ControlWidgetConfigurationBuilder

**Framework**: SwiftUI  
**Kind**: struct

A custom attribute that constructs a control widget’s body.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@resultBuilder
struct ControlWidgetConfigurationBuilder
```

#### Overview

The `@ControlWidgetConfigurationBuilder` attribute allows your control widget’s body closure to produce a control widget configuration after zero or more other statements:

```swift
struct GarageDoorOpener: ControlWidget {
    var body: some ControlWidgetConfiguration {
        let kind = "com.yourcompany.GarageDoorOpener"

        StaticControlConfiguration(
            kind: kind
        ) {
            ...
        }
    }
}
```

## Topics

### Type Methods
- [static func buildBlock<Content>(Content) -> some ControlWidgetConfiguration](controlwidgetconfigurationbuilder/buildblock(_:).md)
  Passes a single control widget configuration written as a child control through unmodified.
- [static func buildExpression<Content>(Content) -> Content](controlwidgetconfigurationbuilder/buildexpression(_:).md)
  Builds an expression within the builder.

## See Also

- [protocol ControlWidget](controlwidget.md)
  The configuration and content of a control widget to display in system spaces such as Control Center, the Lock Screen, and the Action Button.
- [protocol ControlWidgetConfiguration](controlwidgetconfiguration.md)
  A type that describes a control widget’s content.
- [struct EmptyControlWidgetConfiguration](emptycontrolwidgetconfiguration.md)
  An empty control widget configuration.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlwidgetconfigurationbuilder)*