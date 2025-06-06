# init(bitPattern:)

**Framework**: Swift  
**Kind**: init

Creates a new instance with the same memory representation as the given value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(bitPattern: UInt128)
```

#### Discussion

This initializer does not perform any range or overflow checking. The resulting instance may not have the same numeric value as `bitPattern`—it is only guaranteed to use the same pattern of bits in its binary representation.

## Parameters

- `bitPattern`: A value to use as the source of the new instance’s   binary representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int128/init(bitpattern:))*