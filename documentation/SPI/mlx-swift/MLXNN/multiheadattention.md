---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/multiheadattention"
framework: "mlx-swift/MLXNN"
---

# MultiHeadAttention

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Implements the scaled dot product attention with multiple heads.

## Declaration

```swift
class MultiHeadAttention
```

### See Also

- [Transformer](./transformers.md)
- [`init(dimensions:numHeads:queryInputDimensions:keyInputDimensions:valueInputDimensions:valueDimensions:valueOutputDimensions:bias:)`](./multiheadattention/init%28dimensions,numheads,queryinputdimensions,keyinputdimensions,valueinputdimensions,valuedimensions,valueoutputdimensions,bias%29.md)

## Topics

### Initializers
- [init(dimensions: Int, numHeads: Int, queryInputDimensions: Int?, keyInputDimensions: Int?, valueInputDimensions: Int?, valueDimensions: Int?, valueOutputDimensions: Int?, bias: Bool)](./multiheadattention/init%28dimensions,numheads,queryinputdimensions,keyinputdimensions,valueinputdimensions,valuedimensions,valueoutputdimensions,bias%29.md)
  Implements the scaled dot product attention with multiple heads.
### Instance Properties
- [var keyProjection: any UnaryLayer](./multiheadattention/keyprojection.md)
- [let numHeads: Int](./multiheadattention/numheads.md)
- [var outProjection: any UnaryLayer](./multiheadattention/outprojection.md)
- [var queryProjection: any UnaryLayer](./multiheadattention/queryprojection.md)
- [var valueProjection: any UnaryLayer](./multiheadattention/valueprojection.md)
### Instance Methods
- [func callAsFunction(MLXArray, keys: MLXArray, values: MLXArray, mask: MLXArray?) -> MLXArray](./multiheadattention/callasfunction%28_,keys,values,mask%29.md)
### Type Methods
- [static func createAdditiveCausalMask(Int, dtype: DType) -> MLXArray](./multiheadattention/createadditivecausalmask%28_,dtype%29.md)
  Creates an attention mask for use with [`callAsFunction(_:keys:values:mask:)`](./multiheadattention/callasfunction%28_,keys,values,mask%29.md)

## Relationships

### Inherits From
- [Module](./module.md)
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- Swift.CustomStringConvertible

## See Also

### Other Layers
- [class Bilinear](./bilinear.md)
  Applies a bilinear transformation to the inputs.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/multiheadattention)*