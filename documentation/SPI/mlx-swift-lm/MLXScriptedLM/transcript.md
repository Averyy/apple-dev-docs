---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/transcript"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# Transcript

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: struct  
**Role**: Structure

A conversation to script: what the user says and what the model replies.

## Declaration

```swift
struct Transcript
```

#### Overview

Write it as an array in code, or load it from JSON:

```json
{
  "turns": [
    { "system": "Be brief." },
    { "user": "hello" },
    { "assistant": "hi there" },
    { "user": "count" },
    { "assistant": { "text": "one two three", "terminator": "none" } }
  ]
}
```

## Topics

### Structures
- [Transcript.Assistant](./transcript/assistant.md)
### Initializers
- [init([Turn])](./transcript/init%28_%29.md)
- [init(contentsOf: URL) throws](./transcript/init%28contentsof%29.md)
- [init(from: any Decoder) throws](./transcript/init%28from%29.md)
### Instance Properties
- [var assistantTurns: [Assistant]](./transcript/assistantturns.md)
- [var corpus: [String]](./transcript/corpus.md)
  All the text in the transcript, for building a tokenizer’s vocabulary.
- [var turns: [Turn]](./transcript/turns.md)
- [var userMessages: [String]](./transcript/usermessages.md)
### Instance Methods
- [func scripts(tokenizer: any Tokenizer) -> [[Int]]](./transcript/scripts%28tokenizer%29.md)
  The tokens each assistant turn emits: its text, then EOS if it has one.
### Enumerations
- [Transcript.Terminator](./transcript/terminator.md)
  What ends an assistant turn’s script.
- [Transcript.Turn](./transcript/turn.md)
### Default Implementations
- [Encodable Implementations](./transcript/encodable-implementations.md)
- [Equatable Implementations](./transcript/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Scripted Models
- [struct ScriptedScenario](./scriptedscenario.md)
  A transcript, a tokenizer built from it, and a model that follows it.
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/transcript)*