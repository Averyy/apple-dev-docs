# vDSP_vlim

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the single-precision vector test limit using the specified stride.

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
extern void vDSP_vlim(const float *__A, vDSP_Stride __IA, const float *__B, const float *__C, float *__D, vDSP_Stride __ID, vDSP_Length __N);
```

## Discussion

Compares values from vector `A` to limit scalar `*B`. For inputs greater than or equal to `*B`, scalar `*C` is written to `D` . For inputs  less than `*B`, the negated value of scalar `*C` is written to vector  `D`.

This calculates the following:

```objc
    for (n = 0; n < N; ++n)
        if (*B <= A[n*IA])
            D[n*ID] = *C;
        else
            D[n*ID] = -(*C);
```

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Float] = [-2, -0.5, 0.5, 3]
var limit: Float = 0
var value: Float = 2
var d = [Float](repeating: 0, count: a.count)

// Apply a test limit: output `+value` where `a[i]` is at least `limit`, and `-value` otherwise.
vDSP_vlim(a, 1, &limit, &value, &d, 1, vDSP_Length(a.count))

// Prints "[-2.0, -2.0, 2.0, 2.0]".
print(d)
```

**Objective-C**:

```objc
float a[4] = {-2, -0.5, 0.5, 3};
float limit = 0;
float value = 2;
float d[4];

// Apply a test limit: output `+value` where `a[i]` is at least `limit`, and `-value` otherwise.
vDSP_vlim(a, 1, &limit, &value, d, 1, 4);

// Prints "[-2, -2, 2, 2]".
printf("[%g, %g, %g, %g]\n", d[0], d[1], d[2], d[3]);
```

## Parameters

- `__A`: Single-precision real input vector
- `__IA`: Stride for `A`
- `__B`: Pointer to single-precision real input scalar: limit
- `__C`: Pointer to single-precision real input scalar
- `__D`: Single-precision real output vector
- `__ID`: Stride for `D`
- `__N`: The number of elements to process

## See Also

### Limit Operations
- [vDSP_vlimD](./vdsp_vlimd.md)
  Calculates the double-precision vector test limit using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vlim)*