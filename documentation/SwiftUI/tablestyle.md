# TableStyle

**Framework**: SwiftUI  
**Kind**: protocol

A type that applies a custom appearance to all tables within a view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol TableStyle
```

#### Overview

To configure the current table style for a view hierarchy, use the [`tableStyle(_:)`](view/tablestyle(_:).md) modifier.

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

### Getting built-in table styles
- [static var automatic: AutomaticTableStyle](tablestyle/automatic.md)
  The default table style in the current context.
- [static var inset: InsetTableStyle](tablestyle/inset.md)
  The table style that describes the behavior and appearance of a table with its content and selection inset from the table edges.
- [static var bordered: BorderedTableStyle](tablestyle/bordered.md)
  The table style that describes the behavior and appearance of a table with standard border.
### Creating custom table styles
- [func makeBody(configuration: Self.Configuration) -> Self.Body](tablestyle/makebody(configuration:).md)
  Creates a view that represents the body of a table.
- [TableStyle.Configuration](tablestyle/configuration.md)
  The properties of a table.
- [associatedtype Body : View](tablestyle/body.md)
  A view that represents the body of a table.
### Deprecated styles
- [static func inset(alternatesRowBackgrounds: Bool) -> InsetTableStyle](tablestyle/inset(alternatesrowbackgrounds:).md)
  The table style that describes the behavior and appearance of a table with its content and selection inset from the table edges.
- [static func bordered(alternatesRowBackgrounds: Bool) -> BorderedTableStyle](tablestyle/bordered(alternatesrowbackgrounds:).md)
  The table style that describes the behavior and appearance of a table with standard border.
### Supporting types
- [struct AutomaticTableStyle](automatictablestyle.md)
  The default table style in the current context.
- [struct InsetTableStyle](insettablestyle.md)
  The table style that describes the behavior and appearance of a table with its content and selection inset from the table edges.
- [struct BorderedTableStyle](borderedtablestyle.md)
  The table style that describes the behavior and appearance of a table with standard border.

## Relationships

### Conforming Types
- [AutomaticTableStyle](automatictablestyle.md)
- [BorderedTableStyle](borderedtablestyle.md)
- [InsetTableStyle](insettablestyle.md)

## See Also

- [func listStyle<S>(S) -> some View](view/liststyle(_:).md)
  Sets the style for lists within this view.
- [protocol ListStyle](liststyle.md)
  A protocol that describes the behavior and appearance of a list.
- [func tableStyle<S>(S) -> some View](view/tablestyle(_:).md)
  Sets the style for tables within this view.
- [struct TableStyleConfiguration](tablestyleconfiguration.md)
  The properties of a table.
- [func disclosureGroupStyle<S>(S) -> some View](view/disclosuregroupstyle(_:).md)
  Sets the style for disclosure groups within this view.
- [protocol DisclosureGroupStyle](disclosuregroupstyle.md)
  A type that specifies the appearance and interaction of disclosure groups within a view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablestyle)*