# withMutableCharacters(_:)

**Framework**: Swift  
**Kind**: method

Applies the given closure to a mutable view of the string’s characters.

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
mutating func withMutableCharacters<R>(_ body: (inout String) -> R) -> R
```

#### Discussion

Previous versions of Swift provided this view since String itself was not a collection. String is now a collection of characters, so this type is now just an alias for String.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/withmutablecharacters(_:))*