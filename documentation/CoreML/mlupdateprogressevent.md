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

### Getting Progress Event Types
- [static var trainingBegin: MLUpdateProgressEvent](mlupdateprogressevent/trainingbegin.md)
  An event that represents the start of training.
- [static var miniBatchEnd: MLUpdateProgressEvent](mlupdateprogressevent/minibatchend.md)
  An event that represents the end of a mini-batch within a training epoch.
- [static var epochEnd: MLUpdateProgressEvent](mlupdateprogressevent/epochend.md)
  An event that represents the end of training epoch.
### Creating a Progress Event
- [init(rawValue: Int)](mlupdateprogressevent/init(rawvalue:).md)
  Creates a progress event for the given integer.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

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