# textInputAutocapitalization(_:)

**Framework**: RealityKit  
**Kind**: method

Sets how often the shift key in the keyboard is automatically enabled.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func textInputAutocapitalization(_ autocapitalization: TextInputAutocapitalization?) -> some View
```

#### Discussion

Use `textInputAutocapitalization(_:)` when you need to automatically capitalize words, sentences, or other text like proper nouns.

In example below, as the user enters text the shift key is automatically enabled before every word:

```None
TextField("Last, First", text: $fullName)
    .textInputAutocapitalization(.words)
```

The `TextInputAutocapitalization` struct defines the available autocapitalizing behavior. Providing `nil` to  this view modifier does not change the autocapitalization behavior. The default is `TextInputAutocapitalization.sentences`.

## Parameters

- `autocapitalization`: One of the capitalizing behaviors   defined in the   struct or nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewdefaultplaceholder/textinputautocapitalization(_:))*