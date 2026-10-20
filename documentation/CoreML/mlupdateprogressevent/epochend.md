# epochEnd

**Framework**: Core ML  
**Kind**: property  
**Role**: Type Property

An event that represents the end of training epoch.

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
static var epochEnd: MLUpdateProgressEvent { get }
```

```c
MLUpdateProgressEventEpochEnd
```

## See Also

### Getting progress event types
- [static var trainingBegin: MLUpdateProgressEvent](./trainingbegin.md)
  An event that represents the start of training.
- [static var miniBatchEnd: MLUpdateProgressEvent](./minibatchend.md)
  An event that represents the end of a mini-batch within a training epoch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlupdateprogressevent/epochend)*