# relatedAppEntityIdentifier

**Framework**: Core Spotlight  
**Kind**: property

The identifier of the related indexed entity for this searchable item’s attribute set.

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

Use this property to associate a child searchable item such as an attachment or embedded content with its parent `IndexedEntity` instance.

Only an identifier reference is stored. No entity content is embedded in the child item.

Setting this property again replaces the previously set identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/relatedappentityidentifier)*