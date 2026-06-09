# recognizedText(strokeIDs:)

**Framework**: PencilKit  
**Kind**: method

Returns the recognized text from the specified strokes in the drawing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func recognizedText(strokeIDs: Set<UUID>? = nil) async -> String?
```

## Mentions

- [Recognizing handwriting and converting it to text](recognizing-handwriting-and-converting-to-text.md)

## Parameters

- `strokeIDs`: The `id`s of the `PKStrokes` in `drawing` to analyze. Pass `nil` to return the recognized text from the whole drawing.

## See Also

- [var indexableContent: String?](pkstrokerecognizer/indexablecontent.md)
  A string suitable for indexing the drawing’s recognized text in search systems such as Spotlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokerecognizer/recognizedtext(strokeids:))*