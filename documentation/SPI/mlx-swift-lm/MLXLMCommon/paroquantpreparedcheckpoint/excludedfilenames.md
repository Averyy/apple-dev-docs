---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/paroquantpreparedcheckpoint/excludedfilenames"
framework: "mlx-swift-lm/MLXLMCommon"
---

# excludedFileNames

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Type Property

File names that must never be treated as checkpoint sources — by the loader’s raw-safetensors scan, by the manifest, and by any caller computing weight identity over the directory (e.g. the app’s `ModelFingerprint`).

## Declaration

```swift
static let excludedFileNames: Set<String>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/paroquantpreparedcheckpoint/excludedfilenames)*