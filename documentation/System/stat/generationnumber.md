# generationNumber

**Framework**: System  
**Kind**: property

File generation number

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
var generationNumber: Int { get set }
```

#### Discussion

The file generation number is used to distinguish between different files that have used the same inode over time.

The corresponding C property is `st_gen`.

> **Note**: Only available on Darwin, FreeBSD, and OpenBSD.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/generationnumber)*