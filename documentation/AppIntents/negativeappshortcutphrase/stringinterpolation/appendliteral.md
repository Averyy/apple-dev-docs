# appendLiteral(_:)

**Framework**: App Intents  
**Kind**: method

Appends a literal segment to the interpolation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
mutating func appendLiteral(_ literal: String)
```

#### Discussion

Don’t call this method directly. Instead, initialize a variable or constant using a string literal with interpolated expressions.

Interpolated expressions don’t pass through this method; instead, Swift selects an overload of `appendInterpolation`. For more information, see the top-level `StringInterpolationProtocol` documentation.

## Parameters

- `literal`: A string literal containing the characters   that appear next in the string literal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/negativeappshortcutphrase/stringinterpolation/appendliteral(_:))*