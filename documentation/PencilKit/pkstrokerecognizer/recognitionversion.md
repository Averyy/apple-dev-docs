# recognitionVersion

**Framework**: PencilKit  
**Kind**: property

The version number of the recognition engine.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static var recognitionVersion: Int { get }
```

## Mentions

- [Recognizing handwriting and converting it to text](recognizing-handwriting-and-converting-to-text.md)

#### Discussion

If you persist results this recognizer returns, store this value alongside them and regenerate the results when running on an OS with a higher version number.

## See Also

- [static var supportedLanguages: Set<Locale.Language>](pkstrokerecognizer/supportedlanguages.md)
  The languages the recognizer supports.
- [var languages: [Locale.Language]](pkstrokerecognizer/languages.md)
  The languages the recognizer uses, ordered by descending priority.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokerecognizer/recognitionversion)*