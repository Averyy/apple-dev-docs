# buildBlock(_:_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Type Method

Creates an unsortable column result from two sources.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
static func buildBlock<C0, C1>(_ c0: C0, _ c1: C1) -> TupleTableColumnContent<RowValue, Never, (C0, C1)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C0.TableColumnSortComparator == Never, C0.TableRowValue == C1.TableRowValue, C1.TableColumnSortComparator == Never
```

Available when `RowValue` conforms to `Identifiable` and `Sort` conforms to `SortComparator`.

**Other overloads**:

```swift
@export(implementation)
static func buildBlock<C0, C1>(_ c0: C0, _ c1: C1) -> TupleTableColumnContent<RowValue, Sort, (C0, C1)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C0.TableRowValue == C1.TableRowValue
```

## See Also

### Building a column
- [static buildBlock(_:)](./buildblock%28_%29.md)
  Creates a single, unsortable column result.
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
- [static buildExpression(_:)](./buildexpression%28_%29.md)
  Creates a generic, unsortable single column expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumnbuilder/buildblock(_:_:))*