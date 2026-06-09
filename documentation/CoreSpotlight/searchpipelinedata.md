# SearchPipelineData

**Framework**: Core Spotlight  
**Kind**: struct

The value that flows between pipeline stages, carrying a typed payload.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct SearchPipelineData
```

## Topics

### Configuring the pipeline data
- [init(payload: SearchPipelineData.Payload)](searchpipelinedata/init(payload:).md)
- [static func items([CSSearchableItem]) -> SearchPipelineData](searchpipelinedata/items(_:).md)
- [static func scoredItems([ScoredSearchableItem]) -> SearchPipelineData](searchpipelinedata/scoreditems(_:).md)
- [static func groupedItems([SearchableItemAttribute : [CSSearchableItem]]) -> SearchPipelineData](searchpipelinedata/groupeditems(_:).md)
- [static func text(String) -> SearchPipelineData](searchpipelinedata/text(_:).md)
- [static func count(Int) -> SearchPipelineData](searchpipelinedata/count(_:).md)
- [static func statistic(name: String, value: Double) -> SearchPipelineData](searchpipelinedata/statistic(name:value:).md)
- [static func table(SearchResultsTable) -> SearchPipelineData](searchpipelinedata/table(_:).md)
### Getting the pipeline data
- [let payload: SearchPipelineData.Payload](searchpipelinedata/payload-swift.property.md)
  The result payload produced by a stage.
- [SearchPipelineData.Payload](searchpipelinedata/payload-swift.enum.md)
  The typed variants of data a pipeline stage can produce or consume.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol CustomStage](customstage.md)
  A custom processing stage in a Spotlight search pipeline.
- [enum SearchPipelineDataType](searchpipelinedatatype.md)
  Declares the kind of data a pipeline stage accepts or produces.
- [struct ScoredSearchableItem](scoredsearchableitem.md)
  A searchable item paired with a caller-assigned relevance score.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/searchpipelinedata)*