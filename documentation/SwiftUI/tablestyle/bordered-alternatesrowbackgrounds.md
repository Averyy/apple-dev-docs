# bordered(alternatesRowBackgrounds:)

**Framework**: SwiftUI  
**Kind**: method

The table style that describes the behavior and appearance of a table with standard border.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@MainActor
@preconcurrency static func bordered(alternatesRowBackgrounds: Bool) -> BorderedTableStyle
```

#### Discussion

Bordered tables are expected to be inset from their outer containers, but do not have inset style rows or selection.

## Parameters

- `alternatesRowBackgrounds`: Whether the rows should alternate   their backgrounds to help visually distinguish them from each other.

## See Also

- [static func inset(alternatesRowBackgrounds: Bool) -> InsetTableStyle](tablestyle/inset(alternatesrowbackgrounds:).md)
  The table style that describes the behavior and appearance of a table with its content and selection inset from the table edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablestyle/bordered(alternatesrowbackgrounds:))*