# effectWithCumulative

**Framework**: Symbols  
**Kind**: method  
**Role**: Instance Method

An effect that enables each layer of a symbol-based image in sequence.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
- (instancetype) effectWithCumulative;
```

#### Return Value

A copy of the symbol effect options that uses the `cumulative` animation.

#### Discussion

This effect enables each successive variable layer, and the layer remains enabled until the end of the animation cycle. This effect cancels the [`iterative`](../variablecolorsymboleffect/iterative.md) variant.

## See Also

### Controlling fill style
- [- effectWithIterative](./effectwithiterative.md)
  An effect that momentarily enables each layer of a symbol-based image in sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/symbols/nssymbolvariablecoloreffect/effectwithcumulative)*