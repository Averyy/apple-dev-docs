# execute(groupedItems:)

**Framework**: Core Spotlight  
**Kind**: method  
**Required**: Yes

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) func execute(groupedItems: [SearchableItemAttribute : [SearchableItem]]) async throws -> SearchPipelineData
```

## See Also

- [func execute(items: [SearchableItem]) async throws -> SearchPipelineData](customstage/execute(items:).md)
- [func execute(scoredItems: [ScoredSearchableItem]) async throws -> SearchPipelineData](customstage/execute(scoreditems:).md)
- [func execute(text: String) async throws -> SearchPipelineData](customstage/execute(text:).md)
- [func execute(count: Int) async throws -> SearchPipelineData](customstage/execute(count:).md)
- [func execute(statisticName: String, value: Double) async throws -> SearchPipelineData](customstage/execute(statisticname:value:).md)
- [func execute(table: SearchResultsTable) async throws -> SearchPipelineData](customstage/execute(table:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/customstage/execute(groupeditems:))*