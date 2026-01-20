# resultMatrixOrigin

**Framework**: Metal Performance Shaders  
**Kind**: property

The origin of the result matrix.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var resultMatrixOrigin: MTLOrigin { get set }
```

#### Discussion

The origin, relative to `(0,0)`, at which to start reading values. If a different origin is desired, you must modify this property before encoding the matrix multiplication kernel. The default value is `(0,0,0)` (the `z` value must always be 0).

## See Also

- [var leftMatrixOrigin: MTLOrigin](mpsmatrixmultiplication/leftmatrixorigin.md)
  The origin of the left input matrix.
- [var rightMatrixOrigin: MTLOrigin](mpsmatrixmultiplication/rightmatrixorigin.md)
  The origin of the right input matrix.
- [var batchSize: Int](mpsmatrixmultiplication/batchsize.md)
- [var batchStart: Int](mpsmatrixmultiplication/batchstart.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixmultiplication/resultmatrixorigin)*