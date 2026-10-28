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

**State model.** Conceptually `Outside → Inside → Closed`, but represented compactly as `inside: Bool` plus `pendingPrefix` (the diagram’s `PendingStart`/`PendingEnd` are “pendingPrefix is non-empty”; `Closed` is “not inside, having produced reasoning”). When not inside, the scanner watches for the start delimiter; when inside, the end delimiter. A start delimiter always (re)opens a reasoning span — so multiple blocks each route, and the cost is a documented limitation: a literal `<think>` appearing in answer text is misrouted (the deferred token-ID detection is the real fix).

## Topics

### Initializers
- [init(config: ReasoningConfig, primedInside: Bool)](./reasoningeventemitter/init%28config,primedinside%29.md)
### Instance Properties
- [var hasClosedReasoning: Bool](./reasoningeventemitter/hasclosedreasoning.md)
  True once a canonical or implicit end boundary has been observed, i.e. a reasoning span has closed at least once. Unlike [`isInsideReasoning`](./reasoningeventemitter/isinsidereasoning.md), this latches — so a caller (e.g. a think-then-call token collector) can detect a close even when an empty `<think></think>` resolves within a single [`process(_:)`](./reasoningeventemitter/process%28_%29.md) call, where sampling [`isInsideReasoning`](./reasoningeventemitter/isinsidereasoning.md) afterward reads `false` both before and after and the transient open is invisible.
- [var isInsideReasoning: Bool](./reasoningeventemitter/isinsidereasoning.md)
  Whether the scanner is currently inside a reasoning span.
### Instance Methods
- [func finalize() -> [Segment]](./reasoningeventemitter/finalize%28%29.md)
  Flushes any held-back text at end of generation.
- [func process(String) -> [Segment]](./reasoningeventemitter/process%28_%29.md)
  Ingests one decoded chunk and returns the segments it resolves to.
### Type Methods
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