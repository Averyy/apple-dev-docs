# bordered

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The table style that describes the behavior and appearance of a table with standard border.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@MainActor
@export(implementation) @preconcurrency static var bordered: BorderedTableStyle { get }
```

Available when `Self` is `BorderedTableStyle`.

## Discussion

Bordered tables are expected to be inset from their outer containers, but do not have inset style rows or selection.

To customize whether the rows of the table should alternate their backgrounds, use [`alternatingRowBackgrounds(_:)`](../view/alternatingrowbackgrounds%28_%29.md).

## See Also

### Getting built-in table styles
- [static var automatic: AutomaticTableStyle](./automatic.md)
  The default table style in the current context.
- [static var inset: InsetTableStyle](./inset.md)
  The table style that describes the behavior and appearance of a table with its content and selection inset from the table edges.
- [static func inset(alternatesRowBackgrounds: Bool) -> InsetTableStyle](./inset%28alternatesrowbackgrounds%29.md)
  The table style that describes the behavior and appearance of a table with its content and selection inset from the table edges.
- [static func bordered(alternatesRowBackgrounds: Bool) -> BorderedTableStyle](./bordered%28alternatesrowbackgrounds%29.md)
  The table style that describes the behavior and appearance of a table with standard border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablestyle/bordered)*