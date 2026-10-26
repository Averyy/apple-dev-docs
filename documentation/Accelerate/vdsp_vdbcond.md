# vDSP_vdbconD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Converts single-precision power or amplitude values to decibel values.

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
extern void vDSP_vdbconD(const double *__A, vDSP_Stride __IA, const double *__B, double *__C, vDSP_Stride __IC, vDSP_Length __N, unsigned int __F);
```

#### Discussion

The function uses the following calculation to perform the conversion:

```c
If Flag is 1:
    alpha = 20;
If Flag is 0:
    alpha = 10;

for (n = 0; n < N; ++n)
    C[n] = alpha * log10(A[n] / B[0]);
```

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Double] = [1, 10, 100]
var reference: Double = 1
var c = [Double](repeating: 0, count: a.count)

// Convert the power values in `a` to decibels, relative to a reference of `1`.
vDSP_vdbconD(a, 1, &reference, &c, 1, vDSP_Length(a.count), 0)

// Prints "[0.0, 10.0, 20.0]".
print(c)
```

**Objective-C**:

```objc
double a[3] = {1, 10, 100};
double reference = 1;
double c[3];

// Convert the power values in `a` to decibels, relative to a reference of `1`.
vDSP_vdbconD(a, 1, &reference, c, 1, 3, 0);

// Prints "[0, 10, 20]".
printf("[%g, %g, %g]\n", c[0], c[1], c[2]);
```

## Parameters

- `__A`: The input vector.
- `__IA`: The distance between the elements in the input vector.
- `__B`: The zero reference that the function uses for the conversion.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.` `
- `__N`: The number of elements that the function processes.
- `__F`: A value that specifies whether the function converts from power values or amplitude values. Set to `0` to specify power or `1` to specify amplitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vdbcond)*