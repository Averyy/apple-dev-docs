# EmptyControlWidgetConfiguration

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

An empty control widget configuration.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@MainActor
@frozen @preconcurrency struct EmptyControlWidgetConfiguration
```

## Topics

### Initializers
- [init()](./emptycontrolwidgetconfiguration/init%28%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [ControlWidgetConfiguration](./controlwidgetconfiguration.md)
- [Copyable](../Swift/copyable.md)

## See Also

### Composing control widgets
- [protocol ControlWidget](./controlwidget.md)
  The configuration and content of a control widget to display in system spaces such as Control Center, the Lock Screen, and the Action Button.
- [protocol ControlWidgetConfiguration](./controlwidgetconfiguration.md)
  A type that describes a control widget’s content.
- [struct ControlWidgetConfigurationBuilder](./controlwidgetconfigurationbuilder.md)
  A custom attribute that constructs a control widget’s body.
- [protocol ControlWidgetTemplate](./controlwidgettemplate.md)
  A type that describes a control widget’s content.
- [struct EmptyControlWidgetTemplate](./emptycontrolwidgettemplate.md)
  An empty control widget template.
- [struct ControlWidgetTemplateBuilder](./controlwidgettemplatebuilder.md)
  A custom attribute that constructs a control widget template’s body.
- [func controlWidgetActionHint(_:)](./view/controlwidgetactionhint%28_%29.md)
  The action hint of the control described by the modified label.
- [func controlWidgetStatus(_:)](./view/controlwidgetstatus%28_%29.md)
  The status of the control described by the modified label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/emptycontrolwidgetconfiguration)*