# append(_:)

**Framework**: App Intents  
**Kind**: method

Adds the identifier for the specified entity to the collection.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
mutating func append(_ entity: Entity)
```

#### Discussion

- Parameter: - entity: The entity containing the identifier to add.

This method adds the entity’s identifier to the collection, but doesn’t keep a reference to the entity itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entitycollection/append(_:)-yr1u)*