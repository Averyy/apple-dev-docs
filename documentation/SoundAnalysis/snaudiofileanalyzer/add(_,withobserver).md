# add(_:withObserver:)

**Framework**: Sound Analysis  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) addRequest:(id<SNRequest>) request withObserver:(id<SNResultsObserving>) observer error:(NSError **) error;
```

## Mentions

- [Classifying Sounds in an Audio File](../classifying-sounds-in-an-audio-file.md)

#### Discussion

The method throws an error (Swift) or returns an error (Objective-C) if the analyzer is actively processing the file.

## Parameters

- `request`: A sound analysis request.
- `observer`: An [`SNResultsObserving`](../snresultsobserving.md) instance that receives the analyzer’s results. The analyzer maintains a weak reference to the observer.

## See Also

### Managing Requests
- [protocol SNRequest](../snrequest.md)
  A protocol that represents sound analysis requests.
- [protocol SNResultsObserving](../snresultsobserving.md)
  The interface your app implements to receive the results of an analysis request.
- [func remove(any SNRequest)](./remove%28_%29.md)
  Removes an existing request from the audio file analyzer.
- [func removeAllRequests()](./removeallrequests%28%29.md)
  Removes all the sound analysis requests from the audio file analyzer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snaudiofileanalyzer/add(_:withobserver:))*