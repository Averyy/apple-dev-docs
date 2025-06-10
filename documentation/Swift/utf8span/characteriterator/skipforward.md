# skipForward()

**Framework**: Swift  
**Kind**: method

Advance `codeUnitOffset` to the end of the current `Character`, without constructing it.

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
mutating func skipForward() -> Int
```

#### Discussion

Returns the number of `Character`s skipped over, which can be 0 if at the end of the UTF8Span.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/characteriterator/skipforward())*