# isKnownASCII

**Framework**: Swift  
**Kind**: property

Returns whether contents are known to be all-ASCII. A return value of `true` means that all code units are ASCII. A return value of `false` means there  be non-ASCII content.

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
var isKnownASCII: Bool { get }
```

#### Discussion

ASCII-ness is checked and remembered during UTF-8 validation, so this is often equivalent to is-ASCII, but there are some situations where we might return `false` even when the content happens to be all-ASCII.

For example, a UTF-8 span generated from a `String` that at some point contained non-ASCII content would report false for `isKnownASCII`, even if that String had subsequent mutation operations that removed any non-ASCII content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/isknownascii)*