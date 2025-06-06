# buildExpression(_:)

**Framework**: SwiftUI  
**Kind**: method

Creates a generic, unsortable single column expression.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static func buildExpression<Column>(_ column: Column) -> Column where RowValue == Column.TableRowValue, Column : TableColumnContent, Column.TableColumnSortComparator == Never
```

## See Also

- [static buildBlock(_:)](tablecolumnbuilder/buildblock(_:).md)
  Creates a single, unsortable column result.
- [static buildBlock(_:_:)](tablecolumnbuilder/buildblock(_:_:).md)
  Creates an unsortable column result from two sources.
- [static buildBlock(_:_:_:)](tablecolumnbuilder/buildblock(_:_:_:).md)
  Creates an unsortable column result from three sources.
- [static buildBlock(_:_:_:_:)](tablecolumnbuilder/buildblock(_:_:_:_:).md)
  Creates an unsortable column result from four sources.
- [static buildBlock(_:_:_:_:_:)](tablecolumnbuilder/buildblock(_:_:_:_:_:).md)
  Creates an unsortable column result from five sources.
- [static buildBlock(_:_:_:_:_:_:)](tablecolumnbuilder/buildblock(_:_:_:_:_:_:).md)
  Creates an unsortable column result from six sources.
- [static buildBlock(_:_:_:_:_:_:_:)](tablecolumnbuilder/buildblock(_:_:_:_:_:_:_:).md)
  Creates an unsortable column result from seven sources.
- [static buildBlock(_:_:_:_:_:_:_:_:)](tablecolumnbuilder/buildblock(_:_:_:_:_:_:_:_:).md)
  Creates an unsortable column result from eight sources.
- [static buildBlock(_:_:_:_:_:_:_:_:_:)](tablecolumnbuilder/buildblock(_:_:_:_:_:_:_:_:_:).md)
  Creates an unsortable column result from nine sources.
- [static buildBlock(_:_:_:_:_:_:_:_:_:_:)](tablecolumnbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:).md)
  Creates an unsortable column result from ten sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumnbuilder/buildexpression(_:))*