# init(shape:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates an upsample layer with the shape you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0

> **Deprecated**: Use Metal Performance Shaders Graph or BNNS instead.

## Declaration

```swift
convenience init?(shape: [Int])
```

## Parameters

- `shape`: An array that contains the dimensions of the result tensor.

## See Also

### Creating Upsample Layers
- [convenience init?(shape: [Int], sampleMode: MLCSampleMode, alignsCorners: Bool)](./init%28shape,samplemode,alignscorners%29.md)
  Creates an upsample layer with the shape, upsampling algorithm, and corner alignment option you specify.
- [enum MLCSampleMode](../mlcsamplemode.md)
  A sampling mode for an upsample layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcupsamplelayer/init(shape:))*