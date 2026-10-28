# OptionalColumnProtocol

**Framework**: TabularData  
**Kind**: protocol  
**Role**: Protocol

A type that represents a column that has missing values.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
protocol OptionalColumnProtocol<WrappedElement> : ColumnProtocol
```

## Overview

`OptionalColumnProtocol` defines the common functionality for column types that support missing values.

## Topics

### Filling an Optional Column
- [func filled(with: Self.WrappedElement) -> FilledColumn<Self>](./optionalcolumnprotocol/filled%28with%29.md)
  Generates a filled column by replacing missing elements with a value.
### Generating an Optional Column by Adding Two Columns
- [static func + (Self, Self) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/plus%28_,_%29-2qex0.md)
  Generates a column by adding each element in an optional column type to the corresponding elements of another.
- [func + <L, R>(L, R) -> Column<L.Element>](./plus%28_,_%29-1i7oh.md)
  Generates a column by adding each element in a column type to the corresponding elements of an optional column type.
- [func + <L, R>(L, R) -> Column<R.Element>](./plus%28_,_%29-3exmp.md)
  Generates a column by adding each element in an optional column type to the corresponding elements of a column type.
### Generating an Optional Column by Subtracting Two Columns
- [static func - (Self, Self) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/minus%28_,_%29-5xfkx.md)
  Generates a column by subtracting each element in an optional column type from the corresponding elements of another.
- [func - <L, R>(L, R) -> Column<L.Element>](./minus%28_,_%29-25cs6.md)
  Generates a column by subtracting each element in an optional column type from the corresponding elements of a column type.
- [func - <L, R>(L, R) -> Column<R.Element>](./minus%28_,_%29-95yoe.md)
  Generates a column by subtracting each element in a column type from the corresponding elements of an optional column.
### Generating an Optional Column by Multiplying Two Columns
- [static func * (Self, Self) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/star%28_,_%29-5f5kx.md)
  Generates a column by multiplying each element in an optional column type by the corresponding elements of another.
- [func * <L, R>(L, R) -> Column<R.Element>](./star%28_,_%29-2toor.md)
  Generates a column by multiplying each element in an optional column type by the corresponding elements of a column type.
- [func * <L, R>(L, R) -> Column<L.Element>](./star%28_,_%29-l9r3.md)
  Generates a column by multiplying each element in a column type by the corresponding elements of an optional column type.
### Generating an Optional Column by Dividing Two Columns
- [static func / (Self, Self) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/op%28_,_%29-4nmnl.md)
  Generates an integer column by dividing each element in an optional column type by the corresponding elements of another.
- [func / <L, R>(L, R) -> Column<L.Element>](./op%28_,_%29-9v3nw.md)
  Generates an integer column by dividing each element in a column type by the corresponding elements of an optional column type.
- [func / <L, R>(L, R) -> Column<R.Element>](./op%28_,_%29-4igyw.md)
  Generates an integer column by dividing each element in an optional column type by the corresponding elements of a column type.
- [static func / (Self, Self) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/op%28_,_%29-3rlo3.md)
  Generates a floating-point column by dividing each element in an optional column type by the corresponding elements of another.
- [func / <L, R>(L, R) -> Column<L.Element>](./op%28_,_%29-4pr65.md)
  Generates a floating-point column by dividing each element in a column type by the corresponding elements of an optional column type.
- [func / <L, R>(L, R) -> Column<R.Element>](./op%28_,_%29-58kg6.md)
  Generates a floating-point column by dividing each element in an optional column type by the corresponding elements of a column type.
### Generating an Optional Column by Combining a Value
- [static func + (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/plus%28_,_%29-501gg.md)
  Generates a column by adding a value to each element in an optional column.
- [static func + (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/plus%28_,_%29-6ko8x.md)
  Generates a column by adding each element in an optional column to a value.
- [static func - (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/minus%28_,_%29-9mejf.md)
  Generates a column by subtracting a value from each element in an optional column type.
- [static func - (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/minus%28_,_%29-5vffa.md)
  Generates a column by subtracting each element in an optional column from a value.
- [static func * (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/star%28_,_%29-orkq.md)
  Generates a column by multiplying each element in an optional column by a value.
- [static func * (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/star%28_,_%29-5vorv.md)
  Generates a column by multiplying a value by each element in an optional column type.
- [static func / (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/op%28_,_%29-7tbmq.md)
  Generates an integer column by dividing each element in an optional column by a value.
- [static func / (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/op%28_,_%29-56h1d.md)
  Generates an integer column by dividing a value by each element in an optional column type.
- [static func / (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/op%28_,_%29-5qhxr.md)
  Generates a floating-point column by dividing each element in an optional column by a value.
- [static func / (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/op%28_,_%29-2xfqa.md)
  Generates a floating-point column by dividing a value by each element in an optional column type.
### Describing an Optional Column
- [func description(options: FormattingOptions) -> String](./optionalcolumnprotocol/description%28options%29.md)
  Generates a string description of the optional column type.
### Supporting Types
- [associatedtype WrappedElement](./optionalcolumnprotocol/wrappedelement.md)
  The type of the optional column type’s elements.

## Relationships

### Inherits From
- [BidirectionalCollection](../Swift/bidirectionalcollection.md)
- [Collection](../Swift/collection.md)
- [ColumnProtocol](./columnprotocol.md)
- [Sequence](../Swift/sequence.md)
### Conforming Types
- [Column](./column.md)
- [ColumnSlice](./columnslice.md)
- [DiscontiguousColumnSlice](./discontiguouscolumnslice.md)

## See Also

### Typed Columns
- [struct Column](./column.md)
  A column in a data frame.
- [struct ColumnSlice](./columnslice.md)
  A collection that represents a selection of contiguous elements from a typed column.
- [struct FilledColumn](./filledcolumn.md)
  A view on a column that replaces missing elements with a default value.
- [struct DiscontiguousColumnSlice](./discontiguouscolumnslice.md)
  A collection that represents a selection, potentially with gaps, of elements from a typed column.
- [protocol ColumnProtocol](./columnprotocol.md)
  A type that represents a column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/optionalcolumnprotocol)*