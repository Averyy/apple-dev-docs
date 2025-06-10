# vfmodf(_:_:)

**Framework**: Accelerate  
**Kind**: func

For each vector element, calculates `X` modulo `Y`.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func vfmodf(_: vFloat, _: vFloat) -> vFloat
```

## See Also

- [func vremainderf(vFloat, vFloat) -> vFloat](vremainderf(_:_:).md)
  For each vector element, calculates the remainder of `X`/`Y`, according to the IEEE 754 floating-point standard.
- [func vremquof(vFloat, vFloat, UnsafeMutablePointer<vUInt32>) -> vFloat](vremquof(_:_:_:).md)
  For each vector element, calculates the remainder of `X`/`Y`, according to the SANE standard. It stores into `QUO` the 7 low-order bits of the integer quotient, such that -127 <= `QUO` <= 127.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vfmodf(_:_:))*