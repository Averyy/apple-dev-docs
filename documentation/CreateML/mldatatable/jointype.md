# MLDataTable.JoinType

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

Join types available for [`MLDataTable`](../mldatatable.md) join operations.

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
- [MLDataTable.JoinType.inner](./jointype/inner.md)
  An operation that joins the rows of the data tables whose values match exactly.
- [MLDataTable.JoinType.left](./jointype/left.md)
  An operation that is the union between an inner join and the remaining rows from the original data table.
- [MLDataTable.JoinType.right](./jointype/right.md)
  An operation that is the union between an inner join and the remaining rows from the secondary data table.
- [MLDataTable.JoinType.outer](./jointype/outer.md)
  An operation that is the union between a left join and a right join.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Merging data tables
- [func join(with: MLDataTable, on: String..., type: MLDataTable.JoinType) -> MLDataTable](./join%28with,on,type%29.md)
  Creates a new data table by merging two data tables by the given columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/jointype)*