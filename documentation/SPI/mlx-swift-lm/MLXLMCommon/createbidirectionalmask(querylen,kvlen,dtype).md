---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/createbidirectionalmask(querylen:kvlen:dtype:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# createBidirectionalMask(queryLen:kvLen:dtype:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Bidirectional attention mask: every query position attends to every kv position equally (no causal restriction).

## Declaration

```swift
func createBidirectionalMask(queryLen: Int, kvLen: Int, dtype: DType) -> MLXArray
```

## Return Value

`[queryLen, kvLen]` array of zeros.

## Discussion

Used by the MTP drafter, whose queries sit at a single constant position outside the target’s KV cache and need full visibility into the target’s shared K/V pool. Returned as an additive mask (`0` for attend, `-inf` for mask) compatible with `MLXFast.ScaledDotProductAttentionMaskMode.array`.

## Parameters

- `queryLen`: Number of query tokens (typically `1` for MTP drafting)
- `kvLen`: Total kv positions in the shared pool
- `dtype`: Array dtype (must match the queries’ dtype)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/createbidirectionalmask(querylen:kvlen:dtype:))*