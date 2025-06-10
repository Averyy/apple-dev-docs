# integrate(_:using:stepSize:)

**Framework**: Accelerate  
**Kind**: method

Returns the integration of a single-precision vector using the specified rule.

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
static func integrate<U>(_ vector: U, using rule: vDSP.IntegrationRule, stepSize: Float = 1) -> [Float] where U : AccelerateBuffer, U.Element == Float
```

## See Also

- [static func integrate<U>(U, using: vDSP.IntegrationRule, stepSize: Double) -> [Double]](vdsp/integrate(_:using:stepsize:)-1bw3x.md)
  Returns the integration of a double-precision vector using the specified rule.
- [static func integrate<U, V>(U, using: vDSP.IntegrationRule, stepSize: Double, result: inout V)](vdsp/integrate(_:using:stepsize:result:)-75jvf.md)
  Performs the integration of a double-precision using the specified rule.
- [static func integrate<U, V>(U, using: vDSP.IntegrationRule, stepSize: Float, result: inout V)](vdsp/integrate(_:using:stepsize:result:)-44lew.md)
  Performs the integration of a single-precision using the specified rule.
- [vDSP.IntegrationRule](vdsp/integrationrule.md)
  Integration rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/integrate(_:using:stepsize:)-7wei4)*