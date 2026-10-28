# inset

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

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
@export(implementation) @preconcurrency static var inset: InsetTableStyle { get }
```

Available when `Self` is `InsetTableStyle`.

## Discussion

To customize whether the rows of the table should alternate their backgrounds, use [`alternatingRowBackgrounds(_:)`](../view/alternatingrowbackgrounds%28_%29.md).

## See Also

### Getting built-in table styles
- [static var automatic: AutomaticTableStyle](./automatic.md)
  The default table style in the current context.
- [static var bordered: BorderedTableStyle](./bordered.md)
  The table style that describes the behavior and appearance of a table with standard border.
- [static func inset(alternatesRowBackgrounds: Bool) -> InsetTableStyle](./inset%28alternatesrowbackgrounds%29.md)
  The table style that describes the behavior and appearance of a table with its content and selection inset from the table edges.
- [static func bordered(alternatesRowBackgrounds: Bool) -> BorderedTableStyle](./bordered%28alternatesrowbackgrounds%29.md)
  The table style that describes the behavior and appearance of a table with standard border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablestyle/inset)*