# init(_:onCompletion:)

**Framework**: Journaling Suggestions  
**Kind**: init

Creates a suggestions picker with button text defined by the given localized string key.

**Availability**:
- iOS 17.2+

## Declaration

```swift
@MainActor
@preconcurrency init(_ title: LocalizedStringKey, onCompletion: @escaping (JournalingSuggestion) async -> Void)
```

#### Discussion

This initializer creates a text view similar to the results of calling [`init(_:tableName:bundle:comment:)`](https://developer.apple.com/documentation/SwiftUI/Text/init(_:tableName:bundle:comment:)). See [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) for more information about localizing strings.

## Parameters

- `title`: A localized string key that describes the suggestion picker’s purpose in the context of your app.
- `onCompletion`: Code that you supply, which processes any suggestions that a person chooses in the picker.

## See Also

- [init(label: () -> Label, onCompletion: (JournalingSuggestion) async -> Void)](journalingsuggestionspicker/init(label:oncompletion:).md)
  Creates a suggestions picker within the given view.
- [init<S>(S, onCompletion: (JournalingSuggestion) async -> Void)](journalingsuggestionspicker/init(_:oncompletion:)-4e82p.md)
  Creates a suggestions picker with button text defined by the given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/init(_:oncompletion:)-7uxov)*