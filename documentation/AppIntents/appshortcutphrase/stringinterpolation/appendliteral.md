# appendLiteral(_:)

**Framework**: App Intents  
**Kind**: method

Appends a literal segment to the interpolation.

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
mutating func appendLiteral(_ literal: String)
```

#### Discussion

Don’t call this method directly. Instead, initialize a variable or constant using a string literal with interpolated expressions.

Interpolated expressions don’t pass through this method; instead, Swift selects an overload of `appendInterpolation`. For more information, see the top-level `StringInterpolationProtocol` documentation.

## Parameters

- `literal`: A string literal containing the characters   that appear next in the string literal.

## See Also

- [func appendInterpolation(AppShortcutPhraseToken)](appshortcutphrase/stringinterpolation/appendinterpolation(_:)-47gqg.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutphrase/stringinterpolation/appendliteral(_:))*