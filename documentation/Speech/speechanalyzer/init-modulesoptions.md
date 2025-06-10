# init(modules:options:)

**Framework**: Speech  
**Kind**: init

Creates an analyzer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
convenience init(modules: [any SpeechModule], options: SpeechAnalyzer.Options? = nil)
```

## Parameters

- `modules`: An initial list of modules to add to the analyzer. The list can be empty; modules can be added or removed later.
- `options`: A structure specifying analysis options.

## See Also

- [convenience init<InputSequence>(inputSequence: InputSequence, modules: [any SpeechModule], options: SpeechAnalyzer.Options?, analysisContext: AnalysisContext, volatileRangeChangedHandler: sending ((CMTimeRange, Bool, Bool) -> Void)?)](speechanalyzer/init(inputsequence:modules:options:analysiscontext:volatilerangechangedhandler:).md)
  Creates an analyzer and begins analysis.
- [convenience init(inputAudioFile: AVAudioFile, modules: [any SpeechModule], options: SpeechAnalyzer.Options?, analysisContext: AnalysisContext, finishAfterFile: Bool, volatileRangeChangedHandler: sending ((CMTimeRange, Bool, Bool) -> Void)?) async throws](speechanalyzer/init(inputaudiofile:modules:options:analysiscontext:finishafterfile:volatilerangechangedhandler:).md)
  Creates an analyzer and begins analysis on an audio file.
- [SpeechAnalyzer.Options](speechanalyzer/options.md)
  Analysis processing options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/init(modules:options:))*