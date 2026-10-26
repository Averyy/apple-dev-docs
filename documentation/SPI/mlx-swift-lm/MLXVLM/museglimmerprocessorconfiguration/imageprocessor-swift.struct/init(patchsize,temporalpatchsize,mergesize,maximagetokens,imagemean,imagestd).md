---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/museglimmerprocessorconfiguration/imageprocessor-swift.struct/init(patchsize:temporalpatchsize:mergesize:maximagetokens:imagemean:imagestd:)"
framework: "mlx-swift-lm/MLXVLM"
---

# init(patchSize:temporalPatchSize:mergeSize:maxImageTokens:imageMean:imageStd:)

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: init  
**Role**: Initializer

Builds a configuration in code, chiefly so a caller can lower [`maxImageTokens`](./maximagetokens.md) from the checkpoint’s 4096. See the note in [`preprocess(image:processing:)`](../../museglimmerprocessor/preprocess%28image,processing%29.md) on why that budget dominates time-to-first-token.

## Declaration

```swift
init(patchSize: Int = 14, temporalPatchSize: Int = 2, mergeSize: Int = 2, maxImageTokens: Int = 4096, imageMean: [CGFloat] = [0.5, 0.5, 0.5], imageStd: [CGFloat] = [0.5, 0.5, 0.5])
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/museglimmerprocessorconfiguration/imageprocessor-swift.struct/init(patchsize:temporalpatchsize:mergesize:maximagetokens:imagemean:imagestd:))*