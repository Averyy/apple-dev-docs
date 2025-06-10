# SpeechAnalyzer

**Framework**: Speech  
**Kind**: class

Analyzes spoken audio content in various ways and manages the analysis session.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final actor SpeechAnalyzer
```

#### Overview

Analysis is asynchronous. Input, output, and session control are decoupled and may (and typically will) occur over several different tasks created by you or by the session.

The analyzer can only analyze one input sequence at a time.

##### Autonomous Analysis

You can and usually should perform analysis using the [`analyzeSequence(_:)`](speechanalyzer/analyzesequence(_:).md) or [`analyzeSequence(from:)`](speechanalyzer/analyzesequence(from:).md) methods; those methods work well with Swift structured concurrency techniques.

However, you may prefer that the analyzer proceed independently of those methods and perform its analysis autonomously as audio input becomes available in a task managed by the analyzer itself.

To use this capability, create the analyzer with one of the initializers that has an input sequence or file parameter, or call [`start(inputSequence:)`](speechanalyzer/start(inputsequence:).md) or [`start(inputAudioFile:finishAfterFile:)`](speechanalyzer/start(inputaudiofile:finishafterfile:).md). To end the analysis when the input ends, call [`finalizeAndFinishThroughEndOfInput()`](speechanalyzer/finalizeandfinishthroughendofinput().md). To end the analysis of that input and start analysis of different input, call one of the `start` methods.

##### Analyzer States

Several methods cause the analysis session to . When an analysis session is finished, the analyzer will not take any additional input from the input sequence and will not accept a different input sequence or accept module changes. Most methods will do nothing. Modules’ results streams terminate; a module will not publish additional results to its result stream, but the application can continue to iterate over already-published results.

You may terminate the input sequence with a method such as `AsyncStream.Continuation.finish()`. This “finish” does not cause the analysis session to become finished, as you may continue the session with a different input sequence. Therefore, do not expect the analysis to end when the input sequence does. You can call one of this class’s `finish` methods to achieve that expectation.

##### Responding to Errors

When the analyzer or its modules’ result streams throw an error, the analysis session becomes  as described above and the same error (or a `CancellationError`) is thrown from all waiting methods and result streams.

## Topics

### Creating an analyzer
- [convenience init(modules: [any SpeechModule], options: SpeechAnalyzer.Options?)](speechanalyzer/init(modules:options:).md)
  Creates an analyzer.
- [convenience init<InputSequence>(inputSequence: InputSequence, modules: [any SpeechModule], options: SpeechAnalyzer.Options?, analysisContext: AnalysisContext, volatileRangeChangedHandler: sending ((CMTimeRange, Bool, Bool) -> Void)?)](speechanalyzer/init(inputsequence:modules:options:analysiscontext:volatilerangechangedhandler:).md)
  Creates an analyzer and begins analysis.
- [convenience init(inputAudioFile: AVAudioFile, modules: [any SpeechModule], options: SpeechAnalyzer.Options?, analysisContext: AnalysisContext, finishAfterFile: Bool, volatileRangeChangedHandler: sending ((CMTimeRange, Bool, Bool) -> Void)?) async throws](speechanalyzer/init(inputaudiofile:modules:options:analysiscontext:finishafterfile:volatilerangechangedhandler:).md)
  Creates an analyzer and begins analysis on an audio file.
- [SpeechAnalyzer.Options](speechanalyzer/options.md)
  Analysis processing options.
### Managing modules
- [func setModules([any SpeechModule]) async throws](speechanalyzer/setmodules(_:).md)
  Adds or removes modules.
- [var modules: [any SpeechModule]](speechanalyzer/modules.md)
  The modules performing analysis on the audio input.
### Performing analysis
- [func analyzeSequence<InputSequence>(InputSequence) async throws -> CMTime?](speechanalyzer/analyzesequence(_:).md)
  Analyzes an input sequence, returning when the sequence is consumed.
- [func analyzeSequence(from: AVAudioFile) async throws -> CMTime?](speechanalyzer/analyzesequence(from:).md)
  Analyzes an input sequence created from an audio file, returning when the file has been read.
### Performing autonomous analysis
- [func start<InputSequence>(inputSequence: InputSequence) async throws](speechanalyzer/start(inputsequence:).md)
  Starts analysis of an input sequence and returns immediately.
- [func start(inputAudioFile: AVAudioFile, finishAfterFile: Bool) async throws](speechanalyzer/start(inputaudiofile:finishafterfile:).md)
  Starts analysis of an input sequence created from an audio file and returns immediately.
### Finalizing and cancelling results
- [func cancelAnalysis(before: CMTime)](speechanalyzer/cancelanalysis(before:).md)
  Stops analyzing audio predating the given time.
- [func finalize(through: CMTime?) async throws](speechanalyzer/finalize(through:).md)
  Finalizes the modules’ analyses.
### Finishing analysis
- [func cancelAndFinishNow() async](speechanalyzer/cancelandfinishnow.md)
  Finishes analysis immediately.
- [func finalizeAndFinishThroughEndOfInput() async throws](speechanalyzer/finalizeandfinishthroughendofinput.md)
  Finishes analysis after an audio input sequence has been fully consumed and its results are finalized.
- [func finalizeAndFinish(through: CMTime) async throws](speechanalyzer/finalizeandfinish(through:).md)
  Finishes analysis after finalizing results for a given time-code.
- [func finish(after: CMTime) async throws](speechanalyzer/finish(after:).md)
  Finishes analysis once input for a given time is consumed.
### Determining audio formats
- [static func bestAvailableAudioFormat(compatibleWith: [any SpeechModule]) async -> AVAudioFormat?](speechanalyzer/bestavailableaudioformat(compatiblewith:).md)
  Retrieves the best-quality audio format that the specified modules can work with, from assets installed on the device.
- [static func bestAvailableAudioFormat(compatibleWith: [any SpeechModule], considering: AVAudioFormat?) async -> AVAudioFormat?](speechanalyzer/bestavailableaudioformat(compatiblewith:considering:).md)
  Retrieves the best-quality audio format that the specified modules can work with, taking into account the natural format of the audio and assets installed on the device.
### Improving responsiveness
- [func prepareToAnalyze(in: AVAudioFormat?) async throws](speechanalyzer/preparetoanalyze(in:).md)
  Prepares the analyzer to begin work with minimal startup delay.
- [func prepareToAnalyze(in: AVAudioFormat?, withProgressReadyHandler: sending ((Progress) -> Void)?) async throws](speechanalyzer/preparetoanalyze(in:withprogressreadyhandler:).md)
  Prepares the analyzer to begin work with minimal startup delay, reporting the progress of that preparation.
### Monitoring analysis
- [func setVolatileRangeChangedHandler(sending ((CMTimeRange, Bool, Bool) -> Void)?)](speechanalyzer/setvolatilerangechangedhandler(_:).md)
  A closure that the analyzer calls when the volatile range changes.
- [var volatileRange: CMTimeRange?](speechanalyzer/volatilerange.md)
  The range of results that can change.
### Managing contexts
- [func setContext(AnalysisContext) async throws](speechanalyzer/setcontext(_:).md)
  Sets contextual information to improve or inform the analysis.
- [var context: AnalysisContext](speechanalyzer/context.md)
  An object containing contextual information.

## Relationships

### Conforms To
- [Actor](../Swift/Actor.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Bringing advanced speech-to-text capabilities to your app](bringing-advanced-speech-to-text-capabilities-to-your-app.md)
  Learn how to incorporate live speech-to-text transcription into your app with SpeechAnalyzer.
- [class AssetInventory](assetinventory.md)
  Before using `SpeechAnalyzer`, you must install the assets required by the modules you use. These assets are machine-learning models downloaded from Apple’s servers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer)*