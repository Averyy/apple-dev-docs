# buildBlock(_:_:_:_:_:_:_:_:_:_:)

**Framework**: SwiftUI  
**Kind**: method

Creates a row result from ten sources.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(_ c0: C0, _ c1: C1, _ c2: C2, _ c3: C3, _ c4: C4, _ c5: C5, _ c6: C6, _ c7: C7, _ c8: C8, _ c9: C9) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6, C7, C8, C9)> where Value == C0.TableRowValue, C0 : TableRowContent, C1 : TableRowContent, C2 : TableRowContent, C3 : TableRowContent, C4 : TableRowContent, C5 : TableRowContent, C6 : TableRowContent, C7 : TableRowContent, C8 : TableRowContent, C9 : TableRowContent, C0.TableRowValue == C1.TableRowValue, C1.TableRowValue == C2.TableRowValue, C2.TableRowValue == C3.TableRowValue, C3.TableRowValue == C4.TableRowValue, C4.TableRowValue == C5.TableRowValue, C5.TableRowValue == C6.TableRowValue, C6.TableRowValue == C7.TableRowValue, C7.TableRowValue == C8.TableRowValue, C8.TableRowValue == C9.TableRowValue
```

## See Also

- [static func buildBlock<C>(C) -> C](tablerowbuilder/buildblock(_:).md)
  Creates a single row result.
- [static func buildBlock<C0, C1>(C0, C1) -> TupleTableRowContent<Value, (C0, C1)>](tablerowbuilder/buildblock(_:_:).md)
  Creates a row result from two sources.
- [static func buildBlock<C0, C1, C2>(C0, C1, C2) -> TupleTableRowContent<Value, (C0, C1, C2)>](tablerowbuilder/buildblock(_:_:_:).md)
  Creates a row result from three sources.
- [static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> TupleTableRowContent<Value, (C0, C1, C2, C3)>](tablerowbuilder/buildblock(_:_:_:_:).md)
  Creates a row result from four sources.
- [static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4)>](tablerowbuilder/buildblock(_:_:_:_:_:).md)
  Creates a row result from five sources.
- [static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5)>](tablerowbuilder/buildblock(_:_:_:_:_:_:).md)
  Creates a row result from six sources.
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5, C6) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6)>](tablerowbuilder/buildblock(_:_:_:_:_:_:_:).md)
  Creates a row result from seven sources.
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4, C5, C6, C7) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6, C7)>](tablerowbuilder/buildblock(_:_:_:_:_:_:_:_:).md)
  Creates a row result from eight sources.
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3, C4, C5, C6, C7, C8) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6, C7, C8)>](tablerowbuilder/buildblock(_:_:_:_:_:_:_:_:_:).md)
  Creates a row result from nine sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablerowbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:))*