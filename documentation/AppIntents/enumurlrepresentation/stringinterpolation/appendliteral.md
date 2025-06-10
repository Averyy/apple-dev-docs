# appendLiteral(_:)

**Framework**: App Intents  
**Kind**: method

Appends a literal segment to the interpolation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/enumurlrepresentation/stringinterpolation/appendliteral(_:))*