# bordered(alternatesRowBackgrounds:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

The table style that describes the behavior and appearance of a table with standard border.

**Availability**:
- macOS 12.0+ - Deprecated in 27.2

> **Deprecated**: Use the [`bordered`](./bordered.md) style and add the [`alternatingRowBackgrounds(_:)`](../view/alternatingrowbackgrounds%28_%29.md) view modifier instead.

## Declaration

```swift
@MainActor
@export(implementation) @preconcurrency static func bordered(alternatesRowBackgrounds: Bool) -> BorderedTableStyle
```

Available when `Self` is `BorderedTableStyle`.

#### Discussion

Bordered tables are expected to be inset from their outer containers, but do not have inset style rows or selection.

## Parameters

- `alternatesRowBackgrounds`: Whether the rows should alternate their backgrounds to help visually distinguish them from each other.

## See Also

### Getting built-in table styles
- [static var automatic: AutomaticTableStyle](./automatic.md)
  The default table style in the current context.
- [static var inset: InsetTableStyle](./inset.md)
  The table style that describes the behavior and appearance of a table with its content and selection inset from the table edges.
- [static var bordered: BorderedTableStyle](./bordered.md)
  The table style that describes the behavior and appearance of a table with standard border.
- [static func inset(alternatesRowBackgrounds: Bool) -> InsetTableStyle](./inset%28alternatesrowbackgrounds%29.md)
  The table style that describes the behavior and appearance of a table with its content and selection inset from the table edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablestyle/bordered(alternatesrowbackgrounds:))*