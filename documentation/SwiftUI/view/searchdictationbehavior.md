# searchDictationBehavior(_:)

**Framework**: SwiftUI  
**Kind**: method

Configures the dictation behavior for any search fields configured by the searchable modifier.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func searchDictationBehavior(_ dictationBehavior: TextInputDictationBehavior) -> some View
```

#### Discussion

By default, search fields on visionOS will automatically start dictation when looking at the dictation button in the search field. You can change this behavior by providing a value of [`preventDictation`](textinputdictationbehavior/preventdictation.md) to this modifier.

See the [`TextInputDictationBehavior`](textinputdictationbehavior.md) type for more information on the available dictation behaviors.

## See Also

- [struct TextInputDictationActivation](textinputdictationactivation.md)
- [struct TextInputDictationBehavior](textinputdictationbehavior.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/searchdictationbehavior(_:))*