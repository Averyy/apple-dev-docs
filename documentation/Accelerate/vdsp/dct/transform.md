# transform(_:)

**Framework**: Accelerate  
**Kind**: method

Returns the single-precision real discrete cosine transform.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
func transform<U>(_ vector: U) -> [Float] where U : AccelerateBuffer, U.Element == Float
```

## See Also

- [func transform<U, V>(U, result: inout V)](vdsp/dct/transform(_:result:).md)
  Computes an out-of-place single-precision real discrete cosine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/dct/transform(_:))*