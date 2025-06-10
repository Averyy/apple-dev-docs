# AttributedTextSelection

**Framework**: SwiftUI  
**Kind**: struct

Represents a selection of attributed text.

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
struct AttributedTextSelection
```

#### Overview

A selection is either an insertion point (e.g. a cursor in the text), or spans over a range of characters. While that range is always visually contiguous, it may not be logically contiguous in the text storage. Specifically, a single selection value cannot represent multiple cursors.

This is frequently used to represent selection of text in a `TextEditor`. The following example shows a text editor that leverages text selection to offer live suggestions based on the current selection.

```swift
struct SuggestionTextEditor: View {
    @State var text: AttributedString = ""
    @State var selection = AttributedTextSelection()

    var body: some View {
        VStack {
            TextEditor(text: $text, selection: $selection)
            // A helper view that offers live suggestions based on selection.
            SuggestionsView(substrings: getSubstrings(
                text: text, indices: selection.indices(in: text))
        }
    }

    private func getSubstrings(
        text: String, indices: AttributedTextSelection.Indices
    ) -> [Substring] {
        // Resolve substrings representing the current selection...
    }
}

struct SuggestionsView: View { ... }
```

You can also use the [`textSelectionAffinity(_:)`](view/textselectionaffinity(_:).md) modifier to specify a selection affinity on the given hierarchy:

```swift
struct SuggestionTextEditor: View {
    @State var text: AttributedString = ""
    @State var selection = AttributedTextSelection()

    var body: some View {
        VStack {
            TextEditor(text: $text, selection: $selection)
            // A helper view that offers live suggestions based on selection.
            SuggestionsView(substrings: getSubstrings(
                text: text, indices: selection.indices(in: text))
        }
        .textSelectionAffinity(.upstream)
    }

    private func getSubstrings(
        text: String, indices: AttributedTextSelection.Indices
    ) -> [Substring] {
        // Resolve substrings representing the current selection...
    }
}

struct SuggestionsView: View { ... }
```

> **Note**: [`TextSelectionAffinity`](textselectionaffinity.md), [`TextEditor`](texteditor.md)

## Topics

### Structures
- [AttributedTextSelection.Attributes](attributedtextselection/attributes.md)
  A sequence of all attribute values a selection has in a certain text.
### Initializers
- [init()](attributedtextselection/init.md)
  Initialize the default selection for a new text editor.
- [init(insertionPoint: AttributedString.Index, typingAttributes: AttributeContainer?)](attributedtextselection/init(insertionpoint:typingattributes:).md)
  Initialize a selection to a single insertion point.
- [init(range: Range<AttributedString.Index>)](attributedtextselection/init(range:).md)
  Initialize a selection to a character range.
- [init(ranges: RangeSet<AttributedString.Index>)](attributedtextselection/init(ranges:).md)
  Initialize a selection to character ranges.
### Instance Methods
- [func affinity(in: AttributedString) -> TextSelectionAffinity](attributedtextselection/affinity(in:).md)
  Return the selection affinity of the selection.
- [func attributes(in: AttributedString) -> AttributedTextSelection.Attributes<AttributedString>](attributedtextselection/attributes(in:).md)
  Obtain a lazy sequence of all attribute values the selection has in a given text.
- [func indices(in: AttributedString) -> AttributedTextSelection.Indices](attributedtextselection/indices(in:).md)
  The current text selection indices.
- [func typingAttributes(in: AttributedString) -> AttributeContainer](attributedtextselection/typingattributes(in:).md)
  Returns the typing attributes for a corresponding text.
### Enumerations
- [AttributedTextSelection.Indices](attributedtextselection/indices.md)
  The indices of the current selection.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func textSelection<S>(S) -> some View](view/textselection(_:).md)
  Controls whether people can select text within this view.
- [protocol TextSelectability](textselectability.md)
  A type that describes the ability to select text.
- [struct TextSelection](textselection.md)
  Represents a selection of text.
- [func textSelectionAffinity(TextSelectionAffinity) -> some View](view/textselectionaffinity(_:).md)
  Sets the direction of a selection or cursor relative to a text character.
- [var textSelectionAffinity: TextSelectionAffinity](environmentvalues/textselectionaffinity.md)
  A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
- [enum TextSelectionAffinity](textselectionaffinity.md)
  A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/attributedtextselection)*