# appendLiteral(_:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Appends a literal segment to the interpolation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
mutating func appendLiteral(_ literal: Self.StringLiteralType)
```

#### Discussion

Don’t call this method directly. Instead, initialize a variable or constant using a string literal with interpolated expressions.

Interpolated expressions don’t pass through this method; instead, Swift selects an overload of `appendInterpolation`. For more information, see the top-level `StringInterpolationProtocol` documentation.

## Parameters

- `literal`: A string literal containing the characters   that appear next in the string literal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringinterpolationprotocol/appendliteral(_:))*