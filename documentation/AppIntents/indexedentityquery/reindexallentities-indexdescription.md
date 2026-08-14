# reindexAllEntities(indexDescription:)

**Framework**: App Intents  
**Kind**: method  
**Required**: Yes

Reindexes all entities in the app index with the specified characteristics.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func reindexAllEntities(indexDescription: CSSearchableIndexDescription) async throws
```

#### Discussion

- Parameter: - indexDescription: An object that describes the characteristics of the searchable index. Use the information in this type to determine which of your app’s [`CSSearchableIndex`](https://developer.apple.com/documentation/corespotlight/cssearchableindex) instances to update.

The system calls this method when it needs you to reindex all app entities in one of your app’s searchable indexes. In your implementation of this method, fetch all entities and donate them again to your index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/indexedentityquery/reindexallentities(indexdescription:))*