# vDSP_vabs

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the absolute value of each element in the supplied single-precision vector using the specified stride.

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
extern void vDSP_vabs(const float *__A, vDSP_Stride __IA, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

For example, the following code calculates the absolute values of the elements of an array:

**Swift**:

```swift
    let stride = 1
    
    let values: [Float] = [-1, 2, -3, 4, -5, 6, -7, 8]
    
    let absoluteValues = [Float](unsafeUninitializedCapacity: values.count) {
        buffer, initializedCount in
        
        vDSP_vabs(values, stride,
            buffer.baseAddress!, stride,
            vDSP_Length(values.count))
        
        initializedCount = values.count
    }
    
    // Prints "[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]".
    print(absoluteValues)
```

**Objective-C**:

```objc
    vDSP_Stride stride = 1;

    float values[] = {-1, 2, -3, 4, -5, 6, -7, 8};
    vDSP_Length count = 8;
    float absoluteValues[8];

    vDSP_vabs(values, stride,
              absoluteValues, stride,
              count);

    // Prints "[1, 2, 3, 4, 5, 6, 7, 8]".
    printf("[%g, %g, %g, %g, %g, %g, %g, %g]\n",
           absoluteValues[0], absoluteValues[1],
           absoluteValues[2], absoluteValues[3],
           absoluteValues[4], absoluteValues[5],
           absoluteValues[6], absoluteValues[7]);
```

## Parameters

- `__A`: The input vector `A`.
- `__IA`: The distance between the elements in the input vector `A`.
- `__C`: On output, the absolute values of the elements in the input vector.
- `__IC`: The distance between the elements in the output vector `C`.
- `__N`: The number of elements that the function processes.

## See Also

### Vector absolute functions
- [vDSP_vabsi](./vdsp_vabsi.md)
  Calculates the absolute value of each element in the supplied integer vector using the specified stride.
- [vDSP_vabsD](./vdsp_vabsd.md)
  Calculates the absolute value of each element in the supplied double-precision vector using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vabs)*