# AnyColumnProtocol

**Framework**: TabularData  
**Kind**: protocol

A type that represents a type-erased column.

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
protocol AnyColumnProtocol
```

#### Overview

`AnyColumnProtocol` defines the common functionality for type-erased column types. Its typed counterpart is [`ColumnProtocol`](columnprotocol.md).

## Topics

### Inspecting a Type-Erased Column Type
- [var name: String](anycolumnprotocol/name.md)
  The name of the column type.
- [var count: Int](anycolumnprotocol/count.md)
  The number of elements in the column type.
- [var wrappedElementType: any Any.Type](anycolumnprotocol/wrappedelementtype.md)
  The underlying type of the column type’s elements.
### Retrieving Elements
- [subscript(Int) -> Any?](anycolumnprotocol/subscript(_:)-1dl8y.md)
  Retrieves an element at a position in the column type.
- [subscript(Range<Int>) -> AnyColumnSlice](anycolumnprotocol/subscript(_:)-81v4q.md)
  Retrieves a contiguous subrange of the column type’s elements.

## Relationships

### Conforming Types
- [AnyColumn](anycolumn.md)
- [AnyColumnSlice](anycolumnslice.md)

## See Also

- [struct AnyColumn](anycolumn.md)
  A type-erased column.
- [struct AnyColumnSlice](anycolumnslice.md)
  A type-erased column slice.
- [protocol AnyColumnPrototype](anycolumnprototype.md)
  A prototype that creates type-erased columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumnprotocol)*