# previous()

**Framework**: Swift  
**Kind**: method

Return the `Character` ending at `currentCodeUnitOffset`. After the function returns, `currentCodeUnitOffset` holds the position at the start of the returned `Character`, which is also the end of the previous `Character`.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
mutating func previous() -> Character?
```

#### Discussion

Returns `nil` if at the start of the `UTF8Span`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/characteriterator/previous())*