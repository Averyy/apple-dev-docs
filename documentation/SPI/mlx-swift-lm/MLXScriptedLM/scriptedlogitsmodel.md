---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedlogitsmodel"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# ScriptedLogitsModel

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: class  
**Role**: Class

A model that emits scripted tokens by boosting them in a wrapped model’s logits.

## Declaration

```swift
final class ScriptedLogitsModel
```

#### Overview

The wrapped model (usually small with random weights) does the real work: cache updates, prefill chunking, and state. This model only raises the scripted token above each logits row’s maximum, so samplers, processors, and masks still see a realistic distribution.

It appends a [`TranscriptKVCache`](./transcriptkvcache.md) to the wrapped model’s caches, and finds the turn and position from it (see [`TurnScripts`](./turnscripts.md)). Generation trims and copies that entry with the rest of the cache, so the cursor stays right across speculative rejection, prompt cache reuse, and `ChatSession` rebuilds.

Inside a turn where the script has no token, it blocks [`blockedUnscriptedTokens`](./turnscripts/blockedunscriptedtokens.md), so unscripted output cannot end the turn or start the next one.

Reading the input tokens forces evaluation on every call. That is fine for tests but removes the iterator’s overlap of compute and sampling.

## Topics

### Initializers
- [init(wrapping: any LanguageModel, scripts: TurnScripts, margin: Margin)](./scriptedlogitsmodel/init%28wrapping,scripts,margin%29.md)
### Instance Properties
- [let callLog: ForwardCallLog](./scriptedlogitsmodel/calllog.md)
- [let margin: Margin](./scriptedlogitsmodel/margin-swift.property.md)
- [let scripts: TurnScripts](./scriptedlogitsmodel/scripts.md)
### Instance Methods
- [func cacheStatus(parameters: GenerateParameters?) throws -> KVCacheStatus](./scriptedlogitsmodel/cachestatus%28parameters%29.md)
  The status of this model’s own cache, which includes the transcript entry.
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./scriptedlogitsmodel/callasfunction%28_,cache%29.md)
- [func callAsFunction(LMInput.Text, cache: [KVCache]?, state: LMOutput.State?) -> LMOutput](./scriptedlogitsmodel/callasfunction%28_,cache,state%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./scriptedlogitsmodel/newcache%28parameters%29.md)
- [func nextTokenLogits(LMInput.Text, cache: [KVCache]?, state: LMOutput.State?) -> LMOutput](./scriptedlogitsmodel/nexttokenlogits%28_,cache,state%29.md)
- [func prepare(LMInput, cache: [KVCache], state: LMOutput.State?, prefill: PrefillParameters) throws -> PrepareResult](./scriptedlogitsmodel/prepare%28_,cache,state,prefill%29.md)
### Type Methods
- [static func transcript(in: [KVCache]) -> [Int]?](./scriptedlogitsmodel/transcript%28in%29.md)
  The tokens recorded in `cache`, or `nil` if it has no [`TranscriptKVCache`](./transcriptkvcache.md).
### Enumerations
- [ScriptedLogitsModel.Margin](./scriptedlogitsmodel/margin-swift.enum.md)
  How far above a row’s maximum the scripted token goes.

## Relationships

### Inherits From
- [ForwardingLanguageModel](./forwardinglanguagemodel.md)
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- MLXLMCommon.BaseLanguageModel
- MLXLMCommon.ChatConventionsProviding
- MLXLMCommon.LanguageModel
- MLXLMCommon.LoRAModel
- MLXLMCommon.SuppressedTokensProviding
- Swift.CustomStringConvertible
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Scripted Models
- [struct ScriptedScenario](./scriptedscenario.md)
  A transcript, a tokenizer built from it, and a model that follows it.
- [struct Transcript](./transcript.md)
  A conversation to script: what the user says and what the model replies.
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedlogitsmodel)*