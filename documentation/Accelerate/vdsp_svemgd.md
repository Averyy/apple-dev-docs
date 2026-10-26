# vDSP_svemgD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the sum of magnitudes in a double-precision vector.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void vDSP_svemgD(const double *__A, vDSP_Stride __IA, double *__C, vDSP_Length __N);
```

#### Discussion

This function calculates the sum of magnitudes of the first `N` elements of `A` and writes the result to `C`:

![A diagram showing the operation of the vDSP_svemg function. There are three rows. The top row represents the input, vector A. The second row represents the summation operation. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the operation and from the operation to the output vector indicating the relationships between the input and output.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3226728@2x.png)

The operation is:

```c
C[0] = sum(|A[n]|, 0 <= n < N);
```

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Double] = [-1, 2, -3, 4, -5]
var c: Double = 0

// Calculate the sum of the magnitudes of the elements in `a`.
vDSP_svemgD(a, 1, &c, vDSP_Length(a.count))

// Prints "15.0".
print(c)
```

**Objective-C**:

```objc
double a[5] = {-1, 2, -3, 4, -5};
double c;

// Calculate the sum of the magnitudes of the elements in `a`.
vDSP_svemgD(a, 1, &c, 5);

// Prints "15".
printf("%g\n", c);
```

## Parameters

- `__A`: Single-precision real input vector.
- `__IA`: Stride for `A`
- `__C`: Single-precision real output scalar
- `__N`: The number of elements to process

## See Also

### Vector Summation
- [vDSP_sve](./vdsp_sve.md)
  Calculates the sum of values in a single-precision vector.
- [vDSP_sveD](./vdsp_sved.md)
  Calculates the sum of values in a double-precision vector.
- [vDSP_svemg](./vdsp_svemg.md)
  Calculates the sum of magnitudes in a single-precision vector.
- [vDSP_svesq](./vdsp_svesq.md)
  Calculates the sum of squares in a single-precision vector.
- [vDSP_svesqD](./vdsp_svesqd.md)
  Calculates the sum of squares in a double-precision vector.
- [vDSP_sve_svesq](./vdsp_sve_svesq.md)
  Calculates the sum of values and the sum of squares in a single-precision vector.
- [vDSP_sve_svesqD](./vdsp_sve_svesqd.md)
  Calculates the sum of values and the sum of squares in a double-precision vector.
- [vDSP_svs](./vdsp_svs.md)
  Calculates the sum of signed squares in a single-precision vector.
- [vDSP_svsD](./vdsp_svsd.md)
  Calculates the sum of signed squares in a double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_svemgd)*