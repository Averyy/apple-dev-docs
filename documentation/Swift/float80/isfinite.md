# isFinite

**Framework**: Swift  
**Kind**: property

A Boolean value indicating whether this instance is finite.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var isFinite: Bool { get }
```

#### Discussion

All values other than NaN and infinity are considered finite, whether normal or subnormal.  For NaN, both `isFinite` and `isInfinite` are false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/isfinite)*