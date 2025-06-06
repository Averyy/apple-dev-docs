# FormStyle

**Framework**: SwiftUI  
**Kind**: protocol

The appearance and behavior of a form.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol FormStyle
```

#### Overview

To configure the style for a single [`Form`](form.md) or for all form instances in a view hierarchy, use the [`formStyle(_:)`](view/formstyle(_:).md) modifier.

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

### Getting built-in form styles
- [static var automatic: AutomaticFormStyle](formstyle/automatic.md)
  The default form style.
- [static var columns: ColumnsFormStyle](formstyle/columns.md)
  A non-scrolling form style with a trailing aligned column of labels next to a leading aligned column of values.
- [static var grouped: GroupedFormStyle](formstyle/grouped.md)
  A form style with grouped rows.
### Creating custom form styles
- [func makeBody(configuration: Self.Configuration) -> Self.Body](formstyle/makebody(configuration:).md)
  Creates a view that represents the body of a form.
- [FormStyle.Configuration](formstyle/configuration.md)
  The properties of a form instance.
- [associatedtype Body : View](formstyle/body.md)
  A view that represents the appearance and interaction of a form.
### Supporting types
- [struct AutomaticFormStyle](automaticformstyle.md)
  The default form style.
- [struct ColumnsFormStyle](columnsformstyle.md)
  A non-scrolling form style with a trailing aligned column of labels next to a leading aligned column of values.
- [struct GroupedFormStyle](groupedformstyle.md)
  A form style with grouped rows.

## Relationships

### Conforming Types
- [AutomaticFormStyle](automaticformstyle.md)
- [ColumnsFormStyle](columnsformstyle.md)
- [GroupedFormStyle](groupedformstyle.md)

## See Also

- [func controlGroupStyle<S>(S) -> some View](view/controlgroupstyle(_:).md)
  Sets the style for control groups within this view.
- [protocol ControlGroupStyle](controlgroupstyle.md)
  Defines the implementation of all control groups within a view hierarchy.
- [struct ControlGroupStyleConfiguration](controlgroupstyleconfiguration.md)
  The properties of a control group.
- [func formStyle<S>(S) -> some View](view/formstyle(_:).md)
  Sets the style for forms in a view hierarchy.
- [struct FormStyleConfiguration](formstyleconfiguration.md)
  The properties of a form instance.
- [func groupBoxStyle<S>(S) -> some View](view/groupboxstyle(_:).md)
  Sets the style for group boxes within this view.
- [protocol GroupBoxStyle](groupboxstyle.md)
  A type that specifies the appearance and interaction of all group boxes within a view hierarchy.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/formstyle)*