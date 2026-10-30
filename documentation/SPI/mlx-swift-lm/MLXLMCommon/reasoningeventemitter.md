---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningeventemitter"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ReasoningEventEmitter

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Routes a model’s decoded generation stream into reasoning (chain-of-thought) vs response segments by scanning for the model’s reasoning delimiters and any protocol-declared implicit exits.

## Declaration

```swift
struct ReasoningEventEmitter
```

## Overview

A value-type streaming scanner: feed it each decoded chunk via [`process(_:)`](./reasoningeventemitter/process%28_%29.md) and it returns the routed segments, holding back any partial delimiter that straddles a chunk boundary (`pendingPrefix`). This makes detection robust to the detokenizer or tool-call processor fragmenting a `<think>` across chunks.

**Primed state.** The headline reasoning families (Qwen3 with thinking enabled, DeepSeek-R1) prefill the *opening* delimiter into the rendered prompt, so the model’s first generated token is already reasoning content and it never emits an opening `<think>` in the stream — only the closing `</think>`. Construct with `primedInside: true` for those, seeded by inspecting the rendered prompt tail.

**State model.** `Outside -> Inside -> Outside`, plus a `Label` step for the labeled-channel protocol (see [`ReasoningChannel`](./reasoningchannel.md)) where the role label following the start delimiter decides which way the span routes. When outside, the scanner watches for the start delimiter; when inside, the end delimiter and any [`implicitEndDelimiters`](./reasoningconfig/implicitenddelimiters.md), earliest match winning. A canonical end delimiter is framing and is consumed, while an implicit one is answer/tool content and stays in the stream to be re-scanned outside. `pendingPrefix` holds text that may be a delimiter split across a chunk boundary. For a delimiter pair, a start delimiter always (re)opens a reasoning span, so multiple blocks each route. For a labeled channel, a start delimiter inside an open channel also ends it, since channels do not nest.

**Delimiters as tokens.** Scanning text misroutes a delimiter the model only spells out in its answer. The generation loop avoids that when both delimiters are single tokens: it reports them by id through `process(boundary:)`, and their text is then ordinary content. An implicit end delimiter that is a single token is reported the same way. Callers that feed text alone keep the text scan.

## Topics

### Initializers
- [init(config: ReasoningConfig, primedInside: Bool)](./reasoningeventemitter/init%28config,primedinside%29.md)
### Instance Properties
- [var hasClosedReasoning: Bool](./reasoningeventemitter/hasclosedreasoning.md)
  True once a canonical or implicit end boundary has closed a *reasoning* span. Unlike [`isInsideReasoning`](./reasoningeventemitter/isinsidereasoning.md), this latches - so a caller (e.g. a think-then-call token collector) can detect a close even when an empty `<think></think>` resolves within a single [`process(_:)`](./reasoningeventemitter/process%28_%29.md) call, where sampling [`isInsideReasoning`](./reasoningeventemitter/isinsidereasoning.md) afterward reads `false` both before and after and the transient open is invisible.
- [var isInsideReasoning: Bool](./reasoningeventemitter/isinsidereasoning.md)
  Whether the scanner is currently inside a reasoning span.
### Instance Methods
- [func finalize() -> [Segment]](./reasoningeventemitter/finalize%28%29.md)
  Flushes any held-back text at end of generation.
- [func process(String) -> [Segment]](./reasoningeventemitter/process%28_%29.md)
  Ingests one decoded chunk and returns the segments it resolves to.
### Type Methods
- [static func promptEndsInsideReasoning(promptTokens: [Int], config: ReasoningConfig, tokenizer: any Tokenizer) -> Bool](./reasoningeventemitter/promptendsinsidereasoning%28prompttokens,config,tokenizer%29.md)
  Whether a rendered prompt, given as its token ids, ends inside an open reasoning block.
- [static func promptEndsInsideReasoning(renderedPromptTail: String, config: ReasoningConfig) -> Bool](./reasoningeventemitter/promptendsinsidereasoning%28renderedprompttail,config%29.md)
  Whether a rendered prompt ends *inside* an open reasoning block — used to seed `primedInside`.
### Enumerations
- [ReasoningEventEmitter.Segment](./reasoningeventemitter/segment.md)
  A routed slice of the decoded stream.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningeventemitter)*