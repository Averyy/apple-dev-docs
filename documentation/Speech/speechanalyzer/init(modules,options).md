# init(modules:options:)

**Framework**: Speech  
**Kind**: init  
**Role**: Initializer

Creates an analyzer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
convenience init(modules: [any SpeechModule], options: SpeechAnalyzer.Options? = nil)
```

## Parameters

- `modules`: An initial list of modules to add to the analyzer. The list can be empty; modules can be added or removed later.
- `options`: A structure specifying analysis options.

## See Also

### Creating an analyzer
- [convenience init<InputSequence>(inputSequence: InputSequence, modules: [any SpeechModule], options: SpeechAnalyzer.Options?, analysisContext: AnalysisContext, volatileRangeChangedHandler: sending ((CMTimeRange, Bool, Bool) -> Void)?)](./init%28inputsequence,modules,options,analysiscontext,volatilerangechangedhandler%29.md)
  Creates an analyzer and begins analysis.
- [convenience init(inputAudioFile: AVAudioFile, modules: [any SpeechModule], options: SpeechAnalyzer.Options?, analysisContext: AnalysisContext, finishAfterFile: Bool, volatileRangeChangedHandler: sending ((CMTimeRange, Bool, Bool) -> Void)?) async throws](./init%28inputaudiofile,modules,options,analysiscontext,finishafterfile,volatilerangechangedhandler%29.md)
  Creates an analyzer and begins analysis on an audio file.
- [SpeechAnalyzer.Options](./options.md)
  Analysis processing options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/init(modules:options:))*