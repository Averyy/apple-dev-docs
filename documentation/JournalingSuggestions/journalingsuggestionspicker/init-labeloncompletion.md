# init(label:onCompletion:)

**Framework**: Journaling Suggestions  
**Kind**: init

Creates a suggestions picker within the given view.

**Availability**:
- iOS 17.2+

## Declaration

```swift
@MainActor
@preconcurrency init(@ViewBuilder label: () -> Label, onCompletion: @escaping (JournalingSuggestion) async -> Void)
```

## Parameters

- `label`: A view that describes the suggestion picker’s purpose in the context of your app.
- `onCompletion`: Code that you supply, which processes any suggestions that a person chooses in the picker.

## See Also

- [init(LocalizedStringKey, onCompletion: (JournalingSuggestion) async -> Void)](journalingsuggestionspicker/init(_:oncompletion:)-7uxov.md)
  Creates a suggestions picker with button text defined by the given localized string key.
- [init<S>(S, onCompletion: (JournalingSuggestion) async -> Void)](journalingsuggestionspicker/init(_:oncompletion:)-4e82p.md)
  Creates a suggestions picker with button text defined by the given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/init(label:oncompletion:))*