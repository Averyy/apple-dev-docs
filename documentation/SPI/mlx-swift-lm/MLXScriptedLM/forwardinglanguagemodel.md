---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/forwardinglanguagemodel"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# ForwardingLanguageModel

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: class  
**Role**: Class

A `LanguageModel` that forwards every requirement to a wrapped model.

## Declaration

```swift
class ForwardingLanguageModel
```

## Overview

Subclass it to change one behavior and keep the rest. It implements every `LanguageModel` requirement itself, so a subclass override is always reached and no requirement silently falls back to a protocol default.

As a `Module` it is transparent: parameters, children, updates, and freezing go to the wrapped model with its own keys, not under `wrapped.`. So checkpoint loading, `sanitize(weights:)`, quantization, and LoRA work through the wrapper.

Optional capabilities that the library detects with `as?`:

- `LoRAModel` and `SuppressedTokensProviding` are forwarded.
- `PreparedInputSplitting`, `SpeculativeCacheRewindModel`, and `ModelComponentsProviding` are not: conformance cannot depend on the wrapped model, and conforming with a no-op would change behavior.

## Topics

### Initializers
- [init(wrapping: any LanguageModel)](./forwardinglanguagemodel/init%28wrapping%29.md)
### Instance Properties
- [var excludedCheckpointNamespaces: [String]](./forwardinglanguagemodel/excludedcheckpointnamespaces.md)
- [var loraDefaultKeys: [String]](./forwardinglanguagemodel/loradefaultkeys.md)
- [var loraLayers: [Module]](./forwardinglanguagemodel/loralayers.md)
- [var reasoningConfig: ReasoningConfig?](./forwardinglanguagemodel/reasoningconfig.md)
- [var suppressedTokenIds: Set<Int>](./forwardinglanguagemodel/suppressedtokenids.md)
- [var toolCallFormat: ToolCallFormat?](./forwardinglanguagemodel/toolcallformat.md)
- [let wrapped: any LanguageModel](./forwardinglanguagemodel/wrapped.md)
### Instance Methods
- [func cacheStatus(parameters: GenerateParameters?) throws -> KVCacheStatus](./forwardinglanguagemodel/cachestatus%28parameters%29.md)
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./forwardinglanguagemodel/callasfunction%28_,cache%29.md)
- [func callAsFunction(LMInput.Text, cache: [KVCache]?, state: LMOutput.State?) -> LMOutput](./forwardinglanguagemodel/callasfunction%28_,cache,state%29.md)
- [func didSetTrain(Bool)](./forwardinglanguagemodel/didsettrain%28_%29.md)
  `train(_:)` visits the wrapped model’s children but not the wrapped model itself.
- [func freeze(recursive: Bool, keys: [String]?, strict: Bool) throws](./forwardinglanguagemodel/freeze%28recursive,keys,strict%29.md)
- [func items() -> ModuleItems](./forwardinglanguagemodel/items%28%29.md)
- [func newCache(parameters: GenerateParameters?) throws -> [KVCache]](./forwardinglanguagemodel/newcache%28parameters%29.md)
- [func nextTokenLogits(LMInput.Text, cache: [KVCache]?, state: LMOutput.State?) -> LMOutput](./forwardinglanguagemodel/nexttokenlogits%28_,cache,state%29.md)
- [func noGrad() -> Set<String>](./forwardinglanguagemodel/nograd%28%29.md)
- [func prepare() throws](./forwardinglanguagemodel/prepare%28%29.md)
- [func prepare(LMInput, cache: [KVCache], state: LMOutput.State?, prefill: PrefillParameters) throws -> PrepareResult](./forwardinglanguagemodel/prepare%28_,cache,state,prefill%29.md)
- [func prepareCheckpoint(ModelCheckpoint) throws -> ModelCheckpoint](./forwardinglanguagemodel/preparecheckpoint%28_%29.md)
- [func sanitize(weights: [String : MLXArray]) throws -> [String : MLXArray]](./forwardinglanguagemodel/sanitize%28weights%29.md)
- [func sanitize(weights: [String : MLXArray], metadata: [String : String]) throws -> [String : MLXArray]](./forwardinglanguagemodel/sanitize%28weights,metadata%29.md)
- [func unfreeze(recursive: Bool, keys: [String]?, strict: Bool) throws](./forwardinglanguagemodel/unfreeze%28recursive,keys,strict%29.md)
- [func update(modules: ModuleChildren, verify: VerifyUpdate, path: [String], modulePath: [String]) throws -> Self](./forwardinglanguagemodel/update%28modules,verify,path,modulepath%29.md)
- [func update(parameters: ModuleParameters, verify: VerifyUpdate, path: [String], modulePath: [String]) throws -> Self](./forwardinglanguagemodel/update%28parameters,verify,path,modulepath%29.md)
- [func updateModule(key: String, Any) throws](./forwardinglanguagemodel/updatemodule%28key,_%29.md)
### Default Implementations
- [LanguageModel Implementations](./forwardinglanguagemodel/languagemodel-implementations.md)
- [LoRAModel Implementations](./forwardinglanguagemodel/loramodel-implementations.md)

## Relationships

### Inherits From
- MLXNN.Module
### Inherited By
- [ScriptedLogitsModel](./scriptedlogitsmodel.md)
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
- [struct ScriptedInputProcessor](./scriptedinputprocessor.md)
  Renders chat input with a tokenizer’s chat template.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/forwardinglanguagemodel)*