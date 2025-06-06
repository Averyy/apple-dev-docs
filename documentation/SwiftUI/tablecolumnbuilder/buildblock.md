# buildBlock(_:_:_:_:_:_:_:_:_:_:)

**Framework**: SwiftUI  
**Kind**: method

Creates an unsortable column result from ten sources.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(_ c0: C0, _ c1: C1, _ c2: C2, _ c3: C3, _ c4: C4, _ c5: C5, _ c6: C6, _ c7: C7, _ c8: C8, _ c9: C9) -> TupleTableColumnContent<RowValue, Never, (C0, C1, C2, C3, C4, C5, C6, C7, C8, C9)> where RowValue == C0.TableRowValue, C0 : TableColumnContent, C1 : TableColumnContent, C2 : TableColumnContent, C3 : TableColumnContent, C4 : TableColumnContent, C5 : TableColumnContent, C6 : TableColumnContent, C7 : TableColumnContent, C8 : TableColumnContent, C9 : TableColumnContent, C0.TableColumnSortComparator == Never, C0.TableRowValue == C1.TableRowValue, C1.TableColumnSortComparator == Never, C1.TableRowValue == C2.TableRowValue, C2.TableColumnSortComparator == Never, C2.TableRowValue == C3.TableRowValue, C3.TableColumnSortComparator == Never, C3.TableRowValue == C4.TableRowValue, C4.TableColumnSortComparator == Never, C4.TableRowValue == C5.TableRowValue, C5.TableColumnSortComparator == Never, C5.TableRowValue == C6.TableRowValue, C6.TableColumnSortComparator == Never, C6.TableRowValue == C7.TableRowValue, C7.TableColumnSortComparator == Never, C7.TableRowValue == C8.TableRowValue, C8.TableColumnSortComparator == Never, C8.TableRowValue == C9.TableRowValue, C9.TableColumnSortComparator == Never
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
- [static buildExpression(_:)](tablecolumnbuilder/buildexpression(_:).md)
  Creates a generic, unsortable single column expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumnbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:))*