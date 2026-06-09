# relatedAppEntityIdentifier

**Framework**: Core Spotlight  
**Kind**: property

The identifier of the related indexed entity for this searchable item.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var relatedAppEntityIdentifier: EntityIdentifier? { get set }
```

#### Discussion

Convenience property that forwards to the item’s attribute set. Use this property to associate a child searchable item such as an attachment or embedded content with its parent `IndexedEntity` instance.

Only an identifier reference is stored. No entity content is embedded in the child item.

Setting this property again replaces the previously set identifier.

## See Also

- [func associateAppEntity(some IndexedEntity, priority: Int) async](cssearchableitem/associateappentity(_:priority:)-6h7ym.md)
  Associates an app entity with this searchable item. Resolves deferred properties before association.
- [func associateAppEntity(some IndexedEntity, priority: Int)](cssearchableitem/associateappentity(_:priority:)-736lx.md)
  Associates an app entity with this searchable item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitem/relatedappentityidentifier)*