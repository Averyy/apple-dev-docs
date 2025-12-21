# controlWidgetStatus(_:)

**Framework**: SwiftUI  
**Kind**: method

The status of the control described by the modified label.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func controlWidgetStatus(_ status: LocalizedStringResource) -> some View
```

#### Discussion

This text appears in Control Center when your control’s state changes. You can customize the text by applying this modifier to the control’s value label:

```swift
// Status Text: "Do Not Disturb Until This Evening" / "Do Not Disturb Disabled"
ControlWidgetToggle("Do Not Disturb", ...) { isOn in
    Image(systemName: "moon")
        .controlWidgetStatus(isOn ? "Do Not Disturb Until This Evening" : "Do Not Disturb Disabled")
}
```

## Parameters

- `status`: The localized string resource to display.

## See Also

- [protocol ControlWidget](controlwidget.md)
  The configuration and content of a control widget to display in system spaces such as Control Center, the Lock Screen, and the Action Button.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/controlwidgetstatus(_:))*