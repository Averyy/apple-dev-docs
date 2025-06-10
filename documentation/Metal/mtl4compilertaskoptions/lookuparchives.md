# lookupArchives

**Framework**: Metal  
**Kind**: property

Specifies a set of archive instances this compilation process uses for accelerating the build process.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var lookupArchives: [any MTL4Archive]? { get set }
```

#### Discussion

In case of a match in the archive, the compiler can skip one or more compilation tasks, speeding up the build process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compilertaskoptions/lookuparchives)*