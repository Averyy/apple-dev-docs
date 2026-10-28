# layerWithConstantPadding:constantValue:

**Framework**: ML Compute  
**Kind**: method  
**Role**: Type Method

Creates a padding layer with the constant padding sizes and constant valu you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```objc
+ (instancetype) layerWithConstantPadding:(NSArray<NSNumber *> *) padding constantValue:(float) constantValue;
```

## Return Value

A constant padding layer.

## Parameters

- `padding`: An array that contains the constant padding sizes.
- `constantValue`: The constant value to pad the source tensor.

## See Also

### Creating Padding Layers
- [+ layerWithReflectionPadding:](./layerwithreflectionpadding_.md)
  Creates a padding layer with the reflection padding sizes you specify.
- [+ layerWithSymmetricPadding:](./layerwithsymmetricpadding_.md)
  Creates a padding layer with the symmetric padding sizes you specify.
- [+ layerWithZeroPadding:](./layerwithzeropadding_.md)
  Creates a padding layer with the zero padding sizes you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcpaddinglayer/layerwithconstantpadding:constantvalue:)*