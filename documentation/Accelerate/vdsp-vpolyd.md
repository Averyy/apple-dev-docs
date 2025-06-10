# vDSP_vpolyD

**Framework**: Accelerate  
**Kind**: func

Evaluates a double-precision polynomial using specified coefficients, variables, and strides.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_vpolyD(const double * __A, vDSP_Stride __IA, const double * __B, vDSP_Stride __IB, double * __C, vDSP_Stride __IC, vDSP_Length __N, vDSP_Length __P);
```

#### Discussion

For example, the following code evaluates the polynomial with the coefficients `[10.0, 20.0, 30.0]` and the variables `[7.0, 5.0]`:

```swift
    let stride = 1
    
    let coefficients: [Double] = [10, 20, 30]
    let variables: [Double] = [7, 5]
    
    let result = [Double](
        unsafeUninitializedCapacity: variables.count) {
            buffer, initializedCount in
            
            vDSP_vpolyD(coefficients, stride,
                        variables, stride,
                        buffer.baseAddress!, stride,
                        vDSP_Length(variables.count),
                        vDSP_Length(coefficients.count - 1))
            
            initializedCount = 2
        }
    
    // Prints "[660.0, 380.0]".
    //    result[0] = (10 * 7²) + (20 * 7¹) + (30 * 7⁰) = 660
    //    result[1] = (10 * 5²) + (20 * 5¹) + (30 * 5⁰) = 380
    print(result)
```

## Parameters

- `__A`: A vector that contains   coefficients.
- `__IA`: The distance between the elements in the input vector  .
- `__B`: A vector that contains the variables.
- `__IB`: The distance between the elements in the input vector  .
- `__C`: A vector that receives the result of the calculation.
- `__IC`: The distance between the elements in the output vector  .
- `__N`: The number of variables that the function processes to produce the same number of output elements.
- `__P`: The degree of the polynomial.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vpolyd)*