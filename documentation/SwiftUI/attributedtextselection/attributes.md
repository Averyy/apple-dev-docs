# AttributedTextSelection.Attributes

**Framework**: SwiftUI  
**Kind**: struct

A sequence of all attribute values a selection has in a certain text.

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
struct Attributes<Text>
```

#### Overview

The values of a selection are the attribute values of each run that is fully or partially selected, or the typing attributes in the case the selection is an insertion point.

By default, the sequence contains the attribute container for every run or the typing attributes. Use the [`AttributedTextSelection.Attributes`](attributedtextselection/attributes.md)’ subscript to obtain only the values for a single attribute:

```swift
selection.attributes(in: text)[\.foregroundColor].contains(.red)
```

## Topics

### Subscripts
- [subscript(_:)](attributedtextselection/attributes/subscript(_:).md)
  Returns a sequence which iterates of the values of a single attribute.

## Relationships

### Conforms To
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextselection/attributes)*