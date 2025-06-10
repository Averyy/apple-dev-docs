# ColumnID

**Framework**: TabularData  
**Kind**: struct

A column identifier that stores a column’s name and the type of its elements.

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
struct ColumnID<T>
```

## Topics

### Creating a Column ID
- [init(String, T.Type)](columnid/init(_:_:).md)
  Creates a column identifier.
### Getting the Properties
- [var name: String](columnid/name.md)
  The name of the column the identifier represents.
### Instance Properties
- [var type: any Any.Type](columnid/type.md)
  The type of elements stored in the column the identifier represents.
### Default Implementations
- [CustomStringConvertible Implementations](columnid/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum Order](order.md)
  A type that represents a sort ordering.
- [struct FormattingOptions](formattingoptions.md)
  A set of parameters that indicate how to present the contents of data frame or column types to a printable string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnid)*