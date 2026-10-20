# init(constantPadding:constantValue:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a padding layer with the constant padding sizes and constant value you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0

> **Deprecated**: Use Metal Performance Shaders Graph or BNNS instead.

## Declaration

```swift
convenience init(constantPadding: [Int], constantValue: Float)
```

## Parameters

- `constantPadding`: An array that contains the constant padding sizes.
- `constantValue`: The constant value you use to pad the source tensor.

## See Also

### Creating Padding Layers
- [convenience init(reflectionPadding: [Int])](./init%28reflectionpadding%29.md)
  Creates a padding layer with the reflection padding sizes you specify.
- [convenience init(symmetricPadding: [Int])](./init%28symmetricpadding%29.md)
  Creates a padding layer with the symmetric padding sizes you specify.
- [convenience init(zeroPadding: [Int])](./init%28zeropadding%29.md)
  Creates a padding layer with the zero padding sizes you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcpaddinglayer/init(constantpadding:constantvalue:))*