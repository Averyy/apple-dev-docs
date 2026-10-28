---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallparser/supportsmarkerlessnamedjson"
framework: "mlx-swift-lm/MLXLMCommon"
---

# supportsMarkerlessNamedJSON

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Whether a declared tool name that begins a line, followed by a JSON arguments object, is native call syntax for this parser.

## Declaration

```swift
var supportsMarkerlessNamedJSON: Bool { get }
```

## Discussion

The dialect has no markers, so `ToolCallProcessor` detects it only when tool schemas are supplied and the name is one of them.

## Default Implementations

### ToolCallParser Implementations
- [var supportsMarkerlessNamedJSON: Bool](./supportsmarkerlessnamedjson-1f2xc.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallparser/supportsmarkerlessnamedjson)*