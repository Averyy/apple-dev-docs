# significandWidth

**Framework**: Swift  
**Kind**: property

The number of bits required to represent the value’s significand.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var significandWidth: Int { get }
```

#### Discussion

If this value is a finite nonzero number, `significandWidth` is the number of fractional bits required to represent the value of `significand`; otherwise, `significandWidth` is -1. The value of `significandWidth` is always -1 or between zero and `significandBitCount`. For example:

- For any representable power of two, `significandWidth` is zero, because `significand` is `1.0`.
- If `x` is 10, `x.significand` is `1.01` in binary, so `x.significandWidth` is 2.
- If `x` is Float.pi, `x.significand` is `1.10010010000111111011011` in binary, and `x.significandWidth` is 23.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float16/significandwidth)*