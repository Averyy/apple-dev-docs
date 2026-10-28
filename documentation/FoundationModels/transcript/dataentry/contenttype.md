# contentType

**Framework**: Foundation Models  
**Kind**: property  
**Role**: Instance Property

A `UTType` identifying how to interpret [`content`](./content.md).

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- macOS 27.2+
- visionOS 27.2+
- watchOS 27.2+

## Declaration

```swift
var contentType: UTType
```

## Discussion

Packages that ship data entry payloads should declare a dedicated `UTType` conforming to `.data` (or a more specific format like `.json`) and expose it as a static extension member so consumers can match on it directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/dataentry/contenttype)*