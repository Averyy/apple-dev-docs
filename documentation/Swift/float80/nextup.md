# nextUp

**Framework**: Swift  
**Kind**: property

The least representable value that compares greater than this value.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var nextUp: Float80 { get }
```

#### Discussion

For any finite value `x`, `x.nextUp` is greater than `x`. For `nan` or `infinity`, `x.nextUp` is `x` itself. The following special cases also apply:

- If `x` is `-infinity`, then `x.nextUp` is `-greatestFiniteMagnitude`.
- If `x` is `-leastNonzeroMagnitude`, then `x.nextUp` is `-0.0`.
- If `x` is zero, then `x.nextUp` is `leastNonzeroMagnitude`.
- If `x` is `greatestFiniteMagnitude`, then `x.nextUp` is `infinity`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/nextup)*