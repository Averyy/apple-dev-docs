# vDSP_vfilli

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Populates an integer vector with a specified scalar value.

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
extern void vDSP_vfilli(const int *__A, int *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

The functions in this group populate a vector with a specified scalar value.

The following code shows how to clear the array `c`, setting the value of each element to pi:

**Swift**:

```swift
let n = vDSP_Length(10)
let stride = vDSP_Stride(1)

var a: Int32 = 7

var c = [Int32](repeating: 0,
                count: Int(n))

vDSP_vfilli(&a,
            &c,
            stride,
            n)

// Prints "[7, 7, 7, 7, 7, 7, 7, 7, 7, 7]".
print(c)
```

**Objective-C**:

```objc
vDSP_Length n = 10;
vDSP_Stride stride = 1;

int a = 7;

int c[10] = {0};

vDSP_vfilli(&a,
            c,
            stride,
            n);

// Prints "[7, 7, 7, 7, 7, 7, 7, 7, 7, 7]".
printf("[%d, %d, %d, %d, %d, %d, %d, %d, %d, %d]\n",
      c[0], c[1], c[2], c[3], c[4],
      c[5], c[6], c[7], c[8], c[9]);
```

## See Also

### Filling Vectors with a Single Scalar Value
- [vDSP_vfill](./vdsp_vfill.md)
  Populates a single-precision vector with a specified scalar value.
- [vDSP_vfillD](./vdsp_vfilld.md)
  Populates a double-precision vector with a specified scalar value.
- [vDSP_zvfill](./vdsp_zvfill.md)
  Populates a complex single-precision vector with a specified scalar value.
- [vDSP_zvfillD](./vdsp_zvfilld.md)
  Populates a complex double-precision vector with a specified scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vfilli)*