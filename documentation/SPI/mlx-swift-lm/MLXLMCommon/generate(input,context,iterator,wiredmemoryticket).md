---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generate(input:context:iterator:wiredmemoryticket:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# generate(input:context:iterator:wiredMemoryTicket:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

> **Deprecated**: use a higher level generate() call or use generateTask() for fine grained control

## Declaration

```swift
func generate(input: LMInput, context: ModelContext, iterator: TokenIterator, wiredMemoryTicket: WiredMemoryTicket? = nil) -> AsyncStream<Generation>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generate(input:context:iterator:wiredmemoryticket:))*