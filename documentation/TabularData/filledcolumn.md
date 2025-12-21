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
### Supporting Types
- [FilledColumn.Element](filledcolumn/element.md)
  The type of the column’s elements that defines an associated type for the bidirectional collection protocol.
- [FilledColumn.WrappedElement](filledcolumn/wrappedelement.md)
  The type of the column’s elements that defines an associated type for the optional column protocol.
### Default Implementations
- [CustomStringConvertible Implementations](filledcolumn/customstringconvertible-implementations.md)

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