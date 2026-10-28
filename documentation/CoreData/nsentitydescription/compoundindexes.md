# compoundIndexes

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The compound indexes for the entity as an array of arrays.

**Availability**:
- iOS 3.0+ - Deprecated in 11.0
- iPadOS 3.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.5+ - Deprecated in 10.13
- tvOS 9.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 4.0

> **Deprecated**: Use NSEntityDescription.indexes instead

## Declaration

```swift
var compoundIndexes: [[Any]] { get set }
```

```objc
@property (strong) NSArray<NSArray<id> *> * compoundIndexes;
```

## Discussion

The arrays contained in the returned array contain instances of `NSAttributeDescription`, `NSRelationshipDescription` that represent properties of the entity, or of `NSString` that match the name of attributes or relationships of the entity.

Compound indexes are only used by stores that natively support compound indices—setting them is only advisory. Indexes apply to the entire inheritance hierarchy.

## See Also

### Configuring indexes and constraints
- [var indexes: [NSFetchIndexDescription]](./indexes.md)
  An array of fetch index descriptions for the entity.
- [var uniquenessConstraints: [[Any]]](./uniquenessconstraints.md)
  An array of arrays that contains one or more attributes with a value that must be unique over the instances of that entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitydescription/compoundindexes)*