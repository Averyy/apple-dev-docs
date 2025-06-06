# translationTask(source:target:action:)

**Framework**: SwiftUI  
**Kind**: method

Adds a task to perform before this view appears or when the specified source or target languages change.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+

## Declaration

```swift
nonisolated
func translationTask(source: Locale.Language? = nil, target: Locale.Language? = nil, action: @escaping (TranslationSession) async -> Void) -> some View
```

#### Discussion

This task provides an instance of `TranslationSession` to use to perform translations.

If you need to perform new translations again with the same `source` and `target` language, it’s better to use [`translationTask(_:action:)`](View/translationTask(_:action:).md) and call `TranslationSession/Configuration/invalidate()`.

For example, you can translate when content appears:

```swift
 struct ContentView: View {
     var sourceText = "Hallo, Welt!"
     var sourceLanguage: Locale.Language?
     var targetLanguage: Locale.Language?

     @State private var targetText: String?

     var body: some View {
         Text(targetText ?? sourceText)
             .translationTask(
                 source: sourceLanguage,
                 target: targetLanguage
             ) { session in
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
```

The system throws a `fatalError` if you use a `TranslationSession` instance after the view it attaches to disappears, or if you use it after changing the `source` or `target` parameters, causing the `action` closure to provide a new `TranslationSession` instance.

## Parameters

- `source`: The language the source content is in. If this is   the session tries to   identify the language, and prompt the user to pick the source language if it’s unclear. All   text translated within the session should be in the same source language. Changing this   value cancels previous tasks and creates a new one to perform translations again.
- `target`: The language to translate content into. A   value means the session picks a   target according to the user’s  , and the  .   Changing this value cancels previous tasks and create a new one to perform   translations again.
- `action`: A closure that runs when the view first appears, and when   or    change.  It provides a   instance to perform   one or multiple translations.

## See Also

- [func translationPresentation(isPresented: Binding<Bool>, text: String, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge, replacementAction: ((String) -> Void)?) -> some View](view/translationpresentation(ispresented:text:attachmentanchor:arrowedge:replacementaction:).md)
  Presents a translation popover when a given condition is true.
- [func translationTask(TranslationSession.Configuration?, action: (TranslationSession) async -> Void) -> some View](view/translationtask(_:action:).md)
  Adds a task to perform before this view appears or when the translation configuration changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/translationtask(source:target:action:))*