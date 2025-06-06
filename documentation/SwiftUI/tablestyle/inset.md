# inset

**Framework**: SwiftUI  
**Kind**: property

The table style that describes the behavior and appearance of a table with its content and selection inset from the table edges.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static var inset: InsetTableStyle { get }
```

#### Discussion

To customize whether the rows of the table should alternate their backgrounds, use [`alternatingRowBackgrounds(_:)`](view/alternatingrowbackgrounds(_:).md).

## See Also

- [static var automatic: AutomaticTableStyle](tablestyle/automatic.md)
  The default table style in the current context.
- [static var bordered: BorderedTableStyle](tablestyle/bordered.md)
  The table style that describes the behavior and appearance of a table with standard border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablestyle/inset)*