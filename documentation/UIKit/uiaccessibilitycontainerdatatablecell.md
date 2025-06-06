# UIAccessibilityContainerDataTableCell

**Framework**: UIKit  
**Kind**: protocol

Methods that provide the location of a cell in a table.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIAccessibilityContainerDataTableCell : NSObjectProtocol
```

## Topics

### Getting the rows and columns
- [func accessibilityColumnRange() -> NSRange](uiaccessibilitycontainerdatatablecell/accessibilitycolumnrange.md)
  Returns the columns spanned by the cell.
- [func accessibilityRowRange() -> NSRange](uiaccessibilitycontainerdatatablecell/accessibilityrowrange.md)
  Returns the visible range of rows.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol UIAccessibilityContainerDataTable](uiaccessibilitycontainerdatatable.md)
  Methods that convey information about the contents of a table.
- [enum UIAccessibilityContainerType](uiaccessibilitycontainertype.md)
  Constants that indicate the type of content in a data-based container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycontainerdatatablecell)*