# NSEntityMappingType.removeEntityMappingType

**Framework**: Core Data  
**Kind**: case  
**Role**: Case

Specifies that this entity is not present in the destination model.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case removeEntityMappingType
```

```c
NSRemoveEntityMappingType
```

## Discussion

Instances of the entity only exist in the source—source instances are not mapped to destination.

## See Also

### Constants
- [NSEntityMappingType.undefinedEntityMappingType](./undefinedentitymappingtype.md)
  Specifies that the developer handles destination instance creation.
- [NSEntityMappingType.customEntityMappingType](./customentitymappingtype.md)
  Specifies a custom mapping.
- [NSEntityMappingType.addEntityMappingType](./addentitymappingtype.md)
  Specifies that this is a new entity in the destination model.
- [NSEntityMappingType.copyEntityMappingType](./copyentitymappingtype.md)
  Specifies that source instances are migrated as-is.
- [NSEntityMappingType.transformEntityMappingType](./transformentitymappingtype.md)
  Specifies that entity exists in source and destination and is mapped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitymappingtype/removeentitymappingtype)*