# DiscontiguousColumnSlice

**Framework**: TabularData  
**Kind**: struct  
**Role**: Structure

A collection that represents a selection, potentially with gaps, of elements from a typed column.

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
struct DiscontiguousColumnSlice<WrappedElement>
```

## Overview

A column slice contains only certain elements from its parent column. Create a slice by selecting certain elements. For example, use [`filter(_:)`](./discontiguouscolumnslice/filter%28_%29.md) to create a slice that only includes elements with even values.

```swift
let slice = column.filter({ $0.isMultiple(of: 2) })
```

## Topics

### Creating a column slice
- [init(Column<WrappedElement>)](./discontiguouscolumnslice/init%28_%29.md)
  Creates a slice with the contents of a column.
- [init(column: Column<WrappedElement>, ranges: [Range<Int>])](./discontiguouscolumnslice/init%28column,ranges%29.md)
  Creates a slice with the contents of a column.
### Creating a slice of unique elements
- [func distinct() -> DiscontiguousColumnSlice<WrappedElement>](./discontiguouscolumnslice/distinct%28%29.md)
  Generates a discontiguous slice that contains unique elements.
### Creating a slice by filtering elements
- [func filter((DiscontiguousColumnSlice<WrappedElement>.Element) throws -> Bool) rethrows -> DiscontiguousColumnSlice<WrappedElement>](./discontiguouscolumnslice/filter%28_%29.md)
  Generates a slice that contains the elements that satisfy the predicate.
### Creating a type-erased slice
- [func eraseToAnyColumn() -> AnyColumnSlice](./discontiguouscolumnslice/erasetoanycolumn%28%29.md)
  Generates a type-erased copy of the column slice.
### Creating a column of the same type
- [var prototype: any AnyColumnPrototype](./discontiguouscolumnslice/prototype.md)
  A prototype that creates type-erased columns with the same underlying type as the column slice.
### Creating transformed columns
- [func map<T>((DiscontiguousColumnSlice<WrappedElement>.Element) throws -> T?) rethrows -> Column<T>](./discontiguouscolumnslice/map%28_%29.md)
  Creates a new column by applying a transformation to each element.
- [func filled(with: Self.WrappedElement) -> FilledColumn<Self>](./optionalcolumnprotocol/filled%28with%29.md)
  Generates a filled column by replacing missing elements with a value.
### Inspecting a column slice
- [var name: String](./discontiguouscolumnslice/name.md)
  The name of the slice’s parent column.
- [var count: Int](./discontiguouscolumnslice/count.md)
  The number of elements in the column slice.
- [var missingCount: Int](./discontiguouscolumnslice/missingcount.md)
  The number of missing elements in the column slice.
- [var wrappedElementType: any Any.Type](./discontiguouscolumnslice/wrappedelementtype.md)
  The underlying type of the column’s elements.
- [func argmin() -> Int?](./discontiguouscolumnslice/argmin%28%29.md)
  Returns the index of the element with the lowest value, ignoring missing elements.
- [func argmax() -> Int?](./discontiguouscolumnslice/argmax%28%29.md)
  Returns the index of the element with the highest value, ignoring missing elements.
- [func isNil(at: Int) -> Bool](./discontiguouscolumnslice/isnil%28at%29.md)
  Returns a Boolean that indicates whether the element at the index is missing.
### Accessing elements
- [subscript(Int) -> DiscontiguousColumnSlice<WrappedElement>.Element](./discontiguouscolumnslice/subscript%28_%29-9y37v.md)
  Accesses an element at an index.
- [subscript(Range<Int>) -> DiscontiguousColumnSlice<WrappedElement>](./discontiguouscolumnslice/subscript%28_%29-8rd2f.md)
  Accesses a contiguous range of elements.
- [subscript<R>(R) -> DiscontiguousColumnSlice<WrappedElement>](./discontiguouscolumnslice/subscript%28_%29-4k2lh.md)
  Accesses a contiguous range of elements with a range expression.
- [subscript(UnboundedRange) -> DiscontiguousColumnSlice<WrappedElement>](./discontiguouscolumnslice/subscript%28_%29-5xvit.md)
  Accesses a contiguous range of elements with an unbounded range.
### Summarizing a column slice
- [func summary() -> CategoricalSummary<WrappedElement>](./discontiguouscolumnslice/summary%28%29.md)
  Generates a categorical summary of the column slice’s elements.
- [func numericSummary() -> NumericSummary<Double>](./discontiguouscolumnslice/numericsummary%28%29-3r7pn.md)
  Generates a numeric summary of the integer column slice’s elements.
- [func numericSummary() -> NumericSummary<WrappedElement>](./discontiguouscolumnslice/numericsummary%28%29-4b7m0.md)
  Generates a numeric summary of the floating-point column slice’s elements.
### Getting statistical values
- [func sum() -> WrappedElement](./discontiguouscolumnslice/sum%28%29.md)
  Returns the sum of the column slice’s elements, ignoring missing elements.
- [func min() -> DiscontiguousColumnSlice<WrappedElement>.Element](./discontiguouscolumnslice/min%28%29.md)
  Returns the element with the lowest value, ignoring missing elements.
- [func max() -> DiscontiguousColumnSlice<WrappedElement>.Element](./discontiguouscolumnslice/max%28%29.md)
  Returns the element with the highest value, ignoring missing elements.
- [func mean() -> DiscontiguousColumnSlice<WrappedElement>.Element](./discontiguouscolumnslice/mean%28%29-3y11c.md)
  Returns the mean average of the floating-point slice’s elements, ignoring missing elements.
- [func mean() -> Double?](./discontiguouscolumnslice/mean%28%29-49u93.md)
  Returns the mean average of the integer slice’s elements, ignoring missing elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> Double?](./discontiguouscolumnslice/standarddeviation%28deltadegreesoffreedom%29-36nx2.md)
  Returns the standard deviation of the integer column slice’s elements, ignoring missing elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> DiscontiguousColumnSlice<WrappedElement>.Element](./discontiguouscolumnslice/standarddeviation%28deltadegreesoffreedom%29-5vd4r.md)
  Returns the standard deviation of the floating-point column slice’s elements, ignoring missing elements.
### Describing a column slice
- [var description: String](./discontiguouscolumnslice/description.md)
  A text representation of the column slice.
- [var debugDescription: String](./discontiguouscolumnslice/debugdescription.md)
  A text representation of the column slice suitable for debugging.
- [var customMirror: Mirror](./discontiguouscolumnslice/custommirror.md)
  A mirror that reflects the column slice.
### Comparing two column slices
- [static func == (DiscontiguousColumnSlice<WrappedElement>, DiscontiguousColumnSlice<WrappedElement>) -> Bool](./discontiguouscolumnslice/eqeq%28_,_%29.md)
  Returns a Boolean that indicates whether the column slices are equal.
- [static func != (Self, Self.Element) -> [Bool]](./columnprotocol/noteq%28_,_%29-557vb.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type isn’t equal to a value.
- [static func != (Self.Element, Self) -> [Bool]](./columnprotocol/noteq%28_,_%29-72ddh.md)
  Returns a Boolean array that indicates whether the value isn’t equal to the corresponding element of a column type.
### Modifying a column slice with a value
- [static func += (inout DiscontiguousColumnSlice<WrappedElement>, WrappedElement)](./discontiguouscolumnslice/pluseq%28_,_%29-1mzz0.md)
  Modifies a column slice by adding a value to each element.
- [static func -= (inout DiscontiguousColumnSlice<WrappedElement>, WrappedElement)](./discontiguouscolumnslice/minuseq%28_,_%29-2yrui.md)
  Modifies a column slice by subtracting a value from each element.
- [static func *= (inout DiscontiguousColumnSlice<WrappedElement>, WrappedElement)](./discontiguouscolumnslice/stareq%28_,_%29-7gcqc.md)
  Modifies a column slice by multiplying each element by a value.
- [static func /= (inout DiscontiguousColumnSlice<WrappedElement>, WrappedElement)](./discontiguouscolumnslice/opeq%28_,_%29-1g0yb.md)
  Modifies an integer column slice by dividing each element by a value.
- [static func /= (inout DiscontiguousColumnSlice<WrappedElement>, WrappedElement)](./discontiguouscolumnslice/opeq%28_,_%29-6i7hx.md)
  Modifies a floating-point column slice by dividing each element by a value.
### Modifying a column slice with a collection of values
- [static func += <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](./discontiguouscolumnslice/pluseq%28_,_%29-2jxz1.md)
  Modifies a column slice by adding each value in a collection to the corresponding element in the column.
- [static func += <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](./discontiguouscolumnslice/pluseq%28_,_%29-lpai.md)
  Modifies a column slice by adding each optional value in a collection to the corresponding element in the column.
- [static func -= <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](./discontiguouscolumnslice/minuseq%28_,_%29-9nkq6.md)
  Modifies a column slice by subtracting each value in a collection from the corresponding element in the column.
- [static func -= <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](./discontiguouscolumnslice/minuseq%28_,_%29-8a20q.md)
  Modifies a column slice by subtracting each optional value in a collection from the corresponding element in the column.
- [static func *= <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](./discontiguouscolumnslice/stareq%28_,_%29-9jg9h.md)
  Modifies a column slice by multiplying each element in the column by the corresponding value in a collection.
- [static func *= <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](./discontiguouscolumnslice/stareq%28_,_%29-18nlr.md)
  Modifies a column slice by multiplying each element in the column by the corresponding optional value in a collection.
- [static func /= <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](./discontiguouscolumnslice/opeq%28_,_%29-6xf9s.md)
  Modifies an integer column slice by dividing each element in the column by the corresponding value in a collection.
- [static func /= <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](./discontiguouscolumnslice/opeq%28_,_%29-1mzcg.md)
  Modifies an integer column slice by dividing each element in the column by the corresponding optional value in a collection.
- [static func /= <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](./discontiguouscolumnslice/opeq%28_,_%29-39wsi.md)
  Modifies a floating-point column slice by dividing each element in the column by the corresponding value in a collection.
- [static func /= <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](./discontiguouscolumnslice/opeq%28_,_%29-6lzj.md)
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
- [func hash(into: inout Hasher)](./discontiguouscolumnslice/hash%28into%29.md)
  Hashes the essential components of the column slice by feeding them into a hasher.
### Retrieving an index
- [var startIndex: Int](./discontiguouscolumnslice/startindex.md)
  The index of the initial element in the column slice.
- [var endIndex: Int](./discontiguouscolumnslice/endindex.md)
  The index of the final element in the column slice.
- [func index(before: Int) -> Int](./discontiguouscolumnslice/index%28before%29.md)
  Returns the index immediately before an element index.
- [func index(after: Int) -> Int](./discontiguouscolumnslice/index%28after%29.md)
  Returns the index immediately after an element index.
### Supporting types
- [DiscontiguousColumnSlice.Element](./discontiguouscolumnslice/element.md)
  The type of the column slice’s elements.
- [DiscontiguousColumnSlice.Index](./discontiguouscolumnslice/index.md)
  The type that represents a position in the column slice.
### Default Implementations
- [BidirectionalCollection Implementations](./discontiguouscolumnslice/bidirectionalcollection-implementations.md)
- [Collection Implementations](./discontiguouscolumnslice/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](./discontiguouscolumnslice/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](./discontiguouscolumnslice/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](./discontiguouscolumnslice/customstringconvertible-implementations.md)
- [Equatable Implementations](./discontiguouscolumnslice/equatable-implementations.md)
- [Hashable Implementations](./discontiguouscolumnslice/hashable-implementations.md)

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
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Typed columns
- [struct Column](./column.md)
  A column in a data frame.
- [struct ColumnSlice](./columnslice.md)
  A collection that represents a selection of contiguous elements from a typed column.
- [struct FilledColumn](./filledcolumn.md)
  A view on a column that replaces missing elements with a default value.
- [protocol ColumnProtocol](./columnprotocol.md)
  A type that represents a column.
- [protocol OptionalColumnProtocol](./optionalcolumnprotocol.md)
  A type that represents a column that has missing values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice)*