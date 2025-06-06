# deleteAppEntities(identifiedBy:ofType:)

**Framework**: Core Spotlight  
**Kind**: method

Deletes specific app entities from the system’s index.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
func deleteAppEntities<Entity>(identifiedBy identifiers: [Entity.ID], ofType type: Entity.Type) async throws where Entity : IndexedEntity
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindex/deleteappentities(identifiedby:oftype:))*