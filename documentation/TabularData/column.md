# Column

**Framework**: TabularData  
**Kind**: struct

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

A column is a [`Collection`](https://developer.apple.com/documentation/Swift/Collection) that contains values of a specific type, including:

- [`Int`](https://developer.apple.com/documentation/Swift/Int)
- [`Double`](https://developer.apple.com/documentation/Swift/Double)
- [`String`](https://developer.apple.com/documentation/Swift/String)

Each element in a column is an [`Optional`](https://developer.apple.com/documentation/Swift/Optional) of the column’s type. Each `nil` element represents a missing value.

## Topics

### Creating a Column
- [init(name: String, capacity: Int)](column/init(name:capacity:).md)
  Creates a column with a name and a capacity.
- [init(ColumnID<WrappedElement>, capacity: Int)](column/init(_:capacity:).md)
  Creates a column with a column identifier and a capacity.
- [init<S>(name: String, contents: S)](column/init(name:contents:)-6okx3.md)
  Creates a column with a name and a sequence of nonoptional values.
- [init<S>(name: String, contents: S)](column/init(name:contents:)-8nxtj.md)
  Creates a column with a name and a sequence of optional values.
- [init<S>(ColumnID<S.Element>, contents: S)](column/init(_:contents:)-1871a.md)
  Creates a column with an identifier and a sequence of nonoptional values.
- [init<S>(ColumnID<S.Element>, contents: S)](column/init(_:contents:)-7z5ji.md)
  Creates a column with a column identifier and a sequence of optional values.
- [init(ColumnSlice<WrappedElement>)](column/init(_:).md)
  Creates a column from a column slice.
### Creating a Column of the Same Type
- [var prototype: any AnyColumnPrototype](column/prototype.md)
  A prototype that creates type-erased columns with the same underlying type as the column slice.
### Creating a Type-Erased Column
- [func eraseToAnyColumn() -> AnyColumn](column/erasetoanycolumn.md)
  Generates a type-erased copy of the column.
### Creating Transformed Columns
- [func map<T>((Column<WrappedElement>.Element) throws -> T?) rethrows -> Column<T>](column/map(_:).md)
  Creates a new column by applying a transformation to every element.
- [func mapNonNil<T>((WrappedElement) throws -> T?) rethrows -> Column<T>](column/mapnonnil(_:).md)
  Creates a new column by applying the transformation to every element that isn’t missing.
### Inspecting a Column
- [var name: String](column/name.md)
  The name of the column.
- [var count: Int](column/count.md)
  The number of elements in the column.
- [var missingCount: Int](column/missingcount.md)
  The number of missing elements in the column.
- [typealias Element](column/element.md)
  The type of the column’s elements, which is an optional type of the column’s type.
- [var wrappedElementType: any Any.Type](column/wrappedelementtype.md)
  The underlying type of the column’s elements.
### Transforming a Column
- [func transform((WrappedElement) throws -> WrappedElement) rethrows](column/transform(_:)-271dd.md)
  Applies a transformation to every element that isn’t missing.
- [func transform((Column<WrappedElement>.Element) throws -> Column<WrappedElement>.Element) rethrows](column/transform(_:)-6mrwg.md)
  Applies a transformation to every element in the column.
### Adding Elements
- [func append(WrappedElement)](column/append(_:)-qycj.md)
  Appends a nonoptional value to the column.
- [func append(Column<WrappedElement>.Element)](column/append(_:)-4t2pt.md)
  Appends an optional value to the column.
- [func append<S>(contentsOf: S)](column/append(contentsof:)-qb4p.md)
  Appends a sequence of nonoptional values to the column.
- [func append<S>(contentsOf: S)](column/append(contentsof:)-42y1d.md)
  Appends a sequence of optional values to the column.
### Finding an Element Index
- [func argmin() -> Int?](column/argmin.md)
  Returns the index of the element with the lowest value, ignoring missing elements.
- [func argmax() -> Int?](column/argmax.md)
  Returns the index of the element with the highest value, ignoring missing elements.
### Removing an Element
- [func remove(at: Int)](column/remove(at:).md)
  Removes an element from the column.
### Accessing Elements
- [subscript(Int) -> Column<WrappedElement>.Element](column/subscript(_:)-qm4d.md)
  Accesses an element at an index.
- [subscript<R>(R) -> ColumnSlice<WrappedElement>](column/subscript(_:)-52xy1.md)
  Accesses a contiguous range of elements with a range expression.
- [subscript(Range<Int>) -> ColumnSlice<WrappedElement>](column/subscript(_:)-gne9.md)
  Accesses a contiguous range of elements.
### Creating a Slice of Unique Elements
- [func distinct() -> DiscontiguousColumnSlice<WrappedElement>](column/distinct.md)
  Generates a discontiguous slice that contains unique elements.
### Creating a Slice by Masking Elements
- [subscript<C>(C) -> DiscontiguousColumnSlice<WrappedElement>](column/subscript(_:)-56i2s.md)
  Returns a column slice that includes elements that correspond to a collection of Booleans.
### Encoding a Column
- [func encoded<Encoder>(using: Encoder) throws -> Column<Encoder.Output>](column/encoded(using:).md)
  Generates a column by encoding each element’s value.
### Decoding a Column
- [func decoded<T, Decoder>(T.Type, using: Decoder) throws -> Column<T>](column/decoded(_:using:).md)
  Generates a column by decoding each element’s data.
### Summarizing a Column
- [func summary() -> CategoricalSummary<WrappedElement>](column/summary.md)
  Generates a categorical summary of the column’s elements.
- [func numericSummary() -> NumericSummary<Double>](column/numericsummary-2m0sr.md)
  Generates a numeric summary of the integer column’s elements.
- [func numericSummary() -> NumericSummary<WrappedElement>](column/numericsummary-8laeo.md)
  Generates a numeric summary of the floating-point column’s elements.
### Getting Statistical Values
- [func sum() -> WrappedElement](column/sum.md)
  Returns the sum of the column’s elements, ignoring missing elements.
- [func min() -> Column<WrappedElement>.Element](column/min.md)
  Returns the element with the lowest value, ignoring missing elements.
- [func max() -> Column<WrappedElement>.Element](column/max.md)
  Returns the element with the highest value, ignoring missing elements.
- [func mean() -> Double?](column/mean-2si7j.md)
  Returns the mean average of the integer column’s elements, ignoring missing elements.
- [func mean() -> Column<WrappedElement>.Element](column/mean-ic5z.md)
  Returns the mean average of the floating-point column’s elements, ignoring missing elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> Double?](column/standarddeviation(deltadegreesoffreedom:)-9ffqu.md)
  Returns the standard deviation of the integer column’s elements, ignoring missing elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> Column<WrappedElement>.Element](column/standarddeviation(deltadegreesoffreedom:)-4kc16.md)
  Returns the standard deviation of the floating-point column’s elements, ignoring missing elements.
### Describing a Column
- [var description: String](column/description.md)
  A text representation of the column.
- [var debugDescription: String](column/debugdescription.md)
  A text representation of the column suitable for debugging.
- [var customMirror: Mirror](column/custommirror.md)
  A mirror that reflects the column.
### Modifying a Column with a Value
- [static func += (inout Column<WrappedElement>, WrappedElement)](column/+=(_:_:)-94q8g.md)
  Modifies a column by adding a value to each element.
- [static func -= (inout Column<WrappedElement>, WrappedElement)](column/-=(_:_:)-8arlr.md)
  Modifies a column by subtracting a value from each element.
- [static func *= (inout Column<WrappedElement>, WrappedElement)](column/*=(_:_:)-4rraw.md)
  Modifies a column by multiplying each element by a value.
- [static func /= (inout Column<WrappedElement>, WrappedElement)](column/_=(_:_:)-8jmir.md)
  Modifies an integer column by dividing each element by a value.
- [static func /= (inout Column<WrappedElement>, WrappedElement)](column/_=(_:_:)-3hfr5.md)
  Modifies a floating-point column by dividing each element by a value.
### Modifying a Column with a Collection of Values
- [static func += <C>(inout Column<WrappedElement>, C)](column/+=(_:_:)-2w5o4.md)
  Modifies a column by adding each value in a collection to the corresponding element in the column.
- [static func += <C>(inout Column<WrappedElement>, C)](column/+=(_:_:)-2scuy.md)
  Modifies a column by adding each optional value in a collection to the corresponding element in the column.
- [static func -= <C>(inout Column<WrappedElement>, C)](column/-=(_:_:)-8rgjq.md)
  Modifies a column by subtracting each value in a collection from the corresponding element in the column.
- [static func -= <C>(inout Column<WrappedElement>, C)](column/-=(_:_:)-3v0hh.md)
  Modifies a column by subtracting each optional value in a collection from the corresponding element in the column.
- [static func *= <C>(inout Column<WrappedElement>, C)](column/*=(_:_:)-8mmnn.md)
  Modifies a column by multiplying each element in the column by the corresponding value in a collection.
- [static func *= <C>(inout Column<WrappedElement>, C)](column/*=(_:_:)-6kp11.md)
  Modifies a column by multiplying each element in the column by the corresponding optional value in a collection.
- [static func /= <C>(inout Column<WrappedElement>, C)](column/_=(_:_:)-dnma.md)
  Modifies an integer column by dividing each element in the column by the corresponding value in a collection.
- [static func /= <C>(inout Column<WrappedElement>, C)](column/_=(_:_:)-8xhzg.md)
  Modifies an integer column by dividing each element in the column by the corresponding optional value in a collection.
- [static func /= <C>(inout Column<WrappedElement>, C)](column/_=(_:_:)-86t1j.md)
  Modifies a floating-point column by dividing each element in the column by the corresponding value in a collection.
- [static func /= <C>(inout Column<WrappedElement>, C)](column/_=(_:_:)-3acz8.md)
  Modifies a floating-point column by dividing each element in the column by the corresponding optional value in a collection.
### Instance Methods
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<WrappedElement>) throws -> R) rethrows -> R?](column/withcontiguousmutablestorageifavailable(_:)-9j9p8.md)
  Call `body(buffer)`, where `buffer` provides access to the non-optional contiguous mutable storage of the entire column. If the column contains missing values, `body` is not called and `nil` is returned.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<WrappedElement>) throws -> R) rethrows -> R?](column/withcontiguousstorageifavailable(_:)-6nbz3.md)
  Call `body(buffer)`, where `buffer` provides access to the non-optional contiguous storage of the entire column. If the column contains missing values, `body` is not called and `nil` is returned.
### Default Implementations
- [BidirectionalCollection Implementations](column/bidirectionalcollection-implementations.md)
- [CustomDebugStringConvertible Implementations](column/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](column/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](column/customstringconvertible-implementations.md)
- [MutableCollection Implementations](column/mutablecollection-implementations.md)
- [Sequence Implementations](column/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [ColumnProtocol](columnprotocol.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MutableCollection](../Swift/MutableCollection.md)
- [OptionalColumnProtocol](optionalcolumnprotocol.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct ColumnSlice](columnslice.md)
  A collection that represents a selection of contiguous elements from a typed column.
- [struct FilledColumn](filledcolumn.md)
  A view on a column that replaces missing elements with a default value.
- [struct DiscontiguousColumnSlice](discontiguouscolumnslice.md)
  A collection that represents a selection, potentially with gaps, of elements from a typed column.
- [protocol ColumnProtocol](columnprotocol.md)
  A type that represents a column.
- [protocol OptionalColumnProtocol](optionalcolumnprotocol.md)
  A type that represents a column that has missing values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column)*