# AnyColumnPrototype

**Framework**: TabularData  
**Kind**: protocol

A prototype that creates type-erased columns.

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
protocol AnyColumnPrototype
```

## Topics

### Naming a Prototype Column
- [var name: String](anycolumnprototype/name.md)
  The name of the column.
### Creating Columns
- [func makeColumn(capacity: Int) -> AnyColumn](anycolumnprototype/makecolumn(capacity:).md)
  Creates a type-erased column.

## See Also

- [struct AnyColumn](anycolumn.md)
  A type-erased column.
- [struct AnyColumnSlice](anycolumnslice.md)
  A type-erased column slice.
- [protocol AnyColumnProtocol](anycolumnprotocol.md)
  A type that represents a type-erased column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumnprototype)*