# init(maximumError:rootMeanSquaredError:)

**Framework**: Create ML  
**Kind**: init

Creates regressor metrics describing the quality of your model.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(maximumError: Double, rootMeanSquaredError: Double)
```

#### Discussion

You typically don’t initialize metrics directly. Instead you get metrics about your model after training. For example, when you train an [`MLRegressor`](mlregressor.md), you can look at its [`trainingMetrics`](mlregressor/trainingmetrics.md) and [`validationMetrics`](mlregressor/validationmetrics.md) properties. Additionally, you can check the performance on a test set with the [`evaluation(on:)`](mlregressor/evaluation(on:)-7pirm.md) method.

## Parameters

- `maximumError`: The maximum error of the model for the training data.
- `rootMeanSquaredError`: The root mean squared error of the model for the training data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlregressormetrics/init(maximumerror:rootmeansquarederror:))*