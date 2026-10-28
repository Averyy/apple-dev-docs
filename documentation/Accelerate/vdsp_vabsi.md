# vDSP_vabsi

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the absolute value of each element in the supplied integer vector using the specified stride.

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
extern void vDSP_vabsi(const int *__A, vDSP_Stride __IA, int *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

For example, the following code calculates the absolute values of the elements of an array:

**Swift**:

```swift
    let stride = 1
    
    let values: [Int32] = [-1, 2, -3, 4, -5, 6, -7, 8]
    
    let absoluteValues = [Int32](unsafeUninitializedCapacity: values.count) {
        buffer, initializedCount in
        
        vDSP_vabsi(values, stride,
            buffer.baseAddress!, stride,
            vDSP_Length(values.count))
        
        initializedCount = values.count
    }
    
    // Prints "[1, 2, 3, 4, 5, 6, 7, 8]".
    print(absoluteValues)
```

**Objective-C**:

```objc
    vDSP_Stride stride = 1;

    int values[] = {-1, 2, -3, 4, -5, 6, -7, 8};
    vDSP_Length count = 8;
    int absoluteValues[8];

    vDSP_vabsi(values, stride,
               absoluteValues, stride,
               count);

    // Prints "[1, 2, 3, 4, 5, 6, 7, 8]".
    printf("[%d, %d, %d, %d, %d, %d, %d, %d]\n",
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
- [vDSP_vabs](./vdsp_vabs.md)
  Calculates the absolute value of each element in the supplied single-precision vector using the specified stride.
- [vDSP_vabsD](./vdsp_vabsd.md)
  Calculates the absolute value of each element in the supplied double-precision vector using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vabsi)*