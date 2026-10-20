# AnyColumnSlice

**Framework**: TabularData  
**Kind**: struct  
**Role**: Structure

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
- [var name: String](./anycolumnslice/name.md)
  The name of the slice’s parent column.
- [var count: Int](./anycolumnslice/count.md)
  The number of elements in the column slice.
- [var missingCount: Int](./anycolumnslice/missingcount.md)
  The number of missing elements in the column slice.
- [var wrappedElementType: any Any.Type](./anycolumnslice/wrappedelementtype.md)
  The underlying type of the column’s elements.
- [func isNil(at: Int) -> Bool](./anycolumnslice/isnil%28at%29.md)
  Returns a Boolean that indicates whether the element at the index is missing.
### Converting to a Typed Column Slice
- [func assumingType<T>(T.Type) -> DiscontiguousColumnSlice<T>](./anycolumnslice/assumingtype%28_%29.md)
  Returns a slice of the underlying typed column.
### Accessing Elements
- [subscript(Int) -> Any?](./anycolumnslice/subscript%28_%29-g0gb.md)
  Accesses an element at an index.
- [subscript(Range<Int>) -> AnyColumnSlice](./anycolumnslice/subscript%28_%29-3qisq.md)
  Accesses a contiguous range of elements.
### Creating a Slice of Unique Elements
- [func distinct() -> AnyColumnSlice](./anycolumnslice/distinct%28%29.md)
  Generates a column slice that contains unique elements.
### Summarizing a Column Slice
- [func summary() -> AnyCategoricalSummary](./anycolumnslice/summary%28%29.md)
  Generates a categorical summary of the column slice’s elements.
### Describing a Column Slice
- [var description: String](./anycolumnslice/description.md)
  A text representation of the column slice.
- [var debugDescription: String](./anycolumnslice/debugdescription.md)
  A text representation of the column slice suitable for debugging.
- [var customMirror: Mirror](./anycolumnslice/custommirror.md)
  A mirror that reflects the column slice.
### Comparing Two Column Slices
- [static func == (AnyColumnSlice, AnyColumnSlice) -> Bool](./anycolumnslice/eqeq%28_,_%29.md)
  Returns a Boolean that indicates whether the column slices are equal.
### Hashing a Column Slice
- [func hash(into: inout Hasher)](./anycolumnslice/hash%28into%29.md)
  Hashes the essential components of the column slice by feeding them into a hasher.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./anycolumnslice/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](./anycolumnslice/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](./anycolumnslice/customstringconvertible-implementations.md)
- [Equatable Implementations](./anycolumnslice/equatable-implementations.md)
- [Hashable Implementations](./anycolumnslice/hashable-implementations.md)
- [RandomAccessCollection Implementations](./anycolumnslice/randomaccesscollection-implementations.md)

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

### Type-Erased Columns
- [struct AnyColumn](./anycolumn.md)
  A type-erased column.
- [protocol AnyColumnProtocol](./anycolumnprotocol.md)
  A type that represents a type-erased column.
- [protocol AnyColumnPrototype](./anycolumnprototype.md)
  A prototype that creates type-erased columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumnslice)*