# buildExpression(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Creates a generic, unsortable single column expression.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
static func buildExpression<Column>(_ column: Column) -> Column where RowValue == Column.TableRowValue, Column : TableColumnContent, Column.TableColumnSortComparator == Never
```

**Other overloads**:

```swift
@export(implementation)
static func buildExpression<Column>(_ column: Column) -> Column where RowValue == Column.TableRowValue, Sort == Column.TableColumnSortComparator, Column : TableColumnContent
```

```swift
@export(implementation)
static func buildExpression<Content, Label>(_ column: TableColumn<RowValue, Never, Content, Label>) -> TableColumn<RowValue, Never, Content, Label> where Content : View, Label : View
```

```swift
@export(implementation)
static func buildExpression<Content, Label>(_ column: TableColumn<RowValue, Sort, Content, Label>) -> TableColumn<RowValue, Sort, Content, Label> where Content : View, Label : View
```

## See Also

### Building a column
- [static buildBlock(_:)](./buildblock%28_%29.md)
  Creates a single, unsortable column result.
- [static buildBlock(_:_:)](./buildblock%28_,_%29.md)
  Creates an unsortable column result from two sources.
- [static buildBlock(_:_:_:)](./buildblock%28_,_,_%29.md)
  Creates an unsortable column result from three sources.
- [static buildBlock(_:_:_:_:)](./buildblock%28_,_,_,_%29.md)
  Creates an unsortable column result from four sources.
- [static buildBlock(_:_:_:_:_:)](./buildblock%28_,_,_,_,_%29.md)
  Creates an unsortable column result from five sources.
- [static buildBlock(_:_:_:_:_:_:)](./buildblock%28_,_,_,_,_,_%29.md)
  Creates an unsortable column result from six sources.
- [static buildBlock(_:_:_:_:_:_:_:)](./buildblock%28_,_,_,_,_,_,_%29.md)
  Creates an unsortable column result from seven sources.
- [static buildBlock(_:_:_:_:_:_:_:_:)](./buildblock%28_,_,_,_,_,_,_,_%29.md)
  Creates an unsortable column result from eight sources.
- [static buildBlock(_:_:_:_:_:_:_:_:_:)](./buildblock%28_,_,_,_,_,_,_,_,_%29.md)
  Creates an unsortable column result from nine sources.
- [static buildBlock(_:_:_:_:_:_:_:_:_:_:)](./buildblock%28_,_,_,_,_,_,_,_,_,_%29.md)
  Creates an unsortable column result from ten sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumnbuilder/buildexpression(_:))*