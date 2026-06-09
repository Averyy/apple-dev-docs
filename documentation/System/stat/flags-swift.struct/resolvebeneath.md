# resolveBeneath

**Framework**: System  
**Kind**: property

If the path does not reside in the hierarchy beneath the starting directory, return an error.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static var resolveBeneath: Stat.Flags { get }
```

#### Discussion

The corresponding C constant is `AT_RESOLVE_BENEATH`.

> **Note**: Only available on Darwin and FreeBSD.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/flags-swift.struct/resolvebeneath)*