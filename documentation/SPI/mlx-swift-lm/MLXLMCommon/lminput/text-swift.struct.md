---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/lminput/text-swift.struct"
framework: "mlx-swift-lm/MLXLMCommon"
---

# LMInput.Text

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Representation of tokenized input text.

## Declaration

```swift
struct Text
```

## Topics

### Initializers
- [init(tokens: MLXArray, mask: MLXArray?)](./text-swift.struct/init%28tokens,mask%29.md)
### Instance Properties
- [let mask: MLXArray?](./text-swift.struct/mask.md)
  optional mask array
- [var sequenceLengths: [Int]?](./text-swift.struct/sequencelengths.md)
  Per-batch sequence lengths derived from the optional attention mask.
- [let tokens: MLXArray](./text-swift.struct/tokens.md)
  input token array
### Subscripts
- [subscript(MLXArrayIndex..., stream _: StreamOrDevice) -> Text](./text-swift.struct/subscript%28_,stream%29.md)
- [subscript(text _: MLXArrayIndex..., stream _: StreamOrDevice) -> Text](./text-swift.struct/subscript%28text,stream%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/lminput/text-swift.struct)*