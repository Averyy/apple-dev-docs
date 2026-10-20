# remove(_:)

**Framework**: Sound Analysis  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) removeRequest:(id<SNRequest>) request;
```

#### Discussion

You can remove a request while the analyzer is processing it. The analyzer stops sending results to the observer after the method removes the request.

## Parameters

- `request`: A sound analysis request.

## See Also

### Managing Requests
- [func add(any SNRequest, withObserver: any SNResultsObserving) throws](./add%28_,withobserver%29.md)
  Adds a new analysis request to the audio stream analyzer.
- [protocol SNRequest](../snrequest.md)
  A protocol that represents sound analysis requests.
- [protocol SNResultsObserving](../snresultsobserving.md)
  The interface your app implements to receive the results of an analysis request.
- [func removeAllRequests()](./removeallrequests%28%29.md)
  Removes all the sound analysis requests from the audio stream analyzer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snaudiostreamanalyzer/remove(_:))*