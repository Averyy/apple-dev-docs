# PKStrokeRecognizer

**Framework**: PencilKit  
**Kind**: class

An actor that recognizes handwriting and searches for text within a PencilKit drawing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final actor PKStrokeRecognizer
```

## Mentions

- [Recognizing handwriting and converting it to text](recognizing-handwriting-and-converting-to-text.md)

#### Overview

Use `PKStrokeRecognizer` to extract recognized text from individual strokes, generate content suitable for indexing in search systems such as Spotlight, and search for specific words or phrases within handwritten content. The recognizer uses an on-device recognition engine and all operations are asynchronous.

Recognition works best when handwriting is scaled as if drawn on standard US Letter or A4 paper in points. Before creating a recognizer, check [`supportedLanguages`](pkstrokerecognizer/supportedlanguages.md) to confirm your target language is available. If you persist results from a recognizer, store the current [`recognitionVersion`](pkstrokerecognizer/recognitionversion.md) alongside the results and regenerate them when the version advances.

## Topics

### Creating a recognizer
- [init(preferredLanguages: [Locale.Language]?)](pkstrokerecognizer/init(preferredlanguages:).md)
  Creates a recognizer with the specified preferred languages.
### Providing drawing content
- [var drawing: PKDrawing](pkstrokerecognizer/drawing.md)
  The drawing the recognizer analyzes.
- [func updateDrawing(PKDrawing) async](pkstrokerecognizer/updatedrawing(_:).md)
  Updates the drawing the recognizer analyzes.
### Recognizing handwriting
- [func recognizedText(strokeIDs: Set<UUID>?) async -> String?](pkstrokerecognizer/recognizedtext(strokeids:).md)
  Returns the recognized text from the specified strokes in the drawing.
- [var indexableContent: String?](pkstrokerecognizer/indexablecontent.md)
  A string suitable for indexing the drawing’s recognized text in search systems such as Spotlight.
### Searching for text
- [func search(String, fullWordsOnly: Bool, caseMatchingOnly: Bool) async -> [PKStrokeRecognizer.SearchResult]](pkstrokerecognizer/search(_:fullwordsonly:casematchingonly:).md)
  Searches the drawing for strokes whose recognized text matches the query.
- [PKStrokeRecognizer.SearchResult](pkstrokerecognizer/searchresult.md)
  A value that describes a single result returned by a handwriting search.
### Checking language support
- [static var supportedLanguages: Set<Locale.Language>](pkstrokerecognizer/supportedlanguages.md)
  The languages the recognizer supports.
- [var languages: [Locale.Language]](pkstrokerecognizer/languages.md)
  The languages the recognizer uses, ordered by descending priority.
- [static var recognitionVersion: Int](pkstrokerecognizer/recognitionversion.md)
  The version number of the recognition engine.

## Relationships

### Conforms To
- [Actor](../swift/actor.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Building a handwriting recognition experience with PencilKit](building-a-handwriting-recognition-experience-with-pencilkit.md)
  Integrate handwriting recognition into your app to identify written text across multiple languages, and explore path conversion and substrokes to enhance the drawing experience.
- [Recognizing handwriting and converting it to text](recognizing-handwriting-and-converting-to-text.md)
  Analyze handwritten strokes in a PencilKit canvas using on-device recognition, and convert them to text that your app can display, copy, or index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokerecognizer)*