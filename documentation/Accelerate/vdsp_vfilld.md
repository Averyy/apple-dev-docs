# vDSP_vfillD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Populates a double-precision vector with a specified scalar value.

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
extern void vDSP_vfillD(const double *__A, double *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

The functions in this group populate a vector with a specified scalar value.

The following code shows how to clear the array `c`, setting the value of each element to pi:

**Swift**:

```swift
let n = vDSP_Length(10)
let stride = vDSP_Stride(1)

var a = Double.pi

var c = [Double](repeating: .nan,
                 count: Int(n))

vDSP_vfillD(&a,
            &c,
            stride,
            n)

// Prints "[3.1416, 3.1416, 3.1416,
//          3.1416, 3.1416, 3.1416,
//          3.1416, 3.1416, 3.1416,
//          3.1416]".
print(c)
```

**Objective-C**:

```objc
vDSP_Length n = 10;
vDSP_Stride stride = 1;

double a = M_PI;

double c[10];
for (int i = 0; i < 10; i++) c[i] = NAN;

vDSP_vfillD(&a,
            c,
            stride,
            n);

// Prints "[3.1416, 3.1416, 3.1416, 3.1416, 3.1416,
//          3.1416, 3.1416, 3.1416, 3.1416, 3.1416]".
printf("[%g, %g, %g, %g, %g, %g, %g, %g, %g, %g]\n",
      c[0], c[1], c[2], c[3], c[4],
      c[5], c[6], c[7], c[8], c[9]);
```

## See Also

### Filling Vectors with a Single Scalar Value
- [vDSP_vfill](./vdsp_vfill.md)
  Populates a single-precision vector with a specified scalar value.
- [vDSP_vfilli](./vdsp_vfilli.md)
  Populates an integer vector with a specified scalar value.
- [vDSP_zvfill](./vdsp_zvfill.md)
  Populates a complex single-precision vector with a specified scalar value.
- [vDSP_zvfillD](./vdsp_zvfilld.md)
  Populates a complex double-precision vector with a specified scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vfilld)*