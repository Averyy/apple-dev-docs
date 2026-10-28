# init(_:onCompletion:)

**Framework**: Journaling Suggestions  
**Kind**: init  
**Role**: Initializer

Creates a suggestions picker with button text defined by the given string.

**Availability**:
- iOS 17.2+

## Declaration

```swift
@MainActor
@preconcurrency init<S>(_ title: S, onCompletion: @escaping (JournalingSuggestion) async -> Void) where S : StringProtocol
```

Available when `Label` is `Text`.

## Discussion

This initializer creates a text view on your behalf and uses the string argument to set its text.

## Parameters

- `title`: A string that describes the suggestion picker’s purpose in the context of your app.
- `onCompletion`: Code that you supply, which processes any suggestions that a person chooses in the picker.

## See Also

### Creating a suggestions picker
- [init(label: () -> Label, onCompletion: (JournalingSuggestion) async -> Void)](./init%28label,oncompletion%29.md)
  Creates a suggestions picker within the given view.
- [init(LocalizedStringKey, onCompletion: (JournalingSuggestion) async -> Void)](./init%28_,oncompletion%29-7uxov.md)
  Creates a suggestions picker with button text defined by the given localized string key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/init(_:oncompletion:)-4e82p)*