# domain

**Framework**: PHASE  
**Kind**: property

The range of the envelope’s possible input values.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var domain: PHASENumericPair { get }
```

#### Discussion

This property is an ordered pair that describes input values along the  axis for which the [`evaluate(x:)`](phaseenvelope/evaluate(x:).md) function can produce a non-zero output. The first number in the pair is the minimum input value, and the second number in the pair is the maximum input value.

When an envelope graphs volume over time, the framework scales the domain by [`unitsPerSecond`](phaseengine/unitspersecond.md).  Likewise, when an envelope graphs volume over distance, the framework scales this property by [`unitsPerMeter`](phaseengine/unitspermeter.md).

## See Also

- [var range: PHASENumericPair](phaseenvelope/range.md)
  The bounds of the output value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseenvelope/domain)*