# evaluatePolynomial(usingCoefficients:withVariables:result:)

**Framework**: Accelerate  
**Kind**: method

Evaluates a single-precision polynomial using specified coefficients and variables.

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
static func evaluatePolynomial<U, V>(usingCoefficients coefficients: [Float], withVariables variables: U, result: inout V) where U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == Float, V.Element == Float
```

#### Discussion

For example, the following code evaluates the polynomial with the coefficients `[10.0, 20.0, 30.0]` and the variables `[7.0, 5.0]`:

```swift
    let coefficients: [Float] = [10, 20, 30]
    let variables: [Float] = [7, 5]
    
    let result = [Float](
        unsafeUninitializedCapacity: variables.count) {
            buffer, initializedCount in
            
            vDSP.evaluatePolynomial(usingCoefficients: coefficients,
                                                 withVariables: variables,
                                    result: &buffer)
            
            initializedCount = 2
        }
   
    // Prints "[660.0, 380.0]".
    //    result[0] = (10 * 7²) + (20 * 7¹) + (30 * 7⁰) = 660
    //    result[1] = (10 * 5²) + (20 * 5¹) + (30 * 5⁰) = 380
    print(result)
```

## Parameters

- `coefficients`: An array that contains the coefficients.
- `variables`: An array that contains the independent variables.
- `result`: An array that receives the result of the calculation.

## See Also

- [static func evaluatePolynomial<U>(usingCoefficients: [Float], withVariables: U) -> [Float]](vdsp/evaluatepolynomial(usingcoefficients:withvariables:)-7mznu.md)
  Returns a single-precision evaluated polynomial using specified coefficients and variables.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/evaluatepolynomial(usingcoefficients:withvariables:result:)-6eaoc)*