# NSEntityMappingType.removeEntityMappingType

**Framework**: Core Data  
**Kind**: case

Specifies that this entity is not present in the destination model.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case removeEntityMappingType
```

#### Discussion

Instances of the entity only exist in the source—source instances are not mapped to destination.

## See Also

- [NSEntityMappingType.undefinedEntityMappingType](nsentitymappingtype/undefinedentitymappingtype.md)
  Specifies that the developer handles destination instance creation.
- [NSEntityMappingType.customEntityMappingType](nsentitymappingtype/customentitymappingtype.md)
  Specifies a custom mapping.
- [NSEntityMappingType.addEntityMappingType](nsentitymappingtype/addentitymappingtype.md)
  Specifies that this is a new entity in the destination model.
- [NSEntityMappingType.copyEntityMappingType](nsentitymappingtype/copyentitymappingtype.md)
  Specifies that source instances are migrated as-is.
- [NSEntityMappingType.transformEntityMappingType](nsentitymappingtype/transformentitymappingtype.md)
  Specifies that entity exists in source and destination and is mapped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitymappingtype/removeentitymappingtype)*