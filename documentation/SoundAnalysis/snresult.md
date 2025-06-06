# SNResult

**Framework**: Sound Analysis  
**Kind**: protocol

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

#### Overview

Don’t create types that adopt `SNResult`. Only Sound Analysis framework types adopt the protocol.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [SNClassificationResult](snclassificationresult.md)

## See Also

- [func request(any SNRequest, didProduce: any SNResult)](snresultsobserving/request(_:didproduce:).md)
  Provides a new analysis result to your app with the specified time range.
- [func request(any SNRequest, didFailWithError: any Error)](snresultsobserving/request(_:didfailwitherror:).md)
  Provides any errors that occur during processing of the request.
- [func requestDidComplete(any SNRequest)](snresultsobserving/requestdidcomplete(_:).md)
  Notifies your app when the analysis request completes normally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snresult)*