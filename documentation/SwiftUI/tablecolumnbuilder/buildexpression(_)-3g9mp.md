# buildExpression(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Creates a generic, sortable single column expression.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
static func buildExpression<Column>(_ column: Column) -> Column where RowValue == Column.TableRowValue, Sort == Column.TableColumnSortComparator, Column : TableColumnContent
```

**Other overloads**:

```swift
@export(implementation)
static func buildExpression<Column>(_ column: Column) -> Column where RowValue == Column.TableRowValue, Column : TableColumnContent, Column.TableColumnSortComparator == Never
```

```swift
@export(implementation)
static func buildExpression<Content, Label>(_ column: TableColumn<RowValue, Never, Content, Label>) -> TableColumn<RowValue, Never, Content, Label> where Content : View, Label : View
```

```swift
@export(implementation)
static func buildExpression<Content, Label>(_ column: TableColumn<RowValue, Sort, Content, Label>) -> TableColumn<RowValue, Sort, Content, Label> where Content : View, Label : View
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumnbuilder/buildexpression(_:)-3g9mp)*