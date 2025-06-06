# init(for:)

**Framework**: App Intents  
**Kind**: init

Creates an identifier for the specified entity

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init<Entity>(for entity: Entity) where Entity : AppEntity
```

## See Also

- [init<Entity>(for: Entity.Type, identifier: Entity.ID)](entityidentifier/init(for:identifier:).md)
  Creates an `EntityIdentifier` representing an instance of the specified entity type backed by the specified identifier value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityidentifier/init(for:))*