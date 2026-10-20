# removeAllRequests()

**Framework**: Sound Analysis  
**Kind**: method  
**Role**: Instance Method

Removes all the sound analysis requests from the audio file analyzer.

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
func removeAllRequests()
```

```objc
- (void) removeAllRequests;
```

## See Also

### Managing Requests
- [func add(any SNRequest, withObserver: any SNResultsObserving) throws](./add%28_,withobserver%29.md)
  Adds a new analysis request to the audio file analyzer.
- [protocol SNRequest](../snrequest.md)
  A protocol that represents sound analysis requests.
- [protocol SNResultsObserving](../snresultsobserving.md)
  The interface your app implements to receive the results of an analysis request.
- [func remove(any SNRequest)](./remove%28_%29.md)
  Removes an existing request from the audio file analyzer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snaudiofileanalyzer/removeallrequests())*