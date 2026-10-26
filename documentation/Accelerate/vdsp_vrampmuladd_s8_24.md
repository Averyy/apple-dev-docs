# vDSP_vrampmuladd_s8_24

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Adds a fixed-point 8.24 format vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
void vDSP_vrampmuladd_s8_24(const int *__I, vDSP_Stride __IS, int *__Start, const int *__Step, int *__O, vDSP_Stride __OS, vDSP_Length __N);
```

#### Discussion

Use this function to generate and return a vector populated with ramped values with each element multiplied by the corresponding element in a second vector. This function is similar to [`vDSP_vrampmul`](./vdsp_vrampmul.md) but adds the result to the output vector.

The following code generates a ramped vector with values in the range `0 ... 7`. The function multiplies elements at even indices by `10` and multiplies elements at odd indices by `100`, and adds the ramp values to the existing values in the output buffer:

**Swift**:

```swift
    let n = 8
    let input: [Int32] = [10, 100, 10, 100, 10, 100, 10, 100]
    var output: [Int32] = Array(repeating: 1000, count: n)

    var start: Int32 = 0
    var step: Int32 = 1 << 24   // 1.0 in Q8.24

    vDSP_vrampmuladd_s8_24(input, 1,
                           &start,
                           &step,
                           &output, 1,
                           vDSP_Length(n))

    // Prints "[1000, 1100, 1020, 1300, 1040, 1500, 1060, 1700]".
    print(output)

    // Prints "134217728".
    print(start)
```

**Objective-C**:

```objc
int input[8] = {10, 100, 10, 100, 10, 100, 10, 100};
int output[8] = {1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000};

int startVal = 0;
int stepVal = 1 << 24;   // 1.0 in Q8.24

vDSP_vrampmuladd_s8_24(input, 1,
                       &startVal,
                       &stepVal,
                       output, 1,
                       8);

// Prints "[1000, 1100, 1020, 1300, 1040, 1500, 1060, 1700]".
printf("[%d, %d, %d, %d, %d, %d, %d, %d]\n",
      output[0], output[1], output[2], output[3],
      output[4], output[5], output[6], output[7]);

// Prints "134217728".
printf("%d\n", startVal);
```

## Parameters

- `__I`: The input vector that the function multiplies by the ramp.
- `__IS`: The distance between the elements in the input vector.
- `__Start`: On input, the initial value of the ramp. On output, the next value in the ramp.
- `__Step`: The increment, or decrement if negative, between each generated element.
- `__O`: The output vector.
- `__OS`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

### Vector addition with ramps and multiplication by a second vector
- [vDSP_vrampmuladd](./vdsp_vrampmuladd.md)
  Adds a single-precision vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.
- [vDSP_vrampmuladdD](./vdsp_vrampmuladdd.md)
  Adds a double-precision vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.
- [vDSP_vrampmuladd_s1_15](./vdsp_vrampmuladd_s1_15.md)
  Adds a fixed-point 1.15 format vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vrampmuladd_s8_24)*