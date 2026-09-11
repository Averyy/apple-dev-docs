# ==(_:_:)

**Framework**: System  
**Kind**: op

Compares the meaningful file-metadata fields of two `Stat` values.

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
static func == (lhs: Stat, rhs: Stat) -> Bool
```

#### Discussion

Alignment padding and platform reserved/“spare” fields are not compared.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/==(_:_:))*