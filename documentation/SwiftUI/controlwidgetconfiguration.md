# ControlWidgetConfiguration

**Framework**: SwiftUI  
**Kind**: protocol

A type that describes a control widget’s content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency protocol ControlWidgetConfiguration
```

#### Overview

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
- [associatedtype Body : ControlWidgetConfiguration](controlwidgetconfiguration/body-swift.associatedtype.md)
  The type of control widget configuration representing the body of this configuration.
### Instance Properties
- [var body: Self.Body](controlwidgetconfiguration/body-swift.property.md)
  The content and behavior of the control.
### Instance Methods
- [func description(LocalizedStringResource) -> some ControlWidgetConfiguration](controlwidgetconfiguration/description(_:).md)
  Sets the description shown for the control when a user adds or edits it, using the specified string.
- [func displayName(LocalizedStringResource) -> some ControlWidgetConfiguration](controlwidgetconfiguration/displayname(_:).md)
  Sets the name shown for the control when a user adds or edits it, using the specified string.
- [func promptsForUserConfiguration() -> some ControlWidgetConfiguration](controlwidgetconfiguration/promptsforuserconfiguration.md)
  Specifies that a control’s configuration UI should be automatically presented after the widget is added.
- [func pushHandler(any ControlPushHandler.Type) -> some ControlWidgetConfiguration](controlwidgetconfiguration/pushhandler(_:).md)
  Register a type that can handle push tokens changing for controls of this type.

## Relationships

### Conforming Types
- [EmptyControlWidgetConfiguration](emptycontrolwidgetconfiguration.md)

## See Also

- [protocol ControlWidget](controlwidget.md)
  The configuration and content of a control widget to display in system spaces such as Control Center, the Lock Screen, and the Action Button.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlwidgetconfiguration)*