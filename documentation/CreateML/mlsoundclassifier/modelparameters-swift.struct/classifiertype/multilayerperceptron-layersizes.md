# MLSoundClassifier.ModelParameters.ClassifierType.multilayerPerceptron(layerSizes:)

**Framework**: Create ML  
**Kind**: case

A neural network model that uses three or more layers to classify an input into a category.

**Availability**:
- macOS 11.0+

## Declaration

```swift
case multilayerPerceptron(layerSizes: [Int])
```

#### Discussion

The neural network has a minimum of three layers:

- An input layer
- One or more hidden layers
- An output layer

The number of integers in your `layerSizes` array determines the number of hidden layers in the neural network. Each integer in the array determines the size of that hidden layer.

## Parameters

- `layerSizes`: An array of positive integers. Each element represents the number of units for that hidden   layer.

## See Also

- [MLSoundClassifier.ModelParameters.ClassifierType.logisticRegressor](mlsoundclassifier/modelparameters-swift.struct/classifiertype/logisticregressor.md)
  A statistical model that uses logistic regression to classify an input vector into a category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/classifiertype/multilayerperceptron(layersizes:))*