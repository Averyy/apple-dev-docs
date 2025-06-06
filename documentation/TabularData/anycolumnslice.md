# AnyColumnSlice

**Framework**: TabularData  
**Kind**: struct

A type-erased column slice.

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
struct AnyColumnSlice
```

## Topics

### Inspecting a Type-Erased Column Slice
- [var name: String](anycolumnslice/name.md)
  The name of the slice’s parent column.
- [var count: Int](anycolumnslice/count.md)
  The number of elements in the column slice.
- [var missingCount: Int](anycolumnslice/missingcount.md)
  The number of missing elements in the column slice.
- [var wrappedElementType: any Any.Type](anycolumnslice/wrappedelementtype.md)
  The underlying type of the column’s elements.
- [func isNil(at: Int) -> Bool](anycolumnslice/isnil(at:).md)
  Returns a Boolean that indicates whether the element at the index is missing.
### Converting to a Typed Column Slice
- [func assumingType<T>(T.Type) -> DiscontiguousColumnSlice<T>](anycolumnslice/assumingtype(_:).md)
  Returns a slice of the underlying typed column.
### Accessing Elements
- [subscript(Int) -> Any?](anycolumnslice/subscript(_:)-g0gb.md)
  Accesses an element at an index.
- [subscript(Range<Int>) -> AnyColumnSlice](anycolumnslice/subscript(_:)-3qisq.md)
  Accesses a contiguous range of elements.
### Creating a Slice of Unique Elements
- [func distinct() -> AnyColumnSlice](anycolumnslice/distinct.md)
  Generates a column slice that contains unique elements.
### Summarizing a Column Slice
- [func summary() -> AnyCategoricalSummary](anycolumnslice/summary.md)
  Generates a categorical summary of the column slice’s elements.
### Describing a Column Slice
- [var description: String](anycolumnslice/description.md)
  A text representation of the column slice.
- [var debugDescription: String](anycolumnslice/debugdescription.md)
  A text representation of the column slice suitable for debugging.
- [var customMirror: Mirror](anycolumnslice/custommirror.md)
  A mirror that reflects the column slice.
### Comparing Two Column Slices
- [static func == (AnyColumnSlice, AnyColumnSlice) -> Bool](anycolumnslice/==(_:_:).md)
  Returns a Boolean that indicates whether the column slices are equal.
- [static func != (Self, Self) -> Bool](anycolumnslice/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Hashing a Column Slice
- [func hash(into: inout Hasher)](anycolumnslice/hash(into:).md)
  Hashes the essential components of the column slice by feeding them into a hasher.
### Instance Properties
- [var hashValue: Int](anycolumnslice/hashvalue.md)
  The hash value.
### Default Implementations
- [BidirectionalCollection Implementations](anycolumnslice/bidirectionalcollection-implementations.md)
- [Collection Implementations](anycolumnslice/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](anycolumnslice/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](anycolumnslice/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](anycolumnslice/customstringconvertible-implementations.md)
- [Equatable Implementations](anycolumnslice/equatable-implementations.md)
- [Hashable Implementations](anycolumnslice/hashable-implementations.md)
- [MutableCollection Implementations](anycolumnslice/mutablecollection-implementations.md)
- [RandomAccessCollection Implementations](anycolumnslice/randomaccesscollection-implementations.md)
- [Sequence Implementations](anycolumnslice/sequence-implementations.md)

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

- [struct AnyColumn](anycolumn.md)
  A type-erased column.
- [protocol AnyColumnProtocol](anycolumnprotocol.md)
  A type that represents a type-erased column.
- [protocol AnyColumnPrototype](anycolumnprototype.md)
  A prototype that creates type-erased columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumnslice)*