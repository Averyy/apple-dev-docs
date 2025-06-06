# matches(of:)

**Framework**: Swift  
**Kind**: method

Returns a collection containing all non-overlapping matches of the regex, created by the given closure.

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
func matches<Output>(@RegexComponentBuilder of content: () -> some RegexComponent) -> [Regex<Output>.Match]
```

#### Return Value

A collection of matches for the regex returned by `content`. If no matches are found, the returned collection is empty.

## Parameters

- `content`: A closure that returns the regex to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/bidirectionalcollection/matches(of:)-5eey9)*