# PKStrokeRecognizer.SearchResult

**Framework**: PencilKit  
**Kind**: struct

A value that describes a single result returned by a handwriting search.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct SearchResult
```

## Mentions

- [Recognizing handwriting and converting it to text](recognizing-handwriting-and-converting-to-text.md)

#### Overview

Each `SearchResult` identifies the set of strokes that matched the query and the bounding rectangle that contains them, expressed in the coordinate space of the drawing.

## Topics

### Getting the result data
- [let strokes: Set<UUID>](pkstrokerecognizer/searchresult/strokes.md)
  The identifiers of the strokes the result contains.
- [let bounds: CGRect](pkstrokerecognizer/searchresult/bounds.md)
  The bounds of the matched strokes in the coordinate space of their drawing.

## See Also

- [func search(String, fullWordsOnly: Bool, caseMatchingOnly: Bool) async -> [PKStrokeRecognizer.SearchResult]](pkstrokerecognizer/search(_:fullwordsonly:casematchingonly:).md)
  Searches the drawing for strokes whose recognized text matches the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokerecognizer/searchresult)*