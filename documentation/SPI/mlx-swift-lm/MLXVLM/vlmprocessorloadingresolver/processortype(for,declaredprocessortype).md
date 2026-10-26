---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/vlmprocessorloadingresolver/processortype(for:declaredprocessortype:)"
framework: "mlx-swift-lm/MLXVLM"
---

# processorType(for:declaredProcessorType:)

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

The processor type to use for this model, or `nil` to defer to another resolver or the checkpoint declaration. `declaredProcessorType` is `nil` when the selected processor configuration does not contain `processor_class`.

## Declaration

```swift
func processorType(for context: VLMProcessorLoadingContext, declaredProcessorType: String?) throws -> String?
```

## Default Implementations

### VLMProcessorLoadingResolver Implementations
- [func processorType(for: VLMProcessorLoadingContext, declaredProcessorType: String?) throws -> String?](./processortype%28for,declaredprocessortype%29-22xsz.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/vlmprocessorloadingresolver/processortype(for:declaredprocessortype:))*