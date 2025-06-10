# vDSP_vneg

**Framework**: Accelerate  
**Kind**: func

Calculates the negative value of each element in the supplied single-precision vector using the specified stride.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_vneg(const float * __A, vDSP_Stride __IA, float * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

For example, the following code calculates the negative values of the elements of an array:

```swift
    let stride = 1
    
    let values: [Float] = [-1, 2, -3, 4, -5, 6, -7, 8]
    
    let negativeValues = [Float](unsafeUninitializedCapacity: values.count) {
        buffer, initializedCount in
        
        vDSP_vneg(values, stride,
            buffer.baseAddress!, stride,
            vDSP_Length(values.count))
        
        initializedCount = values.count
    }
    
    // Prints "[1.0, -2.0, 3.0, -4.0, 5.0, -6.0, 7.0, -8.0]".
    print(negativeValues)
```

## Parameters

- `__A`: The input vector  .
- `__IA`: The distance between the elements in the input vector  .
- `__C`: On output, the negative values of the elements in the input vector.
- `__IC`: The distance between the elements in the output vector  .
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_vnegD](vdsp_vnegd.md)
  Calculates the negative value of each element in the supplied double-precision vector using specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vneg)*