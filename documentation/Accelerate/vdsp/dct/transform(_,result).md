# transform(_:result:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Computes an out-of-place single-precision real discrete cosine transform.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
func transform<U, V>(_ vector: U, result: inout V) where U : AccelerateBuffer, V : AccelerateMutableBuffer, U.Element == Float, V.Element == Float
```

## See Also

### Instance Methods
- [func transform<U>(U) -> [Float]](./transform%28_%29.md)
  Returns the single-precision real discrete cosine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/dct/transform(_:result:))*