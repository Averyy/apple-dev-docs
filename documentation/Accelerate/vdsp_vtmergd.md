# vDSP_vtmergD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs a tapered merge between two double-precision vectors.

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
extern void vDSP_vtmergD(const double *__A, vDSP_Stride __IA, const double *__B, vDSP_Stride __IB, double *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

The following code performs a tapered merge between two vectors that represent sine waves at different frequencies:

**Swift**:

```swift
let count = 1024

let vectorA: [Double] = (0 ..< count).map {
    return sin(Double($0) * 0.4)
}

let vectorB: [Double] = (0 ..< count).map {
    return sin(Double($0) * 0.025)
}

let stride = 1
let n = vDSP_Length(count)

let tapered = [Double](unsafeUninitializedCapacity: count) {
    buffer, initializedCount in
    
    vDSP_vtmergD(vectorA, stride,
                 vectorB, stride,
                 buffer.baseAddress!, stride,
                 n)
    
    initializedCount = count
}
```

**Objective-C**:

```objc
int count = 1024;

double vectorA[1024];
double vectorB[1024];
double tapered[1024];

for (int i = 0; i < count; i++) {
    vectorA[i] = sin((double)i * 0.4);
}
for (int i = 0; i < count; i++) {
    vectorB[i] = sin((double)i * 0.025);
}

vDSP_vtmergD(vectorA, 1,
             vectorB, 1,
             tapered, 1,
             (vDSP_Length)count);
```

The following image shows the result of the tapered merge in `tapered`:

![Graphic showing the tapered merge from a high-frequency sine wave to a low-frequency sine wave.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-4329457@2x.png)

## Parameters

- `__A`: The first input vector.
- `__IA`: The distance between the elements in the first input vector.``
- `__B`: The second input vector.
- `__IB`: The distance between the elements in the second input vector.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of complex elements in the output vector.

## See Also

### Vector-to-vector merging functions
- [vDSP_vtmerg](./vdsp_vtmerg.md)
  Performs a tapered merge between two single-precision vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vtmergd)*