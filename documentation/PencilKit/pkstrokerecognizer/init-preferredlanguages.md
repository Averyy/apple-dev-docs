# init(preferredLanguages:)

**Framework**: PencilKit  
**Kind**: init

Creates a recognizer with the specified preferred languages.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(preferredLanguages: [Locale.Language]? = nil)
```

#### Discussion

Languages are respected on a best-effort basis. Factors such as feature support may affect which languages the recognizer uses.

## Parameters

- `preferredLanguages`: A list of languages to recognize ordered by descending priority. Pass nil to use the system languages. The system languages may be used if no listed language is available for recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokerecognizer/init(preferredlanguages:))*