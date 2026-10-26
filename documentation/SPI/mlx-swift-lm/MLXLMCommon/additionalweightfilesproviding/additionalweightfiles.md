---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/additionalweightfilesproviding/additionalweightfiles"
framework: "mlx-swift-lm/MLXLMCommon"
---

# additionalWeightFiles

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

File names, relative to the model directory.

## Declaration

```swift
var additionalWeightFiles: [String] { get }
```

#### Discussion

They are loaded after the selected weight files, so a file that is already selected is not loaded twice, and names that are not present are ignored.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/additionalweightfilesproviding/additionalweightfiles)*