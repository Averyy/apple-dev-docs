# TranslationSession.Configuration

**Framework**: Translation  
**Kind**: struct  
**Role**: Structure

A type containing the information to use when performing a translation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+
- macOS 15.0+

## Declaration

```swift
struct Configuration
```

## Overview

Specify the source and target languages to use in a translation session with this object. Initialize an instance of this type using the [`init(source:target:)`](./configuration/init%28source,target%29.md) and passing in the `source` and `target` languages. When you pass this configuration into the [`translationTask(_:action:)`](../../SwiftUI/view/translationtask%28_,action%29.md)  function, the framework uses the languages you specify for translation.

To re-run a translation, store the configuration object as state in your SwiftUI view by using the `State` property wrapper. Then change one of the configuration properties (such as the source or target language) to re-run the translation on a new pair of languages. You can also call [`invalidate()`](./configuration/invalidate%28%29.md) on the configuration instance to re-run the translation using the same languages with new content to translate. When you do, the action closure of [`translationTask(_:action:)`](../../SwiftUI/view/translationtask%28_,action%29.md) runs and the framework translates the text.

The following example demonstrates how to initiate a new translation from a button press:

```swift
struct TranslationExample: View {
    var sourceText: String
    var sourceLanguage: Locale.Language?
    var targetLanguage: Locale.Language?

    @State private var targetText: String?
    @State private var configuration: TranslationSession.Configuration?

    var body: some View {
        VStack {
            Text(targetText ?? sourceText)
            Button("Translate") {
                guard configuration != nil else {
                    configuration = TranslationSession.Configuration(
                        source: sourceLanguage,
                        target: targetLanguage)
                    return
                }
                self.configuration.invalidate()
            }
        }
        .translationTask(configuration) { session in
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

## Topics

### Creating a configuration
- [init(source: Locale.Language?, target: Locale.Language?)](./configuration/init%28source,target%29.md)
  Creates a configuration from a source and target language.
- [init(source: Locale.Language?, target: Locale.Language?, preferredStrategy: TranslationSession.Strategy)](./configuration/init%28source,target,preferredstrategy%29.md)
  Creates a configuration from a source and target language.
### Specifying translation languages
- [var source: Locale.Language?](./configuration/source.md)
  The language to translate content from.
- [var target: Locale.Language?](./configuration/target.md)
  The language to translate content into.
### Configuring translation behavior
- [var preferredStrategy: TranslationSession.Strategy](./configuration/preferredstrategy.md)
  The translation approach for this configuration.
### Updating the translation
- [func invalidate()](./configuration/invalidate%28%29.md)
  Invalidate the current translation session and re-run it with new content.
### Comparing configurations
- [var version: Int](./configuration/version.md)
  A value the equals function uses to represent change in the configuration instance.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)

## See Also

### Preparing for translation
- [func prepareTranslation() async throws](./preparetranslation%28%29.md)
  Asks for permission to download translation languages without doing any translations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/configuration)*