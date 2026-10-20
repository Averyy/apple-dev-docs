# MLCYOLOLossLayer

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A layer that estimates loss for the YOLO algorithm.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCYOLOLossLayer
```

```objc
@interface MLCYOLOLossLayer : MLCLossLayer
```

## Topics

### Creating YOLO Loss Layers
- [convenience init(descriptor: MLCYOLOLossDescriptor)](./mlcyololosslayer/init%28descriptor%29.md)
  Creates a YOLO loss layer with the descriptor you specify.
- [class MLCYOLOLossDescriptor](./mlcyololossdescriptor.md)
  The configuration object you use to create the YOLO loss layer.
### Inspecting YOLO Loss Layers
- [var yoloLossDescriptor: MLCYOLOLossDescriptor](./mlcyololosslayer/yololossdescriptor.md)
  The configuration object you use to create the YOLO loss layer.

## Relationships

### Inherits From
- [MLCLossLayer](./mlclosslayer.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Loss Layers
- [class MLCLossLayer](./mlclosslayer.md)
  A layer that estimates the inaccuracies of the model to reduce the loss on the next evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcyololosslayer)*