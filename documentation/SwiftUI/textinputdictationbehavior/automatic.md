# automatic

**Framework**: SwiftUI  
**Kind**: property

A platform-appropriate default text input dictation behavior.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
static let automatic: TextInputDictationBehavior
```

#### Discussion

The automatic behavior uses a [`TextInputDictationActivation`](textinputdictationactivation.md) value of [`onLook`](textinputdictationactivation/onlook.md) for visionOS apps and [`onSelect`](textinputdictationactivation/onselect.md) for iOS apps.

## See Also

- [static func inline(activation: TextInputDictationActivation) -> TextInputDictationBehavior](textinputdictationbehavior/inline(activation:).md)
  Adds a dictation microphone in the search bar.
- [static let preventDictation: TextInputDictationBehavior](textinputdictationbehavior/preventdictation.md)
  Prevents the search bar from having a dictation microphone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/textinputdictationbehavior/automatic)*