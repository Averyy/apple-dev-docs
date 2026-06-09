# flush()

**Framework**: Speech  
**Kind**: method

Completes pending audio conversions.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func flush() throws -> [AnalyzerInput]
```

#### Return Value

An array of `AnalyzerInput` objects containing completed pending audio conversions.

## See Also

- [func convert(AVAudioBuffer, at: AVAudioTime?) throws -> [AnalyzerInput]](analyzerinputconverter/convert(_:at:).md)
  Converts an audio buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/analyzerinputconverter/flush())*