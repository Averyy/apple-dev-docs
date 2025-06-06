# ControlGroupStyleConfiguration

**Framework**: SwiftUI  
**Kind**: struct

The properties of a control group.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct ControlGroupStyleConfiguration
```

## Topics

### Configuring the label
- [let label: ControlGroupStyleConfiguration.Label](controlgroupstyleconfiguration/label-swift.property.md)
  A view that provides the optional label of the [`ControlGroup`](controlgroup.md).
- [ControlGroupStyleConfiguration.Label](controlgroupstyleconfiguration/label-swift.struct.md)
  A type-erased label of a [`ControlGroup`](controlgroup.md).
### Configuring the content
- [let content: ControlGroupStyleConfiguration.Content](controlgroupstyleconfiguration/content-swift.property.md)
  A view that represents the content of the `ControlGroup`.
- [ControlGroupStyleConfiguration.Content](controlgroupstyleconfiguration/content-swift.struct.md)
  A type-erased content of a `ControlGroup`.

## See Also

- [func controlGroupStyle<S>(S) -> some View](view/controlgroupstyle(_:).md)
  Sets the style for control groups within this view.
- [protocol ControlGroupStyle](controlgroupstyle.md)
  Defines the implementation of all control groups within a view hierarchy.
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
- [protocol LabeledContentStyle](labeledcontentstyle.md)
  The appearance and behavior of a labeled content instance..
- [struct LabeledContentStyleConfiguration](labeledcontentstyleconfiguration.md)
  The properties of a labeled content instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlgroupstyleconfiguration)*