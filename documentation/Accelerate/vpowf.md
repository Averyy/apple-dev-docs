# vpowf(_:_:)

**Framework**: Accelerate  
**Kind**: func

For each vector element, calculates `X` to the floating-point power of `Y`. The result is more accurate than using exp(log(`X`)*`Y`).

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
func vpowf(_: vFloat, _: vFloat) -> vFloat
```

## See Also

- [func vipowf(vFloat, vSInt32) -> vFloat](vipowf(_:_:).md)
  For each vector element, calculates `X` to the integer power of `Y`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vpowf(_:_:))*