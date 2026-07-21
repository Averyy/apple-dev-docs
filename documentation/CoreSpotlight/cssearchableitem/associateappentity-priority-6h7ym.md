# associateAppEntity(_:priority:)

**Framework**: Core Spotlight  
**Kind**: method

Associates an app entity with this searchable item. Resolves deferred properties before association.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func associateAppEntity(_ appEntity: some IndexedEntity, priority: Int = 0) async
```

## Parameters

- `appEntity`: The app entity that will be associated with this searchable item.
- `priority`: The importance of this item compared to the other donated items.

## See Also

- [func associateAppEntity(some IndexedEntity, priority: Int)](cssearchableitem/associateappentity(_:priority:)-736lx.md)
  Associates an app entity with this searchable item.
- [var relatedAppEntityIdentifier: EntityIdentifier?](cssearchableitem/relatedappentityidentifier.md)
  The identifier of the related indexed entity for this searchable item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitem/associateappentity(_:priority:)-6h7ym)*