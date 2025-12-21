# DiscontiguousColumnSlice

**Framework**: TabularData  
**Kind**: struct

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

#### Overview

A column slice contains only certain elements from its parent column. Create a slice by selecting certain elements. For example, use [`filter(_:)`](discontiguouscolumnslice/filter(_:).md) to create a slice that only includes elements with even values.

```swift
let slice = column.filter({ $0.isMultiple(of: 2) })
```

## Topics

### Creating a Column Slice
- [init(Column<WrappedElement>)](discontiguouscolumnslice/init(_:).md)
  Creates a slice with the contents of a column.
- [init(column: Column<WrappedElement>, ranges: [Range<Int>])](discontiguouscolumnslice/init(column:ranges:).md)
  Creates a slice with the contents of a column.
### Creating a Slice of Unique Elements
- [func distinct() -> DiscontiguousColumnSlice<WrappedElement>](discontiguouscolumnslice/distinct.md)
  Generates a discontiguous slice that contains unique elements.
### Creating a Type-Erased Slice
- [func eraseToAnyColumn() -> AnyColumnSlice](discontiguouscolumnslice/erasetoanycolumn.md)
  Generates a type-erased copy of the column slice.
### Creating a Column of the Same Type
- [var prototype: any AnyColumnPrototype](discontiguouscolumnslice/prototype.md)
  A prototype that creates type-erased columns with the same underlying type as the column slice.
### Creating Transformed Columns
- [func map<T>((DiscontiguousColumnSlice<WrappedElement>.Element) throws -> T?) rethrows -> Column<T>](discontiguouscolumnslice/map(_:).md)
  Creates a new column by applying a transformation to each element.
### Inspecting a Column Slice
- [var name: String](discontiguouscolumnslice/name.md)
  The name of the slice’s parent column.
- [var count: Int](discontiguouscolumnslice/count.md)
  The number of elements in the column slice.
- [var wrappedElementType: any Any.Type](discontiguouscolumnslice/wrappedelementtype.md)
  The underlying type of the column’s elements.
- [func argmin() -> Int?](discontiguouscolumnslice/argmin.md)
  Returns the index of the element with the lowest value, ignoring missing elements.
- [func argmax() -> Int?](discontiguouscolumnslice/argmax.md)
  Returns the index of the element with the highest value, ignoring missing elements.
- [func isNil(at: Int) -> Bool](discontiguouscolumnslice/isnil(at:).md)
  Returns a Boolean that indicates whether the element at the index is missing.
### Accessing Elements
- [subscript(Int) -> DiscontiguousColumnSlice<WrappedElement>.Element](discontiguouscolumnslice/subscript(_:)-9y37v.md)
  Accesses an element at an index.
- [subscript(Range<Int>) -> DiscontiguousColumnSlice<WrappedElement>](discontiguouscolumnslice/subscript(_:)-8rd2f.md)
  Accesses a contiguous range of elements.
- [subscript<R>(R) -> DiscontiguousColumnSlice<WrappedElement>](discontiguouscolumnslice/subscript(_:)-4k2lh.md)
  Accesses a contiguous range of elements with a range expression.
- [subscript((UnboundedRange_) -> ()) -> DiscontiguousColumnSlice<WrappedElement>](discontiguouscolumnslice/subscript(_:)-5xvit.md)
  Accesses a contiguous range of elements with an unbounded range.
### Summarizing a Column Slice
- [func summary() -> CategoricalSummary<WrappedElement>](discontiguouscolumnslice/summary.md)
  Generates a categorical summary of the column slice’s elements.
- [func numericSummary() -> NumericSummary<Double>](discontiguouscolumnslice/numericsummary-3r7pn.md)
  Generates a numeric summary of the integer column slice’s elements.
- [func numericSummary() -> NumericSummary<WrappedElement>](discontiguouscolumnslice/numericsummary-4b7m0.md)
  Generates a numeric summary of the floating-point column slice’s elements.
### Getting Statistical Values
- [func sum() -> WrappedElement](discontiguouscolumnslice/sum.md)
  Returns the sum of the column slice’s elements, ignoring missing elements.
- [func min() -> DiscontiguousColumnSlice<WrappedElement>.Element](discontiguouscolumnslice/min.md)
  Returns the element with the lowest value, ignoring missing elements.
- [func max() -> DiscontiguousColumnSlice<WrappedElement>.Element](discontiguouscolumnslice/max.md)
  Returns the element with the highest value, ignoring missing elements.
- [func mean() -> DiscontiguousColumnSlice<WrappedElement>.Element](discontiguouscolumnslice/mean-3y11c.md)
  Returns the mean average of the floating-point slice’s elements, ignoring missing elements.
- [func mean() -> Double?](discontiguouscolumnslice/mean-49u93.md)
  Returns the mean average of the integer slice’s elements, ignoring missing elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> Double?](discontiguouscolumnslice/standarddeviation(deltadegreesoffreedom:)-36nx2.md)
  Returns the standard deviation of the integer column slice’s elements, ignoring missing elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> DiscontiguousColumnSlice<WrappedElement>.Element](discontiguouscolumnslice/standarddeviation(deltadegreesoffreedom:)-5vd4r.md)
  Returns the standard deviation of the floating-point column slice’s elements, ignoring missing elements.
### Describing a Column Slice
- [var description: String](discontiguouscolumnslice/description.md)
  A text representation of the column slice.
- [var debugDescription: String](discontiguouscolumnslice/debugdescription.md)
  A text representation of the column slice suitable for debugging.
- [var customMirror: Mirror](discontiguouscolumnslice/custommirror.md)
  A mirror that reflects the column slice.
### Comparing Two Column Slices
- [static func == (DiscontiguousColumnSlice<WrappedElement>, DiscontiguousColumnSlice<WrappedElement>) -> Bool](discontiguouscolumnslice/==(_:_:).md)
  Returns a Boolean that indicates whether the column slices are equal.
### Modifying a Column Slice with a Value
- [static func += (inout DiscontiguousColumnSlice<WrappedElement>, WrappedElement)](discontiguouscolumnslice/+=(_:_:)-1mzz0.md)
  Modifies a column slice by adding a value to each element.
- [static func -= (inout DiscontiguousColumnSlice<WrappedElement>, WrappedElement)](discontiguouscolumnslice/-=(_:_:)-2yrui.md)
  Modifies a column slice by subtracting a value from each element.
- [static func *= (inout DiscontiguousColumnSlice<WrappedElement>, WrappedElement)](discontiguouscolumnslice/*=(_:_:)-7gcqc.md)
  Modifies a column slice by multiplying each element by a value.
- [static func /= (inout DiscontiguousColumnSlice<WrappedElement>, WrappedElement)](discontiguouscolumnslice/_=(_:_:)-1g0yb.md)
  Modifies an integer column slice by dividing each element by a value.
- [static func /= (inout DiscontiguousColumnSlice<WrappedElement>, WrappedElement)](discontiguouscolumnslice/_=(_:_:)-6i7hx.md)
  Modifies a floating-point column slice by dividing each element by a value.
### Modifying a Column Slice with a Collection of Values
- [static func += <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](discontiguouscolumnslice/+=(_:_:)-2jxz1.md)
  Modifies a column slice by adding each value in a collection to the corresponding element in the column.
- [static func += <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](discontiguouscolumnslice/+=(_:_:)-lpai.md)
  Modifies a column slice by adding each optional value in a collection to the corresponding element in the column.
- [static func -= <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](discontiguouscolumnslice/-=(_:_:)-9nkq6.md)
  Modifies a column slice by subtracting each value in a collection from the corresponding element in the column.
- [static func -= <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](discontiguouscolumnslice/-=(_:_:)-8a20q.md)
  Modifies a column slice by subtracting each optional value in a collection from the corresponding element in the column.
- [static func *= <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](discontiguouscolumnslice/*=(_:_:)-9jg9h.md)
  Modifies a column slice by multiplying each element in the column by the corresponding value in a collection.
- [static func *= <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](discontiguouscolumnslice/*=(_:_:)-18nlr.md)
  Modifies a column slice by multiplying each element in the column by the corresponding optional value in a collection.
- [static func /= <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](discontiguouscolumnslice/_=(_:_:)-6xf9s.md)
  Modifies an integer column slice by dividing each element in the column by the corresponding value in a collection.
- [static func /= <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](discontiguouscolumnslice/_=(_:_:)-1mzcg.md)
  Modifies an integer column slice by dividing each element in the column by the corresponding optional value in a collection.
- [static func /= <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](discontiguouscolumnslice/_=(_:_:)-39wsi.md)
  Modifies a floating-point column slice by dividing each element in the column by the corresponding value in a collection.
- [static func /= <C>(inout DiscontiguousColumnSlice<WrappedElement>, C)](discontiguouscolumnslice/_=(_:_:)-6lzj.md)
  Modifies a floating-point column slice by dividing each element in the column by the corresponding optional value in a collection.
### Hashing a Column Slice
- [func hash(into: inout Hasher)](discontiguouscolumnslice/hash(into:).md)
  Hashes the essential components of the column slice by feeding them into a hasher.
### Supporting Types
- [DiscontiguousColumnSlice.Element](discontiguouscolumnslice/element.md)
  The type of the column slice’s elements.
- [DiscontiguousColumnSlice.Index](discontiguouscolumnslice/index.md)
  The type that represents a position in the column slice.
### Instance Properties
- [var missingCount: Int](discontiguouscolumnslice/missingcount.md)
  The number of missing elements in the column slice.
### Default Implementations
- [BidirectionalCollection Implementations](discontiguouscolumnslice/bidirectionalcollection-implementations.md)
- [Collection Implementations](discontiguouscolumnslice/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](discontiguouscolumnslice/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](discontiguouscolumnslice/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](discontiguouscolumnslice/customstringconvertible-implementations.md)
- [Equatable Implementations](discontiguouscolumnslice/equatable-implementations.md)
- [Hashable Implementations](discontiguouscolumnslice/hashable-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [ColumnProtocol](columnprotocol.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MutableCollection](../Swift/MutableCollection.md)
- [OptionalColumnProtocol](optionalcolumnprotocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct Column](column.md)
  A column in a data frame.
- [struct ColumnSlice](columnslice.md)
  A collection that represents a selection of contiguous elements from a typed column.
- [struct FilledColumn](filledcolumn.md)
  A view on a column that replaces missing elements with a default value.
- [protocol ColumnProtocol](columnprotocol.md)
  A type that represents a column.
- [protocol OptionalColumnProtocol](optionalcolumnprotocol.md)
  A type that represents a column that has missing values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice)*