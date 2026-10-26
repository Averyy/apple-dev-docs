# vDSP_vramp

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Generates a single-precision vector with monotonically incrementing or decrementing values using an initial value and increment.

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
extern void vDSP_vramp(const float *__A, const float *__B, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

Use this function to generate and return a vector populated with ramped values.

The following code generates a ramped vector with values in the range `0 ... 7`:

**Swift**:

```swift
    let n = 8
    let stride = 1
    
    var initialValue: Float = 0
    var increment: Float = 1
    
    let ramp = [Float](unsafeUninitializedCapacity: n) {
        buffer, initializedCount in
        
        vDSP_vramp(&initialValue,
                   &increment,
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
float initialValue = 0;
float increment = 1;
float ramp[8];

vDSP_vramp(&initialValue,
           &increment,
           ramp,
           1,
           8);

// Prints "[0, 1, 2, 3, 4, 5, 6, 7]".
printf("[%g, %g, %g, %g, %g, %g, %g, %g]\n",
      ramp[0], ramp[1], ramp[2], ramp[3],
      ramp[4], ramp[5], ramp[6], ramp[7]);
```

## Parameters

- `__A`: The initial value of the ramp.
- `__B`: The increment, or decrement if negative, between each generated element.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

### Vector generation with ramps using an initial value and increment
- [vDSP_vrampD](./vdsp_vrampd.md)
  Generates a double-precision vector with monotonically incrementing or decrementing values using an initial value and increment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vramp)*