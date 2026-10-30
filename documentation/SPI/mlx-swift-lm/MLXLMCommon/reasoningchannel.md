---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningchannel"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ReasoningChannel

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

The labeled-channel shape of a reasoning protocol: the start delimiter opens a *channel* whose role is named by a short label that follows it, and one shared end delimiter closes every channel whatever its role.

## Declaration

```swift
struct ReasoningChannel
```

## Overview

Gemma 4 is the family that needs this. Its delimiters are real special tokens (`soc_token` id 100 `<|channel>`, `eoc_token` id 101 `<channel|>`) and the reasoning span is named by the label:

```
<|channel>thought\n ... <channel|>the answer
```

A plain [`ReasoningConfig`](./reasoningconfig.md) (start/end delimiter pair) cannot express that. A pair anchored on `<|channel>` emits `thought` as the first word of the thinking; a pair anchored on `<|channel>thought\n` stops matching the moment the label is anything else, leaking the raw opener into the answer.

## Topics

### Initializers
- [init(labelTerminator: String, responseLabels: Set<String>, maxLabelLength: Int)](./reasoningchannel/init%28labelterminator,responselabels,maxlabellength%29.md)
### Instance Properties
- [var labelTerminator: String](./reasoningchannel/labelterminator.md)
  Ends the role label that follows the start delimiter (Gemma 4: a newline).
- [var maxLabelLength: Int](./reasoningchannel/maxlabellength.md)
  How far past the start delimiter a label may run before the opener counts as malformed and its text is shown as reasoning instead of consumed as metadata.
- [var responseLabels: Set<String>](./reasoningchannel/responselabels.md)
  Labels whose channel carries the answer rather than reasoning.
### Type Properties
- [static let gemma4: ReasoningChannel](./reasoningchannel/gemma4.md)
  Gemma 4: `<|channel>thought\n ... <channel|>` carries reasoning.
### Default Implementations
- [Equatable Implementations](./reasoningchannel/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningchannel)*