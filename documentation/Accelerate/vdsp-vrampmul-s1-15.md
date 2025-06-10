# vDSP_vrampmul_s1_15

**Framework**: Accelerate  
**Kind**: func

Generates a fixed-point 1.15 format vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
void vDSP_vrampmul_s1_15(const short * __I, vDSP_Stride __IS, short * __Start, const short * __Step, short * __O, vDSP_Stride __OS, vDSP_Length __N);
```

#### Discussion

Use this function to generate and return a vector populated with ramped values with each element multiplied by the corresponding element in a second vector.

The following code generates a ramped vector with values in the range `0 ... 7`. The function multiplies elements at even indices by `10` and multiplies elements at odd indices by `100`.

```swift
    let n = 8
    let stride = 1
    
    var initialValue: Double = 0
    var increment: Double = 1
    
    let ramp = [Double](unsafeUninitializedCapacity: n) {
        buffer, initializedCount in
        
        vDSP_vrampmulD([10, 100, 10, 100, 10, 100, 10, 100],
                       stride,
                       &initialValue,
                       &increment,
                       buffer.baseAddress!,
                       stride,
                       vDSP_Length(n))
        
        initializedCount = n
    }
    
    // Prints "[0.0, 100.0, 20.0, 300.0, 40.0, 500.0, 60.0, 700.0]".
    print(ramp)
    
    // Prints "8".
    print(initialValue)
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

- [vDSP_vrampmul](vdsp_vrampmul.md)
  Generates a single-precision vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.
- [vDSP_vrampmulD](vdsp_vrampmuld.md)
  Generates a double-precision vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.
- [vDSP_vrampmul_s8_24](vdsp_vrampmul_s8_24.md)
  Generates a fixed-point 8.24 format vector that contains monotonically incrementing or decrementing values, and multiplies that vector by a source vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vrampmul_s1_15)*