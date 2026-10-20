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

#### Overview

A column is a [`Collection`](../Swift/collection.md) that contains values of a specific type, including:

- [`Int`](../Swift/int.md)
- [`Double`](../Swift/double.md)
- [`String`](../Swift/string.md)

Each element in a column is an [`Optional`](../Swift/optional.md) of the column’s type. Each `nil` element represents a missing value.

## Topics

### Creating a Column
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
### Creating a Column of the Same Type
- [var prototype: any AnyColumnPrototype](./column/prototype.md)
  A prototype that creates type-erased columns with the same underlying type as the column slice.
### Creating a Type-Erased Column
- [func eraseToAnyColumn() -> AnyColumn](./column/erasetoanycolumn%28%29.md)
  Generates a type-erased copy of the column.
### Creating Transformed Columns
- [func map<T>((Column<WrappedElement>.Element) throws -> T?) rethrows -> Column<T>](./column/map%28_%29.md)
  Creates a new column by applying a transformation to every element.
- [func mapNonNil<T>((WrappedElement) throws -> T?) rethrows -> Column<T>](./column/mapnonnil%28_%29.md)
  Creates a new column by applying the transformation to every element that isn’t missing.
### Inspecting a Column
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
### Transforming a Column
- [func transform((WrappedElement) throws -> WrappedElement) rethrows](./column/transform%28_%29-271dd.md)
  Applies a transformation to every element that isn’t missing.
- [func transform((Column<WrappedElement>.Element) throws -> Column<WrappedElement>.Element) rethrows](./column/transform%28_%29-6mrwg.md)
  Applies a transformation to every element in the column.
### Adding Elements
- [func append(WrappedElement)](./column/append%28_%29-qycj.md)
  Appends a nonoptional value to the column.
- [func append(Column<WrappedElement>.Element)](./column/append%28_%29-4t2pt.md)
  Appends an optional value to the column.
- [func append<S>(contentsOf: S)](./column/append%28contentsof%29-qb4p.md)
  Appends a sequence of nonoptional values to the column.
- [func append<S>(contentsOf: S)](./column/append%28contentsof%29-42y1d.md)
  Appends a sequence of optional values to the column.
### Finding an Element Index
- [func argmin() -> Int?](./column/argmin%28%29.md)
  Returns the index of the element with the lowest value, ignoring missing elements.
- [func argmax() -> Int?](./column/argmax%28%29.md)
  Returns the index of the element with the highest value, ignoring missing elements.
### Removing an Element
- [func remove(at: Int)](./column/remove%28at%29.md)
  Removes an element from the column.
### Accessing Elements
- [subscript(Int) -> Column<WrappedElement>.Element](./column/subscript%28_%29-qm4d.md)
  Accesses an element at an index.
- [subscript<R>(R) -> ColumnSlice<WrappedElement>](./column/subscript%28_%29-52xy1.md)
  Accesses a contiguous range of elements with a range expression.
- [subscript(Range<Int>) -> ColumnSlice<WrappedElement>](./column/subscript%28_%29-gne9.md)
  Accesses a contiguous range of elements.
### Creating a Slice of Unique Elements
- [func distinct() -> DiscontiguousColumnSlice<WrappedElement>](./column/distinct%28%29.md)
  Generates a discontiguous slice that contains unique elements.
### Creating a Slice by Masking Elements
- [subscript<C>(C) -> DiscontiguousColumnSlice<WrappedElement>](./column/subscript%28_%29-56i2s.md)
  Returns a column slice that includes elements that correspond to a collection of Booleans.
### Encoding a Column
- [func encoded<Encoder>(using: Encoder) throws -> Column<Encoder.Output>](./column/encoded%28using%29.md)
  Generates a column by encoding each element’s value.
### Decoding a Column
- [func decoded<T, Decoder>(T.Type, using: Decoder) throws -> Column<T>](./column/decoded%28_,using%29.md)
  Generates a column by decoding each element’s data.
### Summarizing a Column
- [func summary() -> CategoricalSummary<WrappedElement>](./column/summary%28%29.md)
  Generates a categorical summary of the column’s elements.
- [func numericSummary() -> NumericSummary<Double>](./column/numericsummary%28%29-2m0sr.md)
  Generates a numeric summary of the integer column’s elements.
- [func numericSummary() -> NumericSummary<WrappedElement>](./column/numericsummary%28%29-8laeo.md)
  Generates a numeric summary of the floating-point column’s elements.
### Getting Statistical Values
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
### Describing a Column
- [var description: String](./column/description.md)
  A text representation of the column.
- [var debugDescription: String](./column/debugdescription.md)
  A text representation of the column suitable for debugging.
- [var customMirror: Mirror](./column/custommirror.md)
  A mirror that reflects the column.
### Modifying a Column with a Value
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
### Modifying a Column with a Collection of Values
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
### Instance Methods
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<WrappedElement>) throws -> R) rethrows -> R?](./column/withcontiguousmutablestorageifavailable%28_%29-9j9p8.md)
  Call `body(buffer)`, where `buffer` provides access to the non-optional contiguous mutable storage of the entire column. If the column contains missing values, `body` is not called and `nil` is returned.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<WrappedElement>) throws -> R) rethrows -> R?](./column/withcontiguousstorageifavailable%28_%29-6nbz3.md)
  Call `body(buffer)`, where `buffer` provides access to the non-optional contiguous storage of the entire column. If the column contains missing values, `body` is not called and `nil` is returned.
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

### Typed Columns
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