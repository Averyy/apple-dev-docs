# vDSP_vgenp

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Generates the single-precision linearly interpolated values of a vector at the specified indices.

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
extern void vDSP_vgenp(const float *__A, vDSP_Stride __IA, const float *__B, vDSP_Stride __IB, float *__C, vDSP_Stride __IC, vDSP_Length __N, vDSP_Length __M);
```

## Mentions

- [Using linear interpolation to construct new data points](./using-linear-interpolation-to-construct-new-data-points.md)

## Discussion

The following code creates a five-element vector from two values using linear interpolation. The last index in `indices` determines the length of the operation result:

**Swift**:

```swift
    let values: [Float] = [0, 100]
    let indices: [Float] = [0, 4]
    
    let n = Int(indices.last! + 1)
    let m = values.count
    
    let stride = 1
    
    let interpolatedValues = [Float](unsafeUninitializedCapacity: n) {
        buffer, initializedCount in
        
        vDSP_vgenp(values, stride,
                   indices, stride,
                   buffer.baseAddress!, stride,
                   vDSP_Length(n),
                   vDSP_Length(m))
        
        initializedCount = n
    }
    
    // Prints "[0.0, 25.0, 50.0, 75.0, 100.0]".
    print(interpolatedValues)
```

**Objective-C**:

```objc
float values[2] = {0, 100};
float indices[2] = {0, 4};

int n = 5;  // `indices[last]` + 1 = 4 + 1 = 5; drives `n`
int m = 2;
vDSP_Stride stride = 1;

float interpolatedValues[5] = {0};

vDSP_vgenp(values, stride,
           indices, stride,
           interpolatedValues, stride,
           (vDSP_Length)n,
           (vDSP_Length)m);

// Prints "[0, 25, 50, 75, 100]".
printf("[%g, %g, %g, %g, %g]\n",
      interpolatedValues[0], interpolatedValues[1],
      interpolatedValues[2], interpolatedValues[3],
      interpolatedValues[4]);
```

## Parameters

- `__A`: The input vector that defines the values that the function interpolates.
- `__IA`: The distance between the elements in the values vector.
- `__B`: The input vector that defines the indices at which the function interpolates.
- `__IB`: The distance between the elements in the indices vector.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.
- `__M`: The number of elements in the values and indices input vectors.

## See Also

### Vector generation by extrapolation and interpolation
- [vDSP_vgenpD](./vdsp_vgenpd.md)
  Generates the double-precision linearly interpolated values of a vector at the specified indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vgenp)*