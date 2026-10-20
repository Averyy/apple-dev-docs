# init(validation:algorithm:language:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates model parameters.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(validation: MLWordTagger.ModelParameters.ValidationData = .split(strategy: .automatic), algorithm: MLWordTagger.ModelAlgorithmType = .crf(revision: 1), language: NLLanguage? = nil)
```

## Parameters

- `validation`: The validation data source.
- `algorithm`: The algorithm type.
- `language`: The language of the text to tag.

## See Also

### Creating parameters
- [MLWordTagger.ModelAlgorithmType](../modelalgorithmtype.md)
  The algorithm type.
- [MLWordTagger.ModelParameters.ValidationData](./validationdata-swift.enum.md)
  The validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/modelparameters-swift.struct/init(validation:algorithm:language:))*