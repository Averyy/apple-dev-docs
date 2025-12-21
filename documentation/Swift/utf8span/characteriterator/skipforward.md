# skipForward()

**Framework**: Swift  
**Kind**: method

Advance `codeUnitOffset` to the end of the current `Character`, without constructing it.

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
mutating func skipForward() -> Int
```

#### Discussion

Returns the number of `Character`s skipped over, which can be 0 if at the end of the UTF8Span.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/characteriterator/skipforward())*