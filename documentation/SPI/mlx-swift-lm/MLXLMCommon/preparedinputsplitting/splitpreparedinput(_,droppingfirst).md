---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/preparedinputsplitting/splitpreparedinput(_:droppingfirst:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# splitPreparedInput(_:droppingFirst:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Return the suffix of `input` that begins at `prefixTokenCount`, carrying only the media whose placeholder tokens lie inside that suffix.

## Declaration

```swift
func splitPreparedInput(_ input: LMInput, droppingFirst prefixTokenCount: Int) -> LMInput?
```

#### Return Value

An `LMInput` whose tokens are `input`’s tokens after the first `prefixTokenCount`, with a media payload consistent with those tokens, or `nil` if no such input can be produced.

#### Discussion

Returning `nil` means the input cannot be split safely at this boundary and the caller must fall back to a full prefill. Implementations should return `nil` rather than guess – in particular when the boundary falls inside a media block, when a payload cannot be attributed to individual media items, or when the input carries state the implementation does not know how to slice.

## Parameters

- `input`: The prepared input for the full prompt
- `prefixTokenCount`: Number of leading tokens already represented in the cache


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/preparedinputsplitting/splitpreparedinput(_:droppingfirst:))*