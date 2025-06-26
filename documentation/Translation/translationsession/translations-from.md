# translations(from:)

**Framework**: Translation  
**Kind**: method

Translates multiple strings of text of the same language, returning the results all at once when complete.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+ (Beta)
- macOS 15.0+

## Declaration

```swift
func translations(from batch: [TranslationSession.Request]) async throws -> [TranslationSession.Response]
```

#### Return Value

An array of responses containing the text translations matching the order they were sent.

#### Discussion

This function translates multiple strings as a batch and might display different UI depending on the state of the translation. The languages the framework requires for the translation don’t have to be installed before calling this method.

Pass in the strings of text you want to translate as an array of the [`TranslationSession.Request`](translationsession/request.md) type. This method takes longer to return than [`translate(batch:)`](translationsession/translate(batch:).md), but it has the advantage of not having to map translation requests to responses. The responses return in the same order the requests are sent.

If the required languages for translation have already downloaded and the source language is clear, this function returns results without showing any further prompts to the person.

If the source or target language aren’t installed, the framework asks the person for permission to download the languages. During download a progress indicator displays. After the download completes, the framework performs the translation.

If the `sourceLanguage` is `nil` and the framework can’t detect the source language from the content, the framework prompts the person to choose the source language.

The framework only supports string translations of the same language. The strings must either match the `sourceLanguage` you set in the configuration, or if the `sourceLanguage` is `nil`, be of the same language.

This function throws an `Error` if:

- The person doesn’t agree to downloading the languages
- The person dismisses the progress view during language downloads
- [`TranslationSession`](translationsession.md)  fails system validation
- The session doesn’t allow requesting downloads and languages aren’t installed
- You already cancelled the session
- Something goes wrong during translation

If a person dismisses the progress view while the languages download, the system throws a [`userCancelled`](https://developer.apple.com/documentation/Foundation/CocoaError/Code/userCancelled) error, and the languages continue to download in the background.

> **Note**: Calls to this function can take several minutes while languages download.

## Parameters

- `batch`: The array of requests to translate.

## See Also

- [func translate(String) async throws -> TranslationSession.Response](translationsession/translate(_:).md)
  Translates a single string of text.
- [func translate(batch: [TranslationSession.Request]) -> TranslationSession.BatchResponse](translationsession/translate(batch:).md)
  Translates multiple strings of text of the same language, returning a sequence of responses as they’re available.
- [TranslationSession.Request](translationsession/request.md)
  A translation request containing a single item of text to translate.
- [TranslationSession.Response](translationsession/response.md)
  The response to a translation request.
- [TranslationSession.BatchResponse](translationsession/batchresponse.md)
  A type that provides asynchronous access to translation responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/translations(from:))*