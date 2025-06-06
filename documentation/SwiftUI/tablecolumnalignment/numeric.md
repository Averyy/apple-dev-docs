# numeric(_:)

**Framework**: SwiftUI  
**Kind**: method

Column alignment appropriate for numeric content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static func numeric(_ numberingSystem: Locale.NumberingSystem) -> TableColumnAlignment
```

#### Discussion

Use this alignment when a table column is primarily displaying numeric content, so that the values are easy to visually scan and compare.

This uses the provided numbering system to determine the alignment:

- For left to right numbering systems, this is equivalent to right.
- For right to left numbering systems, this is equivalent to left.

## See Also

- [static var automatic: TableColumnAlignment](tablecolumnalignment/automatic.md)
  The default column alignment.
- [static var leading: TableColumnAlignment](tablecolumnalignment/leading.md)
  Leading column alignment.
- [static var center: TableColumnAlignment](tablecolumnalignment/center.md)
  Center column alignment.
- [static var trailing: TableColumnAlignment](tablecolumnalignment/trailing.md)
  Trailing column alignment.
- [static var numeric: TableColumnAlignment](tablecolumnalignment/numeric.md)
  Column alignment appropriate for numeric content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumnalignment/numeric(_:))*