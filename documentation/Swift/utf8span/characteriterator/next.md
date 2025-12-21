# next()

**Framework**: Swift  
**Kind**: method

Return the `Character` starting at `currentCodeUnitOffset`. After the function returns, `currentCodeUnitOffset` holds the position at the end of the `Character`, which is also the start of the next `Character`.

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
mutating func next() -> Character?
```

#### Discussion

Returns `nil` if at the end of the `UTF8Span`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/characteriterator/next())*