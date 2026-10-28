# buildBlock(_:_:_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Creates a sortable column result from three sources.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
static func buildBlock<C0, C1, C2>(_ c0: C0, _ c1: C1, _ c2: C2) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C2 : TableColumnContent, C0.TableRowValue == C1.TableRowValue, C1.TableRowValue == C2.TableRowValue
```

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to `SortComparator`.

**Other overloads**:

```swift
@export(implementation)
static func buildBlock<C0, C1, C2>(_ c0: C0, _ c1: C1, _ c2: C2) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C2 : TableColumnContent, C0.TableColumnSortComparator == Never, C0.TableRowValue == C1.TableRowValue, C1.TableColumnSortComparator == Never, C1.TableRowValue == C2.TableRowValue, C2.TableColumnSortComparator == Never
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumnbuilder/buildblock(_:_:_:)-3cxda)*