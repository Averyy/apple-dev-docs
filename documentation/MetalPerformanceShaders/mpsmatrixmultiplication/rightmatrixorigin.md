# rightMatrixOrigin

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

The origin of the right input matrix.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var rightMatrixOrigin: MTLOrigin { get set }
```

```objc
@property (nonatomic, readwrite) MTLOrigin rightMatrixOrigin;
```

## Discussion

The origin, relative to `(0,0)`, at which to start reading values. If a different origin is desired, you must modify this property before encoding the matrix multiplication kernel. The default value is `(0,0,0)` (the `z` value must always be 0).

## See Also

### Properties
- [var leftMatrixOrigin: MTLOrigin](./leftmatrixorigin.md)
  The origin of the left input matrix.
- [var resultMatrixOrigin: MTLOrigin](./resultmatrixorigin.md)
  The origin of the result matrix.
- [var batchSize: Int](./batchsize.md)
- [var batchStart: Int](./batchstart.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixmultiplication/rightmatrixorigin)*