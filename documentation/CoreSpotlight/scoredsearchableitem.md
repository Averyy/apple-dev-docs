# ScoredSearchableItem

**Framework**: Core Spotlight  
**Kind**: struct

A searchable item paired with a caller-assigned relevance score.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ScoredSearchableItem
```

## Mentions

- [Making your indexed content available to Foundation Models](making-your-indexed-content-available-to-foundation-models.md)

## Topics

### Creating the item
- [init(item: SearchableItem, score: Double)](scoredsearchableitem/init(item:score:).md)
### Getting the item details
- [let item: SearchableItem](scoredsearchableitem/item.md)
  The underlying searchable item.
- [let score: Double](scoredsearchableitem/score.md)
  A relevance score assigned by the pipeline stage; higher values indicate greater relevance. The scale is stage-defined.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol CustomStage](customstage.md)
  A custom processing stage in a Spotlight search pipeline.
- [struct SearchPipelineData](searchpipelinedata.md)
  The value that flows between pipeline stages, carrying a typed payload.
- [enum SearchPipelineDataType](searchpipelinedatatype.md)
  Declares the kind of data a pipeline stage accepts or produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/scoredsearchableitem)*