# journalingSuggestionsPicker(isPresented:onCompletion:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents a visual picker interface that contains events and images that a person can select to retrieve more information.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+

## Declaration

```swift
@MainActor
@preconcurrency func journalingSuggestionsPicker(isPresented: Binding<Bool>, onCompletion: @escaping (JournalingSuggestion) async -> Void) -> some View
```

## Discussion

For more information about the Journaling Suggestions picker, see: doc:presenting-the-suggestions-picker-and-processing-a-selection.

## Parameters

- `isPresented`: A binding to a `Bool` value that determines whether to show the picker.
- `onCompletion`: Code that you supply, which processes any suggestions that a person may choose in the picker.

## See Also

### Presenting journaling suggestions
- [func journalingSuggestionsPicker(isPresented: Binding<Bool>, journalingSuggestionToken: JournalingSuggestionPresentationToken?, onCompletion: (JournalingSuggestion) async -> Void) -> some View](./journalingsuggestionspicker%28ispresented,journalingsuggestiontoken,oncompletion%29.md)
  Presents a visual picker interface that contains events and images that a person can select to retrieve more information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/journalingsuggestionspicker(ispresented:oncompletion:))*