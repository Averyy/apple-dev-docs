---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/forwardcall"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# ForwardCall

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: struct  
**Role**: Structure

One call into a [`ScriptedLogitsModel`](./scriptedlogitsmodel.md).

## Declaration

```swift
struct ForwardCall
```

## Topics

### Structures
- [ForwardCall.InputMismatch](./forwardcall/inputmismatch-swift.struct.md)
  Input 0 differed from the token the script called for at that position.
### Instance Properties
- [let cacheOffsetBefore: Int](./forwardcall/cacheoffsetbefore.md)
  The absolute position of input 0: the transcript length before the call.
- [let cursor: TurnScripts.Cursor?](./forwardcall/cursor.md)
  The cursor for the last returned row, if it is inside an assistant turn.
- [let hasInboundState: Bool](./forwardcall/hasinboundstate.md)
- [let inputMismatch: InputMismatch?](./forwardcall/inputmismatch-swift.property.md)
- [let inputTokens: [Int]](./forwardcall/inputtokens.md)
- [let kind: Kind](./forwardcall/kind-swift.property.md)
- [let maskPresent: Bool](./forwardcall/maskpresent.md)
- [let processedTokenCount: Int](./forwardcall/processedtokencount.md)
  Tokens the call added to the cache. Less than `inputTokens.count` when `prepare` leaves a remainder for the iterator.
- [let scriptedTokens: [Int?]](./forwardcall/scriptedtokens.md)
  The boosted token for each returned logits row, or `nil` where the row was left as is.
### Enumerations
- [ForwardCall.Kind](./forwardcall/kind-swift.enum.md)
### Default Implementations
- [Equatable Implementations](./forwardcall/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
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
- [class ForwardingLanguageModel](./forwardinglanguagemodel.md)
  A `LanguageModel` that forwards every requirement to a wrapped model.
- [struct ScriptedInputProcessor](./scriptedinputprocessor.md)
  Renders chat input with a tokenizer’s chat template.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/forwardcall)*