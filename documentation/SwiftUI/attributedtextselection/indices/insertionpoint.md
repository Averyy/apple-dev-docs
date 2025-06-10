# AttributedTextSelection.Indices.insertionPoint(_:)

**Framework**: SwiftUI  
**Kind**: case

The index of a single insertion point.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
case insertionPoint(AttributedString.Index)
```

#### Discussion

The an insertion point at the `startIndex` of an attributed string is equivalent to a caret preceding the first character. An insertion point using `endIndex` is valid. It is equivalent to a caret located after the last character in the attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextselection/indices/insertionpoint(_:))*