# LanguageModelExecutorGenerationChannel.Reasoning.Action

**Framework**: Foundation Models  
**Kind**: struct

An operation that can be performed on a reasoning entry.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Action
```

#### Overview

`Action` is an enum-like struct; construct one with a leading-dot factory such as [`appendText(_:segmentID:tokenCount:)`](languagemodelexecutorgenerationchannel/reasoning/action-swift.struct/appendtext(_:segmentid:tokencount:).md).

## Topics

### Reasoning actions
- [static func appendText(String, segmentID: String?, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Reasoning.Action](languagemodelexecutorgenerationchannel/reasoning/action-swift.struct/appendtext(_:segmentid:tokencount:).md)
- [static func replaceTextSegment(String, segmentID: String?, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Reasoning.Action](languagemodelexecutorgenerationchannel/reasoning/action-swift.struct/replacetextsegment(_:segmentid:tokencount:).md)
- [static func updateMetadata([String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.Reasoning.Action](languagemodelexecutorgenerationchannel/reasoning/action-swift.struct/updatemetadata(_:).md)
- [static func updateSignature(Data, tokenCount: Int) -> LanguageModelExecutorGenerationChannel.Reasoning.Action](languagemodelexecutorgenerationchannel/reasoning/action-swift.struct/updatesignature(_:tokencount:).md)
- [static func updateUsage(input: LanguageModelExecutorGenerationChannel.Usage.Input, output: LanguageModelExecutorGenerationChannel.Usage.Output, metadata: [String : any ConvertibleToGeneratedContent]) -> LanguageModelExecutorGenerationChannel.Reasoning.Action](languagemodelexecutorgenerationchannel/reasoning/action-swift.struct/updateusage(input:output:metadata:).md)

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var action: LanguageModelExecutorGenerationChannel.Reasoning.Action](languagemodelexecutorgenerationchannel/reasoning/action-swift.property.md)
  The action to perform.
- [var entryID: String?](languagemodelexecutorgenerationchannel/reasoning/entryid.md)
  The identifier for the entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/reasoning/action-swift.struct)*