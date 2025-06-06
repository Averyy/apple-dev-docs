# destinationEntityName

**Framework**: Core Data  
**Kind**: property

The destination entity name for the entity mapping.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var destinationEntityName: String? { get set }
```

#### Discussion

Mappings are not directly bound to entity descriptions. You can use the migration manager’s [`destinationEntity(for:)`](nsmigrationmanager/destinationentity(for:).md) method to retrieve the entity description for this entity name.

## See Also

- [var sourceEntityName: String?](nsentitymapping/sourceentityname.md)
  The source entity name for the entity mapping.
- [var destinationEntityVersionHash: Data?](nsentitymapping/destinationentityversionhash.md)
  The version hash for the destination entity for the entity mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitymapping/destinationentityname)*