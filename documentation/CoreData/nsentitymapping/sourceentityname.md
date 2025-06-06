# sourceEntityName

**Framework**: Core Data  
**Kind**: property

The source entity name for the entity mapping.

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
var sourceEntityName: String? { get set }
```

#### Discussion

Mappings are not directly bound to entity descriptions; you can use the [`sourceEntity(for:)`](nsmigrationmanager/sourceentity(for:).md) method on the migration manager to retrieve the entity description for this entity name.

## See Also

- [Core Data Model Versioning and Data Migration Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataVersioning/Articles/Introduction.html#//apple_ref/doc/uid/TP40004399)
- [var destinationEntityName: String?](nsentitymapping/destinationentityname.md)
  The destination entity name for the entity mapping.
- [var sourceEntityVersionHash: Data?](nsentitymapping/sourceentityversionhash.md)
  The version hash of the source entity for the entity mapping.
- [var sourceExpression: NSExpression?](nsentitymapping/sourceexpression.md)
  The source expression for the entity mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitymapping/sourceentityname)*