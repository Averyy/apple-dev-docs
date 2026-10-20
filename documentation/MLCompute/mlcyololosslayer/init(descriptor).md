# init(descriptor:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a YOLO loss layer with the descriptor you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(descriptor lossDescriptor: MLCYOLOLossDescriptor)
```

```objc
+ (instancetype) layerWithDescriptor:(MLCYOLOLossDescriptor *) lossDescriptor;
```

## Parameters

- `lossDescriptor`: An object used to configure the YOLO loss layer.

## See Also

### Creating YOLO Loss Layers
- [class MLCYOLOLossDescriptor](../mlcyololossdescriptor.md)
  The configuration object you use to create the YOLO loss layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcyololosslayer/init(descriptor:))*