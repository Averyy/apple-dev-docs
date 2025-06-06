# TranslationSession.Configuration

**Framework**: Translation  
**Kind**: struct

A type containing the information to use when performing a translation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+

## Declaration

```swift
struct Configuration
```

#### Overview

Specify the source and target languages to use in a translation session with this object. Create an instance of this type using the [`init(source:target:)`](translationsession/configuration/init(source:target:).md) initializer passing in the `source` and `target` languages to use for the translation.

When you pass this configuration into the `View/translationTask(_:action:)` function, the framework uses the languages you specify for the translation.

To re-run a translation, store the configuration object as state in your SwiftUI view by using the `State` property wrapper. Then change one of the configuration properties (such as the source or target language) to re-run the translation on a new pair of languages. Or call [`invalidate()`](translationsession/configuration/invalidate().md) on the configuration instance to re-run the translation using the same languages but with new content to translate. When you do, the action closure of `View/translationTask(_:action:)` triggers and the framework translates the text.

The following example demonstrates how to trigger a new translation from a button press:

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

### Operators
- [static func == (TranslationSession.Configuration, TranslationSession.Configuration) -> Bool](translationsession/configuration/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(source: Locale.Language?, target: Locale.Language?)](translationsession/configuration/init(source:target:).md)
  Creates a configuration from a source and target language.
### Instance Properties
- [var source: Locale.Language?](translationsession/configuration/source.md)
  The language to translate content from.
- [var target: Locale.Language?](translationsession/configuration/target.md)
  The language to translate content into.
- [var version: Int](translationsession/configuration/version.md)
  A value the equals function uses to represent change in the configuration instance.
### Instance Methods
- [func invalidate()](translationsession/configuration/invalidate.md)
  Invalidate the current translation session to re-run it again with new content.
### Default Implementations
- [Equatable Implementations](translationsession/configuration/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [func prepareTranslation() async throws](translationsession/preparetranslation.md)
  Asks the user for permission to download translation languages without doing any translations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/configuration)*