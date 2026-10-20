# vremquof(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

For each vector element, calculates the remainder of `X`/`Y`, according to the SANE standard. It stores into `QUO` the 7 low-order bits of the integer quotient, such that -127 <= `QUO` <= 127.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func vremquof(_: vFloat, _: vFloat, _: UnsafeMutablePointer<vUInt32>) -> vFloat
```

```c
extern vFloat vremquof(vFloat , vFloat , vUInt32 *);
```

## See Also

### Remainder Functions (from vfp.h)
- [func vfmodf(vFloat, vFloat) -> vFloat](./vfmodf%28_,_%29.md)
  For each vector element, calculates `X` modulo `Y`.
- [func vremainderf(vFloat, vFloat) -> vFloat](./vremainderf%28_,_%29.md)
  For each vector element, calculates the remainder of `X`/`Y`, according to the IEEE 754 floating-point standard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vremquof(_:_:_:))*