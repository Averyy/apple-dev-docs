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

#### Overview

Use this type to associate a score with a searchable item from the app’s index. You create instances of this type from a [`CustomStage`](customstage.md) when the stage’s output type is [`SearchPipelineDataType.scoredItems`](searchpipelinedatatype/scoreditems.md).

## Topics

### Creating the item
- [init(item: SearchableItem, score: Double)](scoredsearchableitem/init(item:score:).md)
  Initializes the type with the specified item and score values.
### Getting the item details
- [let item: SearchableItem](scoredsearchableitem/item.md)
  The searchable item from the app’s index.
- [let score: Double](scoredsearchableitem/score.md)
  The relevance score for the item.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol CustomStage](customstage.md)
  A custom processing stage the Spotlight search tool uses to identify search results.
- [struct SearchPipelineData](searchpipelinedata.md)
  The type you use to store the output from a custom stage.
- [enum SearchPipelineDataType](searchpipelinedatatype.md)
  Data types that a pipeline stage accepts or produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/scoredsearchableitem)*