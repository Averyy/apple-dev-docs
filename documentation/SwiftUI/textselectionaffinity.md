# TextSelectionAffinity

**Framework**: SwiftUI  
**Kind**: enum

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
enum TextSelectionAffinity
```

#### Overview

This type also determines whether, for example, the insertion point appears after the last character on a line or before the first character on the following line in cases where text wraps across line boundaries.

Given the scenario `hello|مرحبا`, where `|` represents the cursor & `مرحبا` represents “hello” in Arabic, the ambiguity arises because:

- If the cursor is associated with the end of the English word, it would be as if you’re continuing to type in English (LTR).
- If the cursor is associated with the beginning of the Arabic word, it would also be as if you’re continuing to type in Arabic (RTL).

`TextSelectionAffinity` helps resolve this ambiguity by determining the direction or association of the cursor relative to the surrounding text.

You can configure the selection affinity on a given hierarchy by using the [`textSelectionAffinity(_:)`](view/textselectionaffinity(_:).md) modifier:

```swift
struct SuggestionTextEditor: View {
    @State var text: String = ""
    @State var selection: TextSelection? = nil

    var body: some View {
        VStack {
            TextEditor(text: $text, selection: $selection)
            // A helper view that offers live suggestions based on selection.
            SuggestionsView(
                substrings: getSubstrings(text: text, indices: selection?.indices))
        }
        .textSelectionAffinity(.upstream)
    }

    private func getSubstrings(
        text: String, indices: TextSelection.Indices?
    ) -> [Substring] {
        // Resolve substrings representing the current selection...
    }
}

struct SuggestionsView: View { ... }
```

## Topics

### Enumeration Cases
- [TextSelectionAffinity.automatic](textselectionaffinity/automatic.md)
  A selection affinity determined by the framework based on the current context.
- [TextSelectionAffinity.downstream](textselectionaffinity/downstream.md)
  An downstream selection affinity. In this case, the cursor is associated with the character immediately after it.
- [TextSelectionAffinity.upstream](textselectionaffinity/upstream.md)
  An upstream selection affinity. In this case, the cursor is associated with the character immediately before it.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textselectionaffinity)*