# TextInputDictationBehavior

**Framework**: SwiftUI  
**Kind**: struct

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
struct TextInputDictationBehavior
```

## Topics

### Getting behavior values
- [static let automatic: TextInputDictationBehavior](textinputdictationbehavior/automatic.md)
  A platform-appropriate default text input dictation behavior.
- [static func inline(activation: TextInputDictationActivation) -> TextInputDictationBehavior](textinputdictationbehavior/inline(activation:).md)
  Adds a dictation microphone in the search bar.
- [static let preventDictation: TextInputDictationBehavior](textinputdictationbehavior/preventdictation.md)
  Prevents the search bar from having a dictation microphone.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func searchDictationBehavior(TextInputDictationBehavior) -> some View](view/searchdictationbehavior(_:).md)
  Configures the dictation behavior for any search fields configured by the searchable modifier.
- [struct TextInputDictationActivation](textinputdictationactivation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textinputdictationbehavior)*