# deleteAppEntities(ofType:)

**Framework**: Core Spotlight  
**Kind**: method

Deletes all app entities of the given type from the system indices.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
func deleteAppEntities<Entity>(ofType entityType: Entity.Type) async throws where Entity : IndexedEntity
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindex/deleteappentities(oftype:))*