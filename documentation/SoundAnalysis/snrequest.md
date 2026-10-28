# SNRequest

**Framework**: Sound Analysis  
**Kind**: protocol  
**Role**: Protocol

A protocol that represents sound analysis requests.

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
protocol SNRequest : NSObjectProtocol
```

```objc
@protocol SNRequest <NSObject>
```

## Overview

Don’t create types that adopt `SNRequest`. Only Sound Analysis framework types adopt the protocol.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [SNClassifySoundRequest](./snclassifysoundrequest.md)

## See Also

### Managing Requests
- [func add(any SNRequest, withObserver: any SNResultsObserving) throws](./snaudiofileanalyzer/add%28_,withobserver%29.md)
  Adds a new analysis request to the audio file analyzer.
- [protocol SNResultsObserving](./snresultsobserving.md)
  The interface your app implements to receive the results of an analysis request.
- [func remove(any SNRequest)](./snaudiofileanalyzer/remove%28_%29.md)
  Removes an existing request from the audio file analyzer.
- [func removeAllRequests()](./snaudiofileanalyzer/removeallrequests%28%29.md)
  Removes all the sound analysis requests from the audio file analyzer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snrequest)*