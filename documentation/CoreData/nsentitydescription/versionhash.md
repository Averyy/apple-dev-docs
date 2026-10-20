# versionHash

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The version hash for the receiver.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var versionHash: Data { get }
```

```objc
@property (copy, readonly) NSData * versionHash;
```

#### Discussion

The version hash is used to uniquely identify an entity based on the collection and configuration of properties for the entity. The version hash uses only values which affect the persistence of data and the user-defined [`versionHashModifier`](./versionhashmodifier.md) value. (The values which affect persistence are: the name of the entity, the version hash of the superentity (if present), if the entity is abstract, and all of the version hashes for the properties.) This value is stored as part of the version information in the metadata for stores which use this entity, as well as a definition of an entity involved in an [`NSEntityMapping`](../nsentitymapping.md) object.

## See Also

### Managing versioning
- [var versionHashModifier: String?](./versionhashmodifier.md)
  The version hash modifier for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitydescription/versionhash)*