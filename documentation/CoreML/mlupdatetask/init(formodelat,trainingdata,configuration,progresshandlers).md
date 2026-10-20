# init(forModelAt:trainingData:configuration:progressHandlers:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates a task that updates the model at the URL with the training data and configuration, and calls the progress handlers during and after the update.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
convenience init(forModelAt modelURL: URL, trainingData: any MLBatchProvider, configuration: MLModelConfiguration?, progressHandlers: MLUpdateProgressHandlers) throws
```

```objc
+ (instancetype) updateTaskForModelAtURL:(NSURL *) modelURL trainingData:(id<MLBatchProvider>) trainingData configuration:(MLModelConfiguration *) configuration progressHandlers:(MLUpdateProgressHandlers *) progressHandlers error:(NSError **) error;
```

## Parameters

- `modelURL`: The location in the file system of a model file (*ModelName*`.mlmodelc`).
- `trainingData`: The update data for the model, contained in a batch provider.
- `configuration`: The model settings for an updated model object.
- `progressHandlers`: The closures the task calls during the update process.

## See Also

### Creating an update task
- [convenience init(forModelAt: URL, trainingData: any MLBatchProvider, completionHandler: (MLUpdateContext) -> Void) throws](./init%28formodelat,trainingdata,completionhandler%29.md)
  Creates a task that updates the model at the URL with the training data, and calls the completion handler when the update completes.
- [convenience init(forModelAt: URL, trainingData: any MLBatchProvider, progressHandlers: MLUpdateProgressHandlers) throws](./init%28formodelat,trainingdata,progresshandlers%29.md)
  Creates a task that updates the model at the URL with the training data, and calls the progress handlers during and after the update.
- [convenience init(forModelAt: URL, trainingData: any MLBatchProvider, configuration: MLModelConfiguration?, completionHandler: (MLUpdateContext) -> Void) throws](./init%28formodelat,trainingdata,configuration,completionhandler%29.md)
  Creates a task that updates the model at the URL with the training data and configuration, and calls the completion handler when the update completes.
- [convenience init(forModelAtURL: URL, trainingData: any MLBatchProvider, completionHandler: (MLUpdateContext) -> Void) throws](./init%28formodelaturl,trainingdata,completionhandler%29.md)
- [convenience init(forModelAtURL: URL, trainingData: any MLBatchProvider, progressHandlers: MLUpdateProgressHandlers) throws](./init%28formodelaturl,trainingdata,progresshandlers%29.md)
- [convenience init(forModelAtURL: URL, trainingData: any MLBatchProvider, configuration: MLModelConfiguration?, completionHandler: (MLUpdateContext) -> Void) throws](./init%28formodelaturl,trainingdata,configuration,completionhandler%29.md)
- [convenience init(forModelAtURL: URL, trainingData: any MLBatchProvider, configuration: MLModelConfiguration?, progressHandlers: MLUpdateProgressHandlers) throws](./init%28formodelaturl,trainingdata,configuration,progresshandlers%29.md)
- [protocol MLBatchProvider](../mlbatchprovider.md)
  An interface that represents a collection of feature providers.
- [class MLModelConfiguration](../mlmodelconfiguration.md)
  The settings for creating or updating a machine learning model.
- [class MLUpdateContext](../mlupdatecontext.md)
  The context an update task provides to your app’s completion and update progress handlers.
- [class MLUpdateProgressHandlers](../mlupdateprogresshandlers.md)
  A collection of closures an update task uses to notify your app of its progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlupdatetask/init(formodelat:trainingdata:configuration:progresshandlers:))*