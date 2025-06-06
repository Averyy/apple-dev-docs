# TupleTableColumnContent

**Framework**: SwiftUI  
**Kind**: struct

A type of table column content that creates table columns created from a Swift tuple of table columns.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@frozen
struct TupleTableColumnContent<RowValue, Sort, T> where RowValue : Identifiable, Sort : SortComparator
```

#### Overview

Don’t use this type directly; instead, SwiftUI uses this type as the return value from the various `buildBlock` methods in [`TableColumnBuilder`](tablecolumnbuilder.md). The size of the tuple corresponds to how many columns you create in the `columns` closure you provide to the [`Table`](table.md) initializer.

## Topics

### Accessing the value
- [var value: T](tupletablecolumncontent/value.md)
  The value of a row presented by this column content.

## Relationships

### Conforms To
- [TableColumnContent](tablecolumncontent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tupletablecolumncontent)*