# previous()

**Framework**: Swift  
**Kind**: method

Return the `Character` ending at `currentCodeUnitOffset`. After the function returns, `currentCodeUnitOffset` holds the position at the start of the returned `Character`, which is also the end of the previous `Character`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
mutating func previous() -> Character?
```

#### Discussion

Returns `nil` if at the start of the `UTF8Span`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/characteriterator/previous())*