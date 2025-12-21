# init(for:identifier:)

**Framework**: App Intents  
**Kind**: init

Creates an `EntityIdentifier` representing an instance of the specified entity type backed by the specified identifier value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
init<Entity>(for entityType: Entity.Type, identifier: Entity.ID) where Entity : AppEntity
```

## See Also

- [init<Entity>(for: Entity)](entityidentifier/init(for:).md)
  Creates an identifier for the specified entity
- [init?(activityIdentifier: String)](entityidentifier/init(activityidentifier:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityidentifier/init(for:identifier:))*