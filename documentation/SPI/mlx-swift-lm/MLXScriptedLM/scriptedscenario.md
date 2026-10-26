---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedscenario"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# ScriptedScenario

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: struct  
**Role**: Structure

A transcript, a tokenizer built from it, and a model that follows it.

## Declaration

```swift
struct ScriptedScenario
```

#### Overview

```swift
// @_spi(Testing) import MLXLLM
let scenario = try ScriptedScenario(
    transcript: Transcript([.user("hello"), .assistant("hi there")])
) { vocabularySize in
    Gemma3TextModel(.smallConfiguration(vocabularySize: vocabularySize))
}
let session = ChatSession(scenario.context)
let reply = try await session.respond(to: "hello")  // "hi there"
```

## Topics

### Initializers
- [init(transcript: Transcript, template: any ScriptedChatTemplate, margin: ScriptedLogitsModel.Margin, configuration: ModelConfiguration, innerModel: (_ vocabularySize: Int) throws -> any LanguageModel) throws](./scriptedscenario/init%28transcript,template,margin,configuration,innermodel%29.md)
### Instance Properties
- [let context: ModelContext](./scriptedscenario/context.md)
- [let model: ScriptedLogitsModel](./scriptedscenario/model.md)
- [let tokenizer: ScriptedTokenizer](./scriptedscenario/tokenizer.md)
- [let transcript: Transcript](./scriptedscenario/transcript.md)

## See Also

### Scripted Models
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
- [struct ScriptedInputProcessor](./scriptedinputprocessor.md)
  Renders chat input with a tokenizer’s chat template.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedscenario)*