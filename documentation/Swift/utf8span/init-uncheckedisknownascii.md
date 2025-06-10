# init(unchecked:isKnownASCII:)

**Framework**: Swift  
**Kind**: init

Creates a UTF8Span, bypassing safety and security checks. The caller must guarantee that `codeUnits` contains validly-encoded UTF-8, or else undefined behavior may result upon use. If `isKnownASCII: true is passed`, the contents must be ASCII, or else undefined behavior may result upon use.

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
init(unchecked codeUnits: Span<UInt8>, isKnownASCII: Bool = false)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/init(unchecked:isknownascii:))*