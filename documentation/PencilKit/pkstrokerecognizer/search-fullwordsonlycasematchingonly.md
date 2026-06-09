# search(_:fullWordsOnly:caseMatchingOnly:)

**Framework**: PencilKit  
**Kind**: method

Searches the drawing for strokes whose recognized text matches the query.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func search(_ query: String, fullWordsOnly: Bool = false, caseMatchingOnly: Bool = false) async -> [PKStrokeRecognizer.SearchResult]
```

## Mentions

- [Recognizing handwriting and converting it to text](recognizing-handwriting-and-converting-to-text.md)

#### Return Value

An array of all results found.

## Parameters

- `query`: The query string to search for.
- `fullWordsOnly`: Restricts matches to whole words only.
- `caseMatchingOnly`: Restricts matches to exact case.

## See Also

- [PKStrokeRecognizer.SearchResult](pkstrokerecognizer/searchresult.md)
  A value that describes a single result returned by a handwriting search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokerecognizer/search(_:fullwordsonly:casematchingonly:))*