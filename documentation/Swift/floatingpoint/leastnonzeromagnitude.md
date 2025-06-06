# leastNonzeroMagnitude

**Framework**: Swift  
**Kind**: property  
**Required**: Yes

The least positive number.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var leastNonzeroMagnitude: Self { get }
```

#### Discussion

This value compares less than or equal to all positive numbers, but greater than zero. If the type supports subnormal values, `leastNonzeroMagnitude` is smaller than `leastNormalMagnitude`; otherwise they are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/floatingpoint/leastnonzeromagnitude)*