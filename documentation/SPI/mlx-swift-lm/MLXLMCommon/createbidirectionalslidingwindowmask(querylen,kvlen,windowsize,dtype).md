---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/createbidirectionalslidingwindowmask(querylen:kvlen:windowsize:dtype:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# createBidirectionalSlidingWindowMask(queryLen:kvLen:windowSize:dtype:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Bidirectional sliding-window attention mask: when `kvLen` exceeds `windowSize`, each query attends to a contiguous window of the first `windowSize` kv positions; the remaining `kvLen - windowSize` positions are masked with `-inf`. When `windowSize >= kvLen` (the degenerate case — and the production MTP path, where the sliding-attention KV cache is capped at `windowSize` by `RotatingKVCache`), the helper early-exits to an all-zeros mask (every query attends to every kv position).

## Declaration

```swift
func createBidirectionalSlidingWindowMask(queryLen: Int, kvLen: Int, windowSize: Int, dtype: DType) -> MLXArray
```

#### Return Value

`[queryLen, kvLen]` additive mask.

#### Discussion

Matches the fixture convention in `tools/fixtures/masks/` and HF Transformers’ `create_bidirectional_sliding_window_mask` (after the kv-axis flip).

Contract for the non-degenerate path (`kvLen > windowSize`): the mask is built from an absolute-position predicate (`kIdx < windowSize`), NOT a distance-from-`queryOffset` predicate. Callers that need distance-based windowing around a non-zero query offset (e.g. an mlx-vlm- style `|q_idx - k_idx| < windowSize` mask) must build the mask inline rather than calling this helper. MTP production callers don’t hit this path because the target’s sliding-attention cache cap keeps `kvLen` at or under `windowSize`; `Gemma4AssistantDraftModel.forwardHidden` enforces the invariant with a precondition before calling here.

## Parameters

- `queryLen`: Number of query tokens
- `kvLen`: Total kv positions
- `windowSize`: Sliding window size
- `dtype`: Array dtype (must match the queries’ dtype)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/createbidirectionalslidingwindowmask(querylen:kvlen:windowsize:dtype:))*