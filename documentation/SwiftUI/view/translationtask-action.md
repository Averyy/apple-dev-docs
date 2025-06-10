# translationTask(_:action:)

**Framework**: SwiftUI  
**Kind**: method

Adds a task to perform before this view appears or when the translation configuration changes.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+ (Beta)
- macOS 15.0+

## Declaration

```swift
nonisolated
func translationTask(_ configuration: TranslationSession.Configuration?, action: @escaping (TranslationSession) async -> Void) -> some View
```

#### Discussion

This task provides an instance of `TranslationSession` to use in translations. Whenever `TranslationSession/Configuration` changes and isn’t `nil`, the closure `action` runs, providing a `TranslationSession` instance to perform one or more translations.

For example, you can create a `TranslationSession/Configuration` in response to a button press to trigger translation:

```swift
struct ContentView: View {
    @State private var sourceText = "Hallo, Welt!"
    var sourceLanguage: Locale.Language?
    var targetLanguage: Locale.Language?

    @State private var targetText: String?
    @State private var configuration: TranslationSession.Configuration?

    var body: some View {
        VStack {
            Text(targetText ?? sourceText)
            Button("Translate") {
                guard configuration == nil else {
                    configuration?.invalidate()
                    return
                }

                 configuration = TranslationSession.Configuration(
                    source: sourceLanguage,
                    target: targetLanguage)
            }
            .translationTask(configuration) { session in
                Task { @MainActor in
                    do {
                        let response = try await session.translate(sourceText)
                        targetText = response.targetText
                    } catch {
                        // code to handle error
                    }
                }
            }
        }
    }
}
```

The system throws a `fatalError` if you use a `TranslationSession` instance after the view it attaches to disappears, or if you use it after changing the `configuration`, causing the `action` closure to provide a new `TranslationSession` instance.

## Parameters

- `configuration`: A configuration for a  . When this configuration is non-nil and changes.   the   runs providing an instance of    to perform translations.
- `action`: A closure that runs when the  is non-nil and changes.   This closure runs when the view appears if   is initially non-nil. It provides a    instance to perform one or multiple translations.

## See Also

- [func translationPresentation(isPresented: Binding<Bool>, text: String, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge, replacementAction: ((String) -> Void)?) -> some View](view/translationpresentation(ispresented:text:attachmentanchor:arrowedge:replacementaction:).md)
  Presents a translation popover when a given condition is true.
- [func translationTask(source: Locale.Language?, target: Locale.Language?, action: (TranslationSession) async -> Void) -> some View](view/translationtask(source:target:action:).md)
  Adds a task to perform before this view appears or when the specified source or target languages change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/translationtask(_:action:))*