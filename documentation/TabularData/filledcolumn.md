# FilledColumn

**Framework**: TabularData  
**Kind**: struct  
**Role**: Structure

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

### Inspecting a column
- [var name: String](./filledcolumn/name.md)
  The name of the column.
### Finding an element index
- [func argmin() -> Base.Index?](./filledcolumn/argmin%28%29.md)
  Returns the index of the element with the lowest value.
- [func argmax() -> FilledColumn<Base>.Index?](./filledcolumn/argmax%28%29.md)
  Returns the index of the element with the highest value.
### Accessing elements
- [subscript(Base.Index) -> Base.WrappedElement](./filledcolumn/subscript%28_%29.md)
  Retrieves an element at a position in the column type.
### Summarizing a column
- [func summary() -> CategoricalSummary<FilledColumn<Base>.WrappedElement>](./filledcolumn/summary%28%29.md)
  Generates a categorical summary of the filled column’s elements, including default values.
- [func numericSummary() -> NumericSummary<Double>](./filledcolumn/numericsummary%28%29-3ao8s.md)
  Generates a numeric summary of the integer column’s elements.
- [func numericSummary() -> NumericSummary<Base.WrappedElement>](./filledcolumn/numericsummary%28%29-86mgh.md)
  Generates a numeric summary of the floating-point column’s elements.
### Getting statistical values
- [func sum() -> FilledColumn<Base>.Element](./filledcolumn/sum%28%29-5836l.md)
  Returns the sum of the integer column’s elements.
- [func sum() -> FilledColumn<Base>.Element](./filledcolumn/sum%28%29-2805h.md)
  Returns the sum of the floating-point column’s elements.
- [func min() -> FilledColumn<Base>.Element?](./filledcolumn/min%28%29.md)
  Returns the element with the lowest value.
- [func max() -> FilledColumn<Base>.Element?](./filledcolumn/max%28%29.md)
  Returns the element with the highest value.
- [func mean() -> Double?](./filledcolumn/mean%28%29-8xs60.md)
  Returns the mean average of the integer column’s elements.
- [func mean() -> FilledColumn<Base>.Element?](./filledcolumn/mean%28%29-jd3v.md)
  Returns the mean average of the floating-point column’s elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> Double?](./filledcolumn/standarddeviation%28deltadegreesoffreedom%29-4cofd.md)
  Returns the standard deviation of the integer column’s elements.
- [func standardDeviation(deltaDegreesOfFreedom: Int) -> FilledColumn<Base>.Element?](./filledcolumn/standarddeviation%28deltadegreesoffreedom%29-27xnl.md)
  Returns the standard deviation of the floating-point column’s elements.
### Describing a column
- [var description: String](./filledcolumn/description.md)
  A mirror that reflects the filled column.
- [var debugDescription: String](./filledcolumn/debugdescription.md)
  A text representation of the filled column suitable for debugging.
- [func description(options: FormattingOptions) -> String](./filledcolumn/description%28options%29.md)
  Generates a string description of the filled column.
### Generating a column by combining two columns
- [static func + (Self, Self) -> Column<Self.Element>](./columnprotocol/plus%28_,_%29-yc11.md)
  Generates a column by adding each element in a column type to the corresponding elements of another.
- [static func - (Self, Self) -> Column<Self.Element>](./columnprotocol/minus%28_,_%29-36zol.md)
  Generates a column by subtracting each element in a column type from the corresponding elements of another.
- [static func * (Self, Self) -> Column<Self.Element>](./columnprotocol/star%28_,_%29-9db1q.md)
  Generates a column by multiplying each element in a column type by the corresponding elements of another.
- [static func / (Self, Self) -> Column<Self.Element>](./columnprotocol/op%28_,_%29-2urf0.md)
  Generates a floating-point column by dividing each element in a column type by the corresponding elements of another.
- [static func / (Self, Self) -> Column<Self.Element>](./columnprotocol/op%28_,_%29-922ku.md)
  Generates an integer column by dividing each element in a column type by the corresponding elements of another.
### Generating a column by adding a value
- [static func + (Self, Self.Element) -> Column<Self.Element>](./columnprotocol/plus%28_,_%29-39k8v.md)
  Generates a column by adding a value to each element in a column.
- [static func + (Self.Element, Self) -> Column<Self.Element>](./columnprotocol/plus%28_,_%29-94kiv.md)
  Generates a column by adding each element in a column to a value.
### Generating a column by subtracting a value
- [static func - (Self, Self.Element) -> Column<Self.Element>](./columnprotocol/minus%28_,_%29-6up21.md)
  Generates a column by subtracting a value from each element in a column.
- [static func - (Self.Element, Self) -> Column<Self.Element>](./columnprotocol/minus%28_,_%29-4fynh.md)
  Generates a column by subtracting each element in a column from a value.
