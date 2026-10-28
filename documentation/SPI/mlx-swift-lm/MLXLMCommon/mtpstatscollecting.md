---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpstatscollecting"
framework: "mlx-swift-lm/MLXLMCommon"
---

# MTPStatsCollecting

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Introspection surface for token iterators that perform MTP speculative decoding.

## Declaration

```swift
protocol MTPStatsCollecting
```

## Overview

The iterator value lives inside `generateLoopTask` and never escapes the stream, so its per-stream draft proposal and acceptance counters are not reachable through the high-level `generate(...)` API. Conforming the iterator to this protocol lets `generateLoopTask` downcast and thread the counters through the emitted `.info` event’s [`proposedDraftTokens`](./generatecompletioninfo/proposeddrafttokens.md), [`acceptedDraftTokens`](./generatecompletioninfo/accepteddrafttokens.md), and [`passthroughReason`](./generatecompletioninfo/passthroughreason.md) fields. Non-MTP iterators do not conform; the downcast returns nil and the fields default to nil for non-MTP streams.

## Topics

### Instance Properties
- [var acceptedDraftTokens: Int](./mtpstatscollecting/accepteddrafttokens.md)
  Total tokens accepted by the target across all speculation rounds.
- [var passthroughReason: String?](./mtpstatscollecting/passthroughreason.md)
  nil if the iterator stayed in speculative mode for the full stream; non-nil if sticky-passthrough engaged, with the reason string captured at the moment of engagement.
- [var proposedDraftTokens: Int](./mtpstatscollecting/proposeddrafttokens.md)
  Total tokens proposed across all speculation rounds in the stream.

## Relationships

### Conforming Types
- [MTPSpeculativeTokenIterator](./mtpspeculativetokeniterator.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpstatscollecting)*