# MLCYOLOLossLayer

**Framework**: ML Compute  
**Kind**: class

A layer that estimates loss for the YOLO algorithm.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCYOLOLossLayer
```

## Topics

### Creating YOLO Loss Layers
- [convenience init(descriptor: MLCYOLOLossDescriptor)](mlcyololosslayer/init(descriptor:).md)
  Creates a YOLO loss layer with the descriptor you specify.
- [class MLCYOLOLossDescriptor](mlcyololossdescriptor.md)
  The configuration object you use to create the YOLO loss layer.
### Inspecting YOLO Loss Layers
- [var yoloLossDescriptor: MLCYOLOLossDescriptor](mlcyololosslayer/yololossdescriptor.md)
  The configuration object you use to create the YOLO loss layer.

## Relationships

### Inherits From
- [MLCLossLayer](mlclosslayer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MLCLossLayer](mlclosslayer.md)
  A layer that estimates the inaccuracies of the model to reduce the loss on the next evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcyololosslayer)*