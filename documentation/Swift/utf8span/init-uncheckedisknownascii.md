# init(unchecked:isKnownASCII:)

**Framework**: Swift  
**Kind**: init

Creates a UTF8Span, bypassing safety and security checks. The caller must guarantee that `codeUnits` contains validly-encoded UTF-8, or else undefined behavior may result upon use. If `isKnownASCII: true is passed`, the contents must be ASCII, or else undefined behavior may result upon use.

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
init(unchecked codeUnits: Span<UInt8>, isKnownASCII: Bool = false)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/init(unchecked:isknownascii:))*