# compoundIndexes

**Framework**: Core Data  
**Kind**: property

The compound indexes for the entity as an array of arrays.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var compoundIndexes: [[Any]] { get set }
```

#### Discussion

The arrays contained in the returned array contain instances of `NSAttributeDescription`, `NSRelationshipDescription` that represent properties of the entity, or of `NSString` that match the name of attributes or relationships of the entity.

Compound indexes are only used by stores that natively support compound indices—setting them is only advisory. Indexes apply to the entire inheritance hierarchy.

## See Also

- [var indexes: [NSFetchIndexDescription]](nsentitydescription/indexes.md)
  An array of fetch index descriptions for the entity.
- [var uniquenessConstraints: [[Any]]](nsentitydescription/uniquenessconstraints.md)
  An array of arrays that contains one or more attributes with a value that must be unique over the instances of that entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitydescription/compoundindexes)*