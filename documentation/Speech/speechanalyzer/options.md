# SpeechAnalyzer.Options

**Framework**: Speech  
**Kind**: struct

Analysis processing options.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct Options
```

## Topics

### Initializers
- [init(priority: TaskPriority, modelRetention: SpeechAnalyzer.Options.ModelRetention)](speechanalyzer/options/init(priority:modelretention:).md)
  Creates a structure containing analysis processing options.
### Instance Properties
- [let modelRetention: SpeechAnalyzer.Options.ModelRetention](speechanalyzer/options/modelretention-swift.property.md)
  The analyzer’s model caching strategy.
- [let priority: TaskPriority](speechanalyzer/options/priority.md)
  The priority of analysis processing work.
### Enumerations
- [SpeechAnalyzer.Options.ModelRetention](speechanalyzer/options/modelretention-swift.enum.md)
  A model caching strategy.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [convenience init(modules: [any SpeechModule], options: SpeechAnalyzer.Options?)](speechanalyzer/init(modules:options:).md)
  Creates an analyzer.
- [convenience init<InputSequence>(inputSequence: InputSequence, modules: [any SpeechModule], options: SpeechAnalyzer.Options?, analysisContext: AnalysisContext, volatileRangeChangedHandler: sending ((CMTimeRange, Bool, Bool) -> Void)?)](speechanalyzer/init(inputsequence:modules:options:analysiscontext:volatilerangechangedhandler:).md)
  Creates an analyzer and begins analysis.
- [convenience init(inputAudioFile: AVAudioFile, modules: [any SpeechModule], options: SpeechAnalyzer.Options?, analysisContext: AnalysisContext, finishAfterFile: Bool, volatileRangeChangedHandler: sending ((CMTimeRange, Bool, Bool) -> Void)?) async throws](speechanalyzer/init(inputaudiofile:modules:options:analysiscontext:finishafterfile:volatilerangechangedhandler:).md)
  Creates an analyzer and begins analysis on an audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/options)*