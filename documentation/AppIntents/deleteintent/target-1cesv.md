# target

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The entities to delete.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
var target: Self.Target { get }
```

## Discussion

Implement either this parameter or [`entities`](./entities.md), not both. Declare it as an array or set of entities, or as an [`EntityCollection`](../entitycollection.md) to receive the entity identifiers without resolving each one to an entity, which saves time and memory when someone deletes many entities at once:

```swift
struct DeleteNotesIntent: DeleteIntent {
    static let title: LocalizedStringResource = "Delete Notes"

    @Parameter(title: "Notes")
    var target: EntityCollection<NoteEntity>

    func perform() async throws -> some IntentResult {
        try await NoteStore.shared.delete(target.identifiers)
        return .result()
    }
}
```

When `target` is an array or a set, the default implementation of [`entities`](./entities.md) returns its entities. When it’s an [`EntityCollection`](../entitycollection.md), which only guarantees entity identifiers, the default implementation returns an empty array; read the identifiers from `target` instead.

## Default Implementations

### DeleteIntent Implementations
- [var target: Self.Target](./target-5b0ss.md)
  The entities to delete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/deleteintent/target-1cesv)*