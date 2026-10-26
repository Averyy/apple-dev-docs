---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcache/serializedclassname"
framework: "mlx-swift-lm/MLXLMCommon"
---

# serializedClassName

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Type Property  
**Required**: Yes

The class name written to prompt cache files, or `nil` if this cache cannot be saved.

## Declaration

```swift
static var serializedClassName: String? { get }
```

#### Discussion

Use a unique name, for example with a module prefix. A subclass that does not override it saves under its parent’s name and restores as the parent.

## Default Implementations

### KVCache Implementations
- [static var serializedClassName: String?](./serializedclassname-536xn.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcache/serializedclassname)*