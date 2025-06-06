# ColumnProtocol

**Framework**: TabularData  
**Kind**: protocol

A type that represents a column.

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
protocol ColumnProtocol<Element> : BidirectionalCollection
```

#### Overview

`ColumnProtocol` defines the common functionality for typed column types. Its type-erased counterpart is [`AnyColumnProtocol`](anycolumnprotocol.md).

## Topics

### Inspecting a Column Type
- [var name: String](columnprotocol/name.md)
  The name of the column.
### Generating a Column by Adding Two Columns
- [static func + (Self, Self) -> Column<Self.Element>](columnprotocol/+(_:_:)-yc11.md)
  Generates a column by adding each element in a column type to the corresponding elements of another.
- [func + <L, R>(L, R) -> Column<L.Element>](+(_:_:)-1i7oh.md)
  Generates a column by adding each element in a column type to the corresponding elements of an optional column type.
- [func + <L, R>(L, R) -> Column<R.Element>](+(_:_:)-3exmp.md)
  Generates a column by adding each element in an optional column type to the corresponding elements of a column type.
### Generating a Column by Subtracting Two Columns
- [static func - (Self, Self) -> Column<Self.Element>](columnprotocol/-(_:_:)-36zol.md)
  Generates a column by subtracting each element in a column type from the corresponding elements of another.
- [func - <L, R>(L, R) -> Column<L.Element>](-(_:_:)-25cs6.md)
  Generates a column by subtracting each element in an optional column type from the corresponding elements of a column type.
- [func - <L, R>(L, R) -> Column<R.Element>](-(_:_:)-95yoe.md)
  Generates a column by subtracting each element in a column type from the corresponding elements of an optional column.
### Generating a Column by Multiplying Two Columns
- [static func * (Self, Self) -> Column<Self.Element>](columnprotocol/*(_:_:)-9db1q.md)
  Generates a column by multiplying each element in a column type by the corresponding elements of another.
- [func * <L, R>(L, R) -> Column<L.Element>](*(_:_:)-l9r3.md)
  Generates a column by multiplying each element in a column type by the corresponding elements of an optional column type.
- [func * <L, R>(L, R) -> Column<R.Element>](*(_:_:)-2toor.md)
  Generates a column by multiplying each element in an optional column type by the corresponding elements of a column type.
### Generating a Column by Dividing Two Columns
- [static func / (Self, Self) -> Column<Self.Element>](columnprotocol/_(_:_:)-922ku.md)
  Generates an integer column by dividing each element in a column type by the corresponding elements of another.
- [func / <L, R>(L, R) -> Column<L.Element>](_(_:_:)-9v3nw.md)
  Generates an integer column by dividing each element in a column type by the corresponding elements of an optional column type.
- [func / <L, R>(L, R) -> Column<R.Element>](_(_:_:)-4igyw.md)
  Generates an integer column by dividing each element in an optional column type by the corresponding elements of a column type.
- [static func / (Self, Self) -> Column<Self.Element>](columnprotocol/_(_:_:)-2urf0.md)
  Generates a floating-point column by dividing each element in a column type by the corresponding elements of another.
- [func / <L, R>(L, R) -> Column<L.Element>](_(_:_:)-4pr65.md)
  Generates a floating-point column by dividing each element in a column type by the corresponding elements of an optional column type.
- [func / <L, R>(L, R) -> Column<R.Element>](_(_:_:)-58kg6.md)
  Generates a floating-point column by dividing each element in an optional column type by the corresponding elements of a column type.
### Generating a Column by Combining a Value
- [static func + (Self, Self.Element) -> Column<Self.Element>](columnprotocol/+(_:_:)-39k8v.md)
  Generates a column by adding a value to each element in a column.
- [static func + (Self.Element, Self) -> Column<Self.Element>](columnprotocol/+(_:_:)-94kiv.md)
  Generates a column by adding each element in a column to a value.
- [static func - (Self.Element, Self) -> Column<Self.Element>](columnprotocol/-(_:_:)-4fynh.md)
  Generates a column by subtracting each element in a column from a value.
- [static func - (Self, Self.Element) -> Column<Self.Element>](columnprotocol/-(_:_:)-6up21.md)
  Generates a column by subtracting a value from each element in a column.
- [static func * (Self, Self.Element) -> Column<Self.Element>](columnprotocol/*(_:_:)-17vqd.md)
  Generates a column by multiplying each element in a column by a value.
- [static func * (Self.Element, Self) -> Column<Self.Element>](columnprotocol/*(_:_:)-3d6lu.md)
  Generates a column by multiplying a value by each element in a column.
- [static func / (Self, Self.Element) -> Column<Self.Element>](columnprotocol/_(_:_:)-4a632.md)
  Generates an integer column by dividing each element in a column by a value.
- [static func / (Self.Element, Self) -> Column<Self.Element>](columnprotocol/_(_:_:)-7pe3t.md)
  Generates an integer column by dividing a value by each element in a column.
- [static func / (Self, Self.Element) -> Column<Self.Element>](columnprotocol/_(_:_:)-6zigz.md)
  Generates a floating-point column by dividing each element in a column by a value.
- [static func / (Self.Element, Self) -> Column<Self.Element>](columnprotocol/_(_:_:)-4iv15.md)
  Generates a floating-point column by dividing a value by each element in a column.
### Comparing a Column with a Value
- [static func == (Self, Self.Element) -> [Bool]](columnprotocol/==(_:_:)-5jc0x.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type is equal to a value.
- [static func == (Self.Element, Self) -> [Bool]](columnprotocol/==(_:_:)-4hx04.md)
  Returns a Boolean array that indicates whether the value is equal to the corresponding element of a column type.
- [static func != (Self, Self.Element) -> [Bool]](columnprotocol/!=(_:_:)-557vb.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type isn’t equal to a value.
- [static func != (Self.Element, Self) -> [Bool]](columnprotocol/!=(_:_:)-72ddh.md)
  Returns a Boolean array that indicates whether the value isn’t equal to the corresponding element of a column type.
### Operators
- [static func > (Self.Element, Self) -> [Bool]](columnprotocol/_(_:_:)-68any.md)
  Returns a Boolean array that indicates whether the value is greater than the corresponding element of a column type.
- [static func < (Self.Element, Self) -> [Bool]](columnprotocol/_(_:_:)-70vl1.md)
  Returns a Boolean array that indicates whether the value is less than the corresponding element of a column type.
- [static func < (Self, Self.Element) -> [Bool]](columnprotocol/_(_:_:)-7gy2j.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type is less than a value.
- [static func > (Self, Self.Element) -> [Bool]](columnprotocol/_(_:_:)-9rct2.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type is greater than a value.
- [static func <= (Self.Element, Self) -> [Bool]](columnprotocol/_=(_:_:)-17m6l.md)
  Returns a Boolean array that indicates whether the value is less than or equal to the corresponding element of a column type.
- [static func >= (Self, Self.Element) -> [Bool]](columnprotocol/_=(_:_:)-2w8gt.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type is greater than or equal to a value.
- [static func >= (Self.Element, Self) -> [Bool]](columnprotocol/_=(_:_:)-8jak4.md)
  Returns a Boolean array that indicates whether the value is greater than or equal to the corresponding element of a column type.
- [static func <= (Self, Self.Element) -> [Bool]](columnprotocol/_=(_:_:)-9wr8s.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type is less than or equal to a value.

## Relationships

### Inherits From
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Sequence](../Swift/Sequence.md)
### Inherited By
- [OptionalColumnProtocol](optionalcolumnprotocol.md)
### Conforming Types
- [Column](column.md)
- [ColumnSlice](columnslice.md)
- [DiscontiguousColumnSlice](discontiguouscolumnslice.md)
- [FilledColumn](filledcolumn.md)

## See Also

- [struct Column](column.md)
  A column in a data frame.
- [struct ColumnSlice](columnslice.md)
  A collection that represents a selection of contiguous elements from a typed column.
- [struct FilledColumn](filledcolumn.md)
  A view on a column that replaces missing elements with a default value.
- [struct DiscontiguousColumnSlice](discontiguouscolumnslice.md)
  A collection that represents a selection, potentially with gaps, of elements from a typed column.
- [protocol OptionalColumnProtocol](optionalcolumnprotocol.md)
  A type that represents a column that has missing values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnprotocol)*