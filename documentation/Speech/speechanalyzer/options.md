# SpeechAnalyzer.Options

**Framework**: Speech  
**Kind**: struct  
**Role**: Structure

Analysis processing options.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Options
```

## Topics

### Creating an options object
- [init(priority: TaskPriority, modelRetention: SpeechAnalyzer.Options.ModelRetention)](./options/init%28priority,modelretention%29.md)
  Creates a structure containing analysis processing options.
- [init(priority: TaskPriority, modelRetention: SpeechAnalyzer.Options.ModelRetention, ignoresResourceLimits: Bool)](./options/init%28priority,modelretention,ignoresresourcelimits%29.md)
  Creates a structure containing analysis processing options.
- [SpeechAnalyzer.Options.ModelRetention](./options/modelretention-swift.enum.md)
  A model caching strategy.
### Inspecting options
- [let ignoresResourceLimits: Bool](./options/ignoresresourcelimits.md)
  A Boolean value that indicates whether this analyzer ignores predefined system resource limits.
- [let modelRetention: SpeechAnalyzer.Options.ModelRetention](./options/modelretention-swift.property.md)
  The analyzer’s model caching strategy.
- [let priority: TaskPriority](./options/priority.md)
  The priority of analysis processing work.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating an analyzer
- [convenience init(modules: [any SpeechModule], options: SpeechAnalyzer.Options?)](./init%28modules,options%29.md)
  Creates an analyzer.
- [convenience init<InputSequence>(inputSequence: InputSequence, modules: [any SpeechModule], options: SpeechAnalyzer.Options?, analysisContext: AnalysisContext, volatileRangeChangedHandler: sending ((CMTimeRange, Bool, Bool) -> Void)?)](./init%28inputsequence,modules,options,analysiscontext,volatilerangechangedhandler%29.md)
  Creates an analyzer and begins analysis.
- [convenience init(inputAudioFile: AVAudioFile, modules: [any SpeechModule], options: SpeechAnalyzer.Options?, analysisContext: AnalysisContext, finishAfterFile: Bool, volatileRangeChangedHandler: sending ((CMTimeRange, Bool, Bool) -> Void)?) async throws](./init%28inputaudiofile,modules,options,analysiscontext,finishafterfile,volatilerangechangedhandler%29.md)
  Creates an analyzer and begins analysis on an audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/options)*