# init(descriptor:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates an activation layer with the descriptor you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(descriptor: MLCActivationDescriptor)
```

```objc
+ (instancetype) layerWithDescriptor:(MLCActivationDescriptor *) descriptor;
```

## Parameters

- `descriptor`: An object you use to configure the activation layer.

## See Also

### Creating Activation Layers
- [Preconfigured Activation Layers](../preconfigured-activation-layers.md)
  Obtain a preconfigured activation layer with common behavior.
- [class MLCActivationDescriptor](../mlcactivationdescriptor.md)
  A configuration object you use to create an activation layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcactivationlayer/init(descriptor:))*