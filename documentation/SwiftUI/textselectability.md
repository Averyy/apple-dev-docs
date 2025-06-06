# TextSelectability

**Framework**: SwiftUI  
**Kind**: protocol

A type that describes the ability to select text.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
protocol TextSelectability
```

#### Overview

To configure whether people can select text in your app, use the [`textSelection(_:)`](view/textselection(_:).md) modifier, passing in a text selectability value like [`enabled`](textselectability/enabled.md) or [`disabled`](textselectability/disabled.md).

## Topics

### Getting selectability options
- [static var enabled: EnabledTextSelectability](textselectability/enabled.md)
  A selectability value that enables text selection by a person using your app.
- [static var disabled: DisabledTextSelectability](textselectability/disabled.md)
  A selectability value that disables text selection by the person using your app.
### Specifying selectability
- [static var allowsSelection: Bool](textselectability/allowsselection.md)
  A Boolean value that indicates whether the selectability type allows selection.
### Supporting types
- [struct EnabledTextSelectability](enabledtextselectability.md)
  A selectability type that enables text selection by the person using your app.
- [struct DisabledTextSelectability](disabledtextselectability.md)
  A selectability type that disables text selection by the person using your app.

## Relationships

### Conforming Types
- [DisabledTextSelectability](disabledtextselectability.md)
- [EnabledTextSelectability](enabledtextselectability.md)

## See Also

- [func textSelection<S>(S) -> some View](view/textselection(_:).md)
  Controls whether people can select text within this view.
- [struct TextSelection](textselection.md)
  Represents a selection of text.
- [func textSelectionAffinity(TextSelectionAffinity) -> some View](view/textselectionaffinity(_:).md)
  Sets the direction of a selection or cursor relative to a text character.
- [var textSelectionAffinity: TextSelectionAffinity](environmentvalues/textselectionaffinity.md)
  A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
- [enum TextSelectionAffinity](textselectionaffinity.md)
  A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textselectability)*