# AnyColumn

**Framework**: TabularData  
**Kind**: struct

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

#### Overview

`AnyColumn` is a column type that conceals the type of its elements, unlike [`Column`](column.md), its typed counterpart.

## Topics

### Inspecting a Type-Erased Column
- [var name: String](anycolumn/name.md)
  The name of the column.
- [var count: Int](anycolumn/count.md)
  The number of elements in the column.
- [var missingCount: Int](anycolumn/missingcount.md)
  The number of missing elements in the column.
- [var wrappedElementType: any Any.Type](anycolumn/wrappedelementtype.md)
  The underlying type of the column’s elements.
- [func isNil(at: Int) -> Bool](anycolumn/isnil(at:).md)
  Returns a Boolean that indicates whether the element at the index is missing.
### Creating a Column of the Same Type
- [var prototype: any AnyColumnPrototype](anycolumn/prototype.md)
  A prototype that creates type-erased columns with the same underlying type as the column slice.
### Creating a Typed Column
- [func assumingType<T>(T.Type) -> Column<T>](anycolumn/assumingtype(_:).md)
  Returns the underlying typed column.
### Adding Elements
- [func append(Any?)](anycolumn/append(_:).md)
  Appends an optional element to the column.
- [func append(contentsOf: AnyColumn)](anycolumn/append(contentsof:)-2in58.md)
  Appends the contents of another column to the column.
- [func append(contentsOf: AnyColumnSlice)](anycolumn/append(contentsof:)-az5b.md)
  Appends the contents of a column slice to the column.
### Removing an Element
- [func remove(at: Int)](anycolumn/remove(at:).md)
  Removes an element from the column.
### Accessing Elements
- [subscript(Int) -> Any?](anycolumn/subscript(_:)-6z1b5.md)
  Accesses an element at an index.
- [subscript(Range<Int>) -> AnyColumnSlice](anycolumn/subscript(_:)-1n9t9.md)
  Accesses a contiguous subrange of the elements.
### Creating a Slice of Unique Elements
- [func distinct() -> AnyColumnSlice](anycolumn/distinct.md)
  Generates a column slice that contains unique elements.
### Creating a Slice by Masking Elements
- [subscript<C>(C) -> AnyColumnSlice](anycolumn/subscript(_:)-3658g.md)
  Returns a slice of the column by selecting elements with a collection of Booleans.
### Encoding a Column
- [func encode<T, Encoder>(T.Type, using: Encoder) throws](anycolumn/encode(_:using:).md)
  Encodes each element of the column.
- [func encoded<T, Encoder>(T.Type, using: Encoder) throws -> AnyColumn](anycolumn/encoded(_:using:).md)
  Generates a column by encoding each element’s value.
### Decoding a Column
- [func decode<T, Decoder>(T.Type, using: Decoder) throws](anycolumn/decode(_:using:).md)
  Decodes the data in each element of the column.
- [func decoded<T, Decoder>(T.Type, using: Decoder) throws -> AnyColumn](anycolumn/decoded(_:using:).md)
  Decodes data for each element of the column.
### Describing a Column
- [var description: String](anycolumn/description.md)
  A text representation of the column.
- [var debugDescription: String](anycolumn/debugdescription.md)
  A text representation of the column suitable for debugging.
- [var customMirror: Mirror](anycolumn/custommirror.md)
  A mirror that reflects the column.
### Comparing Two Columns
- [static func == (AnyColumn, AnyColumn) -> Bool](anycolumn/==(_:_:).md)
  Returns a Boolean that indicates whether the columns are equal.
- [static func != (Self, Self) -> Bool](anycolumn/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Hashing a Column
- [func hash(into: inout Hasher)](anycolumn/hash(into:).md)
  Hashes the essential components of the column by feeding them into a hasher.
### Instance Properties
- [var hashValue: Int](anycolumn/hashvalue.md)
  The hash value.
### Default Implementations
- [BidirectionalCollection Implementations](anycolumn/bidirectionalcollection-implementations.md)
- [Collection Implementations](anycolumn/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](anycolumn/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](anycolumn/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](anycolumn/customstringconvertible-implementations.md)
- [Equatable Implementations](anycolumn/equatable-implementations.md)
- [Hashable Implementations](anycolumn/hashable-implementations.md)
- [MutableCollection Implementations](anycolumn/mutablecollection-implementations.md)
- [RandomAccessCollection Implementations](anycolumn/randomaccesscollection-implementations.md)
- [Sequence Implementations](anycolumn/sequence-implementations.md)

## Relationships

### Conforms To
- [AnyColumnProtocol](anycolumnprotocol.md)
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MutableCollection](../Swift/MutableCollection.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct AnyColumnSlice](anycolumnslice.md)
  A type-erased column slice.
- [protocol AnyColumnProtocol](anycolumnprotocol.md)
  A type that represents a type-erased column.
- [protocol AnyColumnPrototype](anycolumnprototype.md)
  A prototype that creates type-erased columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumn)*