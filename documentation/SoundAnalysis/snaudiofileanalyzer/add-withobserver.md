# add(_:withObserver:)

**Framework**: Sound Analysis  
**Kind**: method

Adds a new analysis request to the audio file analyzer.

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

- [Classifying Sounds in an Audio File](classifying-sounds-in-an-audio-file.md)

#### Discussion

The method throws an error (Swift) or returns an error (Objective-C) if the analyzer is actively processing the file.

## Parameters

- `request`: A sound analysis request.
- `observer`: An   instance that receives the analyzer’s results. The analyzer maintains a weak reference to the observer.

## See Also

- [protocol SNRequest](snrequest.md)
  A protocol that represents sound analysis requests.
- [protocol SNResultsObserving](snresultsobserving.md)
  The interface your app implements to receive the results of an analysis request.
- [func remove(any SNRequest)](snaudiofileanalyzer/remove(_:).md)
  Removes an existing request from the audio file analyzer.
- [func removeAllRequests()](snaudiofileanalyzer/removeallrequests.md)
  Removes all the sound analysis requests from the audio file analyzer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snaudiofileanalyzer/add(_:withobserver:))*