# add(_:withObserver:)

**Framework**: Sound Analysis  
**Kind**: method

Adds a new analysis request to the audio stream analyzer.

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
func add(_ request: any SNRequest, withObserver observer: any SNResultsObserving) throws
```

## Mentions

- [Classifying Sounds in an Audio Stream](classifying-sounds-in-an-audio-stream.md)

#### Discussion

You can add requests to an analyzer that’s actively analyzing an audio stream. The analyzer throws an error (Swift) or returns [`NO`](https://developer.apple.com/documentation/ObjectiveC/NO) (Objective-C) if it can’t accept the new request, such as a request with an audio format that doesn’t match the analyzer’s.

## Parameters

- `request`: A sound analysis request.
- `observer`: An   instance that receives the analyzer’s results. The analyzer maintains a weak reference to the observer.

## See Also

- [protocol SNRequest](snrequest.md)
  A protocol that represents sound analysis requests.
- [protocol SNResultsObserving](snresultsobserving.md)
  The interface your app implements to receive the results of an analysis request.
- [func remove(any SNRequest)](snaudiostreamanalyzer/remove(_:).md)
  Removes an existing request from the audio stream analyzer.
- [func removeAllRequests()](snaudiostreamanalyzer/removeallrequests.md)
  Removes all the sound analysis requests from the audio stream analyzer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snaudiostreamanalyzer/add(_:withobserver:))*