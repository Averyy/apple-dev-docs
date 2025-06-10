# trunc(_:)

**Framework**: Accelerate  
**Kind**: method

Returns a single-precision array containing each element in the supplied vector truncated to a fraction.

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
static func trunc<U>(_ vector: U) -> [Float] where U : AccelerateBuffer, U.Element == Float
```

## See Also

- [static func trunc<U>(U) -> [Double]](vdsp/trunc(_:)-80rfo.md)
  Returns a double-precision array containing each element in the supplied vector truncated to a fraction.
- [static func trunc<U, V>(U, result: inout V)](vdsp/trunc(_:result:)-4t63c.md)
  Calculates each element in the supplied double-precision vector truncated to a fraction.
- [static func trunc<U, V>(U, result: inout V)](vdsp/trunc(_:result:)-fabn.md)
  Calculates each element in the supplied single-precision vector truncated to a fraction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/trunc(_:)-1npgt)*