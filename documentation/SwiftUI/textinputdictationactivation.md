# TextInputDictationActivation

**Framework**: SwiftUI  
**Kind**: struct

A configuration that determines what starts dictation in a search field.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
struct TextInputDictationActivation
```

#### Overview

Pass a value of this type to [`inline(activation:)`](textinputdictationbehavior/inline(activation:).md) when you want to keep the dictation microphone in a search field but choose how someone begins speaking:

```swift
NavigationStack {
    RecipeList(matching: query)
}
.searchable(text: $query)
.searchDictationBehavior(.inline(activation: .onLook))
```

On visionOS, [`onLook`](textinputdictationactivation/onlook.md) starts dictation as soon as someone looks at the field. Choose [`onSelect`](textinputdictationactivation/onselect.md) instead when speaking early would be disruptive.

## Topics

### Getting activation values
- [static let onLook: TextInputDictationActivation](textinputdictationactivation/onlook.md)
  A configuration that activates dictation when someone selects the microphone or looks at the entry field.
- [static let onSelect: TextInputDictationActivation](textinputdictationactivation/onselect.md)
  A configuration that activates dictation when someone selects the microphone.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func searchDictationBehavior(TextInputDictationBehavior) -> some View](view/searchdictationbehavior(_:).md)
  Configures the dictation behavior for any search fields configured by the searchable modifier.
- [struct TextInputDictationBehavior](textinputdictationbehavior.md)
  A behavior that determines whether a search field offers dictation, and what starts it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textinputdictationactivation)*