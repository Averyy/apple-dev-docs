# ColumnSlice

**Framework**: TabularData  
**Kind**: struct

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

#### Overview

A column slice contains only certain elements from its parent column. Create a slice by using a subscript with a range.

```swift
let slice = column[100 ..< 200]
```

## Topics

### Creating a Column Slice
- [init(Column<WrappedElement>)](columnslice/init(_:).md)
  Creates a slice with the contents of a column.
### Creating a Slice of Unique Elements
- [func distinct() -> DiscontiguousColumnSlice<WrappedElement>](columnslice/distinct.md)
  Generates a discontiguous slice that contains unique elements.
### Creating a Type-Erased Slice
- [func eraseToAnyColumn() -> AnyColumnSlice](columnslice/erasetoanycolumn.md)
  Returns a type-erased column slice.
### Creating a Column of the Same Type
- [var prototype: any AnyColumnPrototype](columnslice/prototype.md)
  A prototype that creates type-erased columns with the same underlying type as the column slice.
### Creating Transformed Columns
- [func map<T>((ColumnSlice<WrappedElement>.Element) throws -> T?) rethrows -> Column<T>](columnslice/map(_:).md)
  Creates a new column by applying a transformation to every element.
- [func filled(with: Self.WrappedElement) -> FilledColumn<Self>](columnslice/filled(with:).md)
  Generates a filled column by replacing missing elements with a value.
### Inspecting a Column Slice
- [var name: String](columnslice/name.md)
  The name of the slice’s parent column.
- [var count: Int](columnslice/count.md)
  The number of elements in the column slice.
- [var wrappedElementType: any Any.Type](columnslice/wrappedelementtype.md)
  The underlying type of the column’s elements.
- [func argmin() -> Int?](columnslice/argmin.md)
  Returns the index of the element with the lowest value, ignoring missing elements.
- [func argmax() -> Int?](columnslice/argmax.md)
  Returns the index of the element with the highest value, ignoring missing elements.
- [func isNil(at: Int) -> Bool](columnslice/isnil(at:).md)
  Returns a Boolean that indicates whether the element at an index is missing.
### Accessing Elements
- [subscript(Int) -> ColumnSlice<WrappedElement>.Element](columnslice/subscript(_:)-38hn8.md)
  Accesses an element at an index.
- [subscript(Range<Int>) -> ColumnSlice<WrappedElement>](columnslice/subscript(_:)-7lrhk.md)
  Accesses a contiguous range of elements.
### Summarizing a Column Slice
- [func summary() -> CategoricalSummary<WrappedElement>](columnslice/summary.md)
  Generates a categorical summary of the column slice’s elements.
- [func numericSummary() -> NumericSummary<Double>](columnslice/numericsummary-68ohj.md)
  Generates a numeric summary of the integer column slice’s elements.
- [func numericSummary() -> NumericSummary<WrappedElement>](columnslice/numericsummary-5swa5.md)
  Generates a numeric summary of the floating-point column slice’s elements.
### Getting Statistical Values
- [func sum() -> WrappedElement](columnslice/sum.md)
  Returns the sum of the column slice’s elements, ignoring missing elements.
- [func min() -> ColumnSlice<WrappedElement>.Element](columnslice/min.md)
  Returns the element with the lowest value, ignoring missing elements.
- [func max() -> ColumnSlice<WrappedElement>.Element](columnslice/max.md)
  Returns the element with the highest value, ignoring missing elements.
- [func mean() -> Double?](columnslice/mean-3inzf.md)
  Returns the mean average of the integer slice’s elements, ignoring missing elements.
- [func mean() -> ColumnSlice<WrappedElement>.Element](columnslice/mean-7u3i0.md)
  Returns the mean average of the floating-point slice’s elements, ignoring missing elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> Double?](columnslice/standarddeviation(deltadegreesoffreedom:)-1i05i.md)
  Returns the standard deviation of the integer column slice’s elements, ignoring missing elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> ColumnSlice<WrappedElement>.Element](columnslice/standarddeviation(deltadegreesoffreedom:)-3d6vo.md)
  Returns the standard deviation of the floating-point column slice’s elements, ignoring missing elements.
### Describing a Column Slice
- [var description: String](columnslice/description.md)
  A text representation of the column slice.
- [var debugDescription: String](columnslice/debugdescription.md)
  A text representation of the column slice suitable for debugging.
- [func description(options: FormattingOptions) -> String](columnslice/description(options:).md)
  Generates a string description of the optional column type.
