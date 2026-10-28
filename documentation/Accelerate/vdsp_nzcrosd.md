# vDSP_nzcrosD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Counts and finds the zero crossings in a double-precision vector.

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
extern void vDSP_nzcrosD(const double *__A, vDSP_Stride __IA, vDSP_Length __B, vDSP_Length *__C, vDSP_Length *__D, vDSP_Length __N);
```

## Discussion

This function is the same as [`vDSP_nzcros`](./vdsp_nzcros.md), except for the type of the input vector.

The following code shows an example of using this function:

**Swift**:

```swift
var a: [Double] = [1, -1, 1, -1, 2]
var lastCrossingIndex: vDSP_Length = 0
var crossingCount: vDSP_Length = 0

// Count the zero crossings in `a`, and find the index of the last one.
vDSP_nzcrosD(a, 1, 4, &lastCrossingIndex, &crossingCount, vDSP_Length(a.count))

// Prints "4".
print(crossingCount)
// Prints "4".
print(lastCrossingIndex)
```

**Objective-C**:

```objc
double a[5] = {1, -1, 1, -1, 2};
vDSP_Length lastCrossingIndex;
vDSP_Length crossingCount;

// Count the zero crossings in `a`, and find the index of the last one.
vDSP_nzcrosD(a, 1, 4, &lastCrossingIndex, &crossingCount, 5);

// Prints "4".
printf("%lu\n", crossingCount);
// Prints "4".
printf("%lu\n", lastCrossingIndex);
```

## See Also

### Single-Vector Zero Crossing Search
- [vDSP_nzcros](./vdsp_nzcros.md)
  Counts and finds the zero crossings in a single-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_nzcrosd)*