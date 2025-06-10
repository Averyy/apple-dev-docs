# init(inputSequence:modules:options:analysisContext:volatileRangeChangedHandler:)

**Framework**: Speech  
**Kind**: init

Creates an analyzer and begins analysis.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
convenience init<InputSequence>(inputSequence: InputSequence, modules: [any SpeechModule], options: SpeechAnalyzer.Options? = nil, analysisContext: AnalysisContext = .init(), volatileRangeChangedHandler: sending ((CMTimeRange, Bool, Bool) -> Void)? = nil) where InputSequence : Sendable, InputSequence : AsyncSequence, InputSequence.Element == AnalyzerInput
```

## Parameters

- `inputSequence`: An asynchronous sequence of audio inputs to analyze. Analysis will begin when the first audio input is added to the sequence.
- `modules`: An initial list of modules that will analyze the audio.
- `options`: A structure specifying analysis options.
- `analysisContext`: An object containing contextual information to improve or inform the analysis.
- `volatileRangeChangedHandler`: A closure called to report the analysis’ progress. The closure takes the following parameters:

## See Also

- [convenience init(modules: [any SpeechModule], options: SpeechAnalyzer.Options?)](speechanalyzer/init(modules:options:).md)
  Creates an analyzer.
- [convenience init(inputAudioFile: AVAudioFile, modules: [any SpeechModule], options: SpeechAnalyzer.Options?, analysisContext: AnalysisContext, finishAfterFile: Bool, volatileRangeChangedHandler: sending ((CMTimeRange, Bool, Bool) -> Void)?) async throws](speechanalyzer/init(inputaudiofile:modules:options:analysiscontext:finishafterfile:volatilerangechangedhandler:).md)
  Creates an analyzer and begins analysis on an audio file.
- [SpeechAnalyzer.Options](speechanalyzer/options.md)
  Analysis processing options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/init(inputsequence:modules:options:analysiscontext:volatilerangechangedhandler:))*