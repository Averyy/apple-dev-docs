# property

**Framework**: Core Data  
**Kind**: property

A property description.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var property: NSPropertyDescription? { get }
```

#### Discussion

This property may also be an [`NSExpressionDescription`](nsexpressiondescription.md) that expresses a function.

## See Also

- [var collationType: NSFetchIndexElementType](nsfetchindexelementdescription/collationtype.md)
  The type of collation that the index element uses, either binary or R-tree.
- [var indexDescription: NSFetchIndexDescription?](nsfetchindexelementdescription/indexdescription.md)
- [var isAscending: Bool](nsfetchindexelementdescription/isascending.md)
  A Boolean value that controls whether an index that supports direction is an ascending or descending index.
- [var propertyName: String?](nsfetchindexelementdescription/propertyname.md)
  The specified name in the property description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchindexelementdescription/property)*