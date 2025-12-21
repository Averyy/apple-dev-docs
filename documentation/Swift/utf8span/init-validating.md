# init(validating:)

**Framework**: Swift  
**Kind**: init

Creates a UTF8Span containing `codeUnits`. Validates that the input is valid UTF-8, otherwise throws an error.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(validating codeUnits: consuming Span<UInt8>) throws(UTF8.ValidationError)
```

#### Discussion

The resulting UTF8Span has the same lifetime constraints as `codeUnits`.

> **Note**: O(n)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/init(validating:))*