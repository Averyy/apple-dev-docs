# TranslationSession

**Framework**: Translation  
**Kind**: class

A class that performs translations between a pair of languages.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+ (Beta)
- macOS 15.0+

## Declaration

```swift
class TranslationSession
```

#### Overview

In most cases you don’t instantiate this class directly. Instead, you obtain an instance of it by adding a [`translationTask(_:action:)`](https://developer.apple.com/documentation/SwiftUI/View/translationTask(_:action:)) or [`translationTask(source:target:action:)`](https://developer.apple.com/documentation/SwiftUI/View/translationTask(source:target:action:)) function to the SwiftUI view containing the content you want to translate, such as a [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) view. When you do, the function passes you an instance of a translation session in its `action` closure which triggers as soon as the view appears. After you receive this instance, use one of the translate functions to translate one or more strings of text.

In contexts where there’s no SwiftUI view to present from, use the [`init(installedSource:target:)`](translationsession/init(installedsource:target:).md) initializer to attempt to translate between languages already installed on the device.

The following example demonstrates how to translate a single string of text:

```swift
struct TranslationExample: View {
    var sourceText: String
    var sourceLanguage: Locale.Language?
    var targetLanguage: Locale.Language?

    @State private var targetText: String?

    var body: some View {
        Text(targetText ?? sourceText)
            .translationTask(
                source: sourceLanguage,
                target: targetLanguage
            ) { session in
                do {
                    let response = try await session.translate(sourceText)
                    targetText = response.targetText
                } catch {
                    // Handle error.
                }
            }
    }
}
```

> **Note**: All translations using the `TranslationSession` class are processed on the user’s device. Apple may collect API usage and performance metrics including the app bundle ID and the original and translated language, but this data does not include the original or translated content.

## Topics

### Translating text
- [func translate(String) async throws -> TranslationSession.Response](translationsession/translate(_:).md)
  Translates a single string of text.
- [func translate(batch: [TranslationSession.Request]) -> TranslationSession.BatchResponse](translationsession/translate(batch:).md)
  Translates multiple strings of text of the same language, returning a sequence of responses as they’re available.
- [func translations(from: [TranslationSession.Request]) async throws -> [TranslationSession.Response]](translationsession/translations(from:).md)
  Translates multiple strings of text of the same language, returning the results all at once when complete.
- [TranslationSession.Request](translationsession/request.md)
  A translation request containing a single item of text to translate.
- [TranslationSession.Response](translationsession/response.md)
  The response to a translation request.
- [TranslationSession.BatchResponse](translationsession/batchresponse.md)
  A type that provides asynchronous access to translation responses.
### Preparing for translation
- [TranslationSession.Configuration](translationsession/configuration.md)
  A type containing the information to use when performing a translation.
- [func prepareTranslation() async throws](translationsession/preparetranslation.md)
  Asks the user for permission to download translation languages without doing any translations.
### Getting configuration
- [let sourceLanguage: Locale.Language?](translationsession/sourcelanguage.md)
  The input language to translate from.
- [let targetLanguage: Locale.Language?](translationsession/targetlanguage.md)
  The output language to translate into.
### Initializers
- [convenience init(installedSource: Locale.Language, target: Locale.Language?)](translationsession/init(installedsource:target:).md)
  Create a `TranslationSession` to translate between a given source and target language already installed on the device.
### Instance Properties
- [var canRequestDownloads: Bool](translationsession/canrequestdownloads.md)
  Whether this session is able to present UI to request downloading languages if they’re not already installed.
- [var isReady: Bool](translationsession/isready.md)
  Whether the source and target languages of this session are installed and ready for translation.
### Instance Methods
- [func cancel()](translationsession/cancel.md)
  Attempt to stop all ongoing work for this session. Future requests will throw an error that the session is cancelled already.

## See Also

- [Translating text within your app](translating-text-within-your-app.md)
  Display simple system translations and create custom translation experiences.
- [nonisolated func translationPresentation(isPresented: Binding<Bool>, text: String, attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds), arrowEdge: Edge = .top, replacementAction: ((String) -> Void)? = nil) -> some View
](../SwiftUI/View/translationPresentation(isPresented:text:attachmentAnchor:arrowEdge:replacementAction:).md)
  Presents a translation popover when a given condition is true.
- [nonisolated func translationTask(_ configuration: TranslationSession.Configuration?, action: @escaping (TranslationSession) async -> Void) -> some View
](../SwiftUI/View/translationTask(_:action:).md)
  Adds a task to perform before this view appears or when the translation configuration changes.
- [nonisolated func translationTask(source: Locale.Language? = nil, target: Locale.Language? = nil, action: @escaping (TranslationSession) async -> Void) -> some View
](../SwiftUI/View/translationTask(source:target:action:).md)
  Adds a task to perform before this view appears or when the specified source or target languages change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession)*