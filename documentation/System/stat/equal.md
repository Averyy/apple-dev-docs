# ==(_:_:)

**Framework**: System  
**Kind**: op

Compares the meaningful file-metadata fields of two `Stat` values.

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
static func == (lhs: Stat, rhs: Stat) -> Bool
```

#### Discussion

Alignment padding and platform reserved/“spare” fields are not compared.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/==(_:_:))*