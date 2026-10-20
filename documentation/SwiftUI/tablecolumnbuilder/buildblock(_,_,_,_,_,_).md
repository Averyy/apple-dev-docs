# buildBlock(_:_:_:_:_:_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Creates an unsortable column result from six sources.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
static func buildBlock<C0, C1, C2, C3, C4, C5>(_ c0: C0, _ c1: C1, _ c2: C2, _ c3: C3, _ c4: C4, _ c5: C5) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C2 : TableColumnContent, C3 : TableColumnContent, C4 : TableColumnContent, C5 : TableColumnContent, C0.TableColumnSortComparator == Never, C0.TableRowValue == C1.TableRowValue, C1.TableColumnSortComparator == Never, C1.TableRowValue == C2.TableRowValue, C2.TableColumnSortComparator == Never, C2.TableRowValue == C3.TableRowValue, C3.TableColumnSortComparator == Never, C3.TableRowValue == C4.TableRowValue, C4.TableColumnSortComparator == Never, C4.TableRowValue == C5.TableRowValue, C5.TableColumnSortComparator == Never
```

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to `SortComparator`.

**Other overloads**:

```swift
@export(implementation)
static func buildBlock<C0, C1, C2, C3, C4, C5>(_ c0: C0, _ c1: C1, _ c2: C2, _ c3: C3, _ c4: C4, _ c5: C5) -> TupleTableColumnContent<RowValue, Sort, (C0, C1, C2, C3, C4, C5)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C2 : TableColumnContent, C3 : TableColumnContent, C4 : TableColumnContent, C5 : TableColumnContent, C0.TableRowValue == C1.TableRowValue, C1.TableRowValue == C2.TableRowValue, C2.TableRowValue == C3.TableRowValue, C3.TableRowValue == C4.TableRowValue, C4.TableRowValue == C5.TableRowValue
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
- [static buildBlock(_:_:_:_:_:_:_:)](./buildblock%28_,_,_,_,_,_,_%29.md)
  Creates an unsortable column result from seven sources.
- [static buildBlock(_:_:_:_:_:_:_:_:)](./buildblock%28_,_,_,_,_,_,_,_%29.md)
  Creates an unsortable column result from eight sources.
- [static buildBlock(_:_:_:_:_:_:_:_:_:)](./buildblock%28_,_,_,_,_,_,_,_,_%29.md)
  Creates an unsortable column result from nine sources.
- [static buildBlock(_:_:_:_:_:_:_:_:_:_:)](./buildblock%28_,_,_,_,_,_,_,_,_,_%29.md)
  Creates an unsortable column result from ten sources.
- [static buildExpression(_:)](./buildexpression%28_%29.md)
  Creates a generic, unsortable single column expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumnbuilder/buildblock(_:_:_:_:_:_:))*