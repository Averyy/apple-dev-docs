# LogisticRegressionClassifier.Configuration

**Framework**: Create ML Components  
**Kind**: struct

A logistic regression classifier configuration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct Configuration
```

## Topics

### Creating a configuration
- [init()](logisticregressionclassifier/configuration-swift.struct/init.md)
  Creates a default logistic regression classifier configuration.
- [init(from: any Decoder) throws](logisticregressionclassifier/configuration-swift.struct/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Getting the properties
- [var convergenceThreshold: Double](logisticregressionclassifier/configuration-swift.struct/convergencethreshold.md)
  The convergence threshold.
- [var earlyStopIterationCount: Int](logisticregressionclassifier/configuration-swift.struct/earlystopiterationcount.md)
  The number of iterations to use when evaluating whether to stop early.
- [var l1Penalty: Double](logisticregressionclassifier/configuration-swift.struct/l1penalty.md)
  Weight of the L1 regularization term.
- [var l2Penalty: Double](logisticregressionclassifier/configuration-swift.struct/l2penalty.md)
  Weight of the L2 regularization term.
- [var maximumIterations: Int](logisticregressionclassifier/configuration-swift.struct/maximumiterations.md)
  The maximum number of allowed passes through the data.
- [var optimizationStrategy: OptimizationStrategy](logisticregressionclassifier/configuration-swift.struct/optimizationstrategy.md)
  The optimization strategy.
- [var scaleFeatures: Bool](logisticregressionclassifier/configuration-swift.struct/scalefeatures.md)
  A Boolean value indicating whether to scale the input features.
- [var stepSize: Double](logisticregressionclassifier/configuration-swift.struct/stepsize.md)
  The starting step size to use for the solver.
### Operators
- [static func == (LogisticRegressionClassifier<Scalar, Label>.Configuration, LogisticRegressionClassifier<Scalar, Label>.Configuration) -> Bool](logisticregressionclassifier/configuration-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](logisticregressionclassifier/configuration-swift.struct/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](logisticregressionclassifier/configuration-swift.struct/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](logisticregressionclassifier/configuration-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](logisticregressionclassifier/configuration-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init(labels: Set<Label>, configuration: LogisticRegressionClassifier<Scalar, Label>.Configuration)](logisticregressionclassifier/init(labels:configuration:).md)
  Creates a logistic regression classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/logisticregressionclassifier/configuration-swift.struct)*