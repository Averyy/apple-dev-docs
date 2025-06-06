# StringInterpolation

**Framework**: Swift  
**Kind**: associatedtype  
**Required**: Yes

The type each segment of a string literal containing interpolations should be appended to.

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
associatedtype StringInterpolation : StringInterpolationProtocol = DefaultStringInterpolation where Self.StringLiteralType == Self.StringInterpolation.StringLiteralType
```

#### Discussion

The `StringLiteralType` of an interpolation type must match the `StringLiteralType` of the conforming type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/expressiblebystringinterpolation/stringinterpolation)*