# MLUpdateProgressEvent

**Framework**: Core ML  
**Kind**: struct

A type of event during a model update task.

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
struct MLUpdateProgressEvent
```

## Topics

### Getting progress event types
- [static var trainingBegin: MLUpdateProgressEvent](mlupdateprogressevent/trainingbegin.md)
  An event that represents the start of training.
- [static var miniBatchEnd: MLUpdateProgressEvent](mlupdateprogressevent/minibatchend.md)
  An event that represents the end of a mini-batch within a training epoch.
- [static var epochEnd: MLUpdateProgressEvent](mlupdateprogressevent/epochend.md)
  An event that represents the end of training epoch.
### Creating a progress event
- [init(rawValue: Int)](mlupdateprogressevent/init(rawvalue:).md)
  Creates a progress event for the given integer.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [var event: MLUpdateProgressEvent](mlupdatecontext/event.md)
  The event type that triggered an update task to notify your app’s completion and update progress handlers.
- [var task: MLUpdateTask](mlupdatecontext/task.md)
  The update task that generated the update context.
- [var parameters: [MLParameterKey : Any]](mlupdatecontext/parameters.md)
  The parameters for the update task.
- [class MLParameterKey](mlparameterkey.md)
  The keys for the parameter dictionary in a model configuration or a model update context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlupdateprogressevent)*