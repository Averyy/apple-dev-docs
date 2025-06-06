# UIAccessibilityContainerDataTable

**Framework**: UIKit  
**Kind**: protocol

Methods that convey information about the contents of a table.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIAccessibilityContainerDataTable : NSObjectProtocol
```

## Topics

### Providing cell elements
- [func accessibilityDataTableCellElement(forRow: Int, column: Int) -> (any UIAccessibilityContainerDataTableCell)?](uiaccessibilitycontainerdatatable/accessibilitydatatablecellelement(forrow:column:).md)
  Returns the accessibility element for the specified cell.
### Providing the table dimensions
- [func accessibilityColumnCount() -> Int](uiaccessibilitycontainerdatatable/accessibilitycolumncount.md)
  Returns the total number of columns in the table.
- [func accessibilityRowCount() -> Int](uiaccessibilitycontainerdatatable/accessibilityrowcount.md)
  Returns the total number of rows in the table.
### Providing header elements
- [func accessibilityHeaderElements(forColumn: Int) -> [any UIAccessibilityContainerDataTableCell]?](uiaccessibilitycontainerdatatable/accessibilityheaderelements(forcolumn:).md)
  Returns the accessibility element for the specified column header.
- [func accessibilityHeaderElements(forRow: Int) -> [any UIAccessibilityContainerDataTableCell]?](uiaccessibilitycontainerdatatable/accessibilityheaderelements(forrow:).md)
  Returns the accessibility element for the specified row header.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol UIAccessibilityContainerDataTableCell](uiaccessibilitycontainerdatatablecell.md)
  Methods that provide the location of a cell in a table.
- [enum UIAccessibilityContainerType](uiaccessibilitycontainertype.md)
  Constants that indicate the type of content in a data-based container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycontainerdatatable)*