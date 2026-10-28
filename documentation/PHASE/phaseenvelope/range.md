# range

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

The bounds of the output value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var range: PHASENumericPair { get }
```

```objc
@property (nonatomic, strong, readonly) PHASENumericPair * range;
```

## Discussion

This property is an ordered pair that defines the range of possible output values along the *y* axis for the [`evaluate(x:)`](./evaluate%28x%29.md) function. The first number in the pair is the minimum output value, and the second number in the pair is the maximum output value.

## See Also

### Bounding the Input
- [var domain: PHASENumericPair](./domain.md)
  The range of the envelope’s possible input values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseenvelope/range)*