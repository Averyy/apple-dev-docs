# init(validating:)

**Framework**: Swift  
**Kind**: init

Creates a UTF8Span containing `codeUnits`. Validates that the input is valid UTF-8, otherwise throws an error.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
init(validating codeUnits: consuming Span<UInt8>) throws(UTF8.ValidationError)
```

#### Discussion

The resulting UTF8Span has the same lifetime constraints as `codeUnits`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/init(validating:))*