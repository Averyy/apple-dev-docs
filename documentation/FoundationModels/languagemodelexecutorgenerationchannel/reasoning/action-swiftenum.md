# LanguageModelExecutorGenerationChannel.Reasoning.Action

**Framework**: Foundation Models  
**Kind**: enum

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum Action
```

## Topics

### Reasoning action cases
- [LanguageModelExecutorGenerationChannel.Reasoning.Action.appendText(_:)](languagemodelexecutorgenerationchannel/reasoning/action-swift.enum/appendtext(_:).md)
- [case replaceTextSegment(LanguageModelExecutorGenerationChannel.TextSegmentReplacement)](languagemodelexecutorgenerationchannel/reasoning/action-swift.enum/replacetextsegment(_:).md)
- [LanguageModelExecutorGenerationChannel.Reasoning.Action.updateMetadata(_:)](languagemodelexecutorgenerationchannel/reasoning/action-swift.enum/updatemetadata(_:)-swift.enum.case.md)
- [case updateSignature(LanguageModelExecutorGenerationChannel.ReasoningSignature)](languagemodelexecutorgenerationchannel/reasoning/action-swift.enum/updatesignature(_:).md)
- [LanguageModelExecutorGenerationChannel.Reasoning.Action.updateUsage(_:)](languagemodelexecutorgenerationchannel/reasoning/action-swift.enum/updateusage(_:).md)
### Reasoning action constants
- [static func appendText(String, segmentID: String?, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Reasoning.Action](languagemodelexecutorgenerationchannel/reasoning/action-swift.enum/appendtext(_:segmentid:tokencount:).md)
- [static func replaceTextSegment(String, segmentID: String?, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Reasoning.Action](languagemodelexecutorgenerationchannel/reasoning/action-swift.enum/replacetextsegment(_:segmentid:tokencount:).md)
- [static func updateMetadata([String : any Sendable & Codable & Equatable]) -> LanguageModelExecutorGenerationChannel.Reasoning.Action](languagemodelexecutorgenerationchannel/reasoning/action-swift.enum/updatemetadata(_:)-swift.type.method.md)
- [static func updateSignature(Data, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Reasoning.Action](languagemodelexecutorgenerationchannel/reasoning/action-swift.enum/updatesignature(_:tokencount:).md)
- [static func updateUsage(input: LanguageModelExecutorGenerationChannel.Usage.Input, output: LanguageModelExecutorGenerationChannel.Usage.Output) -> LanguageModelExecutorGenerationChannel.Reasoning.Action](languagemodelexecutorgenerationchannel/reasoning/action-swift.enum/updateusage(input:output:).md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var action: LanguageModelExecutorGenerationChannel.Reasoning.Action](languagemodelexecutorgenerationchannel/reasoning/action-swift.property.md)
  The action to perform.
- [var entryID: String?](languagemodelexecutorgenerationchannel/reasoning/entryid.md)
  The identifier for the entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/reasoning/action-swift.enum)*