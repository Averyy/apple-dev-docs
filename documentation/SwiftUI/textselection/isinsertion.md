# isInsertion

**Framework**: SwiftUI  
**Kind**: property

Return `true` if the selection is an insertion point.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var isInsertion: Bool { get }
```

#### Discussion

An insertion point effectively represents a range that contains no characters, indicating a location in the string. This location refers to the point in the text where new characters will be inserted. In other words, it represents cases when the start and end index are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textselection/isinsertion)*