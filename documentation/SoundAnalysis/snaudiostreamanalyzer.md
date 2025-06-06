# SNAudioStreamAnalyzer

**Framework**: Sound Analysis  
**Kind**: class

An object you create to analyze a stream of audio data and provide the results to your app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class SNAudioStreamAnalyzer
```

## Mentions

- [Classifying Sounds in an Audio Stream](classifying-sounds-in-an-audio-stream.md)

#### Overview

Run an [`SNRequest`](snrequest.md) on an audio stream by creating an `SNAudioStreamAnalyzer`. You can run the same sound analysis request on multiple stream analyzers, and each analyzer can process multiple requests. An audio file analyzer generates an [`SNResult`](snresult.md) each time any of its active requests recognizes a sound.

## Topics

### Creating an Analyzer
- [init(format: AVAudioFormat)](snaudiostreamanalyzer/init(format:).md)
  Creates a new audio stream analyzer.
### Managing Requests
- [func add(any SNRequest, withObserver: any SNResultsObserving) throws](snaudiostreamanalyzer/add(_:withobserver:).md)
  Adds a new analysis request to the audio stream analyzer.
- [protocol SNRequest](snrequest.md)
  A protocol that represents sound analysis requests.
- [protocol SNResultsObserving](snresultsobserving.md)
  The interface your app implements to receive the results of an analysis request.
- [func remove(any SNRequest)](snaudiostreamanalyzer/remove(_:).md)
  Removes an existing request from the audio stream analyzer.
- [func removeAllRequests()](snaudiostreamanalyzer/removeallrequests.md)
  Removes all the sound analysis requests from the audio stream analyzer.
### Analyzing Data
- [func analyze(AVAudioBuffer, atAudioFramePosition: AVAudioFramePosition)](snaudiostreamanalyzer/analyze(_:ataudioframeposition:).md)
  Adds a new audio buffer to the analyzer’s larger stream buffer.
- [func completeAnalysis()](snaudiostreamanalyzer/completeanalysis.md)
  Notifies the analyzer when it receives the final audio buffer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Classifying Sounds in an Audio File](classifying-sounds-in-an-audio-file.md)
  Identify individual sounds in a file, such as a recording, with an audio file analyzer.
- [class SNAudioFileAnalyzer](snaudiofileanalyzer.md)
  An analyzer that runs sound classification requests on an audio file.
- [Classifying Sounds in an Audio Stream](classifying-sounds-in-an-audio-stream.md)
  Identify individual sounds in an audio data stream, such as from a microphone, with an audio stream analyzer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snaudiostreamanalyzer)*