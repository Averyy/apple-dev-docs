# AnyColumn

**Framework**: TabularData  
**Kind**: struct  
**Role**: Structure

A type-erased column.

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
struct AnyColumn
```

## Overview

`AnyColumn` is a column type that conceals the type of its elements, unlike [`Column`](./column.md), its typed counterpart.

## Topics

### Inspecting a type-erased column
- [var name: String](./anycolumn/name.md)
  The name of the column.
- [var count: Int](./anycolumn/count.md)
  The number of elements in the column.
- [var missingCount: Int](./anycolumn/missingcount.md)
  The number of missing elements in the column.
- [var wrappedElementType: any Any.Type](./anycolumn/wrappedelementtype.md)
  The underlying type of the column’s elements.
- [func isNil(at: Int) -> Bool](./anycolumn/isnil%28at%29.md)
  Returns a Boolean that indicates whether the element at the index is missing.
### Creating a column of the same type
- [var prototype: any AnyColumnPrototype](./anycolumn/prototype.md)
  A prototype that creates type-erased columns with the same underlying type as the column slice.
### Creating a typed column
- [func assumingType<T>(T.Type) -> Column<T>](./anycolumn/assumingtype%28_%29.md)
  Returns the underlying typed column.
### Adding elements
- [func append(Any?)](./anycolumn/append%28_%29.md)
  Appends an optional element to the column.
- [func append(contentsOf: AnyColumn)](./anycolumn/append%28contentsof%29-2in58.md)
  Appends the contents of another column to the column.
- [func append(contentsOf: AnyColumnSlice)](./anycolumn/append%28contentsof%29-az5b.md)
  Appends the contents of a column slice to the column.
### Removing an element
- [func remove(at: Int)](./anycolumn/remove%28at%29.md)
  Removes an element from the column.
### Accessing elements
- [subscript(Int) -> Any?](./anycolumn/subscript%28_%29-6z1b5.md)
  Accesses an element at an index.
- [subscript(Range<Int>) -> AnyColumnSlice](./anycolumn/subscript%28_%29-1n9t9.md)
  Accesses a contiguous subrange of the elements.
### Creating a slice of unique elements
- [func distinct() -> AnyColumnSlice](./anycolumn/distinct%28%29.md)
  Generates a column slice that contains unique elements.
### Creating a slice by masking elements
- [subscript<C>(C) -> AnyColumnSlice](./anycolumn/subscript%28_%29-3658g.md)
  Returns a slice of the column by selecting elements with a collection of Booleans.
### Encoding a column
- [func encode<T, Encoder>(T.Type, using: Encoder) throws](./anycolumn/encode%28_,using%29.md)
  Encodes each element of the column.
- [func encoded<T, Encoder>(T.Type, using: Encoder) throws -> AnyColumn](./anycolumn/encoded%28_,using%29.md)
  Generates a column by encoding each element’s value.
### Decoding a column
- [func decode<T, Decoder>(T.Type, using: Decoder) throws](./anycolumn/decode%28_,using%29.md)
  Decodes the data in each element of the column.
- [func decoded<T, Decoder>(T.Type, using: Decoder) throws -> AnyColumn](./anycolumn/decoded%28_,using%29.md)
  Decodes data for each element of the column.
### Describing a column
- [var description: String](./anycolumn/description.md)
  A text representation of the column.
- [var debugDescription: String](./anycolumn/debugdescription.md)
  A text representation of the column suitable for debugging.
- [var customMirror: Mirror](./anycolumn/custommirror.md)
  A mirror that reflects the column.
### Comparing two columns
- [static func == (AnyColumn, AnyColumn) -> Bool](./anycolumn/eqeq%28_,_%29.md)
  Returns a Boolean that indicates whether the columns are equal.
### Hashing a column
- [func hash(into: inout Hasher)](./anycolumn/hash%28into%29.md)
  Hashes the essential components of the column by feeding them into a hasher.
### Retrieving an index
- [var startIndex: Int](./anycolumn/startindex.md)
  The index of the initial element in the column.
- [var endIndex: Int](./anycolumn/endindex.md)
  The index of the final element in the column.
- [func index(before: Int) -> Int](./anycolumn/index%28before%29.md)
  Returns the index immediately before an element index.
- [func index(after: Int) -> Int](./anycolumn/index%28after%29.md)
  Returns the index immediately after an element index.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./anycolumn/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](./anycolumn/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](./anycolumn/customstringconvertible-implementations.md)
- [Equatable Implementations](./anycolumn/equatable-implementations.md)
- [Hashable Implementations](./anycolumn/hashable-implementations.md)
- [RandomAccessCollection Implementations](./anycolumn/randomaccesscollection-implementations.md)

## Relationships

### Conforms To
- [AnyColumnProtocol](./anycolumnprotocol.md)
- [BidirectionalCollection](../Swift/bidirectionalcollection.md)
- [Collection](../Swift/collection.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [MutableCollection](../Swift/mutablecollection.md)
- [RandomAccessCollection](../Swift/randomaccesscollection.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Type-erased columns
- [struct AnyColumnSlice](./anycolumnslice.md)
  A type-erased column slice.
- [protocol AnyColumnProtocol](./anycolumnprotocol.md)
  A type that represents a type-erased column.
- [protocol AnyColumnPrototype](./anycolumnprototype.md)
  A prototype that creates type-erased columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumn)*