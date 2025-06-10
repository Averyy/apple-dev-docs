# leastNonzeroMagnitude

**Framework**: Swift  
**Kind**: property

The least positive number.

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
static var leastNonzeroMagnitude: Float16 { get }
```

#### Discussion

This value compares less than or equal to all positive numbers, but greater than zero. If the type supports subnormal values, `leastNonzeroMagnitude` is smaller than `leastNormalMagnitude`; otherwise they are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float16/leastnonzeromagnitude)*