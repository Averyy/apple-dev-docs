# vDSP_vpythgD

**Framework**: Accelerate  
**Kind**: func

Calculates the double-precision hypotenuses of right triangles with legs that are the differences of corresponding elements of two pairs of vectors.

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
extern void vDSP_vpythgD(const double * __A, vDSP_Stride __IA, const double * __B, vDSP_Stride __IB, const double * __C, vDSP_Stride __IC, const double * __D, vDSP_Stride __ID, double * __E, vDSP_Stride __IE, vDSP_Length __N);
```

#### Discussion

This function calculates the length of the hypotenuse of  number of triangles, where  is the number of elements in the supplied vectors. The differences between corresponding elements of vectors `x0` and `x1` and vectors `y0` and `y1` define the lengths of the two legs of each triangle.

The functions use the following operation:

```swift
for (n = 0; n < N; ++n)
    E[n] = sqrt((A[n]-B[n])**2 + (C[n]-D[n])**2);
```

For example, the following code calculates the hypotenuse of four Pythagorean triples:

```swift
    let stride = 1
    
    let a: [Double] = [3, 6, 5, 9]
    let b: [Double] = [0, 0, 0, 0]
    
    let c: [Double] = [0, 0, 0, 0]
    let d: [Double] = [4, 8, 12, 12]
    
    let hypotenuses = [Double](
        unsafeUninitializedCapacity: a.count) {
            buffer, initializedCount in
            
            vDSP_vpythgD(
                a, stride,
                b, stride,
                c, stride,
                d, stride,
                buffer.baseAddress!, stride,
                vDSP_Length(a.count)
            )
            
            initializedCount = a.count
        }
    
    // Prints "[5.0, 10.0, 13.0, 15.0]".
    print(hypotenuses)
```

## Parameters

- `__A`: A vector that contains the first values of the first set of legs of the triangles.
- `__IA`: The distance between the elements in the input vector  .
- `__B`: A vector that contains the second values of the first set of legs of the triangles.
- `__IB`: The distance between the elements in the input vector  .
- `__C`: A vector that contains the first values of the second set of legs of the triangles.
- `__IC`: The distance between the elements in the input vector  .
- `__D`: A vector that contains the second values of the second set of legs of the triangles.
- `__ID`: The distance between the elements in the input vector  .
- `__E`: A vector that receives the result of the calculation.
- `__IE`: The distance between the elements in the output vector  .
- `__N`: The number of elements to process.

## See Also

- [vDSP_vpythg](vdsp_vpythg.md)
  Calculates the single-precision hypotenuses of right triangles with legs that are the differences of corresponding elements of two pairs of vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vpythgd)*