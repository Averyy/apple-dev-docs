# MLDataTable.JoinType

**Framework**: Create ML  
**Kind**: enum

Join types available for [`MLDataTable`](mldatatable.md) join operations.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum JoinType
```

## Topics

### Selecting a joining operation
- [MLDataTable.JoinType.inner](mldatatable/jointype/inner.md)
  An operation that joins the rows of the data tables whose values match exactly.
- [MLDataTable.JoinType.left](mldatatable/jointype/left.md)
  An operation that is the union between an inner join and the remaining rows from the original data table.
- [MLDataTable.JoinType.right](mldatatable/jointype/right.md)
  An operation that is the union between an inner join and the remaining rows from the secondary data table.
- [MLDataTable.JoinType.outer](mldatatable/jointype/outer.md)
  An operation that is the union between a left join and a right join.
### Describing a joining operation
- [var hashValue: Int](mldatatable/jointype/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](mldatatable/jointype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Comparing joining operations
- [static func == (MLDataTable.JoinType, MLDataTable.JoinType) -> Bool](mldatatable/jointype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](mldatatable/jointype/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Default Implementations
- [Equatable Implementations](mldatatable/jointype/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func join(with: MLDataTable, on: String..., type: MLDataTable.JoinType) -> MLDataTable](mldatatable/join(with:on:type:).md)
  Creates a new data table by merging two data tables by the given columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/jointype)*