# journalingSuggestionsPicker(isPresented:journalingSuggestionToken:onCompletion:)

**Framework**: SwiftUI  
**Kind**: method

Presents a visual picker interface that contains events and images that a person can select to retrieve more information.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func journalingSuggestionsPicker(isPresented: Binding<Bool>, journalingSuggestionToken: JournalingSuggestionPresentationToken?, onCompletion: @escaping (JournalingSuggestion) async -> Void) -> some View
```

#### Discussion

For more information about the Journaling Suggestions picker, see: doc:presenting-the-suggestions-picker-and-processing-a-selection.

## Parameters

- `isPresented`: A binding to a   value that determines whether to show the picker.
- `journalingSuggestionToken`: A   struct to determine the content shown in the picker.
- `onCompletion`: Code that you supply, which processes any suggestions that a person may choose in the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/journalingsuggestionspicker(ispresented:journalingsuggestiontoken:oncompletion:))*