# buildBlock(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Creates a single, sortable column result.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
static func buildBlock<Column>(_ column: Column) -> Column where RowValue == Column.TableRowValue, Sort == Column.TableColumnSortComparator, Column : TableColumnContent
```

**Other overloads**:

```swift
@export(implementation)
static func buildBlock<Column>(_ column: Column) -> Column where RowValue == Column.TableRowValue, Column : TableColumnContent, Column.TableColumnSortComparator == Never
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumnbuilder/buildblock(_:)-1ysi3)*