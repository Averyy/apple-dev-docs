# hash(into:)

**Framework**: System  
**Kind**: method

Hashes the meaningful file-metadata fields of a `Stat` struct.

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
func hash(into hasher: inout Hasher)
```

#### Discussion

These are the same fields compared by `==`, fed in the same order. Alignment padding and platform reserved/“spare” fields are not hashed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/hash(into:))*