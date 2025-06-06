# TableColumnBuilder

**Framework**: SwiftUI  
**Kind**: struct

A result builder that creates table column content from closures.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@resultBuilder
struct TableColumnBuilder<RowValue, Sort> where RowValue : Identifiable, Sort : SortComparator
```

#### Overview

The `buildBlock` methods in this type create [`TableColumnContent`](tablecolumncontent.md) instances based on the number and types of sources provided as parameters.

Don’t use this type directly; instead, SwiftUI annotates the `columns` parameter of the various [`Table`](table.md) initializers with the `@TableColumnBuilder` annotation, implicitly calling this builder for you.

## Topics

### Building a column
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
- [static buildBlock(_:_:_:_:_:_:_:_:_:_:)](tablecolumnbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:).md)
  Creates an unsortable column result from ten sources.
- [static buildExpression(_:)](tablecolumnbuilder/buildexpression(_:).md)
  Creates a generic, unsortable single column expression.
### Supporting types
- [struct TupleTableColumnContent](tupletablecolumncontent.md)
  A type of table column content that creates table columns created from a Swift tuple of table columns.
### Type Methods
- [static buildEither(first:)](tablecolumnbuilder/buildeither(first:).md)
  Creates a column result for the first of two column content alternatives.
- [static buildEither(second:)](tablecolumnbuilder/buildeither(second:).md)
  Creates a row result for the second of two row content alternatives.
- [static buildIf(_:)](tablecolumnbuilder/buildif(_:).md)
- [static buildLimitedAvailability(_:)](tablecolumnbuilder/buildlimitedavailability(_:).md)

## See Also

- [struct TableColumn](tablecolumn.md)
  A column that displays a view for each row in a table.
- [protocol TableColumnContent](tablecolumncontent.md)
  A type used to represent columns within a table.
- [struct TableColumnAlignment](tablecolumnalignment.md)
  Describes the alignment of the content of a table column.
- [struct TableColumnForEach](tablecolumnforeach.md)
  A structure that computes columns on demand from an underlying collection of identified data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumnbuilder)*