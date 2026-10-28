# vDSP_vnabs

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the negative absolute value of each element in the supplied single-precision vector using the specified stride.

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
extern void vDSP_vnabs(const float *__A, vDSP_Stride __IA, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

For example, the following code calculates the negative absolute values of the elements of an array:

**Swift**:

```swift
let stride = 1

let values: [Float] = [-1, 2, -3, 4, -5, 6, -7, 8]

let negativeAbsoluteValues = [Float](unsafeUninitializedCapacity: values.count) {
    buffer, initializedCount in
    
    vDSP_vnabs(values, stride,
               buffer.baseAddress!, stride,
               vDSP_Length(values.count))
    
    initializedCount = values.count
}

// Prints "[-1.0, -2.0, -3.0, -4.0, -5.0, -6.0, -7.0, -8.0]".
print(negativeAbsoluteValues)
```

**Objective-C**:

```objc
vDSP_Stride stride = 1;

float values[] = {-1, 2, -3, 4, -5, 6, -7, 8};
vDSP_Length count = 8;
float negativeAbsoluteValues[8];

vDSP_vnabs(values, stride,
           negativeAbsoluteValues, stride,
           count);

// Prints "[-1, -2, -3, -4, -5, -6, -7, -8]".
printf("[%g, %g, %g, %g, %g, %g, %g, %g]\n",
      negativeAbsoluteValues[0], negativeAbsoluteValues[1],
      negativeAbsoluteValues[2], negativeAbsoluteValues[3],
      negativeAbsoluteValues[4], negativeAbsoluteValues[5],
      negativeAbsoluteValues[6], negativeAbsoluteValues[7]);
```

## Parameters

- `__A`: The input vector `A`.
- `__IA`: The distance between the elements in the input vector `A`.
- `__C`: On output, the negative absolute values of the elements in the input vector.
- `__IC`: The distance between the elements in the output vector `C`.
- `__N`: The number of elements that the function processes.

## See Also

### Vector negative absolute functions
- [vDSP_vnabsD](./vdsp_vnabsd.md)
  Calculates the negative absolute value of each element in the supplied double-precision vector using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vnabs)*