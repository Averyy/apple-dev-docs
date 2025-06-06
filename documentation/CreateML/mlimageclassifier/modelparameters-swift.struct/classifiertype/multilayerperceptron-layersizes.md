# MLImageClassifier.ModelParameters.ClassifierType.multilayerPerceptron(layerSizes:)

**Framework**: Create ML  
**Kind**: case

Multilayer perceptron, layerSizes holds a list of positive integers that represent the number of hidden units in each layer. An additional fully connected layer with a Softmax activation output will be added that maps to probabilities of sound categories.

**Availability**:
- macOS 11.0+

## Declaration

```swift
case multilayerPerceptron(layerSizes: [Int])
```

## See Also

- [MLImageClassifier.ModelParameters.ClassifierType.logisticRegressor](mlimageclassifier/modelparameters-swift.struct/classifiertype/logisticregressor.md)
  Logistic regression is a statistical model that classifies input feature vector into different categories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/modelparameters-swift.struct/classifiertype/multilayerperceptron(layersizes:))*