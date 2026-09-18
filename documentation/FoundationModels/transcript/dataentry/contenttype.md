# contentType

**Framework**: Foundation Models  
**Kind**: property

A `UTType` identifying how to interpret [`content`](transcript/dataentry/content.md).

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)
- Mac Catalyst 27.2+ (Beta)
- macOS 27.2+ (Beta)
- visionOS 27.2+ (Beta)
- watchOS 27.2+ (Beta)

## Declaration

```swift
var contentType: UTType
```

#### Discussion

Packages that ship data entry payloads should declare a dedicated `UTType` conforming to `.data` (or a more specific format like `.json`) and expose it as a static extension member so consumers can match on it directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/dataentry/contenttype)*