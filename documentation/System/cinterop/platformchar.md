# CInterop.PlatformChar

**Framework**: System  
**Kind**: typealias

The platform’s preferred character type. On Unix, this is an 8-bit C `char` (which may be signed or unsigned, depending on platform). On Windows, this is `UInt16` (a “wide” character).

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
typealias PlatformChar = CInterop.Char
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/cinterop/platformchar)*