# TableRowBuilder

**Framework**: SwiftUI  
**Kind**: struct

A result builder that creates table row content from closures.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@resultBuilder
struct TableRowBuilder<Value> where Value : Identifiable
```

#### Overview

The `buildBlock` methods in this type create [`TableRowContent`](tablerowcontent.md) instances based on the number and types of sources provided as parameters.

Don’t use this type directly; instead, SwiftUI annotates the `rows` parameter of the various [`Table`](table.md) initializers with the `@TableRowBuilder` annotation, implicitly calling this builder for you.

## Topics

### Building a row from sources
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
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2, C3, C4, C5, C6, C7, C8, C9) -> TupleTableRowContent<Value, (C0, C1, C2, C3, C4, C5, C6, C7, C8, C9)>](tablerowbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:).md)
  Creates a row result from ten sources.
### Building a row from conditionals
- [static func buildIf<C>(C?) -> C?](tablerowbuilder/buildif(_:).md)
  Creates a row result for conditional statements.
- [static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>](tablerowbuilder/buildeither(first:).md)
  Creates a row result for the first of two row content alternatives.
- [static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F>](tablerowbuilder/buildeither(second:).md)
  Creates a row result for the second of two row content alternatives.
- [static func buildExpression<Content>(Content) -> Content](tablerowbuilder/buildexpression(_:).md)
  Builds an expression within the builder.

## See Also

- [struct TableRow](tablerow.md)
  A row that represents a data value in a table.
- [protocol TableRowContent](tablerowcontent.md)
  A type used to represent table rows.
- [struct TableHeaderRowContent](tableheaderrowcontent.md)
  A table row that displays a single view instead of columned content.
- [struct TupleTableRowContent](tupletablerowcontent.md)
  A type of table column content that creates table rows created from a Swift tuple of table rows.
- [struct TableForEachContent](tableforeachcontent.md)
  A type of table row content that creates table rows created by iterating over a collection.
- [struct EmptyTableRowContent](emptytablerowcontent.md)
  A table row content that doesn’t produce any rows.
- [protocol DynamicTableRowContent](dynamictablerowcontent.md)
  A type of table row content that generates table rows from an underlying collection of data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablerowbuilder)*