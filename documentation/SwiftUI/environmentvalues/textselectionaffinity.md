# textSelectionAffinity

**Framework**: SwiftUI  
**Kind**: property

A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).

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
var textSelectionAffinity: TextSelectionAffinity { get set }
```

#### Discussion

You can configure the selection affinity on a given hierarchy by using the [`textSelectionAffinity(_:)`](view/textselectionaffinity(_:).md) modifier.

## See Also

- [func textSelection<S>(S) -> some View](view/textselection(_:).md)
  Controls whether people can select text within this view.
- [protocol TextSelectability](textselectability.md)
  A type that describes the ability to select text.
- [struct TextSelection](textselection.md)
  Represents a selection of text.
- [func textSelectionAffinity(TextSelectionAffinity) -> some View](view/textselectionaffinity(_:).md)
  Sets the direction of a selection or cursor relative to a text character.
- [enum TextSelectionAffinity](textselectionaffinity.md)
  A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
- [struct AttributedTextSelection](attributedtextselection.md)
  Represents a selection of attributed text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/textselectionaffinity)*