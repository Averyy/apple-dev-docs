# init(validation:algorithm:language:)

**Framework**: Create ML  
**Kind**: init

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

- [MLWordTagger.ModelAlgorithmType](mlwordtagger/modelalgorithmtype.md)
  The algorithm type.
- [MLWordTagger.ModelParameters.ValidationData](mlwordtagger/modelparameters-swift.struct/validationdata-swift.enum.md)
  The validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/modelparameters-swift.struct/init(validation:algorithm:language:))*