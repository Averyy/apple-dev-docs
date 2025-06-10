# vDSP_mmov

**Framework**: Accelerate  
**Kind**: func

Copies the contents of a single-precision submatrix to another single-precision matrix.

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
extern void vDSP_mmov(const float * __A, float * __C, vDSP_Length __M, vDSP_Length __N, vDSP_Length __TA, vDSP_Length __TC);
```

#### Discussion

This function treats the input and output matrices as row-major order.

The following code copies the 3 x 3 submatrix that starts at the element with the value `22` from the input matrix to the output matrix:

```swift
    let m: vDSP_Length = 3
    let n: vDSP_Length = 3 
    
    let source: [Float] = [ 10, 11, 12, 13, 14,
                            20, 21, 22, 23, 24,
                            30, 31, 32, 33, 34,
                            40, 41, 42, 43, 44,
                            50, 51, 52, 53, 54 ]
    let sourceColumnCount = 5
    
    let destination = [Float](unsafeUninitializedCapacity: Int(m * n)) {
        buffer,initializedCount in
        
        source.withUnsafeBufferPointer { sourcePtr in
            
            let rowOffset = 1 * sourceColumnCount
            let colOffset = 2
            let start = sourcePtr.baseAddress!.advanced(by: rowOffset + colOffset)
            
            vDSP_mmov(start, 
                      buffer.baseAddress!,
                      m, n,
                      vDSP_Length(sourceColumnCount),
                      m)
        }
        
        initializedCount = Int(m * n)
    }
    
    // Prints:
    //    "[ 22.0, 23.0, 24.0,
    //       32.0, 33.0, 34.0,
    //       42.0, 43.0, 44.0 ]".
    print(destination)
```

## Parameters

- `__A`: The input matrix.
- `__C`: The output matrix.
- `__M`: The number of columns that the function copies.
- `__N`: The number of rows that the function copies.
- `__TA`: The number of columns in the matrix of which   is a submatrix.
- `__TC`: The number of columns in the matrix of which   is a submatrix.

## See Also

- [vDSP_mmovD](vdsp_mmovd.md)
  Copies the contents of a double-precision submatrix to another double-precision matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_mmov)*