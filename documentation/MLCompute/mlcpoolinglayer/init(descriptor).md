# init(descriptor:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a pooling layer with the descriptor you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(descriptor: MLCPoolingDescriptor)
```

```objc
+ (instancetype) layerWithDescriptor:(MLCPoolingDescriptor *) descriptor;
```

## Parameters

- `descriptor`: An object you use to configure the pooling layer.

## See Also

### Creating Pooling Layers
- [class MLCPoolingDescriptor](../mlcpoolingdescriptor.md)
  A configuration object you use to create a pooling layer.
- [enum MLCPoolingType](../mlcpoolingtype-wb8j.md)
  A pooling function type for a pooling layer.
- [MLCPoolingType](../mlcpoolingtype-8hrit.md)
  A pooling function type for a pooling layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcpoolinglayer/init(descriptor:))*