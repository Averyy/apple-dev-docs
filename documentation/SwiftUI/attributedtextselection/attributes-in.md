# attributes(in:)

**Framework**: SwiftUI  
**Kind**: method

Obtain a lazy sequence of all attribute values the selection has in a given text.

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
func attributes(in text: AttributedString) -> AttributedTextSelection.Attributes<AttributedString>
```

#### Discussion

The attribute values of a selection are the attribute values of each run that is fully or partially selected, or the typing attributes in the case the selection is an insertion point.

By default, the sequence contains the attribute container for every run or the typing attributes. Use the [`AttributedTextSelection.Attributes`](attributedtextselection/attributes.md)’ subscript to obtain only the values for a single attribute:

```swift
selection.attributtes(in: text)[\.foregroundColor].contains(.red)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextselection/attributes(in:))*