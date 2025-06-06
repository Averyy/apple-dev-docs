# mappingType

**Framework**: Core Data  
**Kind**: property

The mapping type for the entity mapping.

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
var mappingType: NSEntityMappingType { get set }
```

#### Discussion

If you specify a custom entity mapping type, you must specify a value for the migration policy class name as well (see [`entityMigrationPolicyClassName`](nsentitymapping/entitymigrationpolicyclassname.md)).

## See Also

- [var name: String!](nsentitymapping/name.md)
  The name of the entity mapping.
- [var entityMigrationPolicyClassName: String?](nsentitymapping/entitymigrationpolicyclassname.md)
  The class name of the migration policy for the entity mapping.
- [var attributeMappings: [NSPropertyMapping]?](nsentitymapping/attributemappings.md)
  The array of attribute mappings for the entity mapping.
- [var relationshipMappings: [NSPropertyMapping]?](nsentitymapping/relationshipmappings.md)
  The array of relationship mappings for the entity mapping.
- [var userInfo: [AnyHashable : Any]?](nsentitymapping/userinfo.md)
  The user info dictionary for the entity mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitymapping/mappingtype)*