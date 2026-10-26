# vDSP_sve_svesqD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the sum of values and the sum of squares in a double-precision vector.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void vDSP_sve_svesqD(const double *__A, vDSP_Stride __IA, double *__Sum, double *__SumOfSquares, vDSP_Length __N);
```

#### Discussion

This function calculates the sum of values and the sum of squares of the first `N` elements of `A` and writes the result to `Sum` and `SumOfSquares` respectively:

![A diagram showing the operation of the vDSP_sve_svesq function. There are three rows. The top row represents the input, vector A. The second row represents the summation operations. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the operation and from the operation to the output vector indicating the relationships between the input and output.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3226729@2x.png)

The operation is:

```c
Sum          = sum(A[n],      0 <= n < N);
SumOfSquares = sum(A[n] ** 2, 0 <= n < N);
```

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Double] = [1, 2, 3, 4, 5]
var sum: Double = 0
var sumOfSquares: Double = 0

// Calculate both the sum and the sum of squares of the elements in `a`.
vDSP_sve_svesqD(a, 1, &sum, &sumOfSquares, vDSP_Length(a.count))

// Prints "15.0".
print(sum)
// Prints "55.0".
print(sumOfSquares)
```

**Objective-C**:

```objc
double a[5] = {1, 2, 3, 4, 5};
double sum;
double sumOfSquares;

// Calculate both the sum and the sum of squares of the elements in `a`.
vDSP_sve_svesqD(a, 1, &sum, &sumOfSquares, 5);

// Prints "15".
printf("%g\n", sum);
// Prints "55".
printf("%g\n", sumOfSquares);
```

## Parameters

- `__A`: Double-precision input vector.
- `__IA`: Stride for the input vector.
- `__Sum`: Double-precision sum (scalar) of the elements of `A`.
- `__SumOfSquares`: Double-precision sum (scalar) of the squares of the elements of `A`.
- `__N`: Number of elements in `A`.

## See Also

### Vector Summation
- [vDSP_sve](./vdsp_sve.md)
  Calculates the sum of values in a single-precision vector.
- [vDSP_sveD](./vdsp_sved.md)
  Calculates the sum of values in a double-precision vector.
- [vDSP_svemg](./vdsp_svemg.md)
  Calculates the sum of magnitudes in a single-precision vector.
- [vDSP_svemgD](./vdsp_svemgd.md)
  Calculates the sum of magnitudes in a double-precision vector.
- [vDSP_svesq](./vdsp_svesq.md)
  Calculates the sum of squares in a single-precision vector.
- [vDSP_svesqD](./vdsp_svesqd.md)
  Calculates the sum of squares in a double-precision vector.
- [vDSP_sve_svesq](./vdsp_sve_svesq.md)
  Calculates the sum of values and the sum of squares in a single-precision vector.
- [vDSP_svs](./vdsp_svs.md)
  Calculates the sum of signed squares in a single-precision vector.
- [vDSP_svsD](./vdsp_svsd.md)
  Calculates the sum of signed squares in a double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_sve_svesqd)*