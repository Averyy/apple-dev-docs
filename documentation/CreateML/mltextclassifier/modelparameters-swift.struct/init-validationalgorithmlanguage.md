# init(validation:algorithm:language:)

**Framework**: Create ML  
**Kind**: init

Creates model parameters for a text classifier with the specified validation data, algorithm, and language.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
init(validation: MLTextClassifier.ModelParameters.ValidationData = .split(strategy: .automatic), algorithm: MLTextClassifier.ModelAlgorithmType = .maxEnt(revision: 1), language: NLLanguage? = nil)
```

## Parameters

- `validation`: The validation data to use during text classifier training.
- `algorithm`: An algorithm type for the classifier.
- `language`: The language of the text to classify.

## See Also

- [struct NLLanguage](../NaturalLanguage/NLLanguage.md)
  The languages that the Natural Language framework supports.
- [MLTextClassifier.ModelAlgorithmType](mltextclassifier/modelalgorithmtype.md)
  The type of algorithm that a text classifier uses.
- [MLTextClassifier.ModelParameters.ValidationData](mltextclassifier/modelparameters-swift.struct/validationdata-swift.enum.md)
  The validation data that a text classifier uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/modelparameters-swift.struct/init(validation:algorithm:language:))*