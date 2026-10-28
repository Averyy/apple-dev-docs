# TextInputDictationBehavior

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A behavior that determines whether a search field offers dictation, and what starts it.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
struct TextInputDictationBehavior
```

## Overview

Pass a value of this type to the [`searchDictationBehavior(_:)`](./view/searchdictationbehavior%28_%29.md) modifier. Search fields use [`automatic`](./textinputdictationbehavior/automatic.md) unless you choose otherwise.

The following example keeps the dictation microphone in the search field, but waits for someone to select it before listening:

```swift
NavigationStack {
    RecipeList(matching: query)
}
.searchable(text: $query)
.searchDictationBehavior(.inline(activation: .onSelect))
```

On visionOS you can remove the microphone from the field entirely with [`preventDictation`](./textinputdictationbehavior/preventdictation.md).

## Topics

### Getting behavior values
- [static let automatic: TextInputDictationBehavior](./textinputdictationbehavior/automatic.md)
  A platform-appropriate default text input dictation behavior.
- [static func inline(activation: TextInputDictationActivation) -> TextInputDictationBehavior](./textinputdictationbehavior/inline%28activation%29.md)
  Adds a dictation microphone in the search bar.
- [static let preventDictation: TextInputDictationBehavior](./textinputdictationbehavior/preventdictation.md)
  Prevents the search bar from having a dictation microphone.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Dictating text
- [func searchDictationBehavior(TextInputDictationBehavior) -> some View](./view/searchdictationbehavior%28_%29.md)
  Configures the dictation behavior for any search fields configured by the searchable modifier.
- [struct TextInputDictationActivation](./textinputdictationactivation.md)
  A configuration that determines what starts dictation in a search field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textinputdictationbehavior)*