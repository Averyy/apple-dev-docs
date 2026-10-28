# MLUntypedColumn

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

A column of untyped values in a data table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MLUntypedColumn
```

## Overview

A column is a homogenous collection of data values, similar to an [`Array`](../Swift/array.md). Columns are the main components of an [`MLDataTable`](./mldatatable.md) and are designed to efficiently scale with large data sets.

Typically you use [`MLDataColumn`](./mldatacolumn.md), the typed equivalent to [`MLUntypedColumn`](./mluntypedcolumn.md), for its type-specific functionality.

Untyped columns are especially useful when:

- You’re initializing a data table with columns by using [`init(namedColumns:)`](./mldatatable/init%28namedcolumns%29.md).
- You’re using columns of a non-Boolean type to filter a data table with [`subscript(_:)`](./mldatatable/subscript%28_%29-10r4l.md).
- You don’t need to work directly with the underlying type.

Each element of an untyped column is an [`MLDataValue`](./mldatavalue.md), and has an *underlying type* that conforms to [`MLDataValueConvertible`](./mldatavalueconvertible.md). The underlying type is hidden from the Swift compiler and is what makes an [`MLUntypedColumn`](./mluntypedcolumn.md) untyped. Using an untyped column allows you to quickly write type-agnostic code with Create ML.

```swift
let column = MLUntypedColumn([2, 3, 5, 7, 11])
let columnOver2 = column / 2 print(columnOver2)
/* Prints...
 ValueType: Double
 Values:        [1.0, 1.5, 2.5, 3.5, 5.5]
 */
```

However, by avoiding type safety at compile time, you expose your code to errors at runtime. When an error occurs during an operation, Create ML marks the product of that operation *invalid* by setting [`isValid`](./mluntypedcolumn/isvalid.md) to `false` and by setting [`error`](./mluntypedcolumn/error.md) with a value. For example, using a slash (`/`) operator to divide a column of integers with a string produces an invalid column.

```swift
let column = MLUntypedColumn([2, 3, 5, 7, 11])
let invalidColumn = column / "foo"
print(invalidColumn.isValid) // Prints "false"
```

> ❗ **Important**: A mismatch between the underlying types of two columns, or between the underlying type of a column and the type of a value, will result in an invalid column.

Once a column becomes invalid, you can’t use it for any subsequent operation because it will only produce further invalid columns or invalid tables.

Each comparison operator of [`MLUntypedColumn`](./mluntypedcolumn.md) returns a column of Booleans. However, [`MLUntypedColumn`](./mluntypedcolumn.md) uses integers as its underlying type for columns of Booleans, because [`MLDataValue`](./mldatavalue.md) does not have a case for [`Bool`](../Swift/bool.md).

For example, create an untyped column of Booleans using the less-than comparison operator([`<(_:_:)`](./mluntypedcolumn/op%28_,_%29-7zms0.md)).

```swift
let column = MLUntypedColumn([2, 3, 5, 7, 11])
let lessThan5 = column < 5
```

Then print the column to see that its underlying `ValueType` is `Int`, and each Boolean value of `true` or `false` is represented in the column by an integer value of `1` or `0`, respectively.

```swift
print(lessThan5)
/* Prints...
 ValueType: Int
 Values:        [1, 1, 0, 0, 0]
 */
