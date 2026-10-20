# SNResult

**Framework**: Sound Analysis  
**Kind**: protocol  
**Role**: Protocol

A protocol that represents sound analysis results.

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
protocol SNResult : NSObjectProtocol
```

```objc
@protocol SNResult <NSObject>
```

#### Overview

Don’t create types that adopt `SNResult`. Only Sound Analysis framework types adopt the protocol.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [SNClassificationResult](./snclassificationresult.md)

## See Also

### Handling Requests
- [func request(any SNRequest, didProduce: any SNResult)](./snresultsobserving/request%28_,didproduce%29.md)
  Provides a new analysis result to your app with the specified time range.
- [func request(any SNRequest, didFailWithError: any Error)](./snresultsobserving/request%28_,didfailwitherror%29.md)
  Provides any errors that occur during processing of the request.
- [func requestDidComplete(any SNRequest)](./snresultsobserving/requestdidcomplete%28_%29.md)
  Notifies your app when the analysis request completes normally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snresult)*