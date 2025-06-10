# next()

**Framework**: Swift  
**Kind**: method

Return the `Character` starting at `currentCodeUnitOffset`. After the function returns, `currentCodeUnitOffset` holds the position at the end of the `Character`, which is also the start of the next `Character`.

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
mutating func next() -> Character?
```

#### Discussion

Returns `nil` if at the end of the `UTF8Span`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/characteriterator/next())*