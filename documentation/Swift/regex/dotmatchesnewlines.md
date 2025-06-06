# dotMatchesNewlines(_:)

**Framework**: Swift  
**Kind**: method

Returns a regular expression where the “any” metacharacter (`.`) also matches against the start and end of a line.

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
func dotMatchesNewlines(_ dotMatchesNewlines: Bool = true) -> Regex<Regex<Output>.RegexOutput>
```

#### Return Value

The modified regular expression.

## Parameters

- `dotMatchesNewlines`: A Boolean value indicating whether    should match a newline character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regex/dotmatchesnewlines(_:))*