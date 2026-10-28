# translationTask(_:action:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds a task to perform before this view appears or when the translation configuration changes.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+
- macOS 15.0+

## Declaration

```swift
nonisolated
func translationTask(_ configuration: TranslationSession.Configuration?, action: @escaping (TranslationSession) async -> Void) -> some View
```

## Discussion

This task provides an instance of [`TranslationSession`](../../Translation/translationsession.md) to use in translations. Whenever [`TranslationSession.Configuration`](../../Translation/translationsession/configuration.md)  changes and isn’t `nil`, the closure `action` runs, providing a session instance to perform one or more translations.

For example, you can create a configuration in response to a button press to initiate the translation:

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
                        // Handle any errors.
                    }
                }
            }
        }
    }
}
```

The system throws a `fatalError` if you use a [`TranslationSession`](../../Translation/translationsession.md) instance after the attached view disappears or if you use it after changing the configuration. This causes the `action` closure to provide a new session instance.

## Parameters

- `configuration`: A configuration for a [`TranslationSession`](../../Translation/translationsession.md). When this configuration is non-`nil` and changes, the `action` runs providing an instance of the session to perform translations.
- `action`: This closure runs when the [`TranslationSession.Configuration`](../../Translation/translationsession/configuration.md) is non-`nil` and changes. If the configuration is initially non-`nil`, it calls the action closure when the view appears and provides a session to perform one or more translations.

## See Also

### Showing a translation
- [func translationPresentation(isPresented: Binding<Bool>, text: String, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge, replacementAction: ((String) -> Void)?) -> some View](./translationpresentation%28ispresented,text,attachmentanchor,arrowedge,replacementaction%29.md)
  Presents a translation popover when a given condition is true.
- [func translationTask(source: Locale.Language?, target: Locale.Language?, action: (TranslationSession) async -> Void) -> some View](./translationtask%28source,target,action%29.md)
  Adds a task to perform before this view appears or when the specified source or target languages change.
- [func translationTask(source: Locale.Language?, target: Locale.Language?, preferredStrategy: TranslationSession.Strategy, action: (TranslationSession) async -> Void) -> some View](./translationtask%28source,target,preferredstrategy,action%29.md)
  Adds a task to perform before this view appears or when the specified source or target languages change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/translationtask(_:action:))*