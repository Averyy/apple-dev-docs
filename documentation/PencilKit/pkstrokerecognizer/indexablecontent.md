# indexableContent

**Framework**: PencilKit  
**Kind**: property

A string suitable for indexing the drawing’s recognized text in search systems such as Spotlight.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var indexableContent: String? { get async }
```

## Mentions

- [Recognizing handwriting and converting it to text](recognizing-handwriting-and-converting-to-text.md)

#### Discussion

The string may contain multiple concatenated candidate matches for recognized text in the drawing.

## See Also

- [func recognizedText(strokeIDs: Set<UUID>?) async -> String?](pkstrokerecognizer/recognizedtext(strokeids:).md)
  Returns the recognized text from the specified strokes in the drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokerecognizer/indexablecontent)*