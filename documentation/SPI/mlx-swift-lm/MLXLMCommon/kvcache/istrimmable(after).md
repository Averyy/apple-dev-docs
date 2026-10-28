---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcache/istrimmable(after:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# isTrimmable(after:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Predict whether this cache can still be trimmed after appending `positions`.

## Declaration

```swift
func isTrimmable(after positions: Int) -> Bool
```

## Return Value

`true` when a subsequent rewind would remain valid.

## Parameters

- `positions`: The nonnegative number of sequence positions that would be appended.

## Default Implementations

### KVCache Implementations
- [func isTrimmable(after: Int) -> Bool](./istrimmable%28after%29-npwr.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcache/istrimmable(after:))*