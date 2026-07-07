# reindexEntities(for:indexDescription:)

**Framework**: App Intents  
**Kind**: method  
**Required**: Yes

Reindexes a specific subset of app entities within an index.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func reindexEntities(for identifiers: [Self.Entity.ID], indexDescription: CSSearchableIndexDescription) async throws
```

#### Discussion

The system calls this method when it needs you to reindex only some of the app entities in one of your app’s searchable indexes. In your implementation of this method, use the `identifiers` parameter to fetch the app entities again and donate them to the index.

## Parameters

- `identifiers`: The identifiers of app entities to reindex. Use these identifiers to fetch the entities from your app’s data store.
- `indexDescription`: An object that describes the characteristics of the searchable index. Use the information in this type to determine which of your app’s [`CSSearchableIndex`](https://developer.apple.com/documentation/CoreSpotlight/CSSearchableIndex) instances to update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/indexedentityquery/reindexentities(for:indexdescription:))*