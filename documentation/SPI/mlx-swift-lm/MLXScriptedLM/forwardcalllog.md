---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/forwardcalllog"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# ForwardCallLog

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: class  
**Role**: Class

The calls a [`ScriptedLogitsModel`](./scriptedlogitsmodel.md) has received, safe to read from any thread.

## Declaration

```swift
final class ForwardCallLog
```

## Topics

### Initializers
- [init()](./forwardcalllog/init%28%29.md)
### Instance Properties
- [var calls: [ForwardCall]](./forwardcalllog/calls.md)
- [var inputMismatches: [ForwardCall.InputMismatch]](./forwardcalllog/inputmismatches.md)
### Instance Methods
- [func removeAll()](./forwardcalllog/removeall%28%29.md)

## Relationships

### Conforms To
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
- [struct ForwardCall](./forwardcall.md)
  One call into a [`ScriptedLogitsModel`](./scriptedlogitsmodel.md).
- [class ForwardingLanguageModel](./forwardinglanguagemodel.md)
  A `LanguageModel` that forwards every requirement to a wrapped model.
- [struct ScriptedInputProcessor](./scriptedinputprocessor.md)
  Renders chat input with a tokenizer’s chat template.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/forwardcalllog)*