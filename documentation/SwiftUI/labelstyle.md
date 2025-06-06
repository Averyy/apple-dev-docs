# LabelStyle

**Framework**: SwiftUI  
**Kind**: protocol

A type that applies a custom appearance to all labels within a view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol LabelStyle
```

#### Overview

To configure the current label style for a view hierarchy, use the [`labelStyle(_:)`](view/labelstyle(_:).md) modifier.

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

### Getting built-in label styles
- [static var automatic: DefaultLabelStyle](labelstyle/automatic.md)
  A label style that resolves its appearance automatically based on the current context.
- [static var iconOnly: IconOnlyLabelStyle](labelstyle/icononly.md)
  A label style that only displays the icon of the label.
- [static var titleAndIcon: TitleAndIconLabelStyle](labelstyle/titleandicon.md)
  A label style that shows both the title and icon of the label using a system-standard layout.
- [static var titleOnly: TitleOnlyLabelStyle](labelstyle/titleonly.md)
  A label style that only displays the title of the label.
### Creating custom label styles
- [func makeBody(configuration: Self.Configuration) -> Self.Body](labelstyle/makebody(configuration:).md)
  Creates a view that represents the body of a label.
- [LabelStyle.Configuration](labelstyle/configuration.md)
  The properties of a label.
- [associatedtype Body : View](labelstyle/body.md)
  A view that represents the body of a label.
### Supporting types
- [struct DefaultLabelStyle](defaultlabelstyle.md)
  The default label style in the current context.
- [struct IconOnlyLabelStyle](icononlylabelstyle.md)
  A label style that only displays the icon of the label.
- [struct TitleAndIconLabelStyle](titleandiconlabelstyle.md)
  A label style that shows both the title and icon of the label using a system-standard layout.
- [struct TitleOnlyLabelStyle](titleonlylabelstyle.md)
  A label style that only displays the title of the label.

## Relationships

### Conforming Types
- [DefaultLabelStyle](defaultlabelstyle.md)
- [IconOnlyLabelStyle](icononlylabelstyle.md)
- [TitleAndIconLabelStyle](titleandiconlabelstyle.md)
- [TitleOnlyLabelStyle](titleonlylabelstyle.md)

## See Also

- [func labelStyle<S>(S) -> some View](view/labelstyle(_:).md)
  Sets the style for labels within this view.
- [struct LabelStyleConfiguration](labelstyleconfiguration.md)
  The properties of a label.
- [func textFieldStyle<S>(S) -> some View](view/textfieldstyle(_:).md)
  Sets the style for text fields within this view.
- [protocol TextFieldStyle](textfieldstyle.md)
  A specification for the appearance and interaction of a text field.
- [func textEditorStyle(some TextEditorStyle) -> some View](view/texteditorstyle(_:).md)
  Sets the style for text editors within this view.
- [protocol TextEditorStyle](texteditorstyle.md)
  A specification for the appearance and interaction of a text editor.
- [struct TextEditorStyleConfiguration](texteditorstyleconfiguration.md)
  The properties of a text editor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/labelstyle)*