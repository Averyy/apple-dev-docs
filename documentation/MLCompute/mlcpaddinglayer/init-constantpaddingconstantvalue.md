# init(constantPadding:constantValue:)

**Framework**: ML Compute  
**Kind**: init

Creates a padding layer with the constant padding sizes and constant value you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init(constantPadding: [Int], constantValue: Float)
```

## Parameters

- `constantPadding`: An array that contains the constant padding sizes.
- `constantValue`: The constant value you use to pad the source tensor.

## See Also

- [convenience init(reflectionPadding: [Int])](mlcpaddinglayer/init(reflectionpadding:).md)
  Creates a padding layer with the reflection padding sizes you specify.
- [convenience init(symmetricPadding: [Int])](mlcpaddinglayer/init(symmetricpadding:).md)
  Creates a padding layer with the symmetric padding sizes you specify.
- [convenience init(zeroPadding: [Int])](mlcpaddinglayer/init(zeropadding:).md)
  Creates a padding layer with the zero padding sizes you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcpaddinglayer/init(constantpadding:constantvalue:))*