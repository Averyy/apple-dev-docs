# prefixMatch(of:)

**Framework**: Swift  
**Kind**: method

Returns a match if this string is matched by the given regex at its start.

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
func prefixMatch<R>(of regex: R) -> Regex<R.RegexOutput>.Match? where R : RegexComponent
```

#### Return Value

The match, if one is found. If there is no match, or a transformation in `regex` throws an error, this method returns `nil`.

## Parameters

- `regex`: The regular expression to match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/bidirectionalcollection/prefixmatch(of:)-7dq6v)*