# remove(_:)

**Framework**: Sound Analysis  
**Kind**: method

Removes an existing request from the audio stream analyzer.

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
func remove(_ request: any SNRequest)
```

#### Discussion

You can remove a request while the analyzer is processing it. The analyzer stops sending results to the observer after the method removes the request.

## Parameters

- `request`: A sound analysis request.

## See Also

- [func add(any SNRequest, withObserver: any SNResultsObserving) throws](snaudiostreamanalyzer/add(_:withobserver:).md)
  Adds a new analysis request to the audio stream analyzer.
- [protocol SNRequest](snrequest.md)
  A protocol that represents sound analysis requests.
- [protocol SNResultsObserving](snresultsobserving.md)
  The interface your app implements to receive the results of an analysis request.
- [func removeAllRequests()](snaudiostreamanalyzer/removeallrequests.md)
  Removes all the sound analysis requests from the audio stream analyzer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snaudiostreamanalyzer/remove(_:))*