# CInterop

**Framework**: System  
**Kind**: enum

A namespace for C and platform types

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum CInterop
```

## Topics

### Type Aliases
- [typealias Char](cinterop/char.md)
  The C `char` type
- [typealias Mode](cinterop/mode.md)
- [typealias PlatformChar](cinterop/platformchar.md)
  The platform’s preferred character type. On Unix, this is an 8-bit C `char` (which may be signed or unsigned, depending on platform). On Windows, this is `UInt16` (a “wide” character).
- [typealias PlatformUnicodeEncoding](cinterop/platformunicodeencoding.md)
  The platform’s preferred Unicode encoding. On Unix this is UTF-8 and on Windows it is UTF-16. Native strings may contain invalid Unicode, which will be handled by either error-correction or failing, depending on API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/cinterop)*