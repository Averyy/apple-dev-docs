# automatic

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The default table style in the current context.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@export(implementation) @preconcurrency static var automatic: AutomaticTableStyle { get }
```

Available when `Self` is `AutomaticTableStyle`.

## See Also

### Getting built-in table styles
- [static var inset: InsetTableStyle](./inset.md)
  The table style that describes the behavior and appearance of a table with its content and selection inset from the table edges.
- [static var bordered: BorderedTableStyle](./bordered.md)
  The table style that describes the behavior and appearance of a table with standard border.
- [static func inset(alternatesRowBackgrounds: Bool) -> InsetTableStyle](./inset%28alternatesrowbackgrounds%29.md)
  The table style that describes the behavior and appearance of a table with its content and selection inset from the table edges.
- [static func bordered(alternatesRowBackgrounds: Bool) -> BorderedTableStyle](./bordered%28alternatesrowbackgrounds%29.md)
  The table style that describes the behavior and appearance of a table with standard border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablestyle/automatic)*