# patterns

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A set of key paths that represent patterns that the data detection system identifies.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS

## Declaration

```swift
var patterns: Set<PartialKeyPath<UIPasteboard.DetectedValues>> { get }
```

## See Also

### Detected patterns
- [var probableWebSearch: String](./probablewebsearch.md)
  A string that the data detection system identifies as a probable web search item.
- [var probableWebURL: String](./probableweburl.md)
  A string that the data detection system identifies as a probable web URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/detectedvalues/patterns)*