# init(descriptor:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a matrix multiplication layer with the specified descriptor you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init?(descriptor: MLCMatMulDescriptor)
```

```objc
+ (instancetype) layerWithDescriptor:(MLCMatMulDescriptor *) descriptor;
```

## Parameters

- `descriptor`: An object you use to configure the matrix multiplication layer.

## See Also

### Creating Matrix Multiplication Layers
- [class MLCMatMulDescriptor](../mlcmatmuldescriptor.md)
  A configuration object you use to create a matrix multiplication layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcmatmullayer/init(descriptor:))*