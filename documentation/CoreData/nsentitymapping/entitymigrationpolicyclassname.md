# entityMigrationPolicyClassName

**Framework**: Core Data  
**Kind**: property

The class name of the migration policy for the entity mapping.

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
var entityMigrationPolicyClassName: String? { get set }
```

#### Discussion

If not specified, the default migration class name is [`NSEntityMigrationPolicy`](nsentitymigrationpolicy.md). You can specify a subclass to provide custom behavior.

## See Also

- [var name: String!](nsentitymapping/name.md)
  The name of the entity mapping.
- [var mappingType: NSEntityMappingType](nsentitymapping/mappingtype.md)
  The mapping type for the entity mapping.
- [var attributeMappings: [NSPropertyMapping]?](nsentitymapping/attributemappings.md)
  The array of attribute mappings for the entity mapping.
- [var relationshipMappings: [NSPropertyMapping]?](nsentitymapping/relationshipmappings.md)
  The array of relationship mappings for the entity mapping.
- [var userInfo: [AnyHashable : Any]?](nsentitymapping/userinfo.md)
  The user info dictionary for the entity mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitymapping/entitymigrationpolicyclassname)*