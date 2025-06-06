# MLDataColumn

**Framework**: Create ML  
**Kind**: struct

A column of typed values in a data table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MLDataColumn<Element> where Element : MLDataValueConvertible
```

#### Overview

A column is a homogenous collection of data values, similar to an [`Array`](https://developer.apple.com/documentation/Swift/Array). Columns are the main components of an [`MLDataTable`](mldatatable.md) and are designed to efficiently scale with large data sets.

Typically you use [`MLDataColumn`](mldatacolumn.md), the typed equivalent to [`MLUntypedColumn`](mluntypedcolumn.md), to work directly with the column’s element type. A data column has extra math and statistics functionality when its element type is [`Int`](https://developer.apple.com/documentation/Swift/Int) or [`Double`](https://developer.apple.com/documentation/Swift/Double).

## Topics

### Creating a data column
- [init(repeating: Element, count: Int)](mldatacolumn/init(repeating:count:)-5rxbo.md)
  Creates a new column with a repeating element.
- [init(repeating: MLDataValue, count: Int)](mldatacolumn/init(repeating:count:)-4ljwl.md)
  Constructs a new Column containing the specified number of a single, repeated MLDataValue.
- [init<S>(S)](mldatacolumn/init(_:).md)
  Creates a new column from a given sequence of elements.
- [init()](mldatacolumn/init.md)
  Constructs an invalid Column.
### Creating a data column by converting another column
- [func map<T>(to: T.Type) -> MLDataColumn<T>](mldatacolumn/map(to:).md)
  Creates a new column by converting this column to the given type.
- [init<T>(column: MLDataColumn<T>)](mldatacolumn/init(column:)-5rg9u.md)
  Creates a new column of integers from a given column whose elements can be converted to integers.
- [init<T>(column: MLDataColumn<T>)](mldatacolumn/init(column:)-2rxtu.md)
  Creates a new column of arrays of integers from a given column whose elements can be converted to an array of integers.
- [init<T>(column: MLDataColumn<T>)](mldatacolumn/init(column:)-86ge9.md)
  Creates a new column of doubles from a given column whose elements can be converted to doubles.
- [init<T>(column: MLDataColumn<T>)](mldatacolumn/init(column:)-23pmx.md)
  Creates a new column of arrays of doubles from a given column whose elements can be converted to an array of doubles.
- [init<T>(column: MLDataColumn<T>)](mldatacolumn/init(column:)-ztkv.md)
  Creates a new column of strings from a given column whose elements can be converted to strings.
- [init<T>(column: MLDataColumn<T>)](mldatacolumn/init(column:)-8uzuq.md)
  Creates a new column of arrays of strings from a given column whose elements can be converted to an array of strings.
- [init<T>(column: MLDataColumn<T>)](mldatacolumn/init(column:)-855l9.md)
  Creates a new column of machine learning sequences from a given column whose elements can be converted to sequences.
- [init<T>(column: MLDataColumn<T>)](mldatacolumn/init(column:)-s8g5.md)
  Creates a new column of machine learning dictionaries from a given column whose elements can be converted to dictionaries.
### Getting the number of elements
- [var count: Int](mldatacolumn/count.md)
  The number of elements in the column.
- [var isEmpty: Bool](mldatacolumn/isempty.md)
### Getting an element
- [subscript(Int) -> Element](mldatacolumn/subscript(_:)-reid.md)
  Accesses the element at the given row.
- [func element(at: Int) -> Element?](mldatacolumn/element(at:).md)
  Accesses the element at the given index.
### Appending to a data column
- [func append(contentsOf: MLDataColumn<Element>)](mldatacolumn/append(contentsof:).md)
  Appends the elements of the given column to the end of this column.
### Duplicating a column
- [func copy() -> MLDataColumn<Element>](mldatacolumn/copy.md)
  Returns a new MLDataColumn by copying the original MLDataColumn
### Sorting elements to generate a column
- [func sort(byIncreasingOrder: Bool) -> MLDataColumn<Element>](mldatacolumn/sort(byincreasingorder:).md)
  Returns a new MLDataColumn containing values sorted by the specified order.
### Transforming elements to generate a column
- [func map<T>((Element) -> T) -> MLDataColumn<T>](mldatacolumn/map(_:)-7kto3.md)
  Creates a new column by applying the given thread-safe transform to every non-missing element of this column.
- [func map<T>((Element) -> T?) -> MLDataColumn<T>](mldatacolumn/map(_:)-72ypl.md)
  Creates a new column, potentially with missing values, by applying the given thread-safe transform to every non-missing element of this column.
- [func mapMissing<T>((Element?) -> T?) -> MLDataColumn<T>](mldatacolumn/mapmissing(_:).md)
  Creates a new column, potentially with missing elements, by applying the given thread-safe transform to every element of the column, including missing elements.
### Masking elements to generate a column
- [subscript(MLDataColumn<Bool>) -> MLDataColumn<Element>](mldatacolumn/subscript(_:)-78irf.md)
  Creates a subset of the column by masking its elements with a column of Booleans.
- [subscript(MLUntypedColumn) -> MLDataColumn<Element>](mldatacolumn/subscript(_:)-1n3x.md)
  Returns a `MLDataColumn` containing only the elements for which the corresponding mask has a nonzero or non-default value.
### Discarding elements to generate a column
- [func dropMissing() -> MLDataColumn<Element>](mldatacolumn/dropmissing.md)
  Creates a subset of the column by removing all elements without a value.
- [func dropDuplicates() -> MLDataColumn<Element>](mldatacolumn/dropduplicates.md)
  Creates a subset of the column by removing all duplicate elements.
### Selecting elements to generate a column
- [subscript(Range<Int>) -> MLDataColumn<Element>](mldatacolumn/subscript(_:)-pp34.md)
  Creates a subset of the column, given a range of elements.
- [subscript<R>(R) -> MLDataColumn<Element>](mldatacolumn/subscript(_:)-5mczv.md)
  Creates a subset of the column, given a range expression of elements.
- [func prefix(Int) -> MLDataColumn<Element>](mldatacolumn/prefix(_:).md)
  Creates a subset of the column, given a number of initial elements.
- [func suffix(Int) -> MLDataColumn<Element>](mldatacolumn/suffix(_:).md)
  Creates a subset of the column, given a number of final elements.
### Filling in missing elements to generate a column
- [func fillMissing(with: Element) -> MLDataColumn<Element>](mldatacolumn/fillmissing(with:).md)
  Creates a modified copy of the column such that every missing element is replaced with the given value.
### Evaluating elements to generate a column
- [func materialize() throws -> MLDataColumn<Element>](mldatacolumn/materialize.md)
  Creates a new column by immediately evaluating any lazily applied data processing operations stored in the column.
### Combining columns to generate a column
- [static func + (MLDataColumn<Int>, MLDataColumn<Int>) -> MLDataColumn<Int>](mldatacolumn/+(_:_:)-24g38.md)
  Creates a column of integers by adding each element in the first column to the corresponding element in the second column.
- [static func + (MLDataColumn<Double>, MLDataColumn<Double>) -> MLDataColumn<Double>](mldatacolumn/+(_:_:)-q5bb.md)
  Creates a column of doubles by adding each element in the first column to the corresponding element in the second column.
- [static func - (MLDataColumn<Int>, MLDataColumn<Int>) -> MLDataColumn<Int>](mldatacolumn/-(_:_:)-11hbf.md)
  Creates a column of integers by subtracting each element in the second column from the corresponding element in the first column.
- [static func - (MLDataColumn<Double>, MLDataColumn<Double>) -> MLDataColumn<Double>](mldatacolumn/-(_:_:)-3mwsr.md)
  Creates a column of doubles by subtracting each element in the second column from the corresponding element in the first column.
- [static func * (MLDataColumn<Int>, MLDataColumn<Int>) -> MLDataColumn<Int>](mldatacolumn/*(_:_:)-40smy.md)
  Creates a column of integers by multiplying each element in the first column by the corresponding element in the second column.
- [static func * (MLDataColumn<Double>, MLDataColumn<Double>) -> MLDataColumn<Double>](mldatacolumn/*(_:_:)-lchb.md)
  Creates a column of doubles by multiplying each element in the first column by the corresponding element in the second column.
- [static func / (MLDataColumn<Int>, MLDataColumn<Int>) -> MLDataColumn<Int>](mldatacolumn/_(_:_:)-5uxby.md)
  Creates a column of integers by dividing each element in the first column by the corresponding element in the second column.
- [static func / (MLDataColumn<Double>, MLDataColumn<Double>) -> MLDataColumn<Double>](mldatacolumn/_(_:_:)-69vgc.md)
  Creates a column of doubles by dividing each element in the first column by the corresponding element in the second column.
### Combining a column with a value to generate a column
- [static func + (MLDataColumn<Int>, Int) -> MLDataColumn<Int>](mldatacolumn/+(_:_:)-7tghu.md)
  Creates a column of integers by adding each element of the given column to the given integer.
- [static func + (MLDataColumn<Double>, Double) -> MLDataColumn<Double>](mldatacolumn/+(_:_:)-4se2l.md)
  Creates a column of doubles by adding each element of the given column to the given double.
- [static func - (MLDataColumn<Int>, Int) -> MLDataColumn<Int>](mldatacolumn/-(_:_:)-2sddu.md)
  Creates a column of integers by subtracting the given integer from each element of the given column.
- [static func - (MLDataColumn<Double>, Double) -> MLDataColumn<Double>](mldatacolumn/-(_:_:)-9smok.md)
  Creates a column of doubles by subtracting the given double from each element of the given column.
- [static func * (MLDataColumn<Int>, Int) -> MLDataColumn<Int>](mldatacolumn/*(_:_:)-2zih0.md)
  Creates a column of integers by multiplying each element of the given column by the given integer.
- [static func * (MLDataColumn<Double>, Double) -> MLDataColumn<Double>](mldatacolumn/*(_:_:)-4ilhj.md)
  Creates a column of doubles by multiplying each element of the given column by the given double.
- [static func / (MLDataColumn<Int>, Int) -> MLDataColumn<Int>](mldatacolumn/_(_:_:)-3ea6t.md)
  Creates a column of integers by dividing each element of the given column by the given integer.
- [static func / (MLDataColumn<Double>, Double) -> MLDataColumn<Double>](mldatacolumn/_(_:_:)-8k8ao.md)
  Creates a column of doubles by dividing each element of the given column by the given double.
### Combining a value with a column to generate a column
- [static func + (Int, MLDataColumn<Int>) -> MLDataColumn<Int>](mldatacolumn/+(_:_:)-2zcp.md)
  Creates a column of integers by adding the given integer to each element of the given column.
- [static func + (Double, MLDataColumn<Double>) -> MLDataColumn<Double>](mldatacolumn/+(_:_:)-9r67n.md)
  Creates a column of doubles by adding the given double to each element of the given column.
- [static func - (Int, MLDataColumn<Int>) -> MLDataColumn<Int>](mldatacolumn/-(_:_:)-507l8.md)
  Creates a column of integers by subtracting each element of the given column from the given integer.
- [static func - (Double, MLDataColumn<Double>) -> MLDataColumn<Double>](mldatacolumn/-(_:_:)-2e7k4.md)
  Creates a column of doubles by subtracting each element of the given column from the given double.
- [static func * (Int, MLDataColumn<Int>) -> MLDataColumn<Int>](mldatacolumn/*(_:_:)-48xte.md)
  Creates a column of integers by multiplying the given integer by each element of the given column.
- [static func * (Double, MLDataColumn<Double>) -> MLDataColumn<Double>](mldatacolumn/*(_:_:)-9sysp.md)
  Creates a column of doubles by multiplying the given double by each element of the given column.
- [static func / (Int, MLDataColumn<Int>) -> MLDataColumn<Int>](mldatacolumn/_(_:_:)-9ew9w.md)
  Creates a column of integers by dividing the given integer by each element of the given column.
- [static func / (Double, MLDataColumn<Double>) -> MLDataColumn<Double>](mldatacolumn/_(_:_:)-121w8.md)
  Creates a column of doubles by dividing the given double by each element of the given column.
### Comparing columns to generate a column of booleans
- [static func == (MLDataColumn<Element>, MLDataColumn<Element>) -> MLDataColumn<Bool>](mldatacolumn/==(_:_:)-9e3tx.md)
  Creates a column of Booleans by testing whether each element in the first column is equal to the corresponding element in the second column.
- [static func != (MLDataColumn<Element>, MLDataColumn<Element>) -> MLDataColumn<Bool>](mldatacolumn/!=(_:_:)-1vu4e.md)
  Creates a column of Booleans by testing whether each element in the first column is not equal to the corresponding element in the second column.
- [static func < (MLDataColumn<Element>, MLDataColumn<Element>) -> MLDataColumn<Bool>](mldatacolumn/_(_:_:)-3om6w.md)
  Creates a column of Booleans by testing whether each element in the first column is less than the corresponding element in the second column.
- [static func <= (MLDataColumn<Element>, MLDataColumn<Element>) -> MLDataColumn<Bool>](mldatacolumn/_=(_:_:)-6s5v1.md)
  Creates a column of Booleans by testing whether each element in the first column is less than or equal to the corresponding element in the second column.
- [static func > (MLDataColumn<Element>, MLDataColumn<Element>) -> MLDataColumn<Bool>](mldatacolumn/_(_:_:)-2dym4.md)
  Creates a column of Booleans by testing whether each element in the first column is greater than the corresponding element in the second column.
- [static func >= (MLDataColumn<Element>, MLDataColumn<Element>) -> MLDataColumn<Bool>](mldatacolumn/_=(_:_:)-4w60p.md)
  Creates a column of Booleans by testing whether each element in the first column is greater than or equal to the corresponding element in the second column.
### Comparing a column with a value to generate a column of booleans
- [static func == (MLDataColumn<Element>, Element) -> MLDataColumn<Bool>](mldatacolumn/==(_:_:)-7clbs.md)
  Creates a column of Booleans by testing whether each element in the given column is equal to the given value.
- [static func != (MLDataColumn<Element>, Element) -> MLDataColumn<Bool>](mldatacolumn/!=(_:_:)-4jp0y.md)
  Creates a column of Booleans by testing whether each element in the given column is not equal to the given value.
- [static func < (MLDataColumn<Element>, Element) -> MLDataColumn<Bool>](mldatacolumn/_(_:_:)-4ujss.md)
  Creates a column of Booleans by testing whether each element in the given column is less than the given value.
- [static func <= (MLDataColumn<Element>, Element) -> MLDataColumn<Bool>](mldatacolumn/_=(_:_:)-86x3a.md)
  Creates a column of Booleans by testing whether each element in the given column is less than or equal to the given value.
- [static func > (MLDataColumn<Element>, Element) -> MLDataColumn<Bool>](mldatacolumn/_(_:_:)-ebgq.md)
  Creates a column of Booleans by testing whether each element in the given column is greater than the given value.
- [static func >= (MLDataColumn<Element>, Element) -> MLDataColumn<Bool>](mldatacolumn/_=(_:_:)-1ctuz.md)
  Creates a column of Booleans by testing whether each element in the given column is greater than or equal to the given value.
### Comparing a value with a column to generate a column of booleans
- [static func == (Element, MLDataColumn<Element>) -> MLDataColumn<Bool>](mldatacolumn/==(_:_:)-6zz2o.md)
  Creates a column of Booleans by testing whether the given value is equal to each element in the given column.
- [static func != (Element, MLDataColumn<Element>) -> MLDataColumn<Bool>](mldatacolumn/!=(_:_:)-4477j.md)
  Creates a column of Booleans by testing whether the given value is not equal to each element in the given column.
- [static func < (Element, MLDataColumn<Element>) -> MLDataColumn<Bool>](mldatacolumn/_(_:_:)-33lwa.md)
  Creates a column of Booleans by testing whether the given value is less than each element in the given column.
- [static func <= (Element, MLDataColumn<Element>) -> MLDataColumn<Bool>](mldatacolumn/_=(_:_:)-3fx6w.md)
  Creates a column of Booleans by testing whether the given value is less than or equal to each element in the given column.
- [static func > (Element, MLDataColumn<Element>) -> MLDataColumn<Bool>](mldatacolumn/_(_:_:)-6irjn.md)
  Creates a column of Booleans by testing whether the given value is greater than each element in the given column.
- [static func >= (Element, MLDataColumn<Element>) -> MLDataColumn<Bool>](mldatacolumn/_=(_:_:)-8e3ur.md)
  Creates a column of Booleans by testing whether the given value is greater than or equal to each element in the given column.
### Combining columns of booleans to generate a column of booleans
- [static func && (MLDataColumn<Bool>, MLDataColumn<Bool>) -> MLDataColumn<Bool>](mldatacolumn/&&(_:_:).md)
  Creates a column of Booleans by performing a logical AND operation on each element in the first column with the corresponding element in the second column.
- [static func || (MLDataColumn<Bool>, MLDataColumn<Bool>) -> MLDataColumn<Bool>](mldatacolumn/__(_:_:).md)
  Creates a column of Booleans by performing a logical OR operation on each element in the first column with the corresponding element in the second column.
### Getting the min and max element values
- [func min() -> Int?](mldatacolumn/min-6xxpx.md)
  Returns the element with the lowest value in a column of integers.
- [func min() -> Double?](mldatacolumn/min-947f9.md)
  Returns the element with the lowest value in a column of doubles.
- [func max() -> Int?](mldatacolumn/max-5ty6r.md)
  Returns the element with the highest value in a column of integers.
- [func max() -> Double?](mldatacolumn/max-9ryp.md)
  Returns the element with the highest value in a column of doubles.
### Getting sum, mean, and standard deviation values
- [func sum() -> Int?](mldatacolumn/sum-9t8h3.md)
  Returns the sum of the elements in a column of integers.
- [func sum() -> Double?](mldatacolumn/sum-7370q.md)
  Returns the sum of the elements in a column of doubles.
- [func mean() -> Double?](mldatacolumn/mean-5q8pp.md)
  Returns the arithmetic mean of the elements in a column of integers.
- [func mean() -> Double?](mldatacolumn/mean-7pv86.md)
  Returns the arithmetic mean of the elements in a column of doubles.
- [func std() -> Double?](mldatacolumn/std-69udj.md)
  Returns the standard deviation of the elements in a column of integers.
- [func std() -> Double?](mldatacolumn/std-1f7cr.md)
  Returns the standard deviation of the elements in a column of doubles.
- [func stdev() -> Double?](mldatacolumn/stdev-4nvbb.md)
  Returns the standard deviation of the elements in a column of doubles.
- [func stdev() -> Double?](mldatacolumn/stdev-6fy3a.md)
  Standard deviation of the Elements in the MLDataColumn.
### Visualizing a column
- [func show() -> any MLStreamingVisualizable](mldatacolumn/show.md)
  Provides a visualization for the data in the column.
### Getting a description of a data column
- [var description: String](mldatacolumn/description.md)
  A text representation of the column.
- [var playgroundDescription: Any](mldatacolumn/playgrounddescription.md)
  A description of the column shown in a playground.
- [var debugDescription: String](mldatacolumn/debugdescription.md)
  A text representation of the column for debugging.
### Handling data column errors
- [var isValid: Bool](mldatacolumn/isvalid.md)
  A Boolean value that indicates whether the column is valid.
- [var error: (any Error)?](mldatacolumn/error.md)
  The underlying error present when the column is invalid.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mldatacolumn/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mldatacolumn/customplaygrounddisplayconvertible-implementations.md)
- [CustomReflectable Implementations](mldatacolumn/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](mldatacolumn/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [struct MLUntypedColumn](mluntypedcolumn.md)
  A column of untyped values in a data table.
- [func addColumn<Element>(MLDataColumn<Element>, named: String)](mldatatable/addcolumn(_:named:)-kkbw.md)
  Adds a data column to the table.
- [func addColumn(MLUntypedColumn, named: String)](mldatatable/addcolumn(_:named:)-9cb24.md)
  Adds an untyped column to the table.
- [struct MLUntypedColumn](mluntypedcolumn.md)
  A column of untyped values in a data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatacolumn)*