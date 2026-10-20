# autocapitalization(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets whether to apply auto-capitalization to this view.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`textInputAutocapitalization(_:)`](./textinputautocapitalization%28_%29.md) instead.

## Declaration

```swift
nonisolated
func autocapitalization(_ style: UITextAutocapitalizationType) -> some View
```

#### Discussion

Use this method when you need to automatically capitalize words, sentences, or other text like proper nouns.

In example below, as the user enters text each word is automatically capitalized:

```swift
TextField("Last, First", text: $fullName)
    .autocapitalization(UITextAutocapitalizationType.words)
```

The [`UITextAutocapitalizationType`](../../UIKit/uitextautocapitalizationtype.md) enumeration defines the available capitalization modes. The default is [`UITextAutocapitalizationType.sentences`](../../UIKit/uitextautocapitalizationtype/sentences.md).

## Parameters

- `style`: One of the autocapitalization modes defined in the [`UITextAutocapitalizationType`](../../UIKit/uitextautocapitalizationtype.md) enumeration.

## See Also

### Text modifiers
- [func disableAutocorrection(Bool?) -> some View](./disableautocorrection%28_%29.md)
  Sets whether to disable autocorrection for this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/autocapitalization(_:))*