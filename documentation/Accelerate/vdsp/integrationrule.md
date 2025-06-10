# vDSP.IntegrationRule

**Framework**: Accelerate  
**Kind**: enum

Integration rules.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
enum IntegrationRule
```

## Topics

### Enumeration Cases
- [vDSP.IntegrationRule.runningSum](vdsp/integrationrule/runningsum.md)
- [vDSP.IntegrationRule.simpson](vdsp/integrationrule/simpson.md)
- [vDSP.IntegrationRule.trapezoidal](vdsp/integrationrule/trapezoidal.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [static func integrate<U>(U, using: vDSP.IntegrationRule, stepSize: Double) -> [Double]](vdsp/integrate(_:using:stepsize:)-1bw3x.md)
  Returns the integration of a double-precision vector using the specified rule.
- [static func integrate<U>(U, using: vDSP.IntegrationRule, stepSize: Float) -> [Float]](vdsp/integrate(_:using:stepsize:)-7wei4.md)
  Returns the integration of a single-precision vector using the specified rule.
- [static func integrate<U, V>(U, using: vDSP.IntegrationRule, stepSize: Double, result: inout V)](vdsp/integrate(_:using:stepsize:result:)-75jvf.md)
  Performs the integration of a double-precision using the specified rule.
- [static func integrate<U, V>(U, using: vDSP.IntegrationRule, stepSize: Float, result: inout V)](vdsp/integrate(_:using:stepsize:result:)-44lew.md)
  Performs the integration of a single-precision using the specified rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/integrationrule)*