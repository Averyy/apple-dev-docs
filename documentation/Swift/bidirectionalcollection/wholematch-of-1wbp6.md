# wholeMatch(of:)

**Framework**: Swift  
**Kind**: method

Matches a regex in its entirety, where the regex is created by the given closure.

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
func wholeMatch<Output>(@RegexComponentBuilder of content: () -> some RegexComponent) -> Regex<Output>.Match?
```

#### Return Value

The match if there is one, or `nil` if none.

## Parameters

- `content`: A closure that returns a regex to match against.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/bidirectionalcollection/wholematch(of:)-1wbp6)*