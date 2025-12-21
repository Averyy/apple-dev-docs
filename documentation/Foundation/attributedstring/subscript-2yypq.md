# subscript(_:)

**Framework**: Foundation  
**Kind**: subscript

Obtain the discontiguous substring of a selection.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
subscript(selection: AttributedTextSelection) -> DiscontiguousAttributedSubstring { get }
```

#### Overview

In the case of an insertion point, this substring is empty. Otherwise, the substring contains all selected characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/subscript(_:)-2yypq)*