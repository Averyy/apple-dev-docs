# convert(_:at:)

**Framework**: Speech  
**Kind**: method

Converts an audio buffer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func convert(_ buffer: AVAudioBuffer, at audioTime: AVAudioTime?) throws -> [AnalyzerInput]
```

#### Return Value

An array of `AnalyzerInput` objects containing converted audio corresponding to some or all of the audio buffer.

#### Discussion

This method does not necessarily convert the entire audio buffer. Some audio data may be held over and integrated into the conversion of a later audio buffer for correctness or efficiency.

Call [`flush()`](analyzerinputconverter/flush().md) to convert any remaining held-over audio and add it to the analyzer’s input sequence before finishing the sequence.

## Parameters

- `buffer`: An audio buffer to convert. Do not reuse or modify this buffer; it may be retained across calls.
- `audioTime`: The time-code of the start of the audio buffer. If `nil`, the audio buffer is assumed to start immediately after the previous buffer (or at time-code zero if there is no previous buffer).

## See Also

- [func flush() throws -> [AnalyzerInput]](analyzerinputconverter/flush.md)
  Completes pending audio conversions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/analyzerinputconverter/convert(_:at:))*