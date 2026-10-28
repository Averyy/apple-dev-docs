# flush()

**Framework**: Speech  
**Kind**: method  
**Role**: Instance Method

Completes pending audio conversions.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func flush() throws -> [AnalyzerInput]
```

## Return Value

An array of `AnalyzerInput` objects containing completed pending audio conversions.

## See Also

### Converting a buffer
- [func convert(AVAudioBuffer, at: AVAudioTime?) throws -> [AnalyzerInput]](./convert%28_,at%29.md)
  Converts an audio buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/analyzerinputconverter/flush())*