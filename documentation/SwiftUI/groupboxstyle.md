# GroupBoxStyle

**Framework**: SwiftUI  
**Kind**: protocol

A type that specifies the appearance and interaction of all group boxes within a view hierarchy.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol GroupBoxStyle
```

#### Overview

To configure the current `GroupBoxStyle` for a view hierarchy, use the [`groupBoxStyle(_:)`](view/groupboxstyle(_:).md) modifier.

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

### Getting built-in group box styles
- [static var automatic: DefaultGroupBoxStyle](groupboxstyle/automatic.md)
  The default style for group box views.
### Creating custom group box styles
- [func makeBody(configuration: Self.Configuration) -> Self.Body](groupboxstyle/makebody(configuration:).md)
  Creates a view representing the body of a group box.
- [GroupBoxStyle.Configuration](groupboxstyle/configuration.md)
  The properties of a group box instance.
- [associatedtype Body : View](groupboxstyle/body.md)
  A view that represents the body of a group box.
### Supporting types
- [struct DefaultGroupBoxStyle](defaultgroupboxstyle.md)
  The default style for group box views.

## Relationships

### Conforming Types
- [DefaultGroupBoxStyle](defaultgroupboxstyle.md)

## See Also

- [func controlGroupStyle<S>(S) -> some View](view/controlgroupstyle(_:).md)
  Sets the style for control groups within this view.
- [protocol ControlGroupStyle](controlgroupstyle.md)
  Defines the implementation of all control groups within a view hierarchy.
- [struct ControlGroupStyleConfiguration](controlgroupstyleconfiguration.md)
  The properties of a control group.
- [func formStyle<S>(S) -> some View](view/formstyle(_:).md)
  Sets the style for forms in a view hierarchy.
- [protocol FormStyle](formstyle.md)
  The appearance and behavior of a form.
- [struct FormStyleConfiguration](formstyleconfiguration.md)
  The properties of a form instance.
- [func groupBoxStyle<S>(S) -> some View](view/groupboxstyle(_:).md)
  Sets the style for group boxes within this view.
- [struct GroupBoxStyleConfiguration](groupboxstyleconfiguration.md)
  The properties of a group box instance.
- [func indexViewStyle<S>(S) -> some View](view/indexviewstyle(_:).md)
  Sets the style for the index view within the current environment.
- [protocol IndexViewStyle](indexviewstyle.md)
  Defines the implementation of all `IndexView` instances within a view hierarchy.
- [func labeledContentStyle<S>(S) -> some View](view/labeledcontentstyle(_:).md)
  Sets a style for labeled content.
- [protocol LabeledContentStyle](labeledcontentstyle.md)
  The appearance and behavior of a labeled content instance..
- [struct LabeledContentStyleConfiguration](labeledcontentstyleconfiguration.md)
  The properties of a labeled content instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/groupboxstyle)*