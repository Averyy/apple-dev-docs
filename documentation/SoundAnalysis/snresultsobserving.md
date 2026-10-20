# SNResultsObserving

**Framework**: Sound Analysis  
**Kind**: protocol  
**Role**: Protocol

The interface your app implements to receive the results of an analysis request.

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
protocol SNResultsObserving : NSObjectProtocol
```

```objc
@protocol SNResultsObserving <NSObject>
```

## Mentions

- [Classifying Sounds in an Audio File](./classifying-sounds-in-an-audio-file.md)
- [Classifying Sounds in an Audio Stream](./classifying-sounds-in-an-audio-stream.md)

## Topics

### Handling Requests
- [func request(any SNRequest, didProduce: any SNResult)](./snresultsobserving/request%28_,didproduce%29.md)
  Provides a new analysis result to your app with the specified time range.
- [protocol SNResult](./snresult.md)
  A protocol that represents sound analysis results.
- [func request(any SNRequest, didFailWithError: any Error)](./snresultsobserving/request%28_,didfailwitherror%29.md)
  Provides any errors that occur during processing of the request.
- [func requestDidComplete(any SNRequest)](./snresultsobserving/requestdidcomplete%28_%29.md)
  Notifies your app when the analysis request completes normally.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Managing Requests
- [func add(any SNRequest, withObserver: any SNResultsObserving) throws](./snaudiofileanalyzer/add%28_,withobserver%29.md)
  Adds a new analysis request to the audio file analyzer.
- [protocol SNRequest](./snrequest.md)
  A protocol that represents sound analysis requests.
- [func remove(any SNRequest)](./snaudiofileanalyzer/remove%28_%29.md)
  Removes an existing request from the audio file analyzer.
- [func removeAllRequests()](./snaudiofileanalyzer/removeallrequests%28%29.md)
  Removes all the sound analysis requests from the audio file analyzer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snresultsobserving)*