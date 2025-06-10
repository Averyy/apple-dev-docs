# FilledColumn

**Framework**: TabularData  
**Kind**: struct

A view on a column that replaces missing elements with a default value.

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
struct FilledColumn<Base> where Base : OptionalColumnProtocol
```

## Topics

### Inspecting a Column
- [var name: String](filledcolumn/name.md)
  The name of the column.
### Finding an Element Index
- [func argmin() -> Base.Index?](filledcolumn/argmin.md)
  Returns the index of the element with the lowest value.
- [func argmax() -> FilledColumn<Base>.Index?](filledcolumn/argmax.md)
  Returns the index of the element with the highest value.
### Accessing Elements
- [subscript(Base.Index) -> Base.WrappedElement](filledcolumn/subscript(_:).md)
  Retrieves an element at a position in the column type.
### Summarizing a Column
- [func summary() -> CategoricalSummary<FilledColumn<Base>.WrappedElement>](filledcolumn/summary.md)
  Generates a categorical summary of the filled column’s elements, including default values.
- [func numericSummary() -> NumericSummary<Double>](filledcolumn/numericsummary-3ao8s.md)
  Generates a numeric summary of the integer column’s elements.
- [func numericSummary() -> NumericSummary<Base.WrappedElement>](filledcolumn/numericsummary-86mgh.md)
  Generates a numeric summary of the floating-point column’s elements.
### Getting Statistical Values
- [func sum() -> FilledColumn<Base>.Element](filledcolumn/sum-5836l.md)
  Returns the sum of the integer column’s elements.
- [func sum() -> FilledColumn<Base>.Element](filledcolumn/sum-2805h.md)
  Returns the sum of the floating-point column’s elements.
- [func min() -> FilledColumn<Base>.Element?](filledcolumn/min.md)
  Returns the element with the lowest value.
- [func max() -> FilledColumn<Base>.Element?](filledcolumn/max.md)
  Returns the element with the highest value.
- [func mean() -> Double?](filledcolumn/mean-8xs60.md)
  Returns the mean average of the integer column’s elements.
- [func mean() -> FilledColumn<Base>.Element?](filledcolumn/mean-jd3v.md)
  Returns the mean average of the floating-point column’s elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> Double?](filledcolumn/standarddeviation(deltadegreesoffreedom:)-4cofd.md)
  Returns the standard deviation of the integer column’s elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> FilledColumn<Base>.Element?](filledcolumn/standarddeviation(deltadegreesoffreedom:)-27xnl.md)
  Returns the standard deviation of the floating-point column’s elements.
### Describing a Column
- [var description: String](filledcolumn/description.md)
  A mirror that reflects the filled column.
- [var debugDescription: String](filledcolumn/debugdescription.md)
  A text representation of the filled column suitable for debugging.
- [func description(options: FormattingOptions) -> String](filledcolumn/description(options:).md)
  Generates a string description of the filled column.
### Generating a Column by Combining Two Columns
- [static func + (Self, Self) -> Column<Self.Element>](filledcolumn/+(_:_:)-8qqh.md)
  Generates a column by adding each element in a column type to the corresponding elements of another.
- [static func - (Self, Self) -> Column<Self.Element>](filledcolumn/-(_:_:)-bzdl.md)
  Generates a column by subtracting each element in a column type from the corresponding elements of another.
- [static func * (Self, Self) -> Column<Self.Element>](filledcolumn/*(_:_:)-6fyqv.md)
  Generates a column by multiplying each element in a column type by the corresponding elements of another.
- [static func / (Self, Self) -> Column<Self.Element>](filledcolumn/_(_:_:)-9h88r.md)
  Generates an integer column by dividing each element in a column type by the corresponding elements of another.
- [static func / (Self, Self) -> Column<Self.Element>](filledcolumn/_(_:_:)-82d1w.md)
  Generates a floating-point column by dividing each element in a column type by the corresponding elements of another.
### Generating a Column by Adding a Value
- [static func + (Self, Self.Element) -> Column<Self.Element>](filledcolumn/+(_:_:)-9slnq.md)
  Generates a column by adding a value to each element in a column.
- [static func + (Self.Element, Self) -> Column<Self.Element>](filledcolumn/+(_:_:)-57z7f.md)
  Generates a column by adding each element in a column to a value.
### Generating a Column by Subtracting a Value
- [static func - (Self, Self.Element) -> Column<Self.Element>](filledcolumn/-(_:_:)-13zcw.md)
  Generates a column by subtracting a value from each element in a column.
- [static func - (Self.Element, Self) -> Column<Self.Element>](filledcolumn/-(_:_:)-2zphx.md)
  Generates a column by subtracting each element in a column from a value.
### Generating a Column by Multiplying a Value
- [static func * (Self, Self.Element) -> Column<Self.Element>](filledcolumn/*(_:_:)-42o3q.md)
  Generates a column by multiplying each element in a column by a value.
- [static func * (Self.Element, Self) -> Column<Self.Element>](filledcolumn/*(_:_:)-6hhwp.md)
  Generates a column by multiplying a value by each element in a column.
### Generating a Column by Dividing a Value
- [static func / (Self, Self.Element) -> Column<Self.Element>](filledcolumn/_(_:_:)-7ayat.md)
  Generates an integer column by dividing each element in a column by a value.
- [static func / (Self.Element, Self) -> Column<Self.Element>](filledcolumn/_(_:_:)-4yo70.md)
  Generates an integer column by dividing a value by each element in a column.
- [static func / (Self, Self.Element) -> Column<Self.Element>](filledcolumn/_(_:_:)-55imm.md)
  Generates a floating-point column by dividing each element in a column by a value.
- [static func / (Self.Element, Self) -> Column<Self.Element>](filledcolumn/_(_:_:)-74b1.md)
  Generates a floating-point column by dividing a value by each element in a column.
### Comparing a Column with a Value
- [static func == (Self, Self.Element) -> [Bool]](filledcolumn/==(_:_:)-3bp46.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type is equal to a value.
- [static func == (Self.Element, Self) -> [Bool]](filledcolumn/==(_:_:)-3qine.md)
  Returns a Boolean array that indicates whether the value is equal to the corresponding element of a column type.
- [static func != (Self, Self.Element) -> [Bool]](filledcolumn/!=(_:_:)-9l73c.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type isn’t equal to a value.
- [static func != (Self.Element, Self) -> [Bool]](filledcolumn/!=(_:_:)-twj1.md)
  Returns a Boolean array that indicates whether the value isn’t equal to the corresponding element of a column type.
### Supporting Types
- [FilledColumn.Element](filledcolumn/element.md)
  The type of the column’s elements that defines an associated type for the bidirectional collection protocol.
- [FilledColumn.WrappedElement](filledcolumn/wrappedelement.md)
  The type of the column’s elements that defines an associated type for the optional column protocol.
### Type Aliases
- [FilledColumn.Index](filledcolumn/index.md)
  A type that represents a position in the collection.
- [FilledColumn.Indices](filledcolumn/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [FilledColumn.Iterator](filledcolumn/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [FilledColumn.SubSequence](filledcolumn/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [BidirectionalCollection Implementations](filledcolumn/bidirectionalcollection-implementations.md)
- [Collection Implementations](filledcolumn/collection-implementations.md)
- [ColumnProtocol Implementations](filledcolumn/columnprotocol-implementations.md)
- [CustomStringConvertible Implementations](filledcolumn/customstringconvertible-implementations.md)
- [Sequence Implementations](filledcolumn/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [ColumnProtocol](columnprotocol.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct Column](column.md)
  A column in a data frame.
- [struct ColumnSlice](columnslice.md)
  A collection that represents a selection of contiguous elements from a typed column.
- [struct DiscontiguousColumnSlice](discontiguouscolumnslice.md)
  A collection that represents a selection, potentially with gaps, of elements from a typed column.
- [protocol ColumnProtocol](columnprotocol.md)
  A type that represents a column.
- [protocol OptionalColumnProtocol](optionalcolumnprotocol.md)
  A type that represents a column that has missing values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/filledcolumn)*