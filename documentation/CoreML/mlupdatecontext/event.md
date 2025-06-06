# event

**Framework**: Core ML  
**Kind**: property

The event type that triggered an update task to notify your app’s completion and update progress handlers.

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
var event: MLUpdateProgressEvent { get }
```

## See Also

- [struct MLUpdateProgressEvent](mlupdateprogressevent.md)
  A type of event during a model update task.
- [var task: MLUpdateTask](mlupdatecontext/task.md)
  The update task that generated the update context.
- [var parameters: [MLParameterKey : Any]](mlupdatecontext/parameters.md)
  The parameters for the update task.
- [class MLParameterKey](mlparameterkey.md)
  The keys for the parameter dictionary in a model configuration or a model update context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlupdatecontext/event)*