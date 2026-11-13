# Column

**Framework**: TabularData  
**Kind**: struct  
**Role**: Structure

A column in a data frame.

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
struct Column<WrappedElement>
```

## Overview

A column is a [`Collection`](../Swift/collection.md) that contains values of a specific type, including:

- [`Int`](../Swift/int.md)
- [`Double`](../Swift/double.md)
- [`String`](../Swift/string.md)

Each element in a column is an [`Optional`](../Swift/optional.md) of the column’s type. Each `nil` element represents a missing value.

## Topics

### Creating a column
- [init(name: String, capacity: Int)](./column/init%28name,capacity%29.md)
  Creates a column with a name and a capacity.
- [init(ColumnID<WrappedElement>, capacity: Int)](./column/init%28_,capacity%29.md)
  Creates a column with a column identifier and a capacity.
- [init<S>(name: String, contents: S)](./column/init%28name,contents%29-6okx3.md)
  Creates a column with a name and a sequence of nonoptional values.
- [init<S>(name: String, contents: S)](./column/init%28name,contents%29-8nxtj.md)
  Creates a column with a name and a sequence of optional values.
- [init<S>(ColumnID<S.Element>, contents: S)](./column/init%28_,contents%29-1871a.md)
  Creates a column with an identifier and a sequence of nonoptional values.
- [init<S>(ColumnID<S.Element>, contents: S)](./column/init%28_,contents%29-7z5ji.md)
  Creates a column with a column identifier and a sequence of optional values.
- [init(ColumnSlice<WrappedElement>)](./column/init%28_%29.md)
  Creates a column from a column slice.
### Creating a column of the same type
- [var prototype: any AnyColumnPrototype](./column/prototype.md)
  A prototype that creates type-erased columns with the same underlying type as the column slice.
### Creating a type-erased column
- [func eraseToAnyColumn() -> AnyColumn](./column/erasetoanycolumn%28%29.md)
  Generates a type-erased copy of the column.
### Creating transformed columns
- [func map<T>((Column<WrappedElement>.Element) throws -> T?) rethrows -> Column<T>](./column/map%28_%29.md)
  Creates a new column by applying a transformation to every element.
- [func mapNonNil<T>((WrappedElement) throws -> T?) rethrows -> Column<T>](./column/mapnonnil%28_%29.md)
  Creates a new column by applying the transformation to every element that isn’t missing.
- [func filled(with: Self.WrappedElement) -> FilledColumn<Self>](./optionalcolumnprotocol/filled%28with%29.md)
  Generates a filled column by replacing missing elements with a value.
### Inspecting a column
- [var name: String](./column/name.md)
  The name of the column.
- [var count: Int](./column/count.md)
  The number of elements in the column.
- [var missingCount: Int](./column/missingcount.md)
  The number of missing elements in the column.
- [typealias Element](./column/element.md)
  The type of the column’s elements, which is an optional type of the column’s type.
- [var wrappedElementType: any Any.Type](./column/wrappedelementtype.md)
  The underlying type of the column’s elements.
### Transforming a column
- [func transform((WrappedElement) throws -> WrappedElement) rethrows](./column/transform%28_%29-271dd.md)
  Applies a transformation to every element that isn’t missing.
- [func transform((Column<WrappedElement>.Element) throws -> Column<WrappedElement>.Element) rethrows](./column/transform%28_%29-6mrwg.md)
  Applies a transformation to every element in the column.
### Adding elements
- [func append(WrappedElement)](./column/append%28_%29-qycj.md)
  Appends a nonoptional value to the column.
- [func append(Column<WrappedElement>.Element)](./column/append%28_%29-4t2pt.md)
  Appends an optional value to the column.
- [func append<S>(contentsOf: S)](./column/append%28contentsof%29-qb4p.md)
  Appends a sequence of nonoptional values to the column.
- [func append<S>(contentsOf: S)](./column/append%28contentsof%29-42y1d.md)
  Appends a sequence of optional values to the column.
### Finding an element index
- [func argmin() -> Int?](./column/argmin%28%29.md)
  Returns the index of the element with the lowest value, ignoring missing elements.
- [func argmax() -> Int?](./column/argmax%28%29.md)
  Returns the index of the element with the highest value, ignoring missing elements.
### Removing an element
- [func remove(at: Int)](./column/remove%28at%29.md)
  Removes an element from the column.
### Accessing elements
- [subscript(Int) -> Column<WrappedElement>.Element](./column/subscript%28_%29-qm4d.md)
  Accesses an element at an index.
- [subscript<R>(R) -> ColumnSlice<WrappedElement>](./column/subscript%28_%29-52xy1.md)
  Accesses a contiguous range of elements with a range expression.
- [subscript(Range<Int>) -> ColumnSlice<WrappedElement>](./column/subscript%28_%29-gne9.md)
  Accesses a contiguous range of elements.
### Creating a slice of unique elements
- [func distinct() -> DiscontiguousColumnSlice<WrappedElement>](./column/distinct%28%29.md)
  Generates a discontiguous slice that contains unique elements.
### Creating a slice by masking elements
- [subscript<C>(C) -> DiscontiguousColumnSlice<WrappedElement>](./column/subscript%28_%29-56i2s.md)
  Returns a column slice that includes elements that correspond to a collection of Booleans.
### Creating a slice by filtering elements
- [func filter((Column<WrappedElement>.Element) throws -> Bool) rethrows -> DiscontiguousColumnSlice<WrappedElement>](./column/filter%28_%29.md)
  Generates a slice that contains the elements that satisfy a predicate.
### Encoding a column
- [func encoded<Encoder>(using: Encoder) throws -> Column<Encoder.Output>](./column/encoded%28using%29.md)
  Generates a column by encoding each element’s value.
### Decoding a column
- [func decoded<T, Decoder>(T.Type, using: Decoder) throws -> Column<T>](./column/decoded%28_,using%29.md)
  Generates a column by decoding each element’s data.
### Summarizing a column
- [func summary() -> CategoricalSummary<WrappedElement>](./column/summary%28%29.md)
  Generates a categorical summary of the column’s elements.
- [func numericSummary() -> NumericSummary<Double>](./column/numericsummary%28%29-2m0sr.md)
  Generates a numeric summary of the integer column’s elements.
- [func numericSummary() -> NumericSummary<WrappedElement>](./column/numericsummary%28%29-8laeo.md)
  Generates a numeric summary of the floating-point column’s elements.
### Getting statistical values
- [func sum() -> WrappedElement](./column/sum%28%29.md)
  Returns the sum of the column’s elements, ignoring missing elements.
- [func min() -> Column<WrappedElement>.Element](./column/min%28%29.md)
  Returns the element with the lowest value, ignoring missing elements.
- [func max() -> Column<WrappedElement>.Element](./column/max%28%29.md)
  Returns the element with the highest value, ignoring missing elements.
- [func mean() -> Double?](./column/mean%28%29-2si7j.md)
  Returns the mean average of the integer column’s elements, ignoring missing elements.
- [func mean() -> Column<WrappedElement>.Element](./column/mean%28%29-ic5z.md)
  Returns the mean average of the floating-point column’s elements, ignoring missing elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> Double?](./column/standarddeviation%28deltadegreesoffreedom%29-9ffqu.md)
  Returns the standard deviation of the integer column’s elements, ignoring missing elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> Column<WrappedElement>.Element](./column/standarddeviation%28deltadegreesoffreedom%29-4kc16.md)
  Returns the standard deviation of the floating-point column’s elements, ignoring missing elements.
### Describing a column
- [var description: String](./column/description.md)
  A text representation of the column.
- [var debugDescription: String](./column/debugdescription.md)
  A text representation of the column suitable for debugging.
- [var customMirror: Mirror](./column/custommirror.md)
  A mirror that reflects the column.
### Comparing two columns
- [static func != (Self, Self.Element) -> [Bool]](./columnprotocol/noteq%28_,_%29-557vb.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type isn’t equal to a value.
- [static func != (Self.Element, Self) -> [Bool]](./columnprotocol/noteq%28_,_%29-72ddh.md)
  Returns a Boolean array that indicates whether the value isn’t equal to the corresponding element of a column type.
### Modifying a column with a value
- [static func += (inout Column<WrappedElement>, WrappedElement)](./column/pluseq%28_,_%29-94q8g.md)
  Modifies a column by adding a value to each element.
- [static func -= (inout Column<WrappedElement>, WrappedElement)](./column/minuseq%28_,_%29-8arlr.md)
  Modifies a column by subtracting a value from each element.
- [static func *= (inout Column<WrappedElement>, WrappedElement)](./column/stareq%28_,_%29-4rraw.md)
  Modifies a column by multiplying each element by a value.
- [static func /= (inout Column<WrappedElement>, WrappedElement)](./column/opeq%28_,_%29-8jmir.md)
  Modifies an integer column by dividing each element by a value.
- [static func /= (inout Column<WrappedElement>, WrappedElement)](./column/opeq%28_,_%29-3hfr5.md)
  Modifies a floating-point column by dividing each element by a value.
### Modifying a column with a collection of values
- [static func += <C>(inout Column<WrappedElement>, C)](./column/pluseq%28_,_%29-2w5o4.md)
  Modifies a column by adding each value in a collection to the corresponding element in the column.
- [static func += <C>(inout Column<WrappedElement>, C)](./column/pluseq%28_,_%29-2scuy.md)
  Modifies a column by adding each optional value in a collection to the corresponding element in the column.
- [static func -= <C>(inout Column<WrappedElement>, C)](./column/minuseq%28_,_%29-8rgjq.md)
  Modifies a column by subtracting each value in a collection from the corresponding element in the column.
- [static func -= <C>(inout Column<WrappedElement>, C)](./column/minuseq%28_,_%29-3v0hh.md)
  Modifies a column by subtracting each optional value in a collection from the corresponding element in the column.
- [static func *= <C>(inout Column<WrappedElement>, C)](./column/stareq%28_,_%29-8mmnn.md)
  Modifies a column by multiplying each element in the column by the corresponding value in a collection.
- [static func *= <C>(inout Column<WrappedElement>, C)](./column/stareq%28_,_%29-6kp11.md)
  Modifies a column by multiplying each element in the column by the corresponding optional value in a collection.
- [static func /= <C>(inout Column<WrappedElement>, C)](./column/opeq%28_,_%29-dnma.md)
  Modifies an integer column by dividing each element in the column by the corresponding value in a collection.
- [static func /= <C>(inout Column<WrappedElement>, C)](./column/opeq%28_,_%29-8xhzg.md)
  Modifies an integer column by dividing each element in the column by the corresponding optional value in a collection.
- [static func /= <C>(inout Column<WrappedElement>, C)](./column/opeq%28_,_%29-86t1j.md)
  Modifies a floating-point column by dividing each element in the column by the corresponding value in a collection.
- [static func /= <C>(inout Column<WrappedElement>, C)](./column/opeq%28_,_%29-3acz8.md)
  Modifies a floating-point column by dividing each element in the column by the corresponding optional value in a collection.
### Generating a column by combining two columns
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
### Retrieving an index
- [var startIndex: Int](./column/startindex.md)
  The index of the initial element in the column.
- [var endIndex: Int](./column/endindex.md)
  The index of the final element in the column.
- [func index(before: Int) -> Int](./column/index%28before%29.md)
  Returns the index immediately before an element index.
- [func index(after: Int) -> Int](./column/index%28after%29.md)
  Returns the index immediately after an element index.
### Allocating contiguous storage
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<WrappedElement>) throws -> R) rethrows -> R?](./column/withcontiguousstorageifavailable%28_%29-6nbz3.md)
  Call `body(buffer)`, where `buffer` provides access to the non-optional contiguous storage of the entire column. If the column contains missing values, `body` is not called and `nil` is returned.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<WrappedElement?>) throws -> R) rethrows -> R?](./column/withcontiguousstorageifavailable%28_%29-539v3.md)
  This method always returns `nil` without calling `body`.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<WrappedElement>) throws -> R) rethrows -> R?](./column/withcontiguousmutablestorageifavailable%28_%29-9j9p8.md)
  Call `body(buffer)`, where `buffer` provides access to the non-optional contiguous mutable storage of the entire column. If the column contains missing values, `body` is not called and `nil` is returned.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<WrappedElement?>) throws -> R) rethrows -> R?](./column/withcontiguousmutablestorageifavailable%28_%29-77itz.md)
  This method always returns `nil` without calling `body`.
### Default Implementations
- [BidirectionalCollection Implementations](./column/bidirectionalcollection-implementations.md)
- [CustomDebugStringConvertible Implementations](./column/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](./column/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](./column/customstringconvertible-implementations.md)
- [MutableCollection Implementations](./column/mutablecollection-implementations.md)
- [Sequence Implementations](./column/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/bidirectionalcollection.md)
- [Collection](../Swift/collection.md)
- [ColumnProtocol](./columnprotocol.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
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
- [struct ColumnSlice](./columnslice.md)
  A collection that represents a selection of contiguous elements from a typed column.
- [struct FilledColumn](./filledcolumn.md)
  A view on a column that replaces missing elements with a default value.
- [struct DiscontiguousColumnSlice](./discontiguouscolumnslice.md)
  A collection that represents a selection, potentially with gaps, of elements from a typed column.
- [protocol ColumnProtocol](./columnprotocol.md)
  A type that represents a column.
- [protocol OptionalColumnProtocol](./optionalcolumnprotocol.md)
  A type that represents a column that has missing values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column)*