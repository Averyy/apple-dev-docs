---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/speculativedecodingtelemetry"
framework: "mlx-swift-lm/MLXLMCommon"
---

# SpeculativeDecodingTelemetry

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Runtime counters for a speculative decoding pass.

## Declaration

```swift
struct SpeculativeDecodingTelemetry
```

## Topics

### Initializers
- [init(roundCount: Int, draftTokenCount: Int, acceptedDraftTokenCount: Int, targetModelCallCount: Int, draftModelCallCount: Int, targetVerifiedTokenCount: Int, emittedTokenCount: Int)](./speculativedecodingtelemetry/init%28roundcount,drafttokencount,accepteddrafttokencount,targetmodelcallcount,draftmodelcallcount,targetverifiedtokencount,emittedtokencount%29.md)
### Instance Properties
- [var acceptanceRate: Double](./speculativedecodingtelemetry/acceptancerate.md)
  Fraction of drafted tokens accepted by the target model.
- [var acceptedDraftTokenCount: Int](./speculativedecodingtelemetry/accepteddrafttokencount.md)
  Number of draft tokens accepted by the target model.
- [var draftModelCallCount: Int](./speculativedecodingtelemetry/draftmodelcallcount.md)
  Number of draft-model calls.
- [var draftTokenCount: Int](./speculativedecodingtelemetry/drafttokencount.md)
  Number of tokens proposed by the draft model.
- [var emittedTokenCount: Int](./speculativedecodingtelemetry/emittedtokencount.md)
  Number of tokens emitted from speculative rounds, including correction and bonus tokens.
- [var meanAcceptedDraftTokensPerRound: Double](./speculativedecodingtelemetry/meanaccepteddrafttokensperround.md)
  Mean accepted draft tokens per speculative round.
- [var meanEmittedTokensPerTargetCall: Double](./speculativedecodingtelemetry/meanemittedtokenspertargetcall.md)
  Mean emitted tokens per target-model verification call.
- [var rejectedDraftTokenCount: Int](./speculativedecodingtelemetry/rejecteddrafttokencount.md)
  Number of draft tokens rejected by the target model.
- [var roundCount: Int](./speculativedecodingtelemetry/roundcount.md)
  Number of speculative decoding rounds.
- [var targetModelCallCount: Int](./speculativedecodingtelemetry/targetmodelcallcount.md)
  Number of target-model verification calls.
- [var targetVerifiedTokenCount: Int](./speculativedecodingtelemetry/targetverifiedtokencount.md)
  Number of token positions evaluated by the target model during verification.
### Default Implementations
- [Equatable Implementations](./speculativedecodingtelemetry/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/speculativedecodingtelemetry)*