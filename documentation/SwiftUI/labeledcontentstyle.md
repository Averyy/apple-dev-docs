# LabeledContentStyle

**Framework**: SwiftUI  
**Kind**: protocol

The appearance and behavior of a labeled content instance..

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
@preconcurrency protocol LabeledContentStyle
```

#### Overview

Use [`labeledContentStyle(_:)`](view/labeledcontentstyle(_:).md) to set a style on a view.

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

### Getting built-in labeled content styles
- [static var automatic: AutomaticLabeledContentStyle](labeledcontentstyle/automatic.md)
  A labeled content style that resolves its appearance automatically based on the current context.
### Creating custom labeled content styles
- [func makeBody(configuration: Self.Configuration) -> Self.Body](labeledcontentstyle/makebody(configuration:).md)
  Creates a view that represents the body of labeled content.
- [LabeledContentStyle.Configuration](labeledcontentstyle/configuration.md)
  The properties of a labeled content instance.
- [associatedtype Body : View](labeledcontentstyle/body.md)
  A view that represents the appearance and behavior of labeled content.
### Supporting types
- [struct AutomaticLabeledContentStyle](automaticlabeledcontentstyle.md)
  The default labeled content style.

## Relationships

### Conforming Types
- [AutomaticLabeledContentStyle](automaticlabeledcontentstyle.md)

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
- [struct LabeledContentStyleConfiguration](labeledcontentstyleconfiguration.md)
  The properties of a labeled content instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/labeledcontentstyle)*