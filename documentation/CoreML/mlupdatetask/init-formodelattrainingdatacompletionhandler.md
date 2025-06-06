# init(forModelAt:trainingData:completionHandler:)

**Framework**: Core ML  
**Kind**: init

Creates a task that updates the model at the URL with the training data, and calls the completion handler when the update completes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
convenience init(forModelAt modelURL: URL, trainingData: any MLBatchProvider, completionHandler: @escaping (MLUpdateContext) -> Void) throws
```

## Parameters

- `modelURL`: The location in the file system of a model file ( ).
- `trainingData`: The update data for the model, contained in a batch provider.
- `completionHandler`: The closure the task calls when it finishes.

## See Also

- [convenience init(forModelAt: URL, trainingData: any MLBatchProvider, progressHandlers: MLUpdateProgressHandlers) throws](mlupdatetask/init(formodelat:trainingdata:progresshandlers:).md)
  Creates a task that updates the model at the URL with the training data, and calls the progress handlers during and after the update.
- [convenience init(forModelAt: URL, trainingData: any MLBatchProvider, configuration: MLModelConfiguration?, completionHandler: (MLUpdateContext) -> Void) throws](mlupdatetask/init(formodelat:trainingdata:configuration:completionhandler:).md)
  Creates a task that updates the model at the URL with the training data and configuration, and calls the completion handler when the update completes.
- [convenience init(forModelAt: URL, trainingData: any MLBatchProvider, configuration: MLModelConfiguration?, progressHandlers: MLUpdateProgressHandlers) throws](mlupdatetask/init(formodelat:trainingdata:configuration:progresshandlers:).md)
  Creates a task that updates the model at the URL with the training data and configuration, and calls the progress handlers during and after the update.
- [convenience init(forModelAtURL: URL, trainingData: any MLBatchProvider, completionHandler: (MLUpdateContext) -> Void) throws](mlupdatetask/init(formodelaturl:trainingdata:completionhandler:).md)
- [convenience init(forModelAtURL: URL, trainingData: any MLBatchProvider, progressHandlers: MLUpdateProgressHandlers) throws](mlupdatetask/init(formodelaturl:trainingdata:progresshandlers:).md)
- [convenience init(forModelAtURL: URL, trainingData: any MLBatchProvider, configuration: MLModelConfiguration?, completionHandler: (MLUpdateContext) -> Void) throws](mlupdatetask/init(formodelaturl:trainingdata:configuration:completionhandler:).md)
- [convenience init(forModelAtURL: URL, trainingData: any MLBatchProvider, configuration: MLModelConfiguration?, progressHandlers: MLUpdateProgressHandlers) throws](mlupdatetask/init(formodelaturl:trainingdata:configuration:progresshandlers:).md)
- [protocol MLBatchProvider](mlbatchprovider.md)
  An interface that represents a collection of feature providers.
- [class MLModelConfiguration](mlmodelconfiguration.md)
  The settings for creating or updating a machine learning model.
- [class MLUpdateContext](mlupdatecontext.md)
  The context an update task provides to your app’s completion and update progress handlers.
- [class MLUpdateProgressHandlers](mlupdateprogresshandlers.md)
  A collection of closures an update task uses to notify your app of its progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlupdatetask/init(formodelat:trainingdata:completionhandler:))*