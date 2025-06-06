# init(appEntity:priority:)

**Framework**: Core Spotlight  
**Kind**: init

Intializes a new searchable item with the relevant fields populated from the provided app entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
convenience init<Entity>(appEntity: Entity, priority: Int) where Entity : IndexedEntity
```

## Parameters

- `appEntity`: The app entity to use for initialization.
- `priority`: The importance of this item compared to the other donated items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitem/init(appentity:priority:))*