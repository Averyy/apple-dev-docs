---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningtokencollector"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ReasoningTokenCollector

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Drives a [`ReasoningEventEmitter`](./reasoningeventemitter.md) over a raw generated-token stream, accumulating the reasoning-span token IDs while routing decoded text to reasoning/response segments.

## Declaration

```swift
struct ReasoningTokenCollector
```

#### Overview

This is the pure, model-free core of think-then-call **Phase 1**: it owns a [`StreamingDetokenizer`](./streamingdetokenizer.md) and an emitter, so the device-side caller only supplies token IDs (from `generateTokens`) and forwards the returned segments to its channel. Token IDs are carried verbatim — no decode→re-encode round-trip — so the accumulated span prefills the constrained Phase 2 exactly.

**Why a separate type.** The emitter is intentionally text-only (it never sees token IDs). Phase 1 additionally needs to (a) retain the raw IDs for the hand-off and (b) know when to stop generating. Keeping that here — rather than inline in the executor — makes the logic host-testable with no model, and lets the unconstrained reasoning path adopt it later to share one loop.

## Topics

### Initializers
- [init(config: ReasoningConfig, primedInside: Bool, tokenizer: any Tokenizer)](./reasoningtokencollector/init%28config,primedinside,tokenizer%29.md)
### Instance Properties
- [var isInsideReasoning: Bool](./reasoningtokencollector/isinsidereasoning.md)
  Whether the scanner is currently inside a reasoning span.
- [var reasoningTokenIDs: [Int]](./reasoningtokencollector/reasoningtokenids.md)
  Every token ingested so far, in order. Phase 2 prefills the model’s prompt + these to continue from the completed reasoning span.
- [var shouldStopAfterReasoning: Bool](./reasoningtokencollector/shouldstopafterreasoning.md)
  Whether a reasoning span has closed — the Phase 1 → Phase 2 boundary.
### Instance Methods
- [func finalize() -> [ReasoningEventEmitter.Segment]](./reasoningtokencollector/finalize%28%29.md)
  Flush any held-back text at end of generation. If the stream ended mid-reasoning (no close ever arrived), the leftover routes as `.reasoning`.
- [func ingest(Int) -> [ReasoningEventEmitter.Segment]](./reasoningtokencollector/ingest%28_%29.md)
  Ingest one generated token: append it to [`reasoningTokenIDs`](./reasoningtokencollector/reasoningtokenids.md), advance the detokenizer, and return the routed segments (forward these to the channel). Returns an empty array when the token only advanced an incomplete multibyte character or a partial delimiter held back across the chunk boundary.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningtokencollector)*