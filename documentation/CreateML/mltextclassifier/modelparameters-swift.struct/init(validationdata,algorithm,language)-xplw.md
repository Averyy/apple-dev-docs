# init(validationData:algorithm:language:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates parameters for a text classifier with validation data in a dictionary.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0
- Mac Catalyst 15.0+ - Deprecated in 16.0
- macOS 10.14+ - Deprecated in 10.15
- visionOS 1.0+

> **Deprecated**: Use the validation property instead.

## Declaration

```swift
init(validationData: [String : [String]], algorithm: MLTextClassifier.ModelAlgorithmType = .maxEnt(revision: 1), language: NLLanguage? = nil)
```

**Other overloads**:

```swift
init(validationData: MLTextClassifier.DataSource, algorithm: MLTextClassifier.ModelAlgorithmType = .maxEnt(revision: 1), language: NLLanguage? = nil)
```

## Parameters

- `validationData`: A dictionary the text classifier uses for validation data during training.
- `algorithm`: An algorithm type for the classifier.
- `language`: The language of the text to classify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/modelparameters-swift.struct/init(validationdata:algorithm:language:)-xplw)*