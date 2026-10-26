# vDSP_vgathraD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Generates a gathered copy of the specified double-precision vector using a vector that defines the pointers to the values to keep.

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
extern void vDSP_vgathraD(const double * const*__A, vDSP_Stride __IA, double *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

The following code shows an example of gathering the values in `source` using the values in `indices`:

**Swift**:

```swift
    let source: [Double] = [10, 20,
                           30, 40,
                           50, 60,
                           70, 80]
    
    let stride = 1
    
    let result = source.withUnsafeBufferPointer { srcPtr in
        
        let pointers = [srcPtr.baseAddress!.advanced(by: 0),
                        srcPtr.baseAddress!.advanced(by: 2),
                        srcPtr.baseAddress!.advanced(by: 4),
                        srcPtr.baseAddress!.advanced(by: 6)]
        
        let n = pointers.count
        
        return [Double](unsafeUninitializedCapacity: n) {
            buffer, initializedCount in
            
            vDSP_vgathraD(pointers, stride,
                         buffer.baseAddress!, stride,
                         vDSP_Length(n))
            
            initializedCount = n
        }
    }
    
    // Prints "[10.0, 30.0, 50.0, 70.0]".
    print(result)
```

**Objective-C**:

```objc
double source[8] = {10, 20, 30, 40, 50, 60, 70, 80};

const double *pointers[4] = {
    &source[0],
    &source[2],
    &source[4],
    &source[6]
};

int n = 4;
vDSP_Stride stride = 1;

double result[4] = {0};

vDSP_vgathraD(pointers, stride,
              result, stride,
              (vDSP_Length)n);

// Prints "[10, 30, 50, 70]".
printf("[%g, %g, %g, %g]\n", result[0], result[1], result[2], result[3]);
```

## Parameters

- `__A`: The input vector that contains the pointers to the source values.
- `__IA`: The distance between the elements in the input vector.``
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.``
- `__N`: The number of elements in the output vector and the number of elements in the input vector.

## See Also

### Vector gathering functions
- [vDSP_vindex](./vdsp_vindex.md)
  Generates a gathered copy of the specified single-precision vector using a vector that defines the zero-based indices to keep.
- [vDSP_vindexD](./vdsp_vindexd.md)
  Generates a gathered copy of the specified double-precision vector using a vector that defines the zero-based indices to keep.
- [vDSP_vgathr](./vdsp_vgathr.md)
  Generates a gathered copy of the specified single-precision vector using a vector that defines the one-based indices to keep.
- [vDSP_vgathrD](./vdsp_vgathrd.md)
  Generates a gathered copy of the specified double-precision vector using a vector that defines the one-based indices to keep.
- [vDSP_vgathra](./vdsp_vgathra.md)
  Generates a gathered copy of the specified single-precision vector using a vector that defines the pointers to the values to keep.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vgathrad)*