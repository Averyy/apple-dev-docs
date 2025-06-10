# leastNonzeroMagnitude

**Framework**: Swift  
**Kind**: property

The least positive number.

**Availability**:
- macOS 10.10+

## Declaration

```swift
static var leastNonzeroMagnitude: Float80 { get }
```

#### Discussion

This value compares less than or equal to all positive numbers, but greater than zero. If the type supports subnormal values, `leastNonzeroMagnitude` is smaller than `leastNormalMagnitude`; otherwise they are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/leastnonzeromagnitude)*