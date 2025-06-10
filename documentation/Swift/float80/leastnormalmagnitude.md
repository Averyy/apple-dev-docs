# leastNormalMagnitude

**Framework**: Swift  
**Kind**: property

The least positive normal number.

**Availability**:
- macOS 10.10+

## Declaration

```swift
static var leastNormalMagnitude: Float80 { get }
```

#### Discussion

This value compares less than or equal to all positive normal numbers. There may be smaller positive numbers, but they are , meaning that they are represented with less precision than normal numbers.

This value corresponds to type-specific C macros such as `FLT_MIN` and `DBL_MIN`. The naming of those macros is slightly misleading, because subnormals, zeros, and negative numbers are smaller than this value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/leastnormalmagnitude)*