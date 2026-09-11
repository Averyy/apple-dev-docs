# hash(into:)

**Framework**: System  
**Kind**: method

Hashes the meaningful file-metadata fields of a `Stat` struct.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func hash(into hasher: inout Hasher)
```

#### Discussion

These are the same fields compared by `==`, fed in the same order. Alignment padding and platform reserved/“spare” fields are not hashed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/hash(into:))*