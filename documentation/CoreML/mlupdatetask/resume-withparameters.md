# resume(withParameters:)

**Framework**: Core ML  
**Kind**: method

Resumes a model update with updated parameter values.

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
func resume(withParameters updateParameters: [MLParameterKey : Any])
```

#### Discussion

Use this method to resume the model update task with newer parameter values. You use this method within the closures you provide in an [`MLUpdateProgressHandlers`](mlupdateprogresshandlers.md) instance to resume the [`MLUpdateTask`](mlupdatetask.md).

## Parameters

- `updateParameters`: Model training parameter values to replace those currently set in the update task.

## See Also

- [class MLParameterKey](mlparameterkey.md)
  The keys for the parameter dictionary in a model configuration or a model update context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlupdatetask/resume(withparameters:))*