```

Use these untyped columns of Booleans just as you would with a typed column of Booleans (``MLDataColumn```<`<doc://com.apple.documentation/documentation/swift/bool>`>`) to:

- Filter another untyped column with [`subscript(_:)`](./mluntypedcolumn/subscript%28_%29-9hr32.md)
- Logically combine with another untyped column of Booleans with the [`&&(_:_:)`](./mluntypedcolumn/ampamp%28_,_%29.md) and [`||(_:_:)`](./mluntypedcolumn/opop%28_,_%29.md) operators
- Mask rows of an [`MLDataTable`](./mldatatable.md) with its [`subscript(_:)`](./mldatatable/subscript%28_%29-3opgl.md)

## Topics

### Creating an untyped column
- [init(repeating:count:)](./mluntypedcolumn/init%28repeating,count%29.md)
  Creates a new column with a repeating value.
- [init<T>(repeating: T, count: Int)](./mluntypedcolumn/init%28repeating,count%29-7ttf1.md)
  Creates a new column with a repeating value.
- [init(repeating: MLDataValue, count: Int)](./mluntypedcolumn/init%28repeating,count%29-q8yk.md)
  Creates a new column with a repeating value.
- [init(_:)](./mluntypedcolumn/init%28_%29.md)
  Creates a new column of integers from a given closed range.
- [init(Range<Int>)](./mluntypedcolumn/init%28_%29-33tcv.md)
  Creates a new column of integers from a given range.
- [init(ClosedRange<Int>)](./mluntypedcolumn/init%28_%29-9no5.md)
  Creates a new column of integers from a given closed range.
- [init<S>(S)](./mluntypedcolumn/init%28_%29-ag8f.md)
  Creates a new column from a given sequence of elements that can be converted to machine learning data values.
- [init<S>(S)](./mluntypedcolumn/init%28_%29-5by2g.md)
  Creates a new column from a given sequence of machine learning data values.
- [init()](./mluntypedcolumn/init%28%29.md)
  Creates an empty, invalid column used to remove an existing column from a data table.
### Creating an untyped column by converting another column
- [init(ints: MLUntypedColumn)](./mluntypedcolumn/init%28ints%29.md)
  Creates a new column of integers by converting the elements of another column.
- [init(doubles: MLUntypedColumn)](./mluntypedcolumn/init%28doubles%29.md)
  Creates a new column of doubles by converting the elements of another column.
- [init(strings: MLUntypedColumn)](./mluntypedcolumn/init%28strings%29.md)
  Creates a new column of strings by converting the elements of another column.
- [init(sequences: MLUntypedColumn)](./mluntypedcolumn/init%28sequences%29.md)
  Creates a new column of machine learning sequences by converting the elements of another column.
- [init(dictionaries: MLUntypedColumn)](./mluntypedcolumn/init%28dictionaries%29.md)
  Creates a new column of machine learning dictionaries by converting the elements of another column.
- [init(multiArrays: MLUntypedColumn)](./mluntypedcolumn/init%28multiarrays%29.md)
  Creates a MLUntypedColumn of type MLMultiArray from the specified MLUntypedColumn if the values of the given MLUntypedColumn are convertible to MLDataValue.MultiArrayType.
### Getting the number of elements
- [var count: Int](./mluntypedcolumn/count.md)
  The number of elements in the column.
- [var isEmpty: Bool](./mluntypedcolumn/isempty.md)
### Getting an element
- [subscript(Int) -> MLDataValue](./mluntypedcolumn/subscript%28_%29-6j6rb.md)
  Accesses the element at the given position.
### Appending to an untyped column
- [func append(contentsOf: MLUntypedColumn)](./mluntypedcolumn/append%28contentsof%29.md)
  Appends the elements of the given column to the end of this column.
### Duplicating a column
- [func copy() -> MLUntypedColumn](./mluntypedcolumn/copy%28%29.md)
  Returns a new MLUntypedColumn by copying the original MLUntypedColumn
### Sorting elements to generate a column
- [func sort(byIncreasingOrder: Bool) -> MLUntypedColumn](./mluntypedcolumn/sort%28byincreasingorder%29.md)
  Returns a new MLUntypedColumn containing values sorted by the specified order.
### Converting a column to generate a data column
- [func map<T>(to: T.Type) -> MLDataColumn<T>](./mluntypedcolumn/map%28to%29.md)
  Creates a new column of typed values by converting this untyped column to the given type.
### Exposing the underlying type to generate a data column
- [var type: MLDataValue.ValueType](./mluntypedcolumn/type.md)
  The underlying type of the column.
- [var ints: MLDataColumn<Int>?](./mluntypedcolumn/ints.md)
  A cloned data column of integers.
- [var doubles: MLDataColumn<Double>?](./mluntypedcolumn/doubles.md)
  A cloned data column of doubles.
- [var strings: MLDataColumn<String>?](./mluntypedcolumn/strings.md)
  A cloned data column of strings.
- [var sequences: MLDataColumn<MLDataValue.SequenceType>?](./mluntypedcolumn/sequences.md)
  A cloned data column of machine learning sequences.
- [var dictionaries: MLDataColumn<MLDataValue.DictionaryType>?](./mluntypedcolumn/dictionaries.md)
  A cloned data column of machine learning dictionaries.
- [var multiArrays: MLDataColumn<MLDataValue.MultiArrayType>?](./mluntypedcolumn/multiarrays.md)
  A cloned data column of machine learning multi-arrays.
- [func column<T>(type: T.Type) -> MLDataColumn<T>?](./mluntypedcolumn/column%28type%29.md)
  Clones the column to a data column of the given type.
### Transforming elements to generate a data column
- [func map(_:)](./mluntypedcolumn/map%28_%29.md)
  Creates a new column of typed values by applying the given thread-safe transform to every non-missing element of this untyped column.
- [func map<T>((MLDataValue) -> T) -> MLDataColumn<T>](./mluntypedcolumn/map%28_%29-139qy.md)
  Creates a new column of typed values by applying the given thread-safe transform to every non-missing element of this untyped column.
- [func map<T>((MLDataValue) -> T?) -> MLDataColumn<T>](./mluntypedcolumn/map%28_%29-9v61j.md)
  Creates a new column of typed values, potentially with missing values, by applying the given thread-safe transform to every non-missing element of this untyped column.
- [func mapMissing<T>((MLDataValue) -> T?) -> MLDataColumn<T>](./mluntypedcolumn/mapmissing%28_%29.md)
  Creates a new column of typed values by applying the given thread-safe transform to every element of this untyped column, including missing elements.
### Masking elements to generate an untyped column
- [subscript(_:)](./mluntypedcolumn/subscript%28_%29.md)
  Accesses the element at the given position.
- [subscript(MLDataColumn<Bool>) -> MLUntypedColumn](./mluntypedcolumn/subscript%28_%29-8ot43.md)
  Creates a subset of the column by masking its elements with a data column of Booleans.
- [subscript(MLUntypedColumn) -> MLUntypedColumn](./mluntypedcolumn/subscript%28_%29-9hr32.md)
  Creates a subset of the column by masking its elements with another untyped column.
### Discarding elements to generate an untyped column
- [func dropMissing() -> MLUntypedColumn](./mluntypedcolumn/dropmissing%28%29.md)
  Creates a subset of the column by removing all elements without a value.
- [func dropDuplicates() -> MLUntypedColumn](./mluntypedcolumn/dropduplicates%28%29.md)
  Creates a subset of the column by removing all duplicate elements.
### Selecting elements to generate an untyped column
- [subscript(Range<Int>) -> MLUntypedColumn](./mluntypedcolumn/subscript%28_%29-33ua2.md)
  Creates a subset of the column, given a range of elements.
- [subscript<R>(R) -> MLUntypedColumn](./mluntypedcolumn/subscript%28_%29-9dpy7.md)
  Creates a subset of the column, given a range expression of elements.
- [func prefix(Int) -> MLUntypedColumn](./mluntypedcolumn/prefix%28_%29.md)
  Creates a subset of the column, given a number of initial elements.
- [func suffix(Int) -> MLUntypedColumn](./mluntypedcolumn/suffix%28_%29.md)
  Creates a subset of the column, given a number of final elements.
### Filling in missing elements to generate an untyped column
- [func fillMissing(with: MLDataValue) -> MLUntypedColumn](./mluntypedcolumn/fillmissing%28with%29.md)
  Creates a modified copy of the column such that every missing element is replaced with the given value.
### Evaluating elements to generate an untyped column
- [func materialize() throws -> MLUntypedColumn](./mluntypedcolumn/materialize%28%29.md)
  Creates a new column by immediately evaluating any lazily applied data processing operations stored in the column.
### Combining columns
- [static +(_:_:)](./mluntypedcolumn/plus%28_,_%29.md)
  Creates a column by adding each element in the first column to the corresponding element in the second column.
- [static -(_:_:)](./mluntypedcolumn/minus%28_,_%29.md)
  Creates a column by subtracting each element in the second column from the corresponding element in the first column.
- [static *(_:_:)](./mluntypedcolumn/star%28_,_%29.md)
  Creates a column by multiplying each element in the first column by the corresponding element in the second column.
- [static /(_:_:)](./mluntypedcolumn/op%28_,_%29-20v6v.md)
  Creates a column by dividing each element in the first column by the corresponding element in the second column.
### Combining columns to generate an untyped column
- [static func + (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](./mluntypedcolumn/plus%28_,_%29-bcc5.md)
  Creates a column by adding each element in the first column to the corresponding element in the second column.
- [static func - (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](./mluntypedcolumn/minus%28_,_%29-3h4o4.md)
  Creates a column by subtracting each element in the second column from the corresponding element in the first column.
- [static func * (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](./mluntypedcolumn/star%28_,_%29-2p6nm.md)
  Creates a column by multiplying each element in the first column by the corresponding element in the second column.
- [static func / (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](./mluntypedcolumn/op%28_,_%29-45tpp.md)
  Creates a column by dividing each element in the first column by the corresponding element in the second column.
### Combining a column with a value to generate an untyped column
- [static func + (MLUntypedColumn, any MLDataValueConvertible) -> MLUntypedColumn](./mluntypedcolumn/plus%28_,_%29-4vnbk.md)
  Creates a column by adding each element of the given column to the given value.
- [static func - (MLUntypedColumn, any MLDataValueConvertible) -> MLUntypedColumn](./mluntypedcolumn/minus%28_,_%29-4uigi.md)
  Creates a column by subtracting the given value from each element of the given column.
- [static func * (MLUntypedColumn, any MLDataValueConvertible) -> MLUntypedColumn](./mluntypedcolumn/star%28_,_%29-6gnlx.md)
  Creates a column by multiplying each element of the given column by the given value.
- [static func / (MLUntypedColumn, any MLDataValueConvertible) -> MLUntypedColumn](./mluntypedcolumn/op%28_,_%29-18srk.md)
  Creates a column by dividing each element of the given column by the given value.
### Combining a value with a column to generate an untyped column
- [static func + (any MLDataValueConvertible, MLUntypedColumn) -> MLUntypedColumn](./mluntypedcolumn/plus%28_,_%29-miqp.md)
  Creates a column by adding the given value to each element of the given column.
- [static func - (any MLDataValueConvertible, MLUntypedColumn) -> MLUntypedColumn](./mluntypedcolumn/minus%28_,_%29-9gm9i.md)
  Creates a column by subtracting each element of the given column from the given value.
- [static func * (any MLDataValueConvertible, MLUntypedColumn) -> MLUntypedColumn](./mluntypedcolumn/star%28_,_%29-7svdc.md)
  Creates a column by multiplying the given value by each element of the given column.
- [static func / (any MLDataValueConvertible, MLUntypedColumn) -> MLUntypedColumn](./mluntypedcolumn/op%28_,_%29-aw9o.md)
  Creates a column by dividing the given value by each element of the given column.
### Comparing columns
- [static ==(_:_:)](./mluntypedcolumn/eqeq%28_,_%29.md)
  Creates a column of Booleans by testing whether each element in the first column is equal to the corresponding element in the second column.
- [static !=(_:_:)](./mluntypedcolumn/noteq%28_,_%29.md)
  Creates a column of Booleans by testing whether each element in the first column is not equal to the corresponding element in the second column.
- [static >(_:_:)](./mluntypedcolumn/op%28_,_%29-1hr3j.md)
  Creates a column of Booleans by testing whether each element in the first column is greater than the corresponding element in the second column.
- [static <(_:_:)](./mluntypedcolumn/op%28_,_%29-9ke05.md)
  Creates a column of Booleans by testing whether each element in the first column is less than the corresponding element in the second column.
- [static <=(_:_:)](./mluntypedcolumn/opeq%28_,_%29-2i3xz.md)
  Creates a column of Booleans by testing whether each element in the first column is less than or equal to the corresponding element in the second column.
- [static >=(_:_:)](./mluntypedcolumn/opeq%28_,_%29-221lt.md)
  Creates a column of Booleans by testing whether each element in the first column is greater than or equal to the corresponding element in the second column.
### Comparing columns to generate an untyped column of booleans
- [static func == (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](./mluntypedcolumn/eqeq%28_,_%29-3o7mo.md)
  Creates a column of Booleans by testing whether each element in the first column is equal to the corresponding element in the second column.
- [static func != (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](./mluntypedcolumn/noteq%28_,_%29-86hu4.md)
  Creates a column of Booleans by testing whether each element in the first column is not equal to the corresponding element in the second column.
- [static func > (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](./mluntypedcolumn/op%28_,_%29-9r2zq.md)
  Creates a column of Booleans by testing whether each element in the first column is greater than the corresponding element in the second column.
- [static func < (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](./mluntypedcolumn/op%28_,_%29-7zms0.md)
  Creates a column of Booleans by testing whether each element in the first column is less than the corresponding element in the second column.
- [static func <= (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](./mluntypedcolumn/opeq%28_,_%29-5xmwz.md)
  Creates a column of Booleans by testing whether each element in the first column is less than or equal to the corresponding element in the second column.
- [static func >= (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](./mluntypedcolumn/opeq%28_,_%29-4u3ir.md)
  Creates a column of Booleans by testing whether each element in the first column is greater than or equal to the corresponding element in the second column.
### Comparing a column with a value to generate an untyped column of booleans
- [static func == (MLUntypedColumn, any MLDataValueConvertible) -> MLUntypedColumn](./mluntypedcolumn/eqeq%28_,_%29-7xysh.md)
  Creates a column of Booleans by testing whether each element in the given column is equal to the given value.
- [static func != (MLUntypedColumn, any MLDataValueConvertible) -> MLUntypedColumn](./mluntypedcolumn/noteq%28_,_%29-7do9.md)
  Creates a column of Booleans by testing whether each element in the given column is not equal to the given value.
- [static func > (MLUntypedColumn, any MLDataValueConvertible) -> MLUntypedColumn](./mluntypedcolumn/op%28_,_%29-2mdrt.md)
  Creates a column of Booleans by testing whether each element in the given column is greater than the given value.
- [static func < (MLUntypedColumn, any MLDataValueConvertible) -> MLUntypedColumn](./mluntypedcolumn/op%28_,_%29-8w60f.md)
  Creates a column of Booleans by testing whether each element in the given column is less than the given value.
- [static func <= (MLUntypedColumn, any MLDataValueConvertible) -> MLUntypedColumn](./mluntypedcolumn/opeq%28_,_%29-1wkt3.md)
  Creates a column of Booleans by testing whether each element in the given column is less than or equal to the given value.
- [static func >= (MLUntypedColumn, any MLDataValueConvertible) -> MLUntypedColumn](./mluntypedcolumn/opeq%28_,_%29-2vu3g.md)
  Creates a column of Booleans by testing whether each element in the given column is greater than or equal to the given value.
### Comparing a value with a column to generate an untyped column of booleans
- [static func == (any MLDataValueConvertible, MLUntypedColumn) -> MLUntypedColumn](./mluntypedcolumn/eqeq%28_,_%29-6z88q.md)
  Creates a column of Booleans by testing whether the given value is equal to each element in the given column.
- [static func != (any MLDataValueConvertible, MLUntypedColumn) -> MLUntypedColumn](./mluntypedcolumn/noteq%28_,_%29-6k3p6.md)
  Creates a column of Booleans by testing whether the given value is not equal to each element in the given column.
- [static func > (any MLDataValueConvertible, MLUntypedColumn) -> MLUntypedColumn](./mluntypedcolumn/op%28_,_%29-52drj.md)
  Creates a column of Booleans by testing whether the given value is greater than each element in the given column.
- [static func < (any MLDataValueConvertible, MLUntypedColumn) -> MLUntypedColumn](./mluntypedcolumn/op%28_,_%29-6qou9.md)
  Creates a column of Booleans by testing whether the given value is less than each element in the given column.
- [static func <= (any MLDataValueConvertible, MLUntypedColumn) -> MLUntypedColumn](./mluntypedcolumn/opeq%28_,_%29-t4bt.md)
  Creates a column of Booleans by testing whether the given value is less than or equal to each element in the given column.
- [static func >= (any MLDataValueConvertible, MLUntypedColumn) -> MLUntypedColumn](./mluntypedcolumn/opeq%28_,_%29-6yycf.md)
  Creates a column of Booleans by testing whether the given value is greater than or equal to each element in the given column.
### Combining columns of booleans to generate an untyped column of booleans
- [static func && (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](./mluntypedcolumn/ampamp%28_,_%29.md)
  Creates a column of Booleans by performing a logical AND operation on each row of two columns of Booleans.
- [static func || (MLUntypedColumn, MLUntypedColumn) -> MLUntypedColumn](./mluntypedcolumn/opop%28_,_%29.md)
  Creates a column of Booleans by performing a logical OR operation on each row of two columns of Booleans.
### Visualizing a column
- [func show() -> any MLStreamingVisualizable](./mluntypedcolumn/show%28%29.md)
  Provides a visualization for the data in the column.
### Getting a description of an untyped column
- [var description: String](./mluntypedcolumn/description.md)
  A text representation of the column.
- [var playgroundDescription: Any](./mluntypedcolumn/playgrounddescription.md)
  A description of the column shown in a playground.
- [var debugDescription: String](./mluntypedcolumn/debugdescription.md)
  A text representation of the column for debugging.
- [var customMirror: Mirror](./mluntypedcolumn/custommirror.md)
  A view of the column for Xcode Playgrounds and lldb.
### Handling untyped column errors
- [var isValid: Bool](./mluntypedcolumn/isvalid.md)
  A Boolean value that indicates whether the column is valid.
- [var error: (any Error)?](./mluntypedcolumn/error.md)
  The underlying error present when the column is invalid.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./mluntypedcolumn/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](./mluntypedcolumn/customplaygrounddisplayconvertible-implementations.md)
- [CustomReflectable Implementations](./mluntypedcolumn/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](./mluntypedcolumn/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/customplaygrounddisplayconvertible.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Escapable](../Swift/escapable.md)

## See Also

### Adding columns
- [func addColumn(_:named:)](./mldatatable/addcolumn%28_,named%29.md)
  Adds an untyped column to the table.
- [struct MLDataColumn](./mldatacolumn.md)
  A column of typed values in a data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mluntypedcolumn)*