# MLUpdateContext

**Framework**: Core ML  
**Kind**: class

The context an update task provides to your app’s completion and update progress handlers.

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
class MLUpdateContext
```

## Topics

### Getting the update context
- [var event: MLUpdateProgressEvent](mlupdatecontext/event.md)
  The event type that triggered an update task to notify your app’s completion and update progress handlers.
- [struct MLUpdateProgressEvent](mlupdateprogressevent.md)
  A type of event during a model update task.
- [var task: MLUpdateTask](mlupdatecontext/task.md)
  The update task that generated the update context.
- [var parameters: [MLParameterKey : Any]](mlupdatecontext/parameters.md)
  The parameters for the update task.
- [class MLParameterKey](mlparameterkey.md)
  The keys for the parameter dictionary in a model configuration or a model update context.
### Evaluating the update
- [var metrics: [MLMetricKey : Any]](mlupdatecontext/metrics.md)
  The training metrics of the model for the update task, contained in a dictionary.
- [class MLMetricKey](mlmetrickey.md)
  A key for the metrics dictionary in an update context.
### Saving an updated model
- [var model: any MLModel & MLWritable](mlupdatecontext/model.md)
  The underlying Core ML model stored in memory.
- [protocol MLWritable](mlwritable.md)
  A set of methods that saves a machine learning type to the file system.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [convenience init(forModelAt: URL, trainingData: any MLBatchProvider, completionHandler: (MLUpdateContext) -> Void) throws](mlupdatetask/init(formodelat:trainingdata:completionhandler:).md)
  Creates a task that updates the model at the URL with the training data, and calls the completion handler when the update completes.
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
- [class MLUpdateProgressHandlers](mlupdateprogresshandlers.md)
  A collection of closures an update task uses to notify your app of its progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlupdatecontext)*