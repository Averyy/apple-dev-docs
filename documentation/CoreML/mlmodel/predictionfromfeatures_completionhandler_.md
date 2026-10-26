# predictionFromFeatures:completionHandler:

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Generates a prediction asynchronously from the feature values within the input feature provider.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
- (void) predictionFromFeatures:(id<MLFeatureProvider>) input completionHandler:(void (^)(id<MLFeatureProvider>output, NSError *error)) completionHandler;
```

## Parameters

- `input`: A feature provider that stores all the input feature values the model needs for a prediction.
- `completionHandler`: The callback the system invokes when it completes the prediction.

  - **output**: A feature provider that contains the outputs of the prediction.
  - **error**: If an error occurs, an error object that describes the error; otherwise, `nil`.

## See Also

### Loading a model
- [- predictionFromFeatures:options:completionHandler:](./predictionfromfeatures_options_completionhandler_.md)
  Generates a prediction asynchronously from the feature values within the input feature provider using the prediction options.
- [- predictionFromFeatures:usingState:options:completionHandler:](./predictionfromfeatures_usingstate_options_completionhandler_.md)
  Run a stateful prediction asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/predictionfromfeatures:completionhandler:)*