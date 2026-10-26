---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# MLXScriptedLM

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: module  
**Role**: Framework

Deterministic stand-ins for tokenizers and language models, so code built on mlx-swift-lm can run without downloaded weights.

#### Overview

Code that drives `ChatSession` or the generation APIs is hard to test against a real model: weights are large, output varies, and the interesting cases (a tool call, a reasoning block, a stop string) happen only when the model chooses them. This library provides pieces you control instead.

- **[`ScriptedTokenizer`](./scriptedtokenizer.md)**: A tokenizer built from your test’s own text. Encoding is deterministic and lossless, so text survives the decode and re-encode that `ChatSession` performs on each turn.
- **[`PseudoWordTokenizer`](./pseudowordtokenizer.md)**: A tokenizer for random-weight models. Every id decodes to a word, and there is no end-of-sequence token, so generation runs until `maxTokens`.
- **[`ScriptedChatTemplate`](./scriptedchattemplate.md)**: The chat template protocol. [`MinimalChatTemplate`](./minimalchattemplate.md) keeps prompts short and readable; [`ChatMLTemplate`](./chatmltemplate.md) renders plain ChatML.
- **[`Transcript`](./transcript.md)**: The conversation to script, written in code or loaded from JSON.
- **[`ScriptedLogitsModel`](./scriptedlogitsmodel.md)**: Wraps a small random-weight model and boosts the scripted token in its logits, so generation follows the transcript while the cache, samplers, and processors stay real.
- **[`ScriptedScenario`](./scriptedscenario.md)**: Builds the tokenizer, model, and `ModelContext` from a transcript.

```swift
import MLXScriptedLM

let tokenizer = ScriptedTokenizer(
    corpus: ["how are you?", "fine, you?"],
    template: ChatMLTemplate())

let prompt = try tokenizer.applyChatTemplate(
    messages: [["role": "user", "content": "how are you?"]])
```

## Topics

### Tokenizers
- [struct ScriptedTokenizer](./scriptedtokenizer.md)
  A deterministic `Tokenizer` for scripted tests.
- [struct PseudoWordTokenizer](./pseudowordtokenizer.md)
  A deterministic tokenizer for random-weight models.
### Chat Templates
- [protocol ScriptedChatTemplate](./scriptedchattemplate.md)
  A chat template for scripted tests.
- [struct MinimalChatTemplate](./minimalchattemplate.md)
  A minimal one-marker-per-role template for mechanics tests. Not a real model family: prompts stay short and segment assertions stay readable.
- [struct ChatMLTemplate](./chatmltemplate.md)
  Plain ChatML, as used by the Qwen family without its tool extensions.
- [enum ScriptedTemplateMessage](./scriptedtemplatemessage.md)
  Message helpers shared by template implementations.
- [enum ScriptedTemplateError](./scriptedtemplateerror.md)
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
- [struct ScriptedInputProcessor](./scriptedinputprocessor.md)
  Renders chat input with a tokenizer’s chat template.
### Model Support
- [class TranscriptKVCache](./transcriptkvcache.md)
  The tokens a model has processed, kept as an entry in its KV cache.
- [enum TranscriptKVCacheError](./transcriptkvcacheerror.md)
### Vocabulary
- [struct VocabularyBuilder](./vocabularybuilder.md)
  Builds a [`ScriptedVocabulary`](./scriptedvocabulary.md) from a scenario corpus.
- [struct ScriptedVocabulary](./scriptedvocabulary.md)
  A deterministic vocabulary for scripted tests.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm)*