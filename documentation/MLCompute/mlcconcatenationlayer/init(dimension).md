# init(dimension:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a concatenation layer with the dimension you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(dimension: Int)
```

```objc
+ (instancetype) layerWithDimension:(NSUInteger) dimension;
```

## Parameters

- `dimension`: The dimension, or axis, along which you concatenate tensors.

## See Also

### Creating Concatenation Layers
- [convenience init()](./init%28%29.md)
  Creates a concatenation layer with a dimension value of 1, which typically represents feature channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcconcatenationlayer/init(dimension:))*