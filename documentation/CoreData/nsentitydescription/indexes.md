# indexes

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

An array of fetch index descriptions for the entity.

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
var indexes: [NSFetchIndexDescription] { get set }
```

```objc
@property (copy) NSArray<NSFetchIndexDescription *> * indexes;
```

## Discussion

This value doesn’t form part of the entity’s version hash, and stores that don’t natively support indexing may ignore it.

> ❗ **Important**:  Set indexes last in a model. Changing an entity hierarchy in any way that affects the validity of indexes drops all existing indexes for entities in that hierarchy, such as adding or removing superentities or subentities, or adding and removing properties anywhere in the hierarchy.

## See Also

### Configuring indexes and constraints
- [var uniquenessConstraints: [[Any]]](./uniquenessconstraints.md)
  An array of arrays that contains one or more attributes with a value that must be unique over the instances of that entity.
- [var compoundIndexes: [[Any]]](./compoundindexes.md)
  The compound indexes for the entity as an array of arrays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitydescription/indexes)*