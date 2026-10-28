# NSEntityMappingType.addEntityMappingType

**Framework**: Core Data  
**Kind**: case  
**Role**: Case

Specifies that this is a new entity in the destination model.

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
case addEntityMappingType
```

```c
NSAddEntityMappingType
```

## Discussion

Instances of the entity only exist in the destination.

## See Also

### Constants
- [NSEntityMappingType.undefinedEntityMappingType](./undefinedentitymappingtype.md)
  Specifies that the developer handles destination instance creation.
- [NSEntityMappingType.customEntityMappingType](./customentitymappingtype.md)
  Specifies a custom mapping.
- [NSEntityMappingType.removeEntityMappingType](./removeentitymappingtype.md)
  Specifies that this entity is not present in the destination model.
- [NSEntityMappingType.copyEntityMappingType](./copyentitymappingtype.md)
  Specifies that source instances are migrated as-is.
- [NSEntityMappingType.transformEntityMappingType](./transformentitymappingtype.md)
  Specifies that entity exists in source and destination and is mapped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitymappingtype/addentitymappingtype)*