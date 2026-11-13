# ColumnSlice

**Framework**: TabularData  
**Kind**: struct  
**Role**: Structure

A collection that represents a selection of contiguous elements from a typed column.

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
struct ColumnSlice<WrappedElement>
```

## Overview

A column slice contains only certain elements from its parent column. Create a slice by using a subscript with a range.

```swift
let slice = column[100 ..< 200]
```

## Topics

### Creating a column slice
- [init(Column<WrappedElement>)](./columnslice/init%28_%29.md)
  Creates a slice with the contents of a column.
### Creating a slice of unique elements
- [func distinct() -> DiscontiguousColumnSlice<WrappedElement>](./columnslice/distinct%28%29.md)
  Generates a discontiguous slice that contains unique elements.
### Creating a slice by filtering elements
- [func filter((ColumnSlice<WrappedElement>.Element) throws -> Bool) rethrows -> DiscontiguousColumnSlice<WrappedElement>](./columnslice/filter%28_%29.md)
  Generates a slice that contains the elements that satisfy the predicate.
### Creating a type-erased slice
- [func eraseToAnyColumn() -> AnyColumnSlice](./columnslice/erasetoanycolumn%28%29.md)
  Returns a type-erased column slice.
### Creating a column of the same type
- [var prototype: any AnyColumnPrototype](./columnslice/prototype.md)
  A prototype that creates type-erased columns with the same underlying type as the column slice.
### Creating transformed columns
- [func map<T>((ColumnSlice<WrappedElement>.Element) throws -> T?) rethrows -> Column<T>](./columnslice/map%28_%29.md)
  Creates a new column by applying a transformation to every element.
- [func filled(with: Self.WrappedElement) -> FilledColumn<Self>](./optionalcolumnprotocol/filled%28with%29.md)
  Generates a filled column by replacing missing elements with a value.
### Inspecting a column slice
- [var name: String](./columnslice/name.md)
  The name of the slice’s parent column.
- [var count: Int](./columnslice/count.md)
  The number of elements in the column slice.
- [var missingCount: Int](./columnslice/missingcount.md)
  The number of missing elements in the column slice.
- [var wrappedElementType: any Any.Type](./columnslice/wrappedelementtype.md)
  The underlying type of the column’s elements.
- [func argmin() -> Int?](./columnslice/argmin%28%29.md)
  Returns the index of the element with the lowest value, ignoring missing elements.
- [func argmax() -> Int?](./columnslice/argmax%28%29.md)
  Returns the index of the element with the highest value, ignoring missing elements.
- [func isNil(at: Int) -> Bool](./columnslice/isnil%28at%29.md)
  Returns a Boolean that indicates whether the element at an index is missing.
### Accessing elements
- [subscript(Int) -> ColumnSlice<WrappedElement>.Element](./columnslice/subscript%28_%29-38hn8.md)
  Accesses an element at an index.
- [subscript(Range<Int>) -> ColumnSlice<WrappedElement>](./columnslice/subscript%28_%29-7lrhk.md)
  Accesses a contiguous range of elements.
### Summarizing a column slice
- [func summary() -> CategoricalSummary<WrappedElement>](./columnslice/summary%28%29.md)
  Generates a categorical summary of the column slice’s elements.
- [func numericSummary() -> NumericSummary<Double>](./columnslice/numericsummary%28%29-68ohj.md)
  Generates a numeric summary of the integer column slice’s elements.
- [func numericSummary() -> NumericSummary<WrappedElement>](./columnslice/numericsummary%28%29-5swa5.md)
  Generates a numeric summary of the floating-point column slice’s elements.
### Getting statistical values
- [func sum() -> WrappedElement](./columnslice/sum%28%29.md)
  Returns the sum of the column slice’s elements, ignoring missing elements.
- [func min() -> ColumnSlice<WrappedElement>.Element](./columnslice/min%28%29.md)
  Returns the element with the lowest value, ignoring missing elements.
- [func max() -> ColumnSlice<WrappedElement>.Element](./columnslice/max%28%29.md)
  Returns the element with the highest value, ignoring missing elements.
- [func mean() -> Double?](./columnslice/mean%28%29-3inzf.md)
  Returns the mean average of the integer slice’s elements, ignoring missing elements.
- [func mean() -> ColumnSlice<WrappedElement>.Element](./columnslice/mean%28%29-7u3i0.md)
  Returns the mean average of the floating-point slice’s elements, ignoring missing elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> Double?](./columnslice/standarddeviation%28deltadegreesoffreedom%29-1i05i.md)
  Returns the standard deviation of the integer column slice’s elements, ignoring missing elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> ColumnSlice<WrappedElement>.Element](./columnslice/standarddeviation%28deltadegreesoffreedom%29-3d6vo.md)
  Returns the standard deviation of the floating-point column slice’s elements, ignoring missing elements.
### Describing a column slice
- [var description: String](./columnslice/description.md)
  A text representation of the column slice.
- [var debugDescription: String](./columnslice/debugdescription.md)
  A text representation of the column slice suitable for debugging.
- [var customMirror: Mirror](./columnslice/custommirror.md)
  A mirror that reflects the column slice.
### Comparing two column slices
- [static func == (ColumnSlice<WrappedElement>, ColumnSlice<WrappedElement>) -> Bool](./columnslice/eqeq%28_,_%29.md)
  Returns a Boolean that indicates whether the column slices are equal.
- [static func != (Self, Self.Element) -> [Bool]](./columnprotocol/noteq%28_,_%29-557vb.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type isn’t equal to a value.
- [static func != (Self.Element, Self) -> [Bool]](./columnprotocol/noteq%28_,_%29-72ddh.md)
  Returns a Boolean array that indicates whether the value isn’t equal to the corresponding element of a column type.
### Modifying a column slice with a value
- [static func += (inout ColumnSlice<WrappedElement>, WrappedElement)](./columnslice/pluseq%28_,_%29-950qi.md)
  Modifies a column slice by adding a value to each element.
- [static func -= (inout ColumnSlice<WrappedElement>, WrappedElement)](./columnslice/minuseq%28_,_%29-1n1gh.md)
  Modifies a column slice by subtracting a value from each element.
- [static func *= (inout ColumnSlice<WrappedElement>, WrappedElement)](./columnslice/stareq%28_,_%29-i6qs.md)
  Modifies a column slice by multiplying each element by a value.
- [static func /= (inout ColumnSlice<WrappedElement>, WrappedElement)](./columnslice/opeq%28_,_%29-8oi36.md)
  Modifies an integer column slice by dividing each element by a value.
- [static func /= (inout ColumnSlice<WrappedElement>, WrappedElement)](./columnslice/opeq%28_,_%29-8pl3f.md)
  Modifies a floating-point column slice by dividing each element by a value.
### Modifying a column slice with a collection of values
- [static func += <C>(inout ColumnSlice<WrappedElement>, C)](./columnslice/pluseq%28_,_%29-47cwm.md)
  Modifies a column slice by adding each value in a collection to the corresponding element in the column.
- [static func += <C>(inout ColumnSlice<WrappedElement>, C)](./columnslice/pluseq%28_,_%29-4bgdt.md)
  Modifies a column slice by adding each optional value in a collection to the corresponding element in the column.
- [static func -= <C>(inout ColumnSlice<WrappedElement>, C)](./columnslice/minuseq%28_,_%29-3kauw.md)
  Modifies a column slice by subtracting each value in a collection from the corresponding element in the column.
- [static func -= <C>(inout ColumnSlice<WrappedElement>, C)](./columnslice/minuseq%28_,_%29-1bqy4.md)
  Modifies a column slice by subtracting each optional value in a collection from the corresponding element in the column.
- [static func *= <C>(inout ColumnSlice<WrappedElement>, C)](./columnslice/stareq%28_,_%29-7lz8l.md)
  Modifies a column slice by multiplying each element in the column by the corresponding value in a collection.
- [static func *= <C>(inout ColumnSlice<WrappedElement>, C)](./columnslice/stareq%28_,_%29-3v2q0.md)
  Modifies a column slice by multiplying each element in the column by the corresponding optional value in a collection.
- [static func /= <C>(inout ColumnSlice<WrappedElement>, C)](./columnslice/opeq%28_,_%29-46jci.md)
  Modifies an integer column slice by dividing each element in the column by the corresponding value in a collection.
- [static func /= <C>(inout ColumnSlice<WrappedElement>, C)](./columnslice/opeq%28_,_%29-8frqe.md)
  Modifies an integer column slice by dividing each element in the column by the corresponding optional value in a collection.
- [static func /= <C>(inout ColumnSlice<WrappedElement>, C)](./columnslice/opeq%28_,_%29-1fciw.md)
  Modifies a floating-point column slice by dividing each element in the column by the corresponding value in a collection.
- [static func /= <C>(inout ColumnSlice<WrappedElement>, C)](./columnslice/opeq%28_,_%29-6ujes.md)
  Modifies a floating-point column slice by dividing each element in the column by the corresponding optional value in a collection.
### Generating a column by combining two column slices
- [static func + (Self, Self) -> Column<Self.Element>](./columnprotocol/plus%28_,_%29-yc11.md)
  Generates a column by adding each element in a column type to the corresponding elements of another.
- [static func + (Self, Self) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/plus%28_,_%29-2qex0.md)
  Generates a column by adding each element in an optional column type to the corresponding elements of another.
- [static func - (Self, Self) -> Column<Self.Element>](./columnprotocol/minus%28_,_%29-36zol.md)
  Generates a column by subtracting each element in a column type from the corresponding elements of another.
- [static func - (Self, Self) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/minus%28_,_%29-5xfkx.md)
  Generates a column by subtracting each element in an optional column type from the corresponding elements of another.
- [static func * (Self, Self) -> Column<Self.Element>](./columnprotocol/star%28_,_%29-9db1q.md)
  Generates a column by multiplying each element in a column type by the corresponding elements of another.
- [static func * (Self, Self) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/star%28_,_%29-5f5kx.md)
  Generates a column by multiplying each element in an optional column type by the corresponding elements of another.
- [static func / (Self, Self) -> Column<Self.Element>](./columnprotocol/op%28_,_%29-2urf0.md)
  Generates a floating-point column by dividing each element in a column type by the corresponding elements of another.
- [static func / (Self, Self) -> Column<Self.Element>](./columnprotocol/op%28_,_%29-922ku.md)
  Generates an integer column by dividing each element in a column type by the corresponding elements of another.
- [static func / (Self, Self) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/op%28_,_%29-3rlo3.md)
  Generates a floating-point column by dividing each element in an optional column type by the corresponding elements of another.
- [static func / (Self, Self) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/op%28_,_%29-4nmnl.md)
  Generates an integer column by dividing each element in an optional column type by the corresponding elements of another.
### Generating a column by adding a value
- [static func + (Self, Self.Element) -> Column<Self.Element>](./columnprotocol/plus%28_,_%29-39k8v.md)
  Generates a column by adding a value to each element in a column.
- [static func + (Self.Element, Self) -> Column<Self.Element>](./columnprotocol/plus%28_,_%29-94kiv.md)
  Generates a column by adding each element in a column to a value.
- [static func + (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/plus%28_,_%29-501gg.md)
  Generates a column by adding a value to each element in an optional column.
- [static func + (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/plus%28_,_%29-6ko8x.md)
  Generates a column by adding each element in an optional column to a value.
### Generating a column by subtracting a value
- [static func - (Self, Self.Element) -> Column<Self.Element>](./columnprotocol/minus%28_,_%29-6up21.md)
  Generates a column by subtracting a value from each element in a column.
- [static func - (Self.Element, Self) -> Column<Self.Element>](./columnprotocol/minus%28_,_%29-4fynh.md)
  Generates a column by subtracting each element in a column from a value.
- [static func - (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/minus%28_,_%29-9mejf.md)
  Generates a column by subtracting a value from each element in an optional column type.
- [static func - (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/minus%28_,_%29-5vffa.md)
  Generates a column by subtracting each element in an optional column from a value.
### Generating a column by multiplying a value
- [static func * (Self, Self.Element) -> Column<Self.Element>](./columnprotocol/star%28_,_%29-17vqd.md)
  Generates a column by multiplying each element in a column by a value.
- [static func * (Self.Element, Self) -> Column<Self.Element>](./columnprotocol/star%28_,_%29-3d6lu.md)
  Generates a column by multiplying a value by each element in a column.
- [static func * (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/star%28_,_%29-orkq.md)
  Generates a column by multiplying each element in an optional column by a value.
- [static func * (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/star%28_,_%29-5vorv.md)
  Generates a column by multiplying a value by each element in an optional column type.
### Generating a column by dividing a value
- [static func / (Self, Self.Element) -> Column<Self.Element>](./columnprotocol/op%28_,_%29-4a632.md)
  Generates an integer column by dividing each element in a column by a value.
- [static func / (Self, Self.Element) -> Column<Self.Element>](./columnprotocol/op%28_,_%29-6zigz.md)
  Generates a floating-point column by dividing each element in a column by a value.
- [static func / (Self.Element, Self) -> Column<Self.Element>](./columnprotocol/op%28_,_%29-4iv15.md)
  Generates a floating-point column by dividing a value by each element in a column.
- [static func / (Self.Element, Self) -> Column<Self.Element>](./columnprotocol/op%28_,_%29-7pe3t.md)
  Generates an integer column by dividing a value by each element in a column.
- [static func / (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/op%28_,_%29-5qhxr.md)
  Generates a floating-point column by dividing each element in an optional column by a value.
- [static func / (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/op%28_,_%29-7tbmq.md)
  Generates an integer column by dividing each element in an optional column by a value.
- [static func / (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/op%28_,_%29-2xfqa.md)
  Generates a floating-point column by dividing a value by each element in an optional column type.
- [static func / (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](./optionalcolumnprotocol/op%28_,_%29-56h1d.md)
  Generates an integer column by dividing a value by each element in an optional column type.
### Hashing a column slice
- [func hash(into: inout Hasher)](./columnslice/hash%28into%29.md)
  Hashes the essential components of the column slice by feeding them into a hasher.
### Retrieving an index
- [var startIndex: Int](./columnslice/startindex.md)
  The index of the initial element in the column slice.
- [var endIndex: Int](./columnslice/endindex.md)
  The index of the final element in the column slice.
- [func index(before: Int) -> Int](./columnslice/index%28before%29.md)
  Returns the index immediately before an element index.
- [func index(after: Int) -> Int](./columnslice/index%28after%29.md)
  Returns the index immediately after an element index.
### Supporting types
- [ColumnSlice.Element](./columnslice/element.md)
  The type of the column slice’s elements, which is an optional type of the parent column’s type.
- [ColumnSlice.Index](./columnslice/index.md)
  The type that represents a position in the column slice.
### Default Implementations
- [BidirectionalCollection Implementations](./columnslice/bidirectionalcollection-implementations.md)
- [Collection Implementations](./columnslice/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](./columnslice/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](./columnslice/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](./columnslice/customstringconvertible-implementations.md)
- [Equatable Implementations](./columnslice/equatable-implementations.md)
- [Hashable Implementations](./columnslice/hashable-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/bidirectionalcollection.md)
- [Collection](../Swift/collection.md)
- [ColumnProtocol](./columnprotocol.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [MutableCollection](../Swift/mutablecollection.md)
- [OptionalColumnProtocol](./optionalcolumnprotocol.md)
- [RandomAccessCollection](../Swift/randomaccesscollection.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Typed columns
- [struct Column](./column.md)
  A column in a data frame.
- [struct FilledColumn](./filledcolumn.md)
  A view on a column that replaces missing elements with a default value.
- [struct DiscontiguousColumnSlice](./discontiguouscolumnslice.md)
  A collection that represents a selection, potentially with gaps, of elements from a typed column.
- [protocol ColumnProtocol](./columnprotocol.md)
  A type that represents a column.
- [protocol OptionalColumnProtocol](./optionalcolumnprotocol.md)
  A type that represents a column that has missing values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnslice)*