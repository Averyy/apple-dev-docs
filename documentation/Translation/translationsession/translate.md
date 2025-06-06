# translate(_:)

**Framework**: Translation  
**Kind**: method

Translates a single string of text.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+

## Declaration

```swift
func translate(_ string: String) async throws -> TranslationSession.Response
```

#### Return Value

The response containing the text translation.

#### Discussion

This function translates a single line of text and might display different UI depending on the state of the translation. The languages the framework requires for the translation don’t have to be installed before calling this method.

If the required languages for translation have already downloaded and the source language is clear, this function returns results without showing any UI to the user.

If the source or target language aren’t installed, the framework asks the user for permission to download the languages. During download a progress indicator displays. After the download completes, the framework performs the translation.

If the `sourceLanguage` is `nil` and the framework can’t detect the source language from the content, the framework prompts the user to choose the source language.

This function throws an `Error` if:

- the user doesn’t agree to downloading the languages
- the user dismisses the progress UI while the languages download,
- the [`TranslationSession`](translationsession.md) fails to validate, or
- something goes wrong while performing the translation.

If someone dismisses the progress UI while the languages download, the system throws a `CocoaError/userCancelled` error, and the languages continue to download in the background.

> **Note**: Calls to this function can take several minutes while languages download.

## Parameters

- `string`: The string of text to translate.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/translate(_:))*