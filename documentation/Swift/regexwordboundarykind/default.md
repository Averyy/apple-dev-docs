# default

**Framework**: Swift  
**Kind**: property

A word boundary algorithm that implements the “default word boundary” Unicode recommendation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static var `default`: RegexWordBoundaryKind { get }
```

#### Discussion

Default word boundaries use a Unicode algorithm that handles some cases better than simple word boundaries, such as words with internal punctuation, changes in script, and Emoji.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regexwordboundarykind/default)*