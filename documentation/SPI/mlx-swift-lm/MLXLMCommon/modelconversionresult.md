---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconversionresult"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ModelConversionResult

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Result returned after converting and saving a model.

## Declaration

```swift
struct ModelConversionResult
```

## Topics

### Initializers
- [init(outputDirectory: URL, weightsURL: URL)](./modelconversionresult/init%28outputdirectory,weightsurl%29.md)
- [init(outputDirectory: URL, weightsURLs: [URL])](./modelconversionresult/init%28outputdirectory,weightsurls%29.md)
### Instance Properties
- [let outputDirectory: URL](./modelconversionresult/outputdirectory.md)
  Directory containing the converted model files.
- [let weightsURL: URL](./modelconversionresult/weightsurl.md)
  URL of the first written safetensors weights file.
- [let weightsURLs: [URL]](./modelconversionresult/weightsurls.md)
  URLs of the written safetensors shard files.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconversionresult)*