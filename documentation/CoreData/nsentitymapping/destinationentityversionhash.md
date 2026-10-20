# destinationEntityVersionHash

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The version hash for the destination entity for the entity mapping.

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
var destinationEntityVersionHash: Data? { get set }
```

```objc
@property (copy, nullable) NSData * destinationEntityVersionHash;
```

#### Discussion

The version hash is calculated by Core Data based on the property values of the entity (see `NSEntityDescription`’s [`versionHash`](../nsentitydescription/versionhash.md) method). The `destinationEntityVersionHash` must equal the version hash of the destination entity represented by the mapping.

## See Also

### Related Documentation
- [var sourceEntityVersionHash: Data?](./sourceentityversionhash.md)
  The version hash of the source entity for the entity mapping.
### Managing Destination Information
- [var destinationEntityName: String?](./destinationentityname.md)
  The destination entity name for the entity mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitymapping/destinationentityversionhash)*