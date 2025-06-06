# asciiOnlyCharacterClasses(_:)

**Framework**: Swift  
**Kind**: method

Returns a regular expression that matches only ASCII characters when matching character classes.

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
func asciiOnlyCharacterClasses(_ useASCII: Bool = true) -> Regex<Regex<Output>.RegexOutput>
```

#### Return Value

The modified regular expression.

## Parameters

- `useASCII`: A Boolean value indicating whether to match only   ASCII characters when matching character classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regex/asciionlycharacterclasses(_:))*