# vDSP_vgenD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Generates a double-precision vector that contains monotonically incrementing or decrementing values within a range.

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
extern void vDSP_vgenD(const double *__A, const double *__B, double *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

Use this function to generate and return a vector populated with ramped values.

The following code generates a ramped vector with values in the range `0 ... 7`:

**Swift**:

```swift
    let n = 8
    let stride = 1
    
    var start: Double = 0
    var end: Double = 7
    
    let ramp = [Double](unsafeUninitializedCapacity: n) {
        buffer, initializedCount in
        
        vDSP_vgenD(&start,
                   &end,
                   buffer.baseAddress!,
                   stride,
                   vDSP_Length(n))
        
        initializedCount = n
    }
    
    // Prints "[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]".
    print(ramp)
```

**Objective-C**:

```objc
int n = 8;
vDSP_Stride stride = 1;

double start = 0;
double end = 7;

double ramp[8] = {0};

vDSP_vgenD(&start,
           &end,
           ramp,
           stride,
           (vDSP_Length)n);

// Prints "[0, 1, 2, 3, 4, 5, 6, 7]".
printf("[%g, %g, %g, %g, %g, %g, %g, %g]\n",
       ramp[0], ramp[1], ramp[2], ramp[3],
       ramp[4], ramp[5], ramp[6], ramp[7]);
```

## Parameters

- `__A`: The start value of the ramp.
- `__B`: The end value of the ramp.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

### Vector generation with ramps using a range
- [vDSP_vgen](./vdsp_vgen.md)
  Generates a single-precision vector that contains monotonically incrementing or decrementing values within a range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vgend)*