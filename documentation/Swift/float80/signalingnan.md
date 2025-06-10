# signalingNaN

**Framework**: Swift  
**Kind**: property

A signaling NaN (“not a number”).

**Availability**:
- macOS 10.10+

## Declaration

```swift
static var signalingNaN: Float80 { get }
```

#### Discussion

The default IEEE 754 behavior of operations involving a signaling NaN is to raise the Invalid flag in the floating-point environment and return a quiet NaN.

Operations on types conforming to the `FloatingPoint` protocol should support this behavior, but they might also support other options. For example, it would be reasonable to implement alternative operations in which operating on a signaling NaN triggers a runtime error or results in a diagnostic for debugging purposes. Types that implement alternative behaviors for a signaling NaN must document the departure.

Other than these signaling operations, a signaling NaN behaves in the same manner as a quiet NaN.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/signalingnan)*