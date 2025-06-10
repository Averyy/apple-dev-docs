# evaluatePolynomial(usingCoefficients:withVariables:)

**Framework**: Accelerate  
**Kind**: method

Returns a single-precision evaluated polynomial using specified coefficients and variables.

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
static func evaluatePolynomial<U>(usingCoefficients coefficients: [Float], withVariables variables: U) -> [Float] where U : AccelerateBuffer, U.Element == Float
```

#### Discussion

For example, the following code evaluates the polynomial with the coefficients `[10.0, 20.0, 30.0]` and the variables `[7.0, 5.0]`:

```swift
    let coefficients: [Float] = [10, 20, 30]
    let variables: [Float] = [7, 5]
    
    let result = vDSP.evaluatePolynomial(usingCoefficients: coefficients,
                                         withVariables: variables)
    
    // Prints "[660.0, 380.0]".
    //    result[0] = (10 * 7²) + (20 * 7¹) + (30 * 7⁰) = 660
    //    result[1] = (10 * 5²) + (20 * 5¹) + (30 * 5⁰) = 380
    print(result)
```

## Parameters

- `coefficients`: An array that contains the coefficients.
- `variables`: An array that contains the independent variables.

## See Also

- [static func evaluatePolynomial<U, V>(usingCoefficients: [Float], withVariables: U, result: inout V)](vdsp/evaluatepolynomial(usingcoefficients:withvariables:result:)-6eaoc.md)
  Evaluates a single-precision polynomial using specified coefficients and variables.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/evaluatepolynomial(usingcoefficients:withvariables:)-7mznu)*