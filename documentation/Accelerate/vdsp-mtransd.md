# vDSP_mtransD

**Framework**: Accelerate  
**Kind**: func

Transposes a double-precision matrix.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_mtransD(const double * __A, vDSP_Stride __IA, double * __C, vDSP_Stride __IC, vDSP_Length __M, vDSP_Length __N);
```

#### Discussion

The code below uses [`vDSP_mtransD`](vdsp_mtransd.md) to transpose the matrix `source` and write the result to the matrix `transposed`:

```swift
let source: [Double] = [1, 2, 3, 4,
                        5, 6, 7, 8]

let transposed = [Double](unsafeUninitializedCapacity: source.count) {
    
    buffer, unsafeUninitializedCapacity in
    
    vDSP_mtransD(source, 1,
                 buffer.baseAddress!, 1,
                 4, 2)
    
    unsafeUninitializedCapacity = source.count
}

// Prints:
//     "[1.0, 5.0,
//       2.0, 6.0,
//       3.0, 7.0,
//       4.0, 8.0]".
print(transposed)
```

> ⚠️ **Warning**:  This function doesn’t support in-place operation.

## Parameters

- `__A`: The input matrix.
- `__IA`: The stride between elements in the input matrix.
- `__C`: The output matrix.
- `__IC`: The stride between elements in the output matrix.
- `__M`: The number of rows in the output matrix and the number of columns in the input matrix.
- `__N`: The number of columns in the output matrix and the number of rows in the input matrix.

## See Also

- [vDSP_mtrans](vdsp_mtrans.md)
  Transposes a single-precision matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_mtransd)*