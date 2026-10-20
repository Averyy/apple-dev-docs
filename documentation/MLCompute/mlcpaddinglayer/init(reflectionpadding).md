# init(reflectionPadding:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a padding layer with the reflection padding sizes you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0

> **Deprecated**: Use Metal Performance Shaders Graph or BNNS instead.

## Declaration

```swift
convenience init(reflectionPadding: [Int])
```

## Parameters

- `reflectionPadding`: An array that contains the reflection padding sizes.

## See Also

### Creating Padding Layers
- [convenience init(symmetricPadding: [Int])](./init%28symmetricpadding%29.md)
  Creates a padding layer with the symmetric padding sizes you specify.
- [convenience init(zeroPadding: [Int])](./init%28zeropadding%29.md)
  Creates a padding layer with the zero padding sizes you specify.
- [convenience init(constantPadding: [Int], constantValue: Float)](./init%28constantpadding,constantvalue%29.md)
  Creates a padding layer with the constant padding sizes and constant value you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcpaddinglayer/init(reflectionpadding:))*