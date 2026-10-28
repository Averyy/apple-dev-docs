# sourceEntityVersionHash

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The version hash of the source entity for the entity mapping.

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
var sourceEntityVersionHash: Data? { get set }
```

```objc
@property (copy, nullable) NSData * sourceEntityVersionHash;
```

## Discussion

The version hash is calculated by Core Data based on the property values of the entity (see `NSEntityDescription`’s [`versionHash`](../nsentitydescription/versionhash.md) method). The `sourceEntityVersionHash` must equal the version hash of the source entity represented by the mapping.

## See Also

### Related Documentation
- [var destinationEntityVersionHash: Data?](./destinationentityversionhash.md)
  The version hash for the destination entity for the entity mapping.
### Managing Source Information
- [var sourceEntityName: String?](./sourceentityname.md)
  The source entity name for the entity mapping.
- [var sourceExpression: NSExpression?](./sourceexpression.md)
  The source expression for the entity mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitymapping/sourceentityversionhash)*