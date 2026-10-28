# buildBlock(_:_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Creates a sortable column result from two sources.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
static func buildBlock<C0, C1>(_ c0: C0, _ c1: C1) -> TupleTableColumnContent<RowValue, Sort, (C0, C1)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C0.TableRowValue == C1.TableRowValue
```

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to `SortComparator`.

**Other overloads**:

```swift
@export(implementation)
static func buildBlock<C0, C1>(_ c0: C0, _ c1: C1) -> TupleTableColumnContent<RowValue, Never, (C0, C1)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C0.TableColumnSortComparator == Never, C0.TableRowValue == C1.TableRowValue, C1.TableColumnSortComparator == Never
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumnbuilder/buildblock(_:_:)-5mgkp)*