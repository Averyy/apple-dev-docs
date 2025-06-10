# init(inputAudioFile:modules:options:analysisContext:finishAfterFile:volatileRangeChangedHandler:)

**Framework**: Speech  
**Kind**: init

Creates an analyzer and begins analysis on an audio file.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
convenience init(inputAudioFile: AVAudioFile, modules: [any SpeechModule], options: SpeechAnalyzer.Options? = nil, analysisContext: AnalysisContext = .init(), finishAfterFile: Bool = false, volatileRangeChangedHandler: sending ((CMTimeRange, Bool, Bool) -> Void)? = nil) async throws
```

## Parameters

- `inputAudioFile`: An audio file opened for reading.
- `modules`: An initial list of modules that will analyze the audio.
- `options`: A structure specifying analysis options.
- `analysisContext`: An object containing contextual information to improve or inform the analysis.
- `finishAfterFile`: If  , the analysis will automatically finish after the audio file has been fully processed. Equivalent to calling  .
- `volatileRangeChangedHandler`: A closure called to report the analysis’ progress. The closure takes the following parameters:

## See Also

- [convenience init(modules: [any SpeechModule], options: SpeechAnalyzer.Options?)](speechanalyzer/init(modules:options:).md)
  Creates an analyzer.
- [convenience init<InputSequence>(inputSequence: InputSequence, modules: [any SpeechModule], options: SpeechAnalyzer.Options?, analysisContext: AnalysisContext, volatileRangeChangedHandler: sending ((CMTimeRange, Bool, Bool) -> Void)?)](speechanalyzer/init(inputsequence:modules:options:analysiscontext:volatilerangechangedhandler:).md)
  Creates an analyzer and begins analysis.
- [SpeechAnalyzer.Options](speechanalyzer/options.md)
  Analysis processing options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/init(inputaudiofile:modules:options:analysiscontext:finishafterfile:volatilerangechangedhandler:))*