# vDSP_vrampmuladd_s1_15

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Adds a fixed-point 1.15 format vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.

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
void vDSP_vrampmuladd_s1_15(const short *__I, vDSP_Stride __IS, short *__Start, const short *__Step, short *__O, vDSP_Stride __OS, vDSP_Length __N);
```

## Discussion

Use this function to generate and return a vector populated with ramped values with each element multiplied by the corresponding element in a second vector. This function is similar to [`vDSP_vrampmul`](./vdsp_vrampmul.md) but adds the result to the output vector.

The following code generates a ramped vector with values in the range `0 ... 7`. The function multiplies elements at even indices by `10` and multiplies elements at odd indices by `100`, and adds the ramp values to the existing values in the output buffer:

**Swift**:

```swift
    let n = 8
    let stride = 1

    let input: [Int16] = [10, 100, 10, 100, 10, 100, 10, 100]
    var output: [Int16] = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]

    var initialValue: Int16 = 0
    var increment: Int16 = 32767   // approx 1.0 in Q1.15

    vDSP_vrampmuladd_s1_15(input, stride,
                           &initialValue,
                           &increment,
                           &output, stride,
                           vDSP_Length(n))

    // Prints "[1000, 1099, 999, 1099, 999, 1099, 999, 1099]".
    print(output)

    // Prints "-8".
    print(initialValue)
```

**Objective-C**:

```objc
short input[8] = {10, 100, 10, 100, 10, 100, 10, 100};
short output[8] = {1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000};

short startVal = 0;
short stepVal = 32767;   // approx 1.0 in Q1.15

vDSP_vrampmuladd_s1_15(input, 1,
                       &startVal,
                       &stepVal,
                       output, 1,
                       8);

// Prints "[1000, 1099, 999, 1099, 999, 1099, 999, 1099]".
printf("[%d, %d, %d, %d, %d, %d, %d, %d]\n",
      (int)output[0], (int)output[1], (int)output[2], (int)output[3],
      (int)output[4], (int)output[5], (int)output[6], (int)output[7]);

// Prints "-8".
printf("%d\n", (int)startVal);
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
- [vDSP_vrampmuladd_s8_24](./vdsp_vrampmuladd_s8_24.md)
  Adds a fixed-point 8.24 format vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vrampmuladd_s1_15)*