### Generating a column by multiplying a value
- [static func * (Self, Self.Element) -> Column<Self.Element>](./columnprotocol/star%28_,_%29-17vqd.md)
  Generates a column by multiplying each element in a column by a value.
- [static func * (Self.Element, Self) -> Column<Self.Element>](./columnprotocol/star%28_,_%29-3d6lu.md)
  Generates a column by multiplying a value by each element in a column.
### Generating a column by dividing a value
- [static func / (Self, Self.Element) -> Column<Self.Element>](./columnprotocol/op%28_,_%29-4a632.md)
  Generates an integer column by dividing each element in a column by a value.
- [static func / (Self, Self.Element) -> Column<Self.Element>](./columnprotocol/op%28_,_%29-6zigz.md)
  Generates a floating-point column by dividing each element in a column by a value.
- [static func / (Self.Element, Self) -> Column<Self.Element>](./columnprotocol/op%28_,_%29-4iv15.md)
  Generates a floating-point column by dividing a value by each element in a column.
- [static func / (Self.Element, Self) -> Column<Self.Element>](./columnprotocol/op%28_,_%29-7pe3t.md)
  Generates an integer column by dividing a value by each element in a column.
### Comparing a column with a value
- [static func == (Self, Self.Element) -> [Bool]](./columnprotocol/eqeq%28_,_%29-5jc0x.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type is equal to a value.
- [static func == (Self.Element, Self) -> [Bool]](./columnprotocol/eqeq%28_,_%29-4hx04.md)
  Returns a Boolean array that indicates whether the value is equal to the corresponding element of a column type.
- [static func != (Self, Self.Element) -> [Bool]](./columnprotocol/noteq%28_,_%29-557vb.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type isn’t equal to a value.
- [static func != (Self.Element, Self) -> [Bool]](./columnprotocol/noteq%28_,_%29-72ddh.md)
  Returns a Boolean array that indicates whether the value isn’t equal to the corresponding element of a column type.
- [static func < (Self, Self.Element) -> [Bool]](./columnprotocol/op%28_,_%29-7gy2j.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type is less than a value.
- [static func < (Self.Element, Self) -> [Bool]](./columnprotocol/op%28_,_%29-70vl1.md)
  Returns a Boolean array that indicates whether the value is less than the corresponding element of a column type.
- [static func <= (Self, Self.Element) -> [Bool]](./columnprotocol/opeq%28_,_%29-9wr8s.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type is less than or equal to a value.
- [static func <= (Self.Element, Self) -> [Bool]](./columnprotocol/opeq%28_,_%29-17m6l.md)
  Returns a Boolean array that indicates whether the value is less than or equal to the corresponding element of a column type.
- [static func > (Self, Self.Element) -> [Bool]](./columnprotocol/op%28_,_%29-9rct2.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type is greater than a value.
- [static func > (Self.Element, Self) -> [Bool]](./columnprotocol/op%28_,_%29-68any.md)
  Returns a Boolean array that indicates whether the value is greater than the corresponding element of a column type.
- [static func >= (Self, Self.Element) -> [Bool]](./columnprotocol/opeq%28_,_%29-2w8gt.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type is greater than or equal to a value.
- [static func >= (Self.Element, Self) -> [Bool]](./columnprotocol/opeq%28_,_%29-8jak4.md)
  Returns a Boolean array that indicates whether the value is greater than or equal to the corresponding element of a column type.
### Retrieving an index
- [var startIndex: Base.Index](./filledcolumn/startindex.md)
  The index of the initial element in the column.
- [var endIndex: Base.Index](./filledcolumn/endindex.md)
  The index of the final element in the column.
- [func index(before: Base.Index) -> Base.Index](./filledcolumn/index%28before%29.md)
  Returns the row index immediately before a row index.
- [func index(after: Base.Index) -> Base.Index](./filledcolumn/index%28after%29.md)
  Returns the position immediately after an index.
### Supporting types
- [FilledColumn.Element](./filledcolumn/element.md)
  The type of the column’s elements that defines an associated type for the bidirectional collection protocol.
- [FilledColumn.WrappedElement](./filledcolumn/wrappedelement.md)
  The type of the column’s elements that defines an associated type for the optional column protocol.
### Default Implementations
- [CustomStringConvertible Implementations](./filledcolumn/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/bidirectionalcollection.md)
- [Collection](../Swift/collection.md)
- [ColumnProtocol](./columnprotocol.md)
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Typed columns
- [struct Column](./column.md)
  A column in a data frame.
- [struct ColumnSlice](./columnslice.md)
  A collection that represents a selection of contiguous elements from a typed column.
- [struct DiscontiguousColumnSlice](./discontiguouscolumnslice.md)
  A collection that represents a selection, potentially with gaps, of elements from a typed column.
- [protocol ColumnProtocol](./columnprotocol.md)
  A type that represents a column.
- [protocol OptionalColumnProtocol](./optionalcolumnprotocol.md)
  A type that represents a column that has missing values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/filledcolumn)*