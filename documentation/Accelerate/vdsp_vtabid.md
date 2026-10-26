# vDSP_vtabiD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Generates a double-precision vector by interpolating values from a lookup table.

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
extern void vDSP_vtabiD(const double *__A, vDSP_Stride __IA, const double *__S1, const double *__S2, const double *__C, vDSP_Length __M, double *__D, vDSP_Stride __ID, vDSP_Length __N);
```

#### Discussion

The following code shows the result of linearly interpolating a lookup table that contains the values `[-10, 0, 100]` using the offsets `[0, 0.5, 1, 1.5, 2]`.  The integer offsets, `0`, `1`, and `2`, return the corresponding values in the lookup table, `-10`, `0`, and `2`. The noninteger offsets, `0.5` and `1.5`, return the linearly interpolated values between the lookup table values, `-5` and `50`:

**Swift**:

```swift
let offsets: [Double] = [0, 0.5, 1, 1.5, 2]
let lookupTable: [Double] = [-10, 0, 100]

var scale: Double = 1
var baseOffset: Double = 0

let n = offsets.count
let m = lookupTable.count

let stride = 1

let values = [Double](unsafeUninitializedCapacity: n) {
    buffer, initializedCount in
    
    vDSP_vtabiD(offsets, stride,
                &scale,
                &baseOffset,
                lookupTable, vDSP_Length(m),
                buffer.baseAddress!, stride, vDSP_Length(n))
    
    initializedCount = n
}

// Prints "[-10.0, -5.0, 0.0, 50.0, 100.0]".
print(values)
```

**Objective-C**:

```objc
double offsets[5] = {0, 0.5, 1, 1.5, 2};
double lookupTable[3] = {-10, 0, 100};

double scale = 1;
double baseOffset = 0;

double values[5];

vDSP_vtabiD(offsets, 1,
            &scale,
            &baseOffset,
            lookupTable, 3,
            values, 1, 5);

// Prints "[-10, -5, 0, 50, 100]".
printf("[%g, %g, %g, %g, %g]\n",
      values[0], values[1], values[2], values[3], values[4]);
```

## Parameters

- `__A`: The input vector that defines the offsets into the lookup table.
- `__IA`: The distance between the elements in the offsets vector.
- `__S1`: The scale factor.
- `__S2`: The base offset.
- `__C`: The input vector that defines the lookup table.
- `__M`: The number of elements in the lookup table.
- `__D`: The output vector.
- `__ID`: The distance between the elements in the output vector.
- `__N`: The number of elements in the offsets and output vectors.

## See Also

### Vector generation with lookup tables
- [vDSP_vtabi](./vdsp_vtabi.md)
  Generates a single-precision vector by interpolating values from a lookup table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vtabid)*