# bordered

**Framework**: SwiftUI  
**Kind**: property

The table style that describes the behavior and appearance of a table with standard border.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@MainActor
@preconcurrency static var bordered: BorderedTableStyle { get }
```

#### Discussion

Bordered tables are expected to be inset from their outer containers, but do not have inset style rows or selection.

To customize whether the rows of the table should alternate their backgrounds, use [`alternatingRowBackgrounds(_:)`](view/alternatingrowbackgrounds(_:).md).

## See Also

- [static var automatic: AutomaticTableStyle](tablestyle/automatic.md)
  The default table style in the current context.
- [static var inset: InsetTableStyle](tablestyle/inset.md)
  The table style that describes the behavior and appearance of a table with its content and selection inset from the table edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablestyle/bordered)*