# init(id:)

**Framework**: App Intents  
**Kind**: init

Creates an identifier where the local and stable IDs are identical.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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