---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedinputprocessor"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# ScriptedInputProcessor

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: struct  
**Role**: Structure

Renders chat input with a tokenizer’s chat template.

## Declaration

```swift
struct ScriptedInputProcessor
```

## Topics

### Initializers
- [init(tokenizer: any Tokenizer, messageGenerator: any MessageGenerator)](./scriptedinputprocessor/init%28tokenizer,messagegenerator%29.md)
### Instance Properties
- [let messageGenerator: any MessageGenerator](./scriptedinputprocessor/messagegenerator.md)
- [let tokenizer: any Tokenizer](./scriptedinputprocessor/tokenizer.md)
### Instance Methods
- [func prepare(input: UserInput) throws -> LMInput](./scriptedinputprocessor/prepare%28input%29.md)

## Relationships

### Conforms To
- MLXLMCommon.UserInputProcessor
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Scripted Models
- [struct ScriptedScenario](./scriptedscenario.md)
  A transcript, a tokenizer built from it, and a model that follows it.
- [struct Transcript](./transcript.md)
  A conversation to script: what the user says and what the model replies.
- [class ScriptedLogitsModel](./scriptedlogitsmodel.md)
  A model that emits scripted tokens by boosting them in a wrapped model’s logits.
- [struct TurnScripts](./turnscripts.md)
  The tokens a scripted model emits on each assistant turn, and how it finds the turn.
- [class ForwardCallLog](./forwardcalllog.md)
  The calls a [`ScriptedLogitsModel`](./scriptedlogitsmodel.md) has received, safe to read from any thread.
- [struct ForwardCall](./forwardcall.md)
  One call into a [`ScriptedLogitsModel`](./scriptedlogitsmodel.md).
- [class ForwardingLanguageModel](./forwardinglanguagemodel.md)
  A `LanguageModel` that forwards every requirement to a wrapped model.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedinputprocessor)*