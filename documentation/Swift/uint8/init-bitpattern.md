# init(bitPattern:)

**Framework**: Swift  
**Kind**: init

Creates a new instance with the same memory representation as the given value.

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
init(bitPattern x: Int8)
```

#### Discussion

This initializer does not perform any range or overflow checking. The resulting instance may not have the same numeric value as `bitPattern`—it is only guaranteed to use the same pattern of bits in its binary representation.

## Parameters

- `x`: A value to use as the source of the new instance’s binary   representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint8/init(bitpattern:))*