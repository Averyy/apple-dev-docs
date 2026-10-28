# SNAudioFileAnalyzer

**Framework**: Sound Analysis  
**Kind**: class  
**Role**: Class

An analyzer that runs sound classification requests on an audio file.

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
class SNAudioFileAnalyzer
```

```objc
@interface SNAudioFileAnalyzer : NSObject
```

## Mentions

- [Classifying Sounds in an Audio File](./classifying-sounds-in-an-audio-file.md)
- [Classifying Sounds in an Audio Stream](./classifying-sounds-in-an-audio-stream.md)

## Overview

Run an [`SNRequest`](./snrequest.md) on an audio file by creating an `SNAudioFileAnalyzer`. You can run the same sound analysis request on multiple file analyzers, and each analyzer can process multiple requests. An audio file analyzer generates an [`SNResult`](./snresult.md) each time any of its active requests recognizes a sound.

## Topics

### Creating an Analyzer
- [init(url: URL) throws](./snaudiofileanalyzer/init%28url%29-336no.md)
  Creates a new audio file analyzer.
### Managing Requests
- [func add(any SNRequest, withObserver: any SNResultsObserving) throws](./snaudiofileanalyzer/add%28_,withobserver%29.md)
  Adds a new analysis request to the audio file analyzer.
- [protocol SNRequest](./snrequest.md)
  A protocol that represents sound analysis requests.
- [protocol SNResultsObserving](./snresultsobserving.md)
  The interface your app implements to receive the results of an analysis request.
- [func remove(any SNRequest)](./snaudiofileanalyzer/remove%28_%29.md)
  Removes an existing request from the audio file analyzer.
- [func removeAllRequests()](./snaudiofileanalyzer/removeallrequests%28%29.md)
  Removes all the sound analysis requests from the audio file analyzer.
### Analyzing Data
- [func analyze()](./snaudiofileanalyzer/analyze%28%29.md)
  Analyzes the audio file synchronously.
- [func analyze(completionHandler: (Bool) -> Void)](./snaudiofileanalyzer/analyze%28completionhandler%29.md)
  Analyzes the audio file asynchronously.
- [func cancelAnalysis()](./snaudiofileanalyzer/cancelanalysis%28%29.md)
  Cancels all the asynchronous sound analysis requests the analyzer is currently processing.
### Initializers
- [init(URL: URL) throws](./snaudiofileanalyzer/init%28url%29-2skhg.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Audio analyzers
- [Classifying Sounds in an Audio File](./classifying-sounds-in-an-audio-file.md)
  Identify individual sounds in a file, such as a recording, with an audio file analyzer.
- [Classifying Sounds in an Audio Stream](./classifying-sounds-in-an-audio-stream.md)
  Identify individual sounds in an audio data stream, such as from a microphone, with an audio stream analyzer.
- [class SNAudioStreamAnalyzer](./snaudiostreamanalyzer.md)
  An object you create to analyze a stream of audio data and provide the results to your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snaudiofileanalyzer)*