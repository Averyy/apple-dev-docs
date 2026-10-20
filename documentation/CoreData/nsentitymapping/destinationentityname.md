# destinationEntityName

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The destination entity name for the entity mapping.

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
var destinationEntityName: String? { get set }
```

```objc
@property (copy, nullable) NSString * destinationEntityName;
```

#### Discussion

Mappings are not directly bound to entity descriptions. You can use the migration manager’s [`destinationEntity(for:)`](../nsmigrationmanager/destinationentity%28for%29.md) method to retrieve the entity description for this entity name.

## See Also

### Related Documentation
- [var sourceEntityName: String?](./sourceentityname.md)
  The source entity name for the entity mapping.
### Managing Destination Information
- [var destinationEntityVersionHash: Data?](./destinationentityversionhash.md)
  The version hash for the destination entity for the entity mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitymapping/destinationentityname)*