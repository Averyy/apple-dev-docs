# autocapitalization(_:)

**Framework**: Journaling Suggestions  
**Kind**: method

Sets whether to apply auto-capitalization to this view.

**Availability**:
- iOS 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func autocapitalization(_ style: UITextAutocapitalizationType) -> some View
```

#### Discussion

Use `autocapitalization(_:)` when you need to automatically capitalize words, sentences, or other text like proper nouns.

In example below, as the user enters text each word is automatically capitalized:

```None
TextField("Last, First", text: $fullName)
    .autocapitalization(UITextAutocapitalizationType.words)
```

The [`UITextAutocapitalizationType`](https://developer.apple.com/documentation/UIKit/UITextAutocapitalizationType) enumeration defines the available capitalization modes. The default is [`UITextAutocapitalizationType.sentences`](https://developer.apple.com/documentation/UIKit/UITextAutocapitalizationType/sentences).

## Parameters

- `style`: One of the autocapitalization modes defined in the     enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/autocapitalization(_:))*