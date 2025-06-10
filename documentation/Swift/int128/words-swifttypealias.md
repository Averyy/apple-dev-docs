# Int128.Words

**Framework**: Swift  
**Kind**: typealias

A type that represents the words of a binary integer.

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
typealias Words = UInt128.Words
```

#### Discussion

The `Words` type must conform to the `RandomAccessCollection` protocol with an `Element` type of `UInt` and `Index` type of `Int`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int128/words-swift.typealias)*