# words

**Framework**: Swift  
**Kind**: property

A collection containing the words of this value’s binary representation, in order from the least significant to most significant.

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
var words: UInt128.Words { get }
```

#### Discussion

Negative values are returned in two’s complement representation, regardless of the type’s underlying implementation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint128/words-swift.property)*