- [var customMirror: Mirror](columnslice/custommirror.md)
  A mirror that reflects the column slice.
### Comparing Two Column Slices
- [static func == (ColumnSlice<WrappedElement>, ColumnSlice<WrappedElement>) -> Bool](columnslice/==(_:_:).md)
  Returns a Boolean that indicates whether the column slices are equal.
- [static func != (Self, Self) -> Bool](columnslice/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Modifying a Column Slice with a Value
- [static func += (inout ColumnSlice<WrappedElement>, WrappedElement)](columnslice/+=(_:_:)-950qi.md)
  Modifies a column slice by adding a value to each element.
- [static func -= (inout ColumnSlice<WrappedElement>, WrappedElement)](columnslice/-=(_:_:)-1n1gh.md)
  Modifies a column slice by subtracting a value from each element.
- [static func *= (inout ColumnSlice<WrappedElement>, WrappedElement)](columnslice/*=(_:_:)-i6qs.md)
  Modifies a column slice by multiplying each element by a value.
- [static func /= (inout ColumnSlice<WrappedElement>, WrappedElement)](columnslice/_=(_:_:)-8oi36.md)
  Modifies an integer column slice by dividing each element by a value.
- [static func /= (inout ColumnSlice<WrappedElement>, WrappedElement)](columnslice/_=(_:_:)-8pl3f.md)
  Modifies a floating-point column slice by dividing each element by a value.
### Modifying a Column Slice with a Collection of Values
- [static func += <C>(inout ColumnSlice<WrappedElement>, C)](columnslice/+=(_:_:)-47cwm.md)
  Modifies a column slice by adding each value in a collection to the corresponding element in the column.
- [static func += <C>(inout ColumnSlice<WrappedElement>, C)](columnslice/+=(_:_:)-4bgdt.md)
  Modifies a column slice by adding each optional value in a collection to the corresponding element in the column.
- [static func -= <C>(inout ColumnSlice<WrappedElement>, C)](columnslice/-=(_:_:)-3kauw.md)
  Modifies a column slice by subtracting each value in a collection from the corresponding element in the column.
- [static func -= <C>(inout ColumnSlice<WrappedElement>, C)](columnslice/-=(_:_:)-1bqy4.md)
  Modifies a column slice by subtracting each optional value in a collection from the corresponding element in the column.
- [static func *= <C>(inout ColumnSlice<WrappedElement>, C)](columnslice/*=(_:_:)-7lz8l.md)
  Modifies a column slice by multiplying each element in the column by the corresponding value in a collection.
- [static func *= <C>(inout ColumnSlice<WrappedElement>, C)](columnslice/*=(_:_:)-3v2q0.md)
  Modifies a column slice by multiplying each element in the column by the corresponding optional value in a collection.
- [static func /= <C>(inout ColumnSlice<WrappedElement>, C)](columnslice/_=(_:_:)-46jci.md)
  Modifies an integer column slice by dividing each element in the column by the corresponding value in a collection.
- [static func /= <C>(inout ColumnSlice<WrappedElement>, C)](columnslice/_=(_:_:)-8frqe.md)
  Modifies an integer column slice by dividing each element in the column by the corresponding optional value in a collection.
- [static func /= <C>(inout ColumnSlice<WrappedElement>, C)](columnslice/_=(_:_:)-1fciw.md)
  Modifies a floating-point column slice by dividing each element in the column by the corresponding value in a collection.
- [static func /= <C>(inout ColumnSlice<WrappedElement>, C)](columnslice/_=(_:_:)-6ujes.md)
  Modifies a floating-point column slice by dividing each element in the column by the corresponding optional value in a collection.
### Generating a Column by Combining Two Column Slices
- [static func + (Self, Self) -> Column<Self.WrappedElement>](columnslice/+(_:_:)-3mep5.md)
  Generates a column by adding each element in an optional column type to the corresponding elements of another.
- [static func - (Self, Self) -> Column<Self.WrappedElement>](columnslice/-(_:_:)-6dkqb.md)
  Generates a column by subtracting each element in an optional column type from the corresponding elements of another.
- [static func * (Self, Self) -> Column<Self.WrappedElement>](columnslice/*(_:_:)-hl25.md)
  Generates a column by multiplying each element in an optional column type by the corresponding elements of another.
- [static func / (Self, Self) -> Column<Self.WrappedElement>](columnslice/_(_:_:)-3so2z.md)
  Generates an integer column by dividing each element in an optional column type by the corresponding elements of another.
- [static func / (Self, Self) -> Column<Self.WrappedElement>](columnslice/_(_:_:)-4125n.md)
  Generates a floating-point column by dividing each element in an optional column type by the corresponding elements of another.
### Generating a Column by Adding a Value
- [static func + (Self, Self.Element) -> Column<Self.Element>](columnslice/+(_:_:)-2l5ok.md)
  Generates a column by adding a value to each element in a column.
- [static func + (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](columnslice/+(_:_:)-3xsx4.md)
  Generates a column by adding a value to each element in an optional column.
- [static func + (Self.Element, Self) -> Column<Self.Element>](columnslice/+(_:_:)-4bxn6.md)
  Generates a column by adding each element in a column to a value.
- [static func + (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](columnslice/+(_:_:)-ooqt.md)
  Generates a column by adding each element in an optional column to a value.
### Generating a Column by Subtracting a Value
- [static func - (Self, Self.Element) -> Column<Self.Element>](columnslice/-(_:_:)-26wtz.md)
  Generates a column by subtracting a value from each element in a column.
- [static func - (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](columnslice/-(_:_:)-nkha.md)
  Generates a column by subtracting a value from each element in an optional column type.
- [static func - (Self.Element, Self) -> Column<Self.Element>](columnslice/-(_:_:)-8z15n.md)
  Generates a column by subtracting each element in a column from a value.
- [static func - (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](columnslice/-(_:_:)-5mbpd.md)
  Generates a column by subtracting each element in an optional column from a value.
### Generating a Column by Multiplying a Value
- [static func * (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](columnslice/*(_:_:)-4sw7w.md)
  Generates a column by multiplying each element in an optional column by a value.
- [static func * (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](columnslice/*(_:_:)-86zas.md)
  Generates a column by multiplying a value by each element in an optional column type.
### Generating a Column by Dividing a Value
- [static func / (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](columnslice/_(_:_:)-8n9gx.md)
  Generates an integer column by dividing each element in an optional column by a value.
- [static func / (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](columnslice/_(_:_:)-1oxxv.md)
  Generates a floating-point column by dividing each element in an optional column by a value.
- [static func / (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](columnslice/_(_:_:)-992oe.md)
  Generates an integer column by dividing a value by each element in an optional column type.
- [static func / (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](columnslice/_(_:_:)-esxm.md)
  Generates a floating-point column by dividing a value by each element in an optional column type.
### Hashing a Column Slice
- [func hash(into: inout Hasher)](columnslice/hash(into:).md)
  Hashes the essential components of the column slice by feeding them into a hasher.
### Supporting Types
- [ColumnSlice.Element](columnslice/element.md)
  The type of the column slice’s elements, which is an optional type of the parent column’s type.
- [ColumnSlice.Index](columnslice/index.md)
  The type that represents a position in the column slice.
### Instance Properties
- [var missingCount: Int](columnslice/missingcount.md)
  The number of missing elements in the column slice.
### Type Aliases
- [ColumnSlice.Indices](columnslice/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [ColumnSlice.Iterator](columnslice/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [ColumnSlice.SubSequence](columnslice/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [BidirectionalCollection Implementations](columnslice/bidirectionalcollection-implementations.md)
- [Collection Implementations](columnslice/collection-implementations.md)
- [ColumnProtocol Implementations](columnslice/columnprotocol-implementations.md)
- [CustomDebugStringConvertible Implementations](columnslice/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](columnslice/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](columnslice/customstringconvertible-implementations.md)
- [Equatable Implementations](columnslice/equatable-implementations.md)
- [Hashable Implementations](columnslice/hashable-implementations.md)
- [MutableCollection Implementations](columnslice/mutablecollection-implementations.md)
- [OptionalColumnProtocol Implementations](columnslice/optionalcolumnprotocol-implementations.md)
- [Sequence Implementations](columnslice/sequence-implementations.md)

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
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sendable](../Swift/Sendable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct Column](column.md)
  A column in a data frame.
- [struct FilledColumn](filledcolumn.md)
  A view on a column that replaces missing elements with a default value.
- [struct DiscontiguousColumnSlice](discontiguouscolumnslice.md)
  A collection that represents a selection, potentially with gaps, of elements from a typed column.
- [protocol ColumnProtocol](columnprotocol.md)
  A type that represents a column.
- [protocol OptionalColumnProtocol](optionalcolumnprotocol.md)
  A type that represents a column that has missing values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnslice)*