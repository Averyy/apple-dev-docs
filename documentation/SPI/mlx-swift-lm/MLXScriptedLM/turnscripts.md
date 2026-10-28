---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/turnscripts"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# TurnScripts

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: struct  
**Role**: Structure

The tokens a scripted model emits on each assistant turn, and how it finds the turn.

## Declaration

```swift
struct TurnScripts
```

## Overview

A turn starts after each occurrence of [`turnMarker`](./turnscripts/turnmarker.md) (the template’s generation prompt, such as `<|assistant|>`). Within a turn the script is indexed by position, not content: the token after position `start + k` is `script[k + 1]`, whatever the input. So a wrong speculative draft does not move the cursor, and a model with a different script (a draft model) keeps following its own.

Each new turn is the one after the previous turn, unless the prompt ends with one of [`promptEndings`](./turnscripts/promptendings.md). `ChatSession` drops an empty, cancelled, or rejected turn together with the user message before it, so order alone would replay the dropped turn’s script. When several turns match, the first one at or after the next turn wins, otherwise the last one.

A turn past the last script emits [`endOfSequence`](./turnscripts/endofsequence.md) (or a stop token), so an extra turn ends at once with an empty reply instead of running to `maxTokens`.

A marker inside the current turn starts a new turn, unless the script itself has the marker at that position. That handles history that renders a turn shorter than its script (reasoning stripped, for example) and scripts that contain the marker.

## Topics

### Structures
- [TurnScripts.Cursor](./turnscripts/cursor.md)
  Where the next token comes from: `scripts[turn][index]`. An `index` equal to the script’s length means the script is used up.
### Initializers
- [init(scripts: [[Int]], turnMarker: [Int], promptEndings: [[Int]?]?, endOfSequence: Int?, stopTokens: Set<Int>)](./turnscripts/init%28scripts,turnmarker,promptendings,endofsequence,stoptokens%29.md)
- [init(transcript: Transcript, tokenizer: ScriptedTokenizer, stopTokens: Set<Int>) throws](./turnscripts/init%28transcript,tokenizer,stoptokens%29.md)
  Initialize the TurnScripts.
### Instance Properties
- [var blockedUnscriptedTokens: Set<Int>](./turnscripts/blockedunscriptedtokens.md)
  Tokens the model must not emit inside a turn where the script has no token: the stop tokens and the first marker token. Either one would end the turn early or start the next one. Stop strings are not covered.
- [let endOfSequence: Int?](./turnscripts/endofsequence.md)
  The end-of-sequence token. A turn whose script ends with it, or with a stop token, is over after the script.
- [let promptEndings: [[Int]?]](./turnscripts/promptendings.md)
  For each script, the tokens that end its prompt (the user message and the generation prompt), or `nil` to place the turn by order alone.
- [let scripts: [[Int]]](./turnscripts/scripts.md)
  The tokens each assistant turn emits, in order.
- [let stopTokens: Set<Int>](./turnscripts/stoptokens.md)
  Other token ids that stop generation, such as a model configuration’s `eosTokenIds`.
- [let turnMarker: [Int]](./turnscripts/turnmarker.md)
  The tokens that open an assistant turn.
### Instance Methods
- [func cursors(for: [Int]) -> [Cursor?]](./turnscripts/cursors%28for%29.md)
  For each position in `tokens`, the cursor for the token that follows it, or `nil` outside an assistant turn.
- [func token(at: Cursor) -> Int?](./turnscripts/token%28at%29.md)
  The scripted token at `cursor`, or `nil` when the turn has no script or it is used up.
### Default Implementations
- [Equatable Implementations](./turnscripts/equatable-implementations.md)

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
- [class ForwardCallLog](./forwardcalllog.md)
  The calls a [`ScriptedLogitsModel`](./scriptedlogitsmodel.md) has received, safe to read from any thread.
- [struct ForwardCall](./forwardcall.md)
  One call into a [`ScriptedLogitsModel`](./scriptedlogitsmodel.md).
- [class ForwardingLanguageModel](./forwardinglanguagemodel.md)
  A `LanguageModel` that forwards every requirement to a wrapped model.
- [struct ScriptedInputProcessor](./scriptedinputprocessor.md)
  Renders chat input with a tokenizer’s chat template.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/turnscripts)*