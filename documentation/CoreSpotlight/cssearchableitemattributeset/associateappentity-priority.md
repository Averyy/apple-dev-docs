# associateAppEntity(_:priority:)

**Framework**: Core Spotlight  
**Kind**: method

Associates an app entity with this searchable item.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
func associateAppEntity<Entity>(_ appEntity: Entity, priority: Int = 0) where Entity : IndexedEntity
```

## Parameters

- `appEntity`: The app entity that will be associated with the searchable items attribute set.
- `priority`: The importance of this item compared to the other donated items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/associateappentity(_:priority:))*