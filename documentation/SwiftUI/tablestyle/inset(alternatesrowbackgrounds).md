# inset(alternatesRowBackgrounds:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

The table style that describes the behavior and appearance of a table with its content and selection inset from the table edges.

**Availability**:
- macOS 12.0+ - Deprecated in 27.2

> **Deprecated**: Use the [`inset`](./inset.md) style and add the [`alternatingRowBackgrounds(_:)`](../view/alternatingrowbackgrounds%28_%29.md) view modifier instead.

## Declaration

```swift
@MainActor
@export(implementation) @preconcurrency static func inset(alternatesRowBackgrounds: Bool) -> InsetTableStyle
```

Available when `Self` is `InsetTableStyle`.

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
- [static func bordered(alternatesRowBackgrounds: Bool) -> BorderedTableStyle](./bordered%28alternatesrowbackgrounds%29.md)
  The table style that describes the behavior and appearance of a table with standard border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablestyle/inset(alternatesrowbackgrounds:))*