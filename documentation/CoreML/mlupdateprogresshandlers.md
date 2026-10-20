# MLUpdateProgressHandlers

**Framework**: Core ML  
**Kind**: class  
**Role**: Class

A collection of closures an update task uses to notify your app of its progress.

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
class MLUpdateProgressHandlers
```

```objc
@interface MLUpdateProgressHandlers : NSObject
```

## Topics

### Creating progress handlers
- [init(forEvents: MLUpdateProgressEvent, progressHandler: ((MLUpdateContext) -> Void)?, completionHandler: (MLUpdateContext) -> Void)](./mlupdateprogresshandlers/init%28forevents,progresshandler,completionhandler%29.md)
  Creates the collection of closures an update task uses to notify your app of its progress.
- [struct MLUpdateProgressEvent](./mlupdateprogressevent.md)
  A type of event during a model update task.
- [class MLUpdateContext](./mlupdatecontext.md)
  The context an update task provides to your app’s completion and update progress handlers.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating an update task
- [convenience init(forModelAt: URL, trainingData: any MLBatchProvider, completionHandler: (MLUpdateContext) -> Void) throws](./mlupdatetask/init%28formodelat,trainingdata,completionhandler%29.md)
  Creates a task that updates the model at the URL with the training data, and calls the completion handler when the update completes.
- [convenience init(forModelAt: URL, trainingData: any MLBatchProvider, progressHandlers: MLUpdateProgressHandlers) throws](./mlupdatetask/init%28formodelat,trainingdata,progresshandlers%29.md)
  Creates a task that updates the model at the URL with the training data, and calls the progress handlers during and after the update.
- [convenience init(forModelAt: URL, trainingData: any MLBatchProvider, configuration: MLModelConfiguration?, completionHandler: (MLUpdateContext) -> Void) throws](./mlupdatetask/init%28formodelat,trainingdata,configuration,completionhandler%29.md)
  Creates a task that updates the model at the URL with the training data and configuration, and calls the completion handler when the update completes.
- [convenience init(forModelAt: URL, trainingData: any MLBatchProvider, configuration: MLModelConfiguration?, progressHandlers: MLUpdateProgressHandlers) throws](./mlupdatetask/init%28formodelat,trainingdata,configuration,progresshandlers%29.md)
  Creates a task that updates the model at the URL with the training data and configuration, and calls the progress handlers during and after the update.
- [convenience init(forModelAtURL: URL, trainingData: any MLBatchProvider, completionHandler: (MLUpdateContext) -> Void) throws](./mlupdatetask/init%28formodelaturl,trainingdata,completionhandler%29.md)
- [convenience init(forModelAtURL: URL, trainingData: any MLBatchProvider, progressHandlers: MLUpdateProgressHandlers) throws](./mlupdatetask/init%28formodelaturl,trainingdata,progresshandlers%29.md)
- [convenience init(forModelAtURL: URL, trainingData: any MLBatchProvider, configuration: MLModelConfiguration?, completionHandler: (MLUpdateContext) -> Void) throws](./mlupdatetask/init%28formodelaturl,trainingdata,configuration,completionhandler%29.md)
- [convenience init(forModelAtURL: URL, trainingData: any MLBatchProvider, configuration: MLModelConfiguration?, progressHandlers: MLUpdateProgressHandlers) throws](./mlupdatetask/init%28formodelaturl,trainingdata,configuration,progresshandlers%29.md)
- [protocol MLBatchProvider](./mlbatchprovider.md)
  An interface that represents a collection of feature providers.
- [class MLModelConfiguration](./mlmodelconfiguration.md)
  The settings for creating or updating a machine learning model.
- [class MLUpdateContext](./mlupdatecontext.md)
  The context an update task provides to your app’s completion and update progress handlers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlupdateprogresshandlers)*