# MLDataTable.JoinType.right

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

An operation that is the union between an inner join and the remaining rows from the secondary data table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
case right
```

## Discussion

The `.right` join type merges missing values.

## See Also

### Selecting a joining operation
- [MLDataTable.JoinType.inner](./inner.md)
  An operation that joins the rows of the data tables whose values match exactly.
- [MLDataTable.JoinType.left](./left.md)
  An operation that is the union between an inner join and the remaining rows from the original data table.
- [MLDataTable.JoinType.outer](./outer.md)
  An operation that is the union between a left join and a right join.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/jointype/right)*