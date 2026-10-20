# minChildWeight

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The minimum weight of each leaf node.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var minChildWeight: Double
```

#### Discussion

The minimum child weight controls when the tree building should terminate based comparing the sum of the instance weights to the [`minChildWeight`](./minchildweight.md).

## See Also

### Accessing parameters
- [var validationData: MLDataTable?](./validationdata-swift.property.md)
  The data used for the validation set to inform the model training process.
- [var maxDepth: Int](./maxdepth.md)
  The maximum depth of the tree. Must be greater than 0.
- [var minLossReduction: Double](./minlossreduction.md)
  The minimum amount that the loss needs to be reduced to create a new split.
- [var randomSeed: Int](./randomseed.md)
  The seed value for random operations during tree building process.
- [var validation: MLDecisionTreeClassifier.ModelParameters.ValidationData](./validation.md)
  Validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldecisiontreeclassifier/modelparameters-swift.struct/minchildweight)*