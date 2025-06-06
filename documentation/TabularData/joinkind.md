# JoinKind

**Framework**: TabularData  
**Kind**: enum

An operation type that joins two data frame types.

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
enum JoinKind
```

## Topics

### Operators
- [static func == (JoinKind, JoinKind) -> Bool](joinkind/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [JoinKind.full](joinkind/full.md)
  A join kind that contains every row from both data frame types.
- [JoinKind.inner](joinkind/inner.md)
  A join kind that only contains rows with matching values in both data frame types.
- [JoinKind.left](joinkind/left.md)
  A join kind that contains all rows from the left data frame type, and only the rows with matching values from the right data frame type.
- [JoinKind.right](joinkind/right.md)
  A join kind that contains all rows from the right data frame type, and only the rows with matching values from the left data frame type.
### Instance Properties
- [var hashValue: Int](joinkind/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](joinkind/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](joinkind/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func joined<R>(R, on: String, kind: JoinKind) -> DataFrame](dataframeprotocol/joined(_:on:kind:)-1gp6k.md)
  Generates a data frame by joining with another data frame type with a common column you select by name.
- [func joined<R>(R, on: (left: String, right: String), kind: JoinKind) -> DataFrame](dataframeprotocol/joined(_:on:kind:)-7u2tw.md)
  Generates a data frame by joining with another data frame type along the columns that you select by name for both data frame types.
- [func joined<R, T>(R, on: (left: ColumnID<T>, right: ColumnID<T>), kind: JoinKind) -> DataFrame](dataframeprotocol/joined(_:on:kind:)-9629e.md)
  Generates a data frame by joining with another data frame type along the columns that you select by identifier for both data frame types.
- [func joined<R, T>(R, on: ColumnID<T>, kind: JoinKind) -> DataFrame](dataframeprotocol/joined(_:on:kind:)-mvic.md)
  Generates a data frame by joining with another data frame type with a common column that you select by identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/joinkind)*