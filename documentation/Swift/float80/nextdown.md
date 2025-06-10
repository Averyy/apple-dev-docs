# nextDown

**Framework**: Swift  
**Kind**: property

The greatest representable value that compares less than this value.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var nextDown: Self { get }
```

#### Discussion

For any finite value `x`, `x.nextDown` is less than `x`. For `nan` or `-infinity`, `x.nextDown` is `x` itself. The following special cases also apply:

- If `x` is `infinity`, then `x.nextDown` is `greatestFiniteMagnitude`.
- If `x` is `leastNonzeroMagnitude`, then `x.nextDown` is `0.0`.
- If `x` is zero, then `x.nextDown` is `-leastNonzeroMagnitude`.
- If `x` is `-greatestFiniteMagnitude`, then `x.nextDown` is `-infinity`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/nextdown)*