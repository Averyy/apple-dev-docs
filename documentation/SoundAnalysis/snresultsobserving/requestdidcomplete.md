# requestDidComplete(_:)

**Framework**: Sound Analysis  
**Kind**: method

Notifies your app when the analysis request completes normally.

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
optional func requestDidComplete(_ request: any SNRequest)
```

#### Discussion

The analyzer calls this method when it finishes processing the request.

## Parameters

- `request`: The request that’s completing.

## See Also

- [func request(any SNRequest, didProduce: any SNResult)](snresultsobserving/request(_:didproduce:).md)
  Provides a new analysis result to your app with the specified time range.
- [protocol SNResult](snresult.md)
  A protocol that represents sound analysis results.
- [func request(any SNRequest, didFailWithError: any Error)](snresultsobserving/request(_:didfailwitherror:).md)
  Provides any errors that occur during processing of the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snresultsobserving/requestdidcomplete(_:))*