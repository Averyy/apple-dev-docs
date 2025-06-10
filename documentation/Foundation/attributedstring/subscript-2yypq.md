# subscript(_:)

**Framework**: Foundation  
**Kind**: subscript

Obtain the discontiguous substring of a selection.

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
subscript(selection: AttributedTextSelection) -> DiscontiguousAttributedSubstring { get }
```

#### Overview

In the case of an insertion point, this substring is empty. Otherwise, the substring contains all selected characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/subscript(_:)-2yypq)*