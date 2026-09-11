# init(id:)

**Framework**: App Intents  
**Kind**: init

Creates an identifier where the local and stable IDs are identical.

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
init(id: LocalID)
```

#### Discussion

Use this for entities whose identifiers are already stable across devices, such as server-assigned UUIDs or globally unique identifiers.

#### Example

```swift
struct Article: AppEntity, SyncableEntity {
    var id: SyncableEntityIdentifier<UUID, UUID>

    init(id: UUID, title: String) {
        self.id = SyncableEntityIdentifier(id: id)
        self.title = title
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/syncableentityidentifier/init(id:))*