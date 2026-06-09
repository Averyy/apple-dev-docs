# Recognizing handwriting and converting it to text

**Framework**: PencilKit

Analyze handwritten strokes in a PencilKit canvas using on-device recognition, and convert them to text that your app can display, copy, or index.

#### Overview

[`PKStrokeRecognizer`](pkstrokerecognizer.md) uses an on-device engine to recognize handwriting directly from a [`PKDrawing`](pkdrawing-swift.struct.md), so recognition works offline and no handwriting data leaves the device. With this API, you can build features like copy-as-text, where people select handwritten strokes and paste them as typed text, search for a word or phrase across an entire drawing, and index handwritten notes so they appear in Spotlight results.

The recognizer works across a range of languages. You configure it with your preferred languages, give it a drawing, and call the method that fits your use case: recognizing specific strokes, searching for a word, or generating indexable content.

> ❗ **Important**: Recognition works best when handwriting is scaled in points, as if drawn on standard US Letter or A4 paper. If your app lets people zoom in and write very large, or write very small, accuracy may decrease.

#### Create and Configure the Recognizer

[`PKStrokeRecognizer`](pkstrokerecognizer.md) is the object that handles all recognition work in your app. It processes the strokes in a drawing and uses an on-device engine to interpret the writing. Create one recognizer per drawing and store it as a property on your view controller or document object so it stays alive as long as the drawing is open.

When you create the recognizer, specify the languages you expect people to write in, ordered by priority. Providing languages improves accuracy because handwriting recognition is language-specific; the recognizer uses the languages you specify to distinguish between characters and words that look similar across scripts. If you pass `nil`, the recognizer uses the device’s preferred languages.

```swift
let recognizer = PKStrokeRecognizer(
    preferredLanguages: [Locale.Language(identifier: "en")]
)
```

Check [`supportedLanguages`](pkstrokerecognizer/supportedlanguages.md) before offering language options to people, because language support may vary by platform:

```swift
let available = PKStrokeRecognizer.supportedLanguages
let supportsJapanese = available.contains(Locale.Language(identifier: "ja"))
```

#### Provide the Drawing

You need to push the drawing to the recognizer explicitly because it doesn’t automatically observe your canvas. This push gives you control over when recognition processing happens, which is useful if you want to defer it until after a person finishes a stroke or pauses writing; this reduces power usage by avoiding unnecessary work.

Call [`updateDrawing(_:)`](pkstrokerecognizer/updatedrawing(_:).md) to give the recognizer a drawing to analyze. All methods are asynchronous, because recognition takes time.

```swift
await recognizer.updateDrawing(canvasView.drawing)
```

Call [`updateDrawing(_:)`](pkstrokerecognizer/updatedrawing(_:).md) before requesting results. The recognizer works from the last drawing you provided, so if the drawing has changed since then, it returns stale results.

#### Convert Strokes to Text

Each stroke in a [`PKDrawing`](pkdrawing-swift.struct.md) has a unique identifier. You can pass a specific set of identifiers to the recognizer to convert only those strokes rather than the entire drawing. This is useful for features like copy-as-text, where you only want to convert the strokes a person has selected. Read [`selection`](pkcanvasview/selection.md) to get the identifiers of the currently selected strokes.

Call [`recognizedText(strokeIDs:)`](pkstrokerecognizer/recognizedtext(strokeids:).md) with a set of stroke IDs to get a text string for those strokes. Pass `nil` to recognize the entire drawing.

```swift
let selectedIDs = canvasView.selection
if let text = await recognizer.recognizedText(strokeIDs: selectedIDs) {
    UIPasteboard.general.string = text
}
```

The method returns the single most likely interpretation of the handwriting. It returns `nil` when it can’t produce a result, for example, when the strokes don’t contain recognizable handwriting.

#### Search for Text Within a Drawing

Searching lets you find where a specific word or phrase appears in a drawing. It returns the matching strokes and their bounds, which you can use to scroll to or highlight results on screen.

Use [`search(_:fullWordsOnly:caseMatchingOnly:)`](pkstrokerecognizer/search(_:fullwordsonly:casematchingonly:).md) to find all occurrences of a word or phrase across the drawing. Each [`PKStrokeRecognizer.SearchResult`](pkstrokerecognizer/searchresult.md) gives you the identifiers of the matching strokes and a bounding rectangle in the drawing’s coordinate space, which is the same coordinate space as [`bounds`](pkdrawing-swift.struct/bounds.md); you can use this space to scroll to or highlight the match on screen.

```swift
let results = await recognizer.search("apple", fullWordsOnly: true)
for result in results {
    highlight(bounds: result.bounds)
}
```

Set `fullWordsOnly` to `true` to match the word exactly, for example, to find “note” without also matching “notebook” or “notepad”. Set `caseMatchingOnly` to `true` for case-sensitive matching.

#### Index Drawing Content for Spotlight

When you index a drawing, people can find their handwritten notes from Spotlight without opening your app. Use the [`indexableContent`](pkstrokerecognizer/indexablecontent.md) property to get a string to pass to the CoreSpotlight indexing API. This string is different from what [`recognizedText(strokeIDs:)`](pkstrokerecognizer/recognizedtext(strokeids:).md) returns; rather than picking one interpretation of the handwriting, it includes multiple possible readings concatenated together. For example, if a word might be read as either “1” or “l”, both appear in the string. These concatenated possibilities improve the chances that a Spotlight search matches the content.

The property returns `nil` when there are no strokes in the drawing to index.

```swift
if let content = await recognizer.indexableContent {
    let attributeSet = CSSearchableItemAttributeSet(contentType: .text)
    attributeSet.textContent = content

    let item = CSSearchableItem(
        uniqueIdentifier: note.id, // A stable identifier for this note in your data model.
        domainIdentifier: "com.example.notes",
        attributeSet: attributeSet
    )
    try? await CSSearchableIndex.default().indexSearchableItems([item])
}
```

#### Persist Recognized Text

Recognition results may change across OS releases. If you store recognized text, save [`recognitionVersion`](pkstrokerecognizer/recognitionversion.md) alongside it and regenerate stored results at a later time.

```swift
struct RecognizedNote: Codable {
    var text: String
    var recognitionVersion: Int
}

func recognizeAndStore(strokeIDs: Set<UUID>) async -> RecognizedNote? {
    guard let text = await recognizer.recognizedText(strokeIDs: strokeIDs) else {
        return nil
    }
    return RecognizedNote(
        text: text,
        recognitionVersion: PKStrokeRecognizer.recognitionVersion
    )
}

func needsRefresh(_ note: RecognizedNote) -> Bool {
    note.recognitionVersion < PKStrokeRecognizer.recognitionVersion
}
```

## See Also

- [Building a handwriting recognition experience with PencilKit](building-a-handwriting-recognition-experience-with-pencilkit.md)
  Integrate handwriting recognition into your app to identify written text across multiple languages, and explore path conversion and substrokes to enhance the drawing experience.
- [actor PKStrokeRecognizer](pkstrokerecognizer.md)
  An actor that recognizes handwriting and searches for text within a PencilKit drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/recognizing-handwriting-and-converting-to-